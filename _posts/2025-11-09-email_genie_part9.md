---
title: "Email Genie: Web App 🧞‍♀️"
date: 2025-11-09
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/final_cover_photo.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

In my previous post, I explored fine-tuning with the goal of improving embeddings for semantic search. In the end, fine-tuning didn’t improve the results, so I decided to use a general large Sentence Transformer model to generate embeddings.

To build a rich search base, I expanded the dataset to 30,000 Enron emails and created a vector database for semantic retrieval.

I then developed a Flask-based web application that takes a user’s search query and returns the top N most semantically similar emails from the dataset! 

Let’s take a closer look my web app!

<br>

----

<br>

## Web Application Demo

<div style="position: relative; padding-bottom: 56.25%; height: 0;">
  <iframe src="https://www.loom.com/embed/e3fa5a746ec54072bb87189e5846548b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>


The demo walks through how the app takes a user query and returns semantically similar emails from the vector database (with concise summaries for easier reading).

I plan to dockerise this app and host it on a private server. Once that’s done, I’ll make share the link on my GitHub so everyone can try it out!

<br>

----

<br>

##  Web App Considerations

- **Noise in search results**: Early tests returned some irrelevant emails, often with a lot of disclaimers or confidentiality notices.

  **Solution:** Improved email cleaning so the focus of the embeddings would be actual email content.

- **Query length issues:** Short queries sometimes fail to retrieve semantically relevant results.
  
  **Solution:** Used an LLM to enhance queries, expanding them with related terms.
  
- **Long emails:** At times, returned emails can be quite lengthy to read…

  **Solution:** Used an LLM to generate summaries.

- **Layout inconsistencies:** The structure of emails in results wasn’t always clear.
  
  **Solution:** Returned original un-processed email bodies with added formatting to improve readability.

- **Dataset limitations:** The vector search is limited to the 30,000 emails available in the dataset. While sufficient for testing, this naturally limits recall. 


<br>

----

<br>

## Project Retro

This project has definitely been my largest project to date; from cleaning emails, to experimenting with different embedding methods, to classification and finally, to vector search. So, I thought it would be quite nice to go through some of the challenges and takeaways!

#### **Challenges**

Let’s discuss some of the many challenges I faced throughout this project:

**Cleaning and Data Quality**

Emails are a messy dataset and required multiple rounds of cleaning before I could make meaningful progress. Although I removed a lot of noise, some still remains and I now believe that residual dataset noise was the biggest stumbling block for retrieval quality.

Throughout the project I worried that embeddings or chunking were the cause, but in hindsight the noisy text (disclaimers, forwarded headers, repeated signatures, embedded attachments, etc.) had the largest negative impact on vector similarity and ranking. 

If I were to take on another NLP project, I would dedicate far more time to data cleaning. Spending more time exploring the dataset and carefully assessing which parts of the emails could cause problems down the line. For example, I would make sure to view the emails in a way that clearly highlights disclaimers and signatures, so I could handle them appropriately before generating embeddings.

**Web App Development**

Designing a clear UI for email results turned out to be trickier than expected. Especially when making considerations like using LLMs to expand user queries or for generating summaries of emails.

**Time Management**

Unlike my previous projects, this stop/start rhythm slowed me down a bit and I underestimated how long tasks would take.

#### **What went well?**

I’m proud that I pushed through with this project despite the hurdles. In the end, I was able to produce a working product.

This project stretched me the most in terms of learning, from embedding techniques, handling messy NLP data, and building vector databases, all the way to deploying a web app.

#### **Key Learnings**

- **Cleaning and preprocessing data are so important to NLP projects.** Without it, progress is nearly impossible.
  
- **Fine-tuning isn’t always the answer.** With large transformer models like Sentence Transformers, fine-tuning without many or carefully curated positive/negative pairs can actually hurt performance.

- **Noisy data is hard to remove.** Even after multiple passes, I found areas where my cleaning could have been stronger. For example, I could have excluded sign-offs or replaced dates, times and amounts with placeholders instead of removing them entirely.
  
- **Iteration isn’t bad, its part of the process.** Revisiting earlier steps (like data cleaning) was often necessary and did at times help further downstream. A lot of the time, noisy elements which were showing up wasn’t actually something I myself anticipated until I saw it, impossible with NLP to be sure of all possible noise dependent to the task.

<br>

----

<br>

## Summary

Even if the end product isn’t working as well I hoped, I’m proud of what I accomplished with the EmailGenie project. Working with messy, real-world data like emails reminded me that retrieval isn’t always perfect. In fact, inconsistency in results shows how sensitive semantic search is to things like data quality, chunking and embedding choice. While the web app doesn’t always return the most relevant emails, I now have a much better understanding of the challenges of NLP on real-world data and how small decisions, like how to chunk text, can affect performance.

I’ve really enjoyed this project and learned so much over the past months. Shortly, I will make the repository for this project public and share a link to my web app so everyone can try it out!

