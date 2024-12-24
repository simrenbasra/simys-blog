---
title: "12 Days of Data: Project Updates 📓"
date: 2024-12-12
---

Throughout this project, I’ll be sharing regular updates on my progress every few days. 

In each entry, I’ll highlight my main goals, what I’ve accomplished, any challenges I’ve faced, and next steps. The project aim is to build a tailored Christmas story generator using Large Language Models (LLMs) from a set of user inputs.

<br>

----

<br>

## Day 1: 12/12

#### **🎯 Main Objective**

- To successfully connect to the Open AI API and start to send requests.

#### **✅ Accomplished Tasks**

- Set up Open AI account and generated my API key.
- Set up a secure way to pass the API key using environment variables (as recommeded by OpenAI).
- Tested the connection to the API and model.
- Gained experience in using the Chat Completion objects.

#### **🛑 Blockers/Challenges**

- No blockers as of yet.

#### **👣 Next Steps** 

- Design and build Streamlit to gather user inputs.
- Implement prompt engineering based on inputs from Streamlit.
- Display the model (gpt-4o) output in Streamlit.

<br>

----

<br>

## Day 3: 15/12

#### **🎯 Main Objective**

- To set up Streamlit app and begin prompt engineering with user inputs.

#### **✅ Accomplished Tasks**

- Developed a basic Streamlit app to take user inputs such as character type and genre.
- Created two functions: one to build prompts from user inputs and another to get responses from GPT passing generated prompts as input.
- Added a button in Streamlit to display output of the GPT model.
- Added a button in Streamlit for users to download the stories.
- Experimented with different prompts and language to see the effects on the output.
   
#### **🛑 Blockers/Challenges**

- No blockers. However for this project, I am ahead of schedule and may finish before Christmas Eve (12 days). 
  
#### **👣 Next Steps** 

- Refine prompts futher and explore tuning of the GPT parameters to increase the quality of the model's outputs.
- Improve on the design and user interface of the Streamlit app.

<br>

----

<br>

## Day 6: 18/12

#### **🎯 Main Objective**

- To build on the design of my web app and further refine the output of the GPT model by tuning parameters and further refining prompts.

#### **✅ Accomplished Tasks**

- Added in some display features to make the web app more appealing to users while they wait for their story to be generated.
- Experimented with the different parameters of the GPT model to refine the output - with a close focus on temperature.
- Further refined the prompts.

#### **🛑 Blockers/Challenges**

- No blockers but I will most likely finish the project by the end of the week.

#### **👣 Next Steps:** 

- The main focus for me now is to improve the web app and add in some formatting.
- Clean up the project repository as wrap up the project.
  
<br>

----

<br>

## Day 9: 21/12

#### **🎯 Main Objective**

To wrap up any loose ends of the project and improve Streamlit display.

#### **✅ Accomplished Tasks**

- Added extra inputs for the user to enter to further personalise stories. 
- Added in a button where inputs are randomly selected, for cases where users does not want to choose inputs.
- Personalised Streamlit display.
- Refactored code and added in comments since the repository will be made public soon.

#### **🛑 Blockers/Challenges**

- No blockers.

#### **👣 Next Steps** 

- To record video of Streamlit to show how the web app works.
- Repository to be made public on Christmas Eve.

<br>

----

<br>

## Day 12: 24/12

#### **🎯 Main Objective**
Deploy the Streamlit app for public use without requiring users to download the project repository.

#### **✅ Accomplished Tasks**
- Attempted deployment using Streamlit Cloud.
- Debugged deployment issues related to libraries installed via conda.
- Reinstalled libraries but still encountered the same issues, possibly linked to Homebrew-installed packages.

#### **🛑 Blockers/Challenges**
- Despite thorough debugging efforts, deployment using Streamlit Cloud was unsuccessful.

#### **💡 Reflection** 
- Going forward, I think it best to explore other ways to create and deploy apps outside of Streamlit. This will likely become my next project for the new year, as I’ve faced deployment challenges with Streamlit apps in previous projects as well.
- To write a blog post summarising key concepts of prompt engineering and sharing implementation steps of this project.
