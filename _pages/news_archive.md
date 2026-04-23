---
layout: archive
title: "News Archive"
permalink: /news/
author_profile: true
---

<style>
.news-archive-container {
    margin-top: 20px;
    border-left: 3px solid #549B8C;
    padding-left: 25px;
}
.news-archive-item {
    margin-bottom: 30px;
    position: relative;
}
.news-archive-item::before {
    content: '';
    position: absolute;
    left: -33px;
    top: 6px;
    width: 13px;
    height: 13px;
    background: #549B8C;
    border: 3px solid #fff;
    border-radius: 50%;
    box-shadow: 0 0 0 2px #549B8C;
}
.news-archive-year {
    margin-top: 40px;
    margin-bottom: 20px;
    color: #549B8C;
    font-weight: bold;
    font-size: 1.3em;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
}
.news-archive-date {
    font-size: 0.82em;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
}
.news-archive-title {
    font-weight: 600;
    font-size: 1.0em;
    color: #2c3e50;
    margin-bottom: 4px;
}
.news-archive-snippet {
    color: #555;
    font-size: 0.9em;
    line-height: 1.5;
    margin: 4px 0 8px 0;
}
.news-archive-links {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.news-archive-link {
    padding: 3px 10px;
    background: #f5f5f5;
    border-radius: 12px;
    font-size: 0.78em;
    color: #444;
    text-decoration: none;
    border: 1px solid #e0e0e0;
    transition: all 0.2s ease;
}
.news-archive-link:hover {
    background: seagreen;
    color: white;
    border-color: seagreen;
}
</style>

<div class="news-archive-container">
{% assign news_sorted = site.data.news | sort: "date" | reverse %}
{% assign last_year = "" %}
{% for item in news_sorted %}
  {% assign current_year = item.date | date: "%Y" %}
  {% if current_year != last_year %}
    <h2 class="news-archive-year">{{ current_year }}</h2>
    {% assign last_year = current_year %}
  {% endif %}
  <div class="news-archive-item">
    <div class="news-archive-date">{{ item.date | date: "%B %d, %Y" }}</div>
    <div class="news-archive-title">{{ item.title }}</div>
    {% if item.snippet %}<p class="news-archive-snippet">{{ item.snippet }}</p>{% endif %}
    <div class="news-archive-links">
      {% if item.link %}<a href="{{ item.link }}" class="news-archive-link">🔗 Read more</a>{% endif %}
      {% if item.paper %}<a href="{{ item.paper }}" class="news-archive-link" target="_blank">📄 Paper</a>{% endif %}
      {% if item.arxiv %}<a href="{{ item.arxiv }}" class="news-archive-link" target="_blank">📃 arXiv</a>{% endif %}
      {% if item.webpage %}<a href="{{ item.webpage }}" class="news-archive-link" target="_blank">🌐 Project</a>{% endif %}
      {% if item.code %}<a href="{{ item.code }}" class="news-archive-link" target="_blank">💻 Code</a>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
