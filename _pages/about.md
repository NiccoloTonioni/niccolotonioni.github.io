---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
Hello!

I am a PhD candidate in Fluid Mechanics at Université de Poitiers. My research focuses on fluid dynamical system prediction and reduced-order modeling 🌪️, leveraging deep learning methods such as autoencoders and transformers 🤖.

I am a proud alumnus of the Von Karman Institute. My European academic journey has taken me across Italy 🇮🇹, Belgium 🇧🇪, and France 🇫🇷, shaping both my research perspective and my appreciation for diverse cultures. Having lived in Belgium for over three years, I remain deeply connected to its culture 🍟🍫. However, as a true Italian at heart, pizza reigns supreme.

## News

---

### 2025

* **September 2025 – VIVALDy Preprint Paper: Extended version of the framework presented at AiFluids, Chania**  
  Our latest work extends the framework initially presented at AiFluids 2025 with deeper analysis of the learned latent space dynamics. VIVALDy combines a β-VAE-GAN architecture with transformers to reconstruct vortex-induced vibrations from cylinder displacement alone, revealing physically meaningful flow structures through latent space topology.  
  [Project page](https://niccolotonioni.github.io/vivaldy.github.io/) | [Preprint](https://arxiv.org/abs/2509.24965)

* **July 2025 – Presented at THMT25, Tokyo**  
  I presented an extension of the work presented at EUROMECH 629, with deeper analysis of the latent space, and the possibility for the model to reconstruct 3D fields.

* **May 2025 – VIVALDy debuts at AiFluids, Chania**  
  Our latest framework, VIVALDy, was presented at AiFluids 2025. It combines a β-VAE-GAN architecture with transformers to reconstruct vortex-induced vibrations from cylinder displacement alone.

* **April 2025 – Presented at EUROMECH 629, London**  
  Our work on modeling near-wall turbulence using a β-VAE-GAN and transformer framework was presented at EUROMECH 629.

* **February 2025 – Presented at DTE AICOMAS, Paris**  
  Our work on reduced-order modeling of experimental turbulent flows was presented at DTE-AICOMAS 2025, covering POD, variational autoencoders, and advanced ROM techniques.

## Photos from around the world

*A glimpse of the cities where research takes me*

<div class="photo-carousel">
  <div class="carousel-container">
    <div class="carousel-slide active">
      <img src="/photos_world/DSCF1704.jpg" alt="Minato City skyline at midnight">
      <p><em>Tokyo, Japan</em> - Minato City skyline at midnight during THMT 2025</p>
    </div>
    <div class="carousel-slide">
      <img src="/photos_world/DSCF1861.jpg" alt="Godzilla in Shinjuku">
      <p><em>Tokyo, Japan</em> - ゴジラ (Gojira) at Shinjuku during THMT 2025</p>
    </div>
    <div class="carousel-slide">
      <img src="/photos_world/PXL_Chania_Goat.jpg" alt="Goat in Chania">
      <p><em>Chania, Greece</em> - Wonderful goat near AiFluids 2025 venue</p>
    </div>
    <div class="carousel-slide">
      <img src="/photos_world/PXL_Chania_Monk.jpg" alt="Holy Trinity Monastery">
      <p><em>Chania, Greece</em> - Agia Triada Monastery after AiFluids 2025</p>
    </div>
  </div>
  
  <!-- Navigation buttons -->
  <button class="carousel-btn prev" onclick="changeSlide(-1)">❮</button>
  <button class="carousel-btn next" onclick="changeSlide(1)">❯</button>
  
  <!-- Dots indicator -->
  <div class="carousel-dots">
    <span class="dot active" onclick="currentSlide(1)"></span>
    <span class="dot" onclick="currentSlide(2)"></span>
    <span class="dot" onclick="currentSlide(3)"></span>
    <span class="dot" onclick="currentSlide(4)"></span>
  </div>
</div>

<style>
.photo-carousel {
  position: relative;
  max-width: 800px;
  margin: 2rem auto;
}

.carousel-container {
  position: relative;
  width: 100%;
}

.carousel-slide {
  display: none;
  text-align: center;
}

.carousel-slide.active {
  display: block;
}

.carousel-slide img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.carousel-slide p {
  margin-top: 1rem;
  font-size: 0.9rem;
}

.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 16px;
  cursor: pointer;
  font-size: 18px;
  border-radius: 4px;
  transition: background 0.3s;
}

.carousel-btn:hover {
  background: rgba(0, 0, 0, 0.8);
}

.carousel-btn.prev {
  left: 10px;
}

.carousel-btn.next {
  right: 10px;
}

.carousel-dots {
  text-align: center;
  margin-top: 1rem;
}

.dot {
  height: 12px;
  width: 12px;
  margin: 0 5px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  cursor: pointer;
  transition: background-color 0.3s;
}

.dot.active,
.dot:hover {
  background-color: #717171;
}
</style>

<script>
let currentSlideIndex = 1;
showSlide(currentSlideIndex);

function changeSlide(n) {
  showSlide(currentSlideIndex += n);
}

function currentSlide(n) {
  showSlide(currentSlideIndex = n);
}

function showSlide(n) {
  let slides = document.querySelectorAll('.carousel-slide');
  let dots = document.querySelectorAll('.dot');
  
  if (n > slides.length) { currentSlideIndex = 1; }
  if (n < 1) { currentSlideIndex = slides.length; }
  
  slides.forEach(slide => slide.classList.remove('active'));
  dots.forEach(dot => dot.classList.remove('active'));
  
  slides[currentSlideIndex - 1].classList.add('active');
  dots[currentSlideIndex - 1].classList.add('active');
}
</script>

