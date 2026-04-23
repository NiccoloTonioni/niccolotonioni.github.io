---
title: "VIVALDy: A Hybrid Generative Reduced-Order Model for Turbulent Flows, Applied to Vortex-Induced Vibrations"
authors: "Niccolò Tonioni, Lionel Agostini, Franck Kerhervé, Laurent Cordier, Ricardo Vinuesa"
collection: publications
category: manuscripts
permalink: "/publication/2026-04-03-vivaldy-prf"
excerpt: 'Machine-Learning, Deep Learning, Reduced-Order Models, Turbulent Flows, Vortex-Induced Vibrations'
date: 2026-04-03
venue: 'Physical Review Fluids'
paperurl: 'https://journals.aps.org/prfluids/abstract/10.1103/t7d2-mv5c'
citation: 'Tonioni, N., Agostini, L., Kerhervé, F., Cordier, L., & Vinuesa, R. (2026). VIVALDy: A Hybrid Generative Reduced-Order Model for Turbulent Flows, Applied to Vortex-Induced Vibrations. Physical Review Fluids, 11, 044902.'
pubtype: 'journal'
---

## Abstract

Developing reduced-order models applicable to fluid-dynamics problems involving complex geometries and different flow conditions remains a critical challenge for turbulent flows. This study introduces VIVALDy, a novel machine-learning framework that employs a hybrid β-Variational Autoencoder-Generative Adversarial Network (β-VAE-GAN) architecture with masked convolutions to extract dominant flow features into a compact latent space while preserving fidelity at solid-fluid interfaces. A bidirectional transformer then models the temporal evolution of these features, learning to predict flow trajectories from minimal sensor inputs. This two-stage approach enables the transformer to map sensor measurements to dominant flow variables identified by the autoencoder, advancing reduced-order modeling capabilities for real-time flow prediction. The effectiveness of the framework is demonstrated through application to a problem relevant to vortex-induced vibration (VIV) energy harvesting systems, reconstructing the turbulent flow around a one-degree-of-freedom moving cylinder. Validated against experimental data spanning fluid-structure interaction regimes of interest, VIVALDy accurately predicts different flow states using only the cylinder displacement.

[Paper](https://journals.aps.org/prfluids/abstract/10.1103/t7d2-mv5c) | [arXiv](https://arxiv.org/abs/2509.24965) | [Project Page](https://niccolotonioni.github.io/vivaldy.github.io/)
