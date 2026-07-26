---
title: "SimBot Has Skills: Quiz Users 📝"
date: 2026-07-26
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/cover_photo_5.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

In this post, I’ll show the development of my latest skill: a quiz skill that tests users’ understanding of topics explored in my posts.

<br>

----

<br>

## Skill Overview: Quiz Users

An important part of learning is testing your understanding of what you have learned. This skill helps users reinforce their knowledge by answering quiz questions.
The Quiz Skill generates five multiple-choice questions, along with the correct answers and explanations for each question. In the future, the goal is to add more interactivity so that users answer the questions before the answers are displayed. For now, like the other skills, I have kept the implementation relatively simple while I plan out how the different skills will fit together and how I want the overall chatbot tutor system to work. 

<br>

----

<br>

## Skill Implementation

Below is a screenshot of the skill logic:

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/quiz_skill.png" alt="Quiz users skill" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

#### **Step 1: Retrieval**

The same RAG process currently used in SimBot is used here, based on a hybrid retrieval approach that combines keyword search and vector search with recency weighting. There are no changes to how retrieval currently works.

#### **Step 2: Prompt to Generate Questions**

A prompt is defined to generate questions that test the user’s understanding of a topic. I designed the prompt so that questions gradually increase in difficulty and avoid simple recall-based questions such as _“What is RAG?”_. Instead, the goal is to test whether users can apply what they have learned, for example by asking them to reason about designing or debugging RAG systems.

#### **Step 3: Return Sources**

Similar to other SimBot skills, the generated response includes the retrieved sources. This allows users to revisit the material or review posts if a question highlights a gap in their knowledge.

#### **Step 4: Return Response and Sources**

Finally, the generated quiz questions, answers, explanations and extracted sources are returned to the user.

<br>

----

<br>

## Orchestrator Update

Added a new `QUIZ_SKILL` category so quiz-related requests can be correctly routed to the new skill.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot_has_skills/orchestrator_3.png" alt="Orchestrator update" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

<br>

----

<br>

## Summary	

This skill is the last one I plan to develop for now. I think these three skills provide the core functionality needed for a tutor-like system. There may be more skills to add in the future, but at this stage, I want to focus on refining the overall design.

Building these skills in a simple way has really helped me think more deeply about how I want the final system to work and how the different skills need to interact with each other to create a more realistic tutor experience.
Over the next few weeks, I will focus on designing the overall tutor system, including how the different skills should work together and how the chatbot should function as a useful learning tool.

