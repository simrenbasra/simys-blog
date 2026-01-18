---
title: "SimBot: A Simple Chatbot 🗨️"
date: 2026-01-18
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/simple_chatbot_cover_photo.jpg" alt="Cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

As discussed in my previous post, SimBot will be built in phases. In this post, I’ll share details about the first phase; building a simple chatbot. Starting small helps me build a solid understanding of chatbots and how they are set up. All of this will be useful when it comes to building a RAG chatbot later.
While this step isn’t really necessary, I want to make sure I understand the simple things before moving to anything more complex!

_**So, what do I mean by a “Simple Chatbot”?**_

**Chatbot should:**

-	Receive a prompt from a user
  
-	Acknowledge the prompt
  
-	Return a related, meaningful response 

**Chatbot should not:**

-	Perform any information retrieval

This type of chatbot only uses what it has learnt through training to generate a response, there is no external data to reason with.

<br>

----

<br>

## Simple Chatbot Pipeline

At a high level, the chatbot follows these steps:

1.	Receives a user prompt

2.	Tokenises the input text

3.	Matches patterns learned during training to return a likely response

    **NOTE:** Different models have different training data and so, respond differently.
    
4.	Decodes tokens back into readable language

5.	Returns the response to the user

<br>

----

<br>

## Implementation

#### **Step 1: Model Selection**

I chose a small set of lightweight and easy-to-load models to experiment with and compare responses:

**1). GPT-2**

- Chosen as a baseline model to compare more advanced models to 

- Widely used and easy to run locally

- Useful to see how a general purpose model (that predicts the next token) handles instruction and conversation based prompts 

**2). Dialo-GPT**

- Trained on large amounts of conversational data from Reddit

- Designed to generate dialogue 

- Useful to see how conversation-focused training data affects chatbot behaviour

**3). FLAN-T5 (Base)**

- An instruction tuned model trained to follow explicit instructions

- Expected to perform best for prompt-based interactions (to be tested)


#### **Step 2: Load the tokenisers and model for each chatbot**

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/load_chatbot_models.png" alt="Step 2a" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/define_models.png" alt="Step 2b" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

#### **Step 3: Define a Variety of Prompts / Roles**

I’ve chosen five different prompts to test the main qualities I want the final chatbot to have.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/define_prompts.png" alt="Step 3" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

Although the models I’m experimenting with are small (and do not use retrieval), I think it’s still useful to start thinking early about the kind of prompts users will send to the final chatbot. Some prompts are instruction-based, like asking the model to perform a specific task, while others are conversational, like asking “How are you?”.

#### **Step 4: Run Experiments**

Iterate over the defined prompts and models, storing the generated responses for evaluation.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/iterate_over_models.png" alt="Step 4a" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

I store the generated responses in a dataframe for easier evaluation:

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/results_df.png" alt="Step 4b" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

Below is the function used to generate responses from each chatbot model. I adapted this function from a Hugging Face tutorial on chat templating [(see here)](https://huggingface.co/docs/transformers/en/chat_templating). The function handles prompt formatting, tokenisation, response generation and decoding.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/get_responses.png" alt="Step 4c" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>


#### **Step 5: Evaluate the Results**

I evaluated responses by reading each one and judging its quality. This is a qualitative approach, which felt right given the small number of prompts being tested. It’s a tricky task to evaluate LLM responses and requires some thought if I want to build some quantitative metrics! This is something to think more carefully about in later stages of the project. For example, when building the final chatbot it may be useful to use an LLM as a judge.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/simbot/phase_1/display_model_responses.png" alt="Step 4" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>


<br>

----

<br>

## Results

#### **GPT-2**

-	Often repeats the prompt before responding
  
-	Responses are frequently off-topic
  
-	Not well suited for instruction-based prompts
  
#### **DialoGPT**

-	Frequently echoes the prompt
  
-	Sometimes fails to produce a response at all
  
-	Best suited for informal chat, not instructions

#### **FLAN-T5**

-	Performs best overall
  
-	Does not echo the prompt or role
  
-	Responds to all prompts
  
-	Occasionally brief or repetitive responses
  
<br>

----

<br>

## Main Takeaways

#### **Prompt Echoing**

Prompt echoing was common in GPT-2 and DialoGPT.

I initially tried removing the role from the prompt, thinking it might be causing the issue, but this didn’t help. The models continued to repeat the input regardless.
This behaviour makes sense when considering training data:

-	GPT-2 is designed to continue text, not follow instructions
  
- DialoGPT was trained on Reddit conversations, where mirroring input is common

The models were behaving as expected based on their design.

#### **Instruction Tuning Matters**

FLAN-T5, despite also being a small model, handled prompts much better.

Instruction tuning clearly improves response relevance and reduces prompt echoing.

#### **Speed vs Quality Trade-off**

- Smaller models load quickly but struggle with instructions and output quality
  
-	Instruction-tuned models give better responses but may require more compute
  
This is an important trade-off to consider when moving towards a RAG chatbot.

<br>

----

<br>

## **Web App Demo**

As a final part of this phase, I wanted to test how to deploy the best-performing model using Streamlit. Below is a quick demo:
The model performs okay but as mentioned earlier, I will need a larger model with more parameters to return high quality responses. This phase was mainly about understanding chatbots and exploring the full end-to-end workflow!


<div style="position: relative; padding-bottom: 55.23809523809524%; height: 0;">
  <iframe src="https://www.loom.com/embed/562900a6b51a4d64815970f86cb4be27" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>


<br>

----

<br>

## Summary 

This was a quick experiment with relatively low implementation efforts but I’ve already learned a lot about how chatbots actually work! Before this, I hadn’t really considered how different chatbot models can be. Naively, I assumed that most chatbots operated in a similar way and all were designed to answer similar prompts.
One of the biggest takeaways was understanding prompt echoing and why it happens, especially in smaller or non-instruction-tuned models. I feel much more confident and better prepared to move on to the next stage: choosing the right model and processing documents for the RAG chatbot. 
