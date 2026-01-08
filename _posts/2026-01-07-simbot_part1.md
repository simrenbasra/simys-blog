---
title: "SimBot: Project Introduction 📝"
date: 2026-01-07
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/project_intro_cover_photo.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

Most of my blog posts build on previous ones and I know it can be tricky to follow along especially when weeks pass between each post. At times, even I forget what I wrote two posts ago…

That’s when I started thinking: wouldn’t it be great to have something on my blog that can catch readers up, summarise past posts or answer questions without them needing to reread everything?

Introducing my next project SimBot! A custom chatbot that helps readers ask questions and understand past content without having to dig through older posts (which, I’ll admit, can get a little hefty…).

<br>

----

<br>

## Project Overview

The end goal of this project is to add a working chatbot to my blog so readers can easily interact with it and get responses instantly without jumping to another site.

Since this is my first time building a custom chatbot, I’m breaking the project down into phases:

#### **Phase 1: Build a simple chatbot**

This first phase focuses on creating a basic chatbot without any document parsing. The goal is to get comfortable calling different chatbot models, experimenting with prompts and assessing model responses. By starting simple, I can build a working understanding of how chatbots work before adding complexity.

#### **Phase 2: Experimenting with RAG**

For the second phase, my plan is to experiment with Retrieval-Augmented Generation (RAG). This includes preprocessing my blog posts, chunking and embedding the text and experimenting with different retrieval methods. I’ll also start evaluating how well each setup performs.

The goal of this phase is to figure out which approach works best for the final chatbot, SimBot.

#### **Phase 3: SimBot development**

In the final phase, I’ll bring everything together to build SimBot. Using the insights from the earlier phases, I’ll refine the prompts, improve retrieval and build the final chatbot.

By the end of this phase, I hope to have a chatbot ready to be integrated into my blog!

<br>

----

<br>

## Project Scope

At the start of each project, I try to define a rough project scope. I don’t usually share the planning stage of my projects, but I thought it would be a nice addition this time! I always try to stick to project plans, but not too rigidly. Once I get into the dataset or start experimenting, new findings often force the scope to change. This used to stress me out, but I’ve learned that in data science you’re always at the mercy of the data!

This project is slightly different because I have more flexibility with the “dataset” (my own blog posts), but things can still change… For example, embeddings might not work as well as expected, or I might run into issues with how the chatbot integrates into the blog.

But anyway, for now let’s take a look at what the chatbot will and won’t do!

#### **What SimBot Will Do**

-	Answer questions about my previous blog posts
  
-	Summarise content
  
-	Help readers find the right post or explanation
  
-	Clarify steps or concepts mentioned in posts
  
- Provide a quick way to revisit topics without rereading everything

#### **What SimBot Won’t Do**

-	Interpret diagrams or images (as discussed below, this may be explored in a later version, but not now)
  
-	Have conversations unrelated to my blog
  
-	Replace my posts

<br>

----

<br>


## Expected Challenges	

#### **1. Project Scoping**

I have a feeling that building a custom chatbot can get complex very quickly. To avoid going down a rabbit hole, I’m intentionally starting simple and breaking the project into clear phases. This approach helps me stay focused and ensures I properly understand things!

#### **2. Handling Images in Blog Posts**

Some posts include diagrams or screenshots. While, to the best of my knowledge, it’s possible to embed images and pass them to the model, I’m not entirely sure it’s necessary for this project. 

Most posts already describe processes step by step and I am assuming most user questions will refer to the text rather than the images. Image embeddings may be an unnecessary complexity to add to the project, especially in the first version. If needed, I can add in image support in a later version of SimBot!

#### **3. Evaluating the Chatbot**
   
There are no easy quantitative metrics I can use to evaluate responses of the chatbots. Most likely will evaluate models by:

- Asking the same questions to different chatbots
  
- Comparing clarity and accuracy of responses
  
- Picking the model that performs best (with a bit of bias)
  
#### **4. Integrating the Chatbot Into GitHub Pages**

My blog runs on GitHub Pages, which is static, so hosting a live chatbot directly on the blog is a bit of a challenge. I’m not yet sure what the best approach is, but will be something to solve before moving to phase 3! 

<br>

----

<br>

## Summary 

I’m excited to start this project!

I’ve been wanting to build a chatbot for a while, and now that I’ve just wrapped up a gnarly NLP project, it feels like the perfect time (especially with my new understanding of embeddings)!

