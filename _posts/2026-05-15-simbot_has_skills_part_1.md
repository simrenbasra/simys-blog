---
title: "SimBot Has Skills: Project Introduction 😎"
date: 2026-05-15
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/cover_photo.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

SimBot has been working great so far! There are still some improvements I want to make, but overall I’m happy with how things are working. 

That said, I started to wonder… instead of just retrieving information, could my chatbot do more? What if it could help people learn the concepts covered in my posts, rather than just repeating information back to them?

Introducing my next project: **SimBot Has Skills!**

The idea is to add skills to SimBot, taking it from a retrieval chatbot to a tutor-like assistant. It will be able to:

- Recommend relevant reading from my blog posts

- Explain concepts from posts (going beyond simple retrieval)

- Generate questions and quizzes for users to answer

- Evaluate user responses and provide corrections where needed

<br>

----

<br>

## So, what are Skills?

You can think of skills like functions that allow a system to carry out specific tasks. 

For SimBot, one skill might generate quiz questions, another could recommend relevant blog posts for reading, while another might evaluate a user’s answers. By combining different skills together, SimBot can support all stages of a typical learning process, from explanation to practice and feedback.

In the next post, I’ll explain what skills mean in the context of this project and how they interact with LLMs, as well as how I plan to integrate them into SimBot.

<br>

----

<br>

## How Skills Work in SimBot

As is, SimBot is a RAG chatbot. This means when a user sends a message, the chatbot retrieves the `top_n` most similar chunks using vector search. These are then added to the user’s prompt and passed to an LLM, which generates a response that is returned to the user. 

To help visualise this, here is an overview of a RAG pipeline:

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/chatbot_rag.png" alt="RAG Chatbot" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

With skills, this flow changes. When a user sends a message, SimBot first interprets what they are asking and decides which skill or skills are most relevant.

The chatbot itself (the LLM part of SimBot) acts as an orchestrator, deciding which skills to use and how to combine their outputs into a final response.

<br>

----

<br>

## Project Plan

The end goal is to add a tutor mode to SimBot, where users can follow a more structured learning path, get quizzed and ask questions to clarify their understanding.

A key assumption here is that the content in my blog posts is correct (a bold claim but I will be reviewing posts over time). This may change but for now the blog acts as the main knowledge base for the system.

Since I haven’t worked much with skills before, I will break the project into phases, where each phase focuses on building a specific skill:

#### **Skill 1:** Recommend blog posts

Suggest relevant reading from my blog based on the user’s question or topic

#### **Skill 2:** Explain concepts (beyond simple retrieval)

Break down ideas from blog posts into clearer, more digestible explanations

#### **Skill 3:** Generate questions and quizzes

Create questions to test understanding

#### **Skill 4:** Evaluate user understanding and provide feedback

Assess user answers, explain mistakes and suggest corrections.

#### **Skill 5:** Adapt difficulty based on user performance

Adjust explanations and questions depending on how well the user is doing.

#### **End goal**

A tutor mode that combines all of these skills into a single system, allowing SimBot to act as a tutor while still keeping simple retrieval for quick questions. This likely means adding an optional mode, so users can choose between simple retrieval and more structured learning.

<br>

----

<br>

## Summary 

I’m excited to gain some experience with skills and think this project is a great way to upskill myself.

In the next post, I’ll go deeper into what skills are, how they work and how they interact with LLMs and agents. After that, I’ll start building the first skill: recommending relevant blog posts.

