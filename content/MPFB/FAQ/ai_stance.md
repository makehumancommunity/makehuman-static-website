---
title: "What is your stance on AI?"
draft: false
description: "MPFB intends to align with Blender's general stance on AI"
---

The question about AI is difficult and lots of aspects need to be taken into account. For a small project, this might seem overwhelming. 

After some discussions we have decided to align as closely as possible with Blender's AI policies, which makes sense given that 
MPFB is a Blender extension. We are aware extensions are not required to follow these policies, but given that Blender has the muscles 
needed to think this through, we opt to trust their conclusions.

Blender has the following documents so far; [Blender's AI contribution policy](https://developer.blender.org/docs/handbook/contributing/ai_contributions/) 
and a [short statement](https://www.blender.org/news/upcoming-blender-development-fund-and-ai-policies/). In the latter, the central quote 
is this:

> Blender is a tool for artists and creators, it’s made by humans for humans. No generative AI functionality is currently available or planned to be integrated in Blender.

This is true for MPFB too. We are not going to include any generative AI functionality per se in the MPFB extension. Functionality which makes 
using generative AI somewhere else easier is within scope, for example exporting OpenPose files. But generative AI as such will not 
be included in the MPFB extension.

Regarding the assets, we will not change the existing policy: It's the contributor's responsibility to ensure an asset does not violate
any copyright or trademark. This does not change just because AI has been used.

This said:

- None of the system assets (in the system assets pack) have been generated with AI, nor has the base mesh or targets
- To our knowledge, none of the user contributed assets in the other asset packs have been generated with AI. But this is a guess based mainly on the age of the assets. Users are not obliged to tell us about this.

We _are_ experimenting with AI-assisted toolchains for mass rendering honest images showing what assets look like (for example in thumbnails). So far this mostly involves having AI positioning cameras and lights
based on asset coordinates.
