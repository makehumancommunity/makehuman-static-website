---
title: "MPFB 2.0-next"
draft: false
weight: 1
description: "Preliminary release notes for the upcoming MPFB release."
---

These are the release notes of what is to become MPFB 2.0.19. The changes listed are since the [2.0.18]({{% relref "release_2018" %}}) release.

## General

This is a feature release with:

- New hair card bake functionality for the hair editor (see below)

There is also a set of bug fixes:

- A crash in bake sculpt was fixed ("use_bake_multires" has changed property name in modern blenders)

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender.

## Updated hair editor

(mostly to be written, needs a few screenshots)

The hair editor has been improved with new bake to hair cards functionality, as well as having received a general overhaul.

Note that in order to use the new hair editor functionality, you need the updated [hair editor asset pack]({{% relref "../../Assets/AssetPacks/haireditor" %}}) (which is 
18 mb as opposed to the prior one which was 12 mb).

## Developer changes

Type hint annotations have now been added to most of the entity and service layers.
