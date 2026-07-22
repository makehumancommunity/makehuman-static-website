---
title: "Randomizing characters"
draft: false
weight: 27
description: "How to generate random characters with MPFB in Blender: randomized body shapes, skins, body parts and clothes, one character at a time or in batches."
alwaysopen: false
---

**NOTE THAT THIS FEATURE REQUIRES MPFB 2.0.17**

MPFB can generate random characters for you. This is useful when you want to quickly populate a scene with varied
background characters, or when you simply want a starting point that is not the default neutral human. The
randomization is controlled rather than chaotic: you decide which attributes are allowed to vary, how far from a
neutral value they may stray, and which assets (skins, hair, clothes and so on) may be picked.

You will find the functionality in the "Random human" panel, which is located under the "New human" panel on the
MPFB tab in the N-panel shelf of the 3D viewport. It is collapsed by default.

![The Random human panel in the MPFB sidebar](randomize_panel.png)

In its simplest form, using the feature is a one-click operation: expand the "Random human" panel and click
"Create random human" in the "Creation settings" sub-panel. This will generate a character with the default
randomization settings. Everything else in the panel is there to let you tune what "random" should mean.

The panel is organized into a set of collapsible sub-panels: Presets, General settings, Macrodetails, Breast shape,
Details, Skin, Body parts, Clothes, Creation settings and Batch. Each is described on its own page below.

## Concepts

Before diving into the individual settings, it is worth understanding a few core concepts, such as seeds,
distributions and deviations. These are shared by all parts of the randomization:

* [Randomization concepts]({{% relref "concepts" %}}): Seeds, probability distributions, deviations and presets

## The parts of the randomization

* [Phenotype]({{% relref "phenotype" %}}): Randomizing macrodetails such as age, gender, height and race
* [Details]({{% relref "details" %}}): Randomizing detail features such as nose shape or eye position
* [Skin]({{% relref "skin" %}}): Picking a random skin from your installed skin assets
* [Body parts]({{% relref "bodyparts" %}}): Picking random hair, eyes, eyebrows, eyelashes, teeth and tongue
* [Clothes]({{% relref "clothes" %}}): Dressing the character with random clothes
* [Creation settings]({{% relref "creation" %}}): Rig, scale and other settings for the generated character
* [Batch generation]({{% relref "batch" %}}): Generating many characters in one go
