---
title: "Adding bodyparts"
draft: false
weight: 50
description: "How to add body parts such as eyes, eyebrows, eyelashes, hair and teeth to an MPFB character in Blender from the asset library."
alwaysopen: false
---

Everything which is not the body as such needs to be attached to the body. This includes things such as:

* Hair
* Eyeballs
* Eyebrows and eyelashes
* Tongue
* Teeth

## Adding eyes

Before adding eyes, it might make sense to read up on You might want to read up on [material models]({{% relref "../Materials" %}}) to get some background information. 
In quick summary, you can choose between texture based eye materials ("MakeSkin", "GameEngine") or procedural based eyes ("procedural eyes"). This choice is made
on the "apply assets" -> "library settings" -> "materials" panel. 

Once that choice has been made, you can load eyeballs from the "Apply assets" -> "eyes" panel

![Loading eyeballs onto an MPFB character from the apply-assets eyes panel](bodypartseye.png)

There are only two eyes to choose between:

* High poly: This has an outer glass layer which is only visible when using procedural eyes
* Low poly: This is a simple sphere with only one layer

## Adding other bodyparts

For all other body parts, simply add them from their respective part of the "apply assets" panel. For example hair:

![Loading hair onto an MPFB character from the apply-assets hair panel](bodypartshair.png)

