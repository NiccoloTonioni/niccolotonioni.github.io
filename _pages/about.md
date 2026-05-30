---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<p class="interest-tags">
  <span class="interest-tag">🌊 Turbulent Flows</span>
  <span class="interest-tag">🧬 AI4Science</span>
  <span class="interest-tag">🤖 Deep Learning</span>
  <span class="interest-tag">📉 Reduced-Order Modelling</span>
</p>

I am a PhD candidate in **Fluid Mechanics** at **Université de Poitiers**. My research focuses on prediction and reduced-order modeling of turbulent flows, leveraging **deep learning** methods such as autoencoders and transformers.

I am an alumnus of the **Von Karman Institute**. My European academic journey has taken me across Italy, Belgium, and France, shaping both my research perspective and my appreciation for diverse cultures. Having lived in Belgium for over three years, I remain deeply connected to its culture. However, as a true Italian at heart, pizza reigns supreme.

<div style="display:flex; justify-content:space-between; align-items:baseline; margin: 1.5em 0 0.6em;">
  <h2 style="margin:0;">Latest News</h2>
  <a href="/news/" style="font-size:0.8rem; color:seagreen; text-decoration:none; font-weight:600; border-bottom:none;">All news →</a>
</div>

<div class="news-timeline">
{% assign news_sorted = site.data.news | sort: "date" | reverse %}
{% for item in news_sorted limit:5 %}
<div class="news-card">
  <div class="news-dot"></div>
  <div class="news-card__date">{{ item.date | date: "%B %Y" }}</div>
  <div class="news-card__body">
    <strong>{{ item.title }}</strong>
    {% if item.snippet %}<p>{{ item.snippet }}</p>{% endif %}
    {% if item.paper or item.arxiv or item.webpage or item.code %}
    <div class="news-card__links">
      {% if item.paper %}<a href="{{ item.paper }}" class="news-link" target="_blank">📄 Paper</a>{% endif %}
      {% if item.arxiv %}<a href="{{ item.arxiv }}" class="news-link" target="_blank">📃 arXiv</a>{% endif %}
      {% if item.webpage %}<a href="{{ item.webpage }}" class="news-link" target="_blank">🌐 Project</a>{% endif %}
      {% if item.code %}<a href="{{ item.code }}" class="news-link" target="_blank">💻 Code</a>{% endif %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>

Photos from around the world
======
*A glimpse of the cities where research takes me*

<div class="photo-carousel" id="photoCarousel">
  <div class="photo-carousel__track" id="carouselTrack">
    <div class="photo-carousel__slide">
      <img src="/photos_world/minato-city.jpg" alt="Minato city skyline">
      <p class="photo-carousel__caption"><em>Tokyo, Japan</em> — Minato city skyline at midnight during THMT 2025</p>
    </div>
    <div class="photo-carousel__slide">
      <img src="/photos_world/godzilla.jpg" alt="Godzilla head">
      <p class="photo-carousel__caption"><em>Tokyo, Japan</em> — ゴジラ (Gojira) at Shinjuku during THMT 2025</p>
    </div>
    <div class="photo-carousel__slide">
      <img src="/photos_world/chania-goat.jpg" alt="Beautiful chania goat">
      <p class="photo-carousel__caption"><em>Chania, Greece</em> — Wonderful goat near AiFluids 2025 venue</p>
    </div>
    <div class="photo-carousel__slide">
      <img src="/photos_world/chania-monk.jpg" alt="Agia Triada Monastery">
      <p class="photo-carousel__caption"><em>Chania, Greece</em> — Agia Triada Monastery after AiFluids 2025</p>
    </div>
  </div>
  <button class="photo-carousel__btn photo-carousel__btn--prev" aria-label="Previous">&#8249;</button>
  <button class="photo-carousel__btn photo-carousel__btn--next" aria-label="Next">&#8250;</button>
  <div class="photo-carousel__dots">
    <button class="photo-carousel__dot active" aria-label="Slide 1"></button>
    <button class="photo-carousel__dot" aria-label="Slide 2"></button>
    <button class="photo-carousel__dot" aria-label="Slide 3"></button>
    <button class="photo-carousel__dot" aria-label="Slide 4"></button>
  </div>
</div>

<script>
(function () {
  var carousel = document.getElementById('photoCarousel');
  var track    = carousel.querySelector('.photo-carousel__track');
  var dots     = carousel.querySelectorAll('.photo-carousel__dot');
  var total    = carousel.querySelectorAll('.photo-carousel__slide').length;
  var current  = 0;
  var startX   = 0;

  function goTo(n) {
    current = ((n % total) + total) % total;
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    dots.forEach(function (d, i) { d.classList.toggle('active', i === current); });
  }

  carousel.querySelector('.photo-carousel__btn--prev').addEventListener('click', function () { goTo(current - 1); });
  carousel.querySelector('.photo-carousel__btn--next').addEventListener('click', function () { goTo(current + 1); });
  dots.forEach(function (d, i) { d.addEventListener('click', function () { goTo(i); }); });

  track.addEventListener('touchstart', function (e) { startX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend',   function (e) {
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 40) goTo(current + (dx < 0 ? 1 : -1));
  }, { passive: true });
}());
</script>

