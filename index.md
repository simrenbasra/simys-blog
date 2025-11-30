---
layout: page 
title: ""
permalink: /
---

<style>
  /* Resize all images inside post excerpts */
  .home-post-excerpt img, 
  .home-post-excerpt p img {
    max-width: 200px !important;
    height: auto !important;
    display: block;
    margin: 10px auto; /* center the images */
  }
</style>


<div style="text-align: center; margin: 20px 0;">
  <img src="{{ site.baseurl }}/assets/index/index_cover_banner.png" 
       alt="Banner" 
       style="width: 100%; max-width: 1200px; height: auto;">
</div>

<h3 style="text-align:center;">
  <strong>Hey, I’m Simy - welcome to my blog!</strong>
</h3>

I build AI projects, explain what I learn, and try not to break too many things along the way...

<br> 

### **Want to Learn AI from Scratch? 🤖**

Subscribe to my newsletter, Simy Says!

<div style="text-align: center;">
  <iframe src="https://simrenbasra.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
</div>

**First Newsletter Series: Foundation**

This 5-part series is designed for complete novices to introduce the basics of AI and machine learning in a fun, beginner-friendly way.

**Out Now!**

<br> 

### Upcoming Posts
  
#### **SimBot 💬**

I’m building a custom chatbot for my blog that can answer questions and guide readers through my past posts!

<br> 

----- 

<br>

### Most Recent Posts

<div class="home-post-excerpt">
  {% for post in site.posts limit:3 %}
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 30px; gap: 20px;">
      <!-- Text on the left -->
      <div style="max-width: 400px; text-align: left;">
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
        <p>{{ post.excerpt | strip_html }}</p>
      </div>
      <!-- Image on the right -->
      {% if post.thumbnail %}
        <img src="{{ post.thumbnail }}" alt="{{ post.title }}" style="max-width: 150px; height: auto;">
      {% endif %}
    </div>
  {% endfor %}
</div>


<a href="/simys-blog/my_projects/">View all posts →</a>
