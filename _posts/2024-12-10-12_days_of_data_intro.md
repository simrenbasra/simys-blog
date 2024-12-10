---
title: "12 Days of Data: An Introduction 🌟"
date: 2024-12-10
---

One challenge I often face when working on my projects is that I tend to spend more time completing them then planned. I like to thoroughly explore solutions, starting with simple approaches and gradually increasing the complexity. This method helps me gain a deeper understanding of the data and problem at hand. While this is ideal for personal projects, it’s not always a possibility in the real-world. Often, you’re required to deliver results within a tight timeline.

With that in mind, I’ve decided to cap my next project to 12 days!

**Introducing the 12 Days of Data!**

This Thursday _(12/12)_, I will start work on this project with the goal of having a working prototype ready by Christmas Eve! I’m excited to see how well I can progress over the next 12 days.

In this post, I’ll introduce the project objective and outline how I plan to document the process and share updates!

<br>

----

<br>

## Project Objective

With Christmas approaching, I wanted my project to have a festive theme! The aim of this project is to generate short, tailored Christmas stories using a Large Language Model (LLM).

The idea is for users to input story details such as characters and genre. The LLM will process this input to produce a personalised Christmas story. 

<br>

----

<br>

## Getting Started

To make things easier for me, I’ve decided to plan out a few things before diving into the project. This includes selecting the LLM I will use, determining user inputs, defining the expected output and decide how best to evaluate the model’s performance. By clarifying these points ahead of time, I’ll be ready to hit the ground running when I start on Thursday!

#### **LLM**

Given the time constraints of this project, I have decided to use GPT-4o with prompt engineering rather than fine-tuning a generative AI model. Here is why:

**1.	Data Collection**

-	Collecting a large, high-quality dataset of Christmas-themed short stories is time-consuming. To fine-tune a model effectively, I would need at least 100 examples for meaningful results.
  
-	All data must come from publicly available or open-source datasets to avoid copyright infringement. This makes data collection even more challenging and time consuming.
  
-	Prompt engineering does not require any training data. This frees up my time to focus on designing prompts that leverage GPT 4’s full capabilities to get the best output.
  
-	I considered using GPT to generate training data for a generative model, but this felt counterproductive. I thought using GPT-4 with prompt engineering, would deliver better outputs rather than using GPT-generated data to train another generative AI model.
  
-	GPT-4’s creativity and ability to generate text make it well-suited for this project without additional fine-tuning.

**2.	Time**

-	Fine-tuning a large generative model can be both computationally expensive and time-consuming.
  
-	With a tight 12-day timeline, fine-tuning a model (including data collection) would likely take more than 12 days.
  
-	Using GPT-4 allows me to start generating stories almost immediately. 

Overall, GPT-4 seems to be the more suitable choice for this project due to the model’s ability to generate creative text without the need for fine-tuning. By combining GPT-4 with effective prompt engineering, I believe the results can still achieve a high level of quality. 

#### **Inputs**

For this project, LLM will generate short Christmas stories based on user-provided inputs. Here's a breakdown of details users can provide to personalise their story:

**Mandatory Inputs:** 

1.	Character Type: Choose a classic Christmas Character (Santa, Elf, Reindeer, etc)

2.	Genre: Choose genre of story (action, comedy, etc)

**Optional Inputs:** 

1.	Moral: Key takeaway from the story (giving, kindness, etc)

2.	Location: Main setting of the story (North Pole, Santas Workshop, etc)

The goal of this project is to test the LLM’s creative abilities, so I intentionally kept mandatory inputs to a minimum. The fewer details the user provides, the more the LLM has to generate itself, allowing it to demonstrate creativity in creating stories. Minimum inputs would also test my ability to create meaningful prompts. The optional inputs allow users to further customise their stories.

#### **Expected Output**

-	**Length:** Between 500 to 1000 words.
  
- **Cohesiveness:** The generated story should be logical with a clear flow from beginning to end.

- **User Inputs**: The story should include and reflect all the inputs provided by the user.

- **Creativity:** The story should show creativity in character profiles and storylines. The LLM should fill in details the user hasn't provided, such as personality traits of characters.

- **Response Time:** The LLM should be able to create high-quality outputs within a reasonable time.

To evaluate the model, I will check the output meets the above criteria and will add in some other checks if needed. 

<br>

----

<br>

## Sharing Updates

Every three days, I will be sharing my progress as part of my project. 

The aim is to develop a fully working solution by the end of the 12 days. This diary will help me stay on track, and if needed, I can adjust the project scope depending if I'm ahead or behind. 

By keeping a record of what I accomplish each day, I hope to improve my time management and better plan for following stages of the project.

#### **Diary Template:**

-	**Main Objective:** What was the main focus for these couple of days?

- **Accomplished Tasks:** What did I achieve during this period?

-	**Blockers/Challenges**: What problems did I face? How did I resolve them or plan to resolve them?

-	**Next Steps:** Tasks to tackle over the next few days. 

<br>

----

<br>

## Summary	

In this post, I have outlined the scope of my project and how I plan to share my progress along the way. This is an exciting project for me, I have not worked with LLMs before. I am intrigued to see how far I can progress within 12 days and to learn about prompt engineering.

Once the project is complete, I plan to write another post summarising what I’ve learned about LLMs and prompt engineering, along with explaining key takeaways and sharing code snippets to provide further insights.  

