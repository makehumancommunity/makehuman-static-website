---
title: "MPFB 2.0-next"
draft: false
weight: 1
---

These are the release notes of MPFB 2.0.11, which has not yet been released. Listed below are the changes since [2.0.10]({{% relref "release_2010" %}}).

## General

This is a feature release focusing on experimental support for geometry nodes hair and fur. There is also a new mixamo rig variation
and a bug fix for MakeClothes.

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender. 

## Support for geometry nodes hair and fur

The major addition in this release is experimental support for adding and working with geometry hair. This is largely based on 
work done by Tomáš Klecer, as part of his CS thesis.

A new panel is available in the UI: the Hair Editor. 

![no hair](2011_hair_editor_no_hair.png)

Here you can add basic starter geometry nodes hair systems

![hair added](2011_hair_added.png)

Once added, you can modify basic properties of the hair system, such as noise, curl and color

![hair added](2011_hair_editor_modified.png)

Then you can enter sculpt mode and use the hair sculpt brushes

![hair added](2011_hair_editor_sculpt.png)

Note that the geometry hair support is still in an early stage. User feedback and bug reporting are especially welcome for this 
functionality.

## Mixamo rig with Unity extensions

An extended mixamo rig has been contributed by github user rmarma (Maxim). This rig has extra bones for controlling, for example, face and breast,
and it is suitable for mecanim.

Note that when snapping to mixamo in MPFB, you will need an animation which was created via a reduced doll with a matching rig. That is, 
you can't map an animation which was made for the "mixamo" rig onto "mixamo_unity" and vice versa.

![mixamo_unity](2011_mixamo_unity.png)

## MakeClothes check for same object scale

MakeClothes expects the basemesh and the clothes object to have the same scale, and the clothes generating procedure will fail if the
scale isn't the same. However, the "clothes check" button did not check for this, and the error was hidden in the producing routine due
to another message appearing immediately after. This caused the clothes production to fail without any user readable error message. 

In this version, the clothes check routine now also checks for scale, and the error message will be visible if the scale is different
when producing clothes.



