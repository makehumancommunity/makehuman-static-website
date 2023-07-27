---
title: "MakeSkin"
draft: false
weight: 5
description: "Description of the default MPFB material"
---

The default material model in MPFB (and in MakeHuman) is "MakeSkin", also known as "MHMAT", "plain material" and "default material". This material 
is serialized to a simple text descriptor, listing which texture files that are used and set of other settings. The descriptor is typically
saved in a file with a ".mhmat" extension. MPFB will read and parse these files and use them to set up a shader node tree with a Blender material. 

In MPFB all clothes will use this format. The skin and the eys _can_ use this material too, although for body and eyes the default is to
use specific procedural materials instead. If the end goal is an external application (for example Unity or UE), the best bet is to use the 
MakeSkin material for everything.

The following pages describe the defails of the MakeSkin material model:

- Creating materials introduces the MakeSkin tool which is bundled with MPFB.
- Using materials gives a few hints on how to load materials as well as how to connect a material to an asset.
- [MakeSkin reference]({{< relref "reference" >}}) lists all available settings in the MHMAT file format, with notes on what is supported and where.



