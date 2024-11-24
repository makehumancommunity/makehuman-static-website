---
title: "Import paths for MakeHuman"
draft: false
weight: 5
description: "Options when importing from MakeHuman"
alwaysopen: false
---

There are a few ways to import from MakeHuman, each with their pros and cons.

## Importing via MHM

This is the recommended import path. This will give you a human character functionally equivalent of a human
which was modeled from scratch in MPFB.

Most importantly, this will allow you to continue to work on the character in MPFB, for example modifying
target values or adding clothes.

The downside is that there are a few configuration options you need to keep track of.

See main article, [Importing via MHM]({{% relref "importing_via_mhm" %}})

## Importing via Socket

This is the previously recommended import path. This will import a set of _baked_ meshes from MakeHuman via
an socket connection. 

While the upside is that you need not do a few configuration steps in MPFB, the downside is that the meshes
you get are baked and cannot be worked on further with MPFB. Most importantly, you will not be able to equip
clothes or modify target values. 

See main article, [Importing via Socket]({{% relref "importing_via_socket" %}})

## Mostly non-functional import paths

There are also older ways in which MakeHuman characters could be imported. These are mostly non-functional
in the sense that they do not work at all or give unsatisfactory results:

* MHX: This was the recommended import path in ancient times. However, MHX is not updated to work with recent Blender versions.
* Collada: Exporting to collada in MakeHuman and then importing into blender works so-so, but materials will need to be adjusted
* FBX: Exporting to FBX in MakeHuman and then importing into blender results in an unusable rig and a broken mesh. It is currently unclear why, but the FBX implementation in MakeHuman is based on an ancient reverse engineering of the FBX binary format.

