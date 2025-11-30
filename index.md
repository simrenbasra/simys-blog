---
layout: home 
title: ""
---

<div style="text-align: center; margin: 20px 0;">
  <img src="{{ site.baseurl }}/assets/index/index_cover_banner.png" 
       alt="Banner" 
       style="width: 100%; max-width: 1200px; height: auto;">
</div>

<h2 style="text-align:center;">
  <strong>Hey, I’m Simy - welcome to my blog!</strong>
</h2>

I build AI projects, explain what I learn, and try not to break too many things along the way...

<br> 

## **Want to Learn AI from Scratch? 🤖**

Subscribe to my newsletter, Simy Says!

<div style="text-align: center;">
  <iframe src="https://simrenbasra.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
</div>

**First Newsletter Series: Foundation**

This 5-part series is designed for complete novices to introduce the basics of AI and machine learning in a fun, beginner-friendly way.

**Out Now!**

<br> 

## Upcoming Posts
  
### **SimBot 💬**

I’m building a custom chatbot for my blog that can answer questions and guide readers through my past posts!

<br> 

----- 

<br>

{% for post in site.posts limit:3 %}
  <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  <p>{{ post.excerpt }}</p>
{% endfor %}
<a href="/projects">View all posts →</a>
