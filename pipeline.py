from preprocessing import BlogPostPreparer, BlogChunker, BlogFetcher
from retrieval_utils_2 import KeywordSearch, VectorSearch
import pandas as pd
import requests

class BlogChatbotPipeline:

    def __init__(self, github_user, repo, branch, post_paths, df=None,embedding_model="text-embedding-3-small", max_length=512):

        self.github_user = github_user
        self.repo = repo
        self.branch = branch
        self.post_paths = post_paths

        self.max_length = max_length
        self.fetcher = BlogFetcher(self.github_user, self.repo, self.branch, self.post_paths)
        self.preparer = BlogPostPreparer()
        self.chunker = BlogChunker(embedding_model)
        self.df=df

    def build_dataframe(self):

        if self.df is not None:
            return self.df

        posts = self.fetcher.get_posts()

        all_chunks = []

        for post in posts:

            response = requests.get(post["download_url"])
            markdown_text = response.text

            processed_post = self.preparer.preprocess_post(
            markdown_text,
            post["download_url"]
        )

            chunks = self.chunker.chunk_content(processed_post["content"])
            for i, (title, text) in enumerate(chunks):

                all_chunks.append({
                    "chunk_index": i,
                    "chunk_title": title,
                    "chunk_text": text,
                    "post_title": processed_post["title"],
                    "date": processed_post["date"],
                    "source": processed_post["source"]
                })

        return pd.DataFrame(all_chunks)

