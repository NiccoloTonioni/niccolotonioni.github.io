---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
# Hi, I'm Niccolò

🌊 Turbulent Flows · 🤖 Deep Learning · 📉 Reduced-Order Modelling · 🔬 CFD

Hello!

I am a PhD candidate in Fluid Mechanics at Université de Poitiers. My research focuses on fluid dynamical system prediction and reduced-order modeling 🌪️, leveraging deep learning methods such as autoencoders and transformers 🤖.

I am a proud alumnus of the Von Karman Institute 🎓. My European academic journey has taken me across Italy 🇮🇹, Belgium 🇧🇪, and France 🇫🇷, shaping both my research perspective and my appreciation for diverse cultures. Having lived in Belgium for over three years, I remain deeply connected to its culture 🍟🍫. However, as a true Italian at heart, pizza reigns supreme.

News
======

{% assign news_sorted = site.data.news | sort: "date" | reverse %}
{% for item in news_sorted %}
<div class="news-item">
  <p>
    <strong>
      {% if item.link %}<a href="{{ item.link }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
    </strong>
    {% if item.ai_generated %}<span class="badge-ai">AI-generated</span>{% endif %}
    <br>
    <small class="news-date">{{ item.date | date: "%B %Y" }}</small>
  </p>
  <p>{{ item.snippet }}</p>
</div>
{% endfor %}

Photos from around the world
======
*A glimpse of the cities where research takes me*

<div class="photo-gallery">
  <div class="photo-item">
    <img src="/images/chania-harbor.jpg" alt="Chania Harbor at sunset">
    <p><em>Chania, Greece</em> - Venetian Harbor during AiFluids 2025</p>
  </div>
  
  <div class="photo-item">
    <img src="/images/london-thames.jpg" alt="London Thames view">
    <p><em>London, UK</em> - Thames view near EUROMECH 629 venue</p>
  </div>
  
  <div class="photo-item">
    <img src="/images/paris-seine.jpg" alt="Paris Seine at dusk">
    <p><em>Paris, France</em> - Seine reflections after DTE AICOMAS 2025</p>
  </div>
</div>

