---
title: "What are the differences between MPFB2 and MakeHuman?"
draft: false
---

Conceptually, MPFB2 can be thought of as a reimplementation of MakeHuman as a blender addon. However, apart from that they are
different applications with different codebases and different contexts for running.

_MakeHuman_ is a standalone GUI application with no relation to Blender. It has been around in various forms for close to two decades. Its aim is to 
enable rough modeling of characters which can then be exported to another application for further work. It does not implement any general 3d modeling 
apart from this.

_MPFB2_ is an addon for Blender, and can as such not be run without Blender. The current codebase (MPFB2) has been around since 2021. Its aim is 
to enable all needs for character modeling inside Blender. It leans heavily on Blender for all generic 3d modeling needs.

This said, and this is important, _all assets are shared between MPFB2 and MakeHuman_. They use the same file formats and the same system assets, 
such as the base mesh and the body modifications. You can start working on a character in MakeHuman, save it as MHM and then continue working 
on it inside MPFB2.