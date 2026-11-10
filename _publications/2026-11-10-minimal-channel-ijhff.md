---
title: "A Hybrid Generative Reduced-Order Model for the Minimal Flow Unit"
authors: "Niccolò Tonioni, Lionel Agostini, Marcial Sanchis-Agudo, Mohammad Umair, Franck Kerhervé, Laurent Cordier, Ricardo Vinuesa"
collection: publications
category: manuscripts
permalink: "/publication/2026-11-10-minimal-channel-ijhff"
excerpt: 'Near-wall turbulence, Reduced-Order Models, Minimal Flow Unit, Generative AI, Transformers, Variational Autoencoder, Generative Adversarial Networks'
date: 2026-11-10
venue: 'International Journal of Heat and Fluid Flow'
paperurl: 'https://doi.org/10.1016/j.ijheatfluidflow.2026.110784'
citation: 'Tonioni, N., Agostini, L., Sanchis-Agudo, M., Umair, M., Kerhervé, F., Cordier, L., & Vinuesa, R. (2026). A Hybrid Generative Reduced-Order Model for the Minimal Flow Unit. International Journal of Heat and Fluid Flow, 122, 110784.'
pubtype: 'journal'
---

## Abstract

This work introduces an equation-free, data-driven reduced-order model for wall-bounded turbulent flows, designed for potential integration into active control loops. The framework integrates a β-VAE-GAN for non-linear spatial dimensionality reduction with a sensor-conditioned Easy Attention Transformer for temporal evolution. Evaluated on the Minimal Flow Unit at Re<sub>τ</sub> = 200 at y<sup>+</sup> = 14, the architecture compresses the flow into a four-variable latent space while preserving the turbulent kinetic energy and integral length scales. This learned manifold autonomously isolates the low-frequency signatures of the near-wall intermittent regeneration cycle. By conditioning the Transformer on three sensors, the model sustains accurate latent trajectories over extended horizons from a minimal initialization window. End-to-end inference reconstructs flow fields near the upper limit of the compression stage, with quadrant analysis confirming the accurate capture of dominant ejection and sweep events. While extreme bursts are slightly attenuated, the framework's ability to track alternating active and quiescent phases demonstrates its potential as a robust state-estimator for future model-based control applications.

[Paper](https://doi.org/10.1016/j.ijheatfluidflow.2026.110784) | [arXiv](https://arxiv.org/abs/2606.09044) | [Code](https://github.com/NiccoloTonioni/minimal_channel_generative_code)
