---
layout: page
title: CS61B
description: "CS61B notes"
permalink: /cs61b/
sitemap: false
noindex: true
category: base
---

<hr class="gh">
<div class="posts">
  {% for post in site.categories.cs61b %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ site.url }}{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

 {% if post.description.size > 0 %}{{ post.description | markdownify | remove: '<p>' | remove: '</p>' }}{% else %}{{ post.excerpt | markdownify | remove: '<p>' | remove: '</p>' }}{% endif %}
  </div>
  {% unless forloop.last %}<hr class="transp">{% endunless %}
  {% endfor %}
</div>
