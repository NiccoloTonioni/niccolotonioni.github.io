---
title: "Simulation of a wingtip vortex flow with Linear Eddy Viscosity turbulence models at Re=4.6E6 and Re=1.2E6"
authors: "Niccolò Tonioni"
collection: publications
category: masterthesis
permalink: /publication/2022-10-06-simulation-wingtip-vortex
excerpt: 'Linear Eddy Viscosity Models, wingtip vortex, Large Eddy Simulations, Reynolds Average Navier-Stokes simulations.'
date: 2022-10-06
venue: 'Politecnico di Milano, Universitè de Liege'
paperurl: 'https://www.politesi.polimi.it/handle/10589/195016'
---

## Abstract

This work studies the accuracy of Linear Eddy Viscosity models on the prediction of wingtip vortex flow. The geometry selected for the study is a NACA-0012 half wing mounted at the wall, with a rounded end cap and trailing edge, inclined by 10° at its quarter chord. Computations of the flow were conducted using the open source software SU2. Two turbulence closures were investigated: the Negative Spalart-Allmaras and the Menter's Shear Stress Transport models. The flow was considered at two Reynolds and Mach numbers: Re = 4.3 × 10⁶, M = 0.14 and Re = 1.2 × 10⁶, M = 0.1. To study the models accuracy, the initial objective of the work was to produce high-fidelity LES data using the software ARGO provided by Cenaero. However, due to the setup of the simulations and the computing time requirements, we were not able to obtain statistically steady LES simulations of the entire wing. Therefore, the computed flow is compared against the experimental and numerical data found in the literature. The results showed that the Linear Eddy Viscosity models could characterize the main vortical structures' topology and surface flow quantities. However, they fail to predict the evolution of the mean quantities on the vortex core. This divergence between the numerical simulations and the experimental results was associated with the eddy viscosity, which caused a diffusion of the mean quantities. Moreover, it was noted that, due to the models' assumptions, the Linear Eddy Viscosity models cannot correctly represent the Reynolds stress and strain rate tensors misalignment observed in the experimental data. Although we could not fulfill the project's initial objective, we were still able to provide indications of how to continue this work by comparing the RANS results with the reference experimental and numerical data, notably how supervised learning techniques could be employed to build improved turbulence models.

[Thesis](https://www.politesi.polimi.it/handle/10589/195016)