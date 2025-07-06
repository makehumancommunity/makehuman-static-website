---
title: "MPFB 2.0.10"
draft: false
weight: 1
---

These are the release notes of MPFB 2.0.10, which was released 2025-07-06. Listed below are the changes since [2.0.9]({{% relref "release_209" %}}).

## General

This is a bug fix release. If you did not run into trouble with paths or with MakeClothes, you will not see much difference compared to 2.0.9.

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender. 

## Tilde paths now resolved

A bug in MPFB 2.0.9 caused paths containing a tilde to be interpreted as literal. Thus a path like "~/mpfb" would first look for a directory
actually called "~" rather than resolve to the user's home directory.

In 2.0.10 tilde paths specified in the user preferences should now correctly resolve relative to the user's home directory.

## Rigid group strategy added to MakeClothes

In the stand alone MakeClothes it was possible to create a rigid part of clothing by creating a human vertex group with exactly three 
vertices. This was overlooked when porting MC into a submodule of MPFB.

This only affected clothes _creation_. Clothes which were created with rigid groups using other versions would still _load_ correctly.

In 2.0.10 the rigid group strategy has been added to the bundled MakeClothes, making it possible to create rigid groups again.

### What is a rigid group anyway?

Normally, clothes will deform to follow the surface of the human. Thus, if the human mesh changes shape, the clothes will deform with it.

In some cases, this is not desirable. Think for example a sword: If it changes shape with the surface of the fingers, it will end up 
bent and wonky. A rigid item such as that should only change overall size, without changing structure or form.

With a rigid group, the clothes item (or as it were, the rigid group of the clothes) will scale with the overall size of the human 
rather than deform with the surface.


