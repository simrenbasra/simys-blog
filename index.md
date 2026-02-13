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
  <strong>Hey, I’m Simy! Welcome to my blog!</strong>
</h3>

I build AI projects, explain what I learn, and try not to break too many things along the way...

<br> 

## Upcoming Posts
  
#### **SimBot 💬**

I’m building a custom chatbot for my blog that can answer questions and guide readers through my past posts!

<br> 

----- 

<br>

## Recent Posts

{% for post in site.posts limit:5 %}
  <div style="margin-bottom: 20px;">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p style="color: #555; font-size: 0.9em; margin-bottom: 5px;">
      {{ post.date | date: "%b %-d, %Y" }}
    </p>
    <p>{{ post.excerpt | strip_html }}</p>
  </div>
{% endfor %}

<a href="/simys-blog/my_posts/">View all posts →</a>
