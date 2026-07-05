---
title: "SimBot Has Skills: Explain Concepts 🗣️"
date: 2026-07-05
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/cover_photo_4.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

In my previous blog post, I introduced SimBot’s first skill: Recommend Blog Posts. The goal of that skill was to suggest blog posts to users based on what they want to learn. Building on this, I’ve now implemented SimBot’s second skill: Explain Concepts.

In this post, I’ll give an overview of the skill and its purpose and explain how I implemented it.

<br>

----

<br>

## Skill Overview: Explain Concepts

The main aim of this project is to turn SimBot into an AI tutor to help beginners learn data science through the projects and blog posts. A big part of learning is having things explained in a way that you can actually understand, so I thought it made sense to build a dedicated skill for that.

The Explain Concepts skill is similar to the original chatbot. It takes the user query, finds the top n relevant chunks and uses them to generate a response. The main difference is that instead of focusing purely on retrieval, we now do more with the retrieved chunks to ensure better understanding. To do this, I defined a layout for the response so it returns:

-	**What it is:** introduces the concept in simple language
  
-	**Why it matters:** explains why the concept is important
  
-	**How I apply it:** connects the concept back to examples from my projects and blog posts
  
- **Example or analogy:** provides an easy-to-understand example if it is needed

-	**Key takeaway:** summarises the concept for the user
  
Below is the implementation of the skill. As mentioned in previous blog posts, I had already implemented a Question Answer skill. The Explain Concepts skill reuses much of the same retrieval pipeline. The main difference is the prompt used to generate the response.

<br>

----

<br>

## Skill Implementation

Below is a screenshot of the skill logic:

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/explain_concept_skill.png" alt="Skill logic" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

#### **Step 1: Query Rewrite**
Before doing any search or retrieval, the query gets rewritten.

I found this improves performance because it expands short or vague questions. Users often ask things like _“what is X?”_ or _“how does Y work?”_ so rewriting helps make the intent clearer.

It also makes retrieval more accurate since the system can better match relevant chunks from the blog.

#### **Step 2: Retrieval**

The same RAG process is used here, based on a hybrid approach that combines keyword search and vector search (with recency).

There are no changes to how retrieval currently works in SimBot.

**Note:** If there is previous conversation history, it is added to the prompt, I might change this in the future to only include user messages instead of full conversation history. This could make things cleaner and reduce noise in the prompt. On the other hand, keeping the full history can still be useful in cases where the user wants to clarify or refer back to something the chatbot previously said, so I need to think a bit more about this…

#### **Step 3: Prompt for response**

This is the most important part of the skill, as it defines how the model teaches concepts. I thought that setting a fixed layout for explanations would help ensure better understanding and it’s a format that I personally would find useful.

**Note:** One thing to improve in the future would be adding difficulty levels to the responses.

#### **Step 4: Extract sources**

Similar to SimBot, I thought it would be useful to add a dedicated section for sources. This makes it easy for users to revisit blog posts and reread parts of them if needed.

#### **Step 5: Return response and sources**

Finally, the model’s response and the extracted sources are returned.

<br>

----

<br>

## Orchestrator Update

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/orchestrator_2.png" alt="Skill logic" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

I added a new `EXPLAIN_CONCEPTS` category, so now the chatbot can distinguish between answering general questions and helping users learn concepts.

For now, I’m keeping things simple and focusing on building each skill independently. Once all the skills are ready and I’m happy with them, I’ll move on to adding interaction between them and allowing multiple skills to be triggered together.

<br>

----

<br>

## Summary	

Overall, things are progressing fairly well. I’m happy with how the two skills are working so far, although they are still independent of each other (as in only one skill can be called at a time).

I think the real test will come once all the skills are implemented and can work together in a single call, along with adding difficulty levels to customise responses a bit more.

Next up, I’ll build the skill for quizzing users.
