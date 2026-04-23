---
title: "SimBot: Project Wrap Up 🚀"
date: 2026-04-23
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/last_cover_image.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

In my last post, I focused on improving retrieval for SimBot by experimenting with different methods to see what worked best. While that helped to refine performance, getting SimBot ready for real use turned out to be a very different process altogether.

<br>

----

<br>

## Recap: What to expect from SimBot?

SimBot is designed to help users better understand and navigate my blog content. It retrieves information from my previous posts and uses this to generate responses.

#### **Core Features**

- **Memory:** Ask follow-up questions without needing to repeat context
- **Hybrid retrieval:** Combines keyword, vector and recency-aware search
- **Source-grounded answers:** Responses are based on my blog content
- **Source linking**: Returns links to relevant posts when requested
- **Multi-post understanding**: Combines information from multiple posts into one answer

#### **Try it yourself!**

🤖 [SimBot](https://simrenbasra.github.io/simys-blog/chat/) 

**Suggested prompts:**

- _“What are vector databases? How do they work?”_
- _“Explain recommendation systems”_
- _“Return all posts which explain reinforcement learning”_
- _“What is the difference between sentence transformers and TF-IDF"_

<br>

----

<br>

## Future Improvements

#### **1). Questions about me**

Improve how SimBot handles personal context, sometimes the chatbot struggles to distinguish between past and present stages of my data science journey. This could be fixed by including an “About Me” section in the prompt and keeping it up to date. 

#### **2). Consistent source linking**

Ensure responses always return links to relevant posts, along with specific headings where possible.

#### **3). Memory handling**

Improve how conversation history is managed so the chatbot remains relevant when switching topics. At times, the chatbot mixes earlier context with new topics when providing links.

#### **4). Automated ingestion of posts**

Move from manual updates to an automated pipeline (using GitHub Actions) to regularly pull new posts and update the vector database.

#### **5). Flexibility of language**

Improve how the chatbot handles different phrasings of the same question, making it less sensitive to wording. 

#### **6). Images and diagrams**

Improve the chatbot’s ability to explain through diagrams without image embeddings. I am not quite sure how but am thinking to give diagrams a better description when I create placeholders.

<br>

----

<br>

## Project Learnings

This project felt a lot smoother than my previous ones, usually projects have taken different directions and at times taken a lot longer than I initially planned. One thing that felt different this time was that I had some previous experience with embeddings and was more aware of what could go wrong in chunking and how these early decisions shape the end product. I am someone who learns best by doing and I really did see that here. 

My main challenge was productionising the chatbot. While it worked well in notebooks, a few issues only really showed up once I built the app and started testing it properly. Things like memory handling, returning links to posts and setting up automated ingestion all came up at that stage.

Looking back, I should have thought more carefully about the actual use cases earlier on. That would have made productionising a lot easier. Instead, I ended up making changes directly in Hugging Face, which sometimes felt like two steps forward and one step back because new features occasionally broke existing functionality.

<br>

----

<br>

## Summary

I’m really happy with the first version of SimBot and excited that it’s now on the blog for users to try. I’d really appreciate any feedback, so if anything could be improved please let me know!

Over the next few weeks, I’ll be focusing on building out some of the improvements to SimBot that I mentioned earlier!
