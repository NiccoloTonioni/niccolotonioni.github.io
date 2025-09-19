---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Fluid Mechanics, Universitè de Poitiers 🇫🇷, 2026 (expected)
* M.S. in Fluid Dynamics, Von Karman Institute 🇧🇪, 2023
* M.S. in Aerospace Engineering, Université de Liège 🇧🇪, 2022
* M.S. in Aeronautical Engineering, Politecnico di Milano 🇮🇹, 2022
* B.S. in Aerospace Engineering, Politecnico di Milano 🇮🇹, 2019

Work experience
======
* Jun. 2025: Visiting PHD Student
  * Department of Chemical Engineering and Technology, KTH 🇸🇪
  * Host: Christophe Duwig

* Apr. 2024 - Jun. 2024: Visiting PHD Student
  * Vinuesa Lab, KTH 🇸🇪
  * Supervisor: Ricardo Vinuesa

* Oct. 2022 - Jun. 2023: Postgraduate Intership
  * Turbomachinery and Propulsion Department, VKI 🇧🇪
  * Supervisor: Frank Eulitz, Sergio Lavagnoli

* Feb. 2022 - Sep. 2022: Master Thesis Intership
  * Aerospace and Mechanical Engineering Department, ULiège 🇧🇪
  * Multiphysic and Turbulent Flow Computation Group,
  * Supervisor: Vincent Terrapon, Koen Hillewaert  
  
Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
