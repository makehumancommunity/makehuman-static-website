---
title: "MPFB 2.0.12"
draft: false
weight: 1
description: "Release notes for MPFB 2.0.12 (2025-10-18): bug-fix release restoring Blender 5 and Blender 4.2.x compatibility plus a Mixamo Unity rig T-pose fix."
---

These are the release notes of MPFB 2.0.12, which was released 2025-10-18. Listed below are the changes since [2.0.11]({{% relref "release_2011" %}}).

## General

This is a bug fix release. No new functionality has been added. 

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender. 

## Fixed bugs

* The T-pose for the unity mixamo rig still used the old name internally
* Replaced shader nodes which broke compatibility with blender 5
* Fixed wrong setting that broke compatibility with blender 4.2.x.
