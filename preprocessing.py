import pandas as pd
from pathlib import Path
import frontmatter
import os
import re
from datetime import datetime
import emoji
import tiktoken
import requests

class BlogFetcher:

    def __init__(self, github_user, repo_name, branch, posts_path):
        
        self.github_user = github_user
        self.repo_name = repo_name
        self.branch = branch
        self.posts_path = posts_path

    def get_posts(self) -> list:

        all_posts = []
        for path in self.posts_path:
            url = f"https://api.github.com/repos/{self.github_user}/{self.repo_name}/contents/{path}?ref={self.branch}"
            response = requests.get(url)
            files = response.json()

            if isinstance(files, dict) and files.get("message"):

                error_msg = files["message"]
            
                if "rate limit exceeded" in error_msg.lower():
                    raise Exception(
                        "GitHub is temporarily limiting requests. "
                        "Please try again in a few minutes."
                    )
            
                raise Exception(f"GitHub API Error: {error_msg}")
            
            if path in ['about_me.md', 'my_projects.md']:
                all_posts.append(files)
            elif isinstance(files, list):
                md_files = [f for f in files if f['name'].endswith(".md")]
                all_posts.extend(md_files)
        
        return all_posts

class BlogPostPreparer:

    PLACEHOLDER_PATTERNS = [
        (r'<img [^>]*>', '[Image removed: see diagram in original post]'),
        (r'<iframe [^>]*>.*?</iframe>', '[Embedded content removed: see original post]'),
        (r'<video [^>]*>.*?</video>', '[Embedded content removed: see original post]'),
        (r'<script [^>]*>.*?</script>', '')
        ]
    
    def __init__(self):
        pass

    def remove_emojis(self, text: str) -> str:
        """
        Remove emojis from a given text string suing the emoji library.
        """
        return emoji.replace_emoji(text, replace='')
        

    def replace_media_with_placeholders(self, content: str) -> str:
        """
        Replace any media with placeholders for text processing.
        """
        for pattern, placeholder in self.PLACEHOLDER_PATTERNS:
            content = re.sub(
                pattern,
                placeholder,
                content,
                flags=re.IGNORECASE | re.DOTALL
            )

        content = re.sub(
            r'<div[^>]*>(.*?)</div>',
            lambda m: m.group(1).strip(),
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        return content.strip()

    def preprocess_post(self, post_content: str, post_path : Path) -> dict:   
        """
        Extract metadata and cleaned content from a Markdown blog post.

        This function loads a Markdown post using `python-frontmatter`, cleans it
        and returns a dictionary containing relevant information for use in a RAG chatbot
        """
        post = frontmatter.loads(post_content)

        title = self.remove_emojis(post.metadata.get("title", "")).strip()

        raw_date = post.metadata.get("date")
        if not raw_date or pd.isna(raw_date):
            date = datetime.now().date().isoformat()
        else:
            date = str(raw_date)

        content = self.replace_media_with_placeholders(self.remove_emojis(post.content))

        return {
            "title": title,
            "date": date,
            "content": content,
            "source": post_path
        }

class BlogChunker:

    def __init__(self, embedding_model, max_length=512):
        self.max_length = max_length
        self.tokeniser = tiktoken.encoding_for_model(embedding_model)

        
    def split_sections(self, content: str) -> list:
        """ 
        Split a post into main sections based on headings (##) and line breaks.
        """
        sections = re.split(
            r'<br>\s*-+\s*<br>\s*##\s*',
            content,
            flags=re.IGNORECASE
        )
        return sections

    def extract_heading_body(self, section: str, default_heading: str ="Unknown") -> tuple:
        """
        Separate a section into its heading (first line) and body (rest of section).
        If no heading is found, a default heading is used.
        """
        lines = section.split("\n", 1)
        heading = lines[0].strip() if lines else default_heading
        body = lines[1].strip() if len(lines) > 1 else ""
        return heading, body

    def count_tokens(self, text:str) -> int:
        """
        Counts tokens in a given text using OpenAI tokeniser.
        """
        return len(self.tokeniser.encode(text))

    def split_sub_sections(self, content : str) -> list:
        """
        Split content into sub-sections.
        - If #### headings exist, split by them.
        - Otherwise, return the whole content as one block.
        """
        if re.search(r'^####\s+', content, flags=re.MULTILINE):
            parts = re.split(r'(?=^####\s+)', content, flags=re.MULTILINE)
            return [p.strip() for p in parts if p.strip()]
        else:
            return [content.strip()]

    def clean_heading(self, text: str) -> str:
        """
        Clean a section heading by removing Markdown syntax and formatting characters.
        """
        # remove leading markdown headers (####, ###, ##, #)
        text = re.sub(r'^\s*#{1,6}\s*', '', text)

        # remove bold markers **
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)

        # remove trailing colon or whitespace
        return text.strip(" :\n\t")

    def chunk_content(self, content):
        """
        Chunk the content of a blog post into sections and sub-sections, ensuring each chunk is within the token limit.
        """
        sections = self.split_sections(content) 

        chunks = []

        if sections:
            chunks.append(("Intro", sections[0]))

        for section in sections[1:]:
            heading, body = self.extract_heading_body(section)
            if self.count_tokens(body) <= self.max_length:
                chunks.append((heading, body))
                continue

            sub_sections = self.split_sub_sections(body)
            chunk_counter = 1
            for sub in sub_sections:

                if sub.startswith("####"):
                    lines = sub.splitlines()
                    sub_heading = lines[0].replace("####", "").strip()
                    sub_body = "\n".join(lines[1:]).strip()
                else:
                    sub_heading = None
                    sub_body = sub.strip()

                paragraphs = re.split(r'\n\s*\n+', sub_body)
                current_chunk = ""

                for p in paragraphs:
                    candidate = current_chunk + ("\n\n" if current_chunk else "") + p
                    if self.count_tokens(candidate) <=self.max_length:
                        current_chunk = candidate
                    else:
                        if current_chunk:
                            title = f"{heading} {chunk_counter}"
                            if sub_heading:
                                title += f" - {sub_heading}"
                            chunks.append((title, current_chunk))
                            chunk_counter += 1
                        current_chunk = p
                if current_chunk:
                    title = f"{heading} {chunk_counter}"
                    if sub_heading:
                        title += f" - {sub_heading}"
                    chunks.append((title, current_chunk))
                    chunk_counter += 1

        return chunks


