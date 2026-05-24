---
title: "Clothes, hair and body parts"
draft: false
weight: 15
description: "How MPFB models clothes, hair and body parts as MHCLO-based assets in Blender, including how each type binds to the basemesh helpers."
---

All mesh assets attached to the Basemesh are actually technically the same thing: MHCLO assets. Thus not only clothes are "clothes". Eyelashes, eyes, tongue, teeth and hair are technically "clothes" too.

An MHCLO asset is in rough summary a mesh object combined with instructions on how a vertex on the asset should be matched with a vertex on the Basemesh.

![MPFB character wearing a MHCLO work-suit asset in Blender](mhclo_worksuit.png)

When modifying the shape of the Basemesh, the clothes will deform with it. 

![MPFB MHCLO clothes deforming together with the basemesh in Blender](mhclo_deform.png)

Note that if you change the basemesh after having equipped the clothes, you either have to click "refit assets to basemesh" or check the "auto refit assets" for the clothes to actually adapt to the updated basemesh.
