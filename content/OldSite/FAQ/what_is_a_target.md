---
title: "What is a target?"
draft: false
---

In the simplest form, a target is roughly equivalent with a slider inside MakeHuman (it's not exactly as easy as that, but it's a reasonable summary). 

Targets are used internally by MH to deform the basemesh. They are the magic that happens when you pull some of the sliders. Behind each of the sliders in MH there is one or multiple targets that are created by artists. Those are usually created for one specific characteristic, so you can apply them individually, but you can put as many combined transformations in them as you want.

Custom targets are targets that you can create yourself for achieving other transformations than those obtained within MH itself. Often they are used for more specific things like creating fantasy characters.

Technically, a target is a collection of relative offsets of vertices of the basemesh. They remain compatible with new versions of makehuman as long as the basemesh does not change (which it did between 1.0.x and 1.1.x).

For a longer discussion on targets, see [[ Documentation:MHBlenderTools: MakeTarget|MHBlenderTools: MakeTarget ]]