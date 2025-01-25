---
title: "MPFB says 'cannot .. on a baked mesh'"
draft: false
---

Under normal circumstances, you are working on a live character in MPFB. It has shape keys for model parameters and
helper geometry for fitting clothes. If this is the situation and you still see the message, then this should be
reported as a bug.

However, there are also circumstances where the character is "baked". This means that shape keys have been applied
(or did not exist in the first place) or other properties of the character are missing or have been applied. 

This will happen for example when:

* Having imported a character via socket from MakeHuman
* Having done "operations" -> "basemesh" -> "bake all shapekeys"

In these cases, important things are missing for MPFB to be able to do modeling or equipping assets. 

For the import from MakeHuman, the solution is to [import via MHM]({{% relref "../Docs/makehuman/importing_via_mhm" %}}) instead of via socket. 

## Advanced

If you want to override this behavior and perform some operations anyway, there is a checkbox "Override bake check" under "Apply assets" -> "Library settings"
-> "Advanced". There are situations where this makes sense. However, you should not be surprised if MPFB displays unexpected behavior if you do stuff
using the override.
