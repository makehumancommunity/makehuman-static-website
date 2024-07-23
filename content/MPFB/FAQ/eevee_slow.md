---
title: "Why is rendering/animation on eevee slow?"
date: 2017-10-17T15:26:15Z
draft: false
---

When using default settings, Eevee can be experienced as very slow in the viewport and when rendering, if there is a human visible.

This is because you are most likely using the "multilayered" skin material model. This is geared towards single renders using Cycles,
and is less useful together with Eevee. It is a very complex procedural material.

If your use case is more in the realm of animation and needs efficiency, you might need to consider using another material model 
for both the skin and the eyes.

On the "apply assets" -> "library settings" panel there is a section "Materials". Here you can choose which material model to
use for different aspects of the human.

If you do not need any procedural aspects and prefer using materials with image textures, choose "MakeSkin" on everything. Alternatively, 
if you intend to export to an external application, the "GameEngine" material might make sense too.
