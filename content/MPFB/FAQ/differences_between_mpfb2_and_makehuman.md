---
title: "What are the differences between MPFB2 and MakeHuman?"
draft: false
description: "An overview of similarities and differences between MPFB2 and MakeHuman"
---

Conceptually, MPFB2 can be thought of as a reimplementation of MakeHuman as a blender addon. However, apart from that they are
different applications with different codebases and different contexts for running.

_MakeHuman_ is a standalone GUI application with no relation to Blender. It has been around in various forms for close to two decades. Its aim is to enable rough modeling of characters which can then be exported to another application for further work. It does not implement any general 3d modeling apart from this.

_MPFB2_ is an addon for Blender, and can as such not be run without Blender. The current codebase (MPFB2) has been around since 2021. Its aim is to enable all needs for character modeling inside Blender. It leans heavily on Blender for all generic 3d modeling needs.

This said, and this is important, _all assets are shared between MPFB2 and MakeHuman_. They use the same file formats and the same system assets, 
such as the base mesh and the body modifications. You can start working on a character in MakeHuman, save it as MHM and then continue working 
on it inside MPFB2.

## Overview of differences and similarities

|                          | MakeHuman                  | MPFB2                                   | MPFB1                          |
| ------------------------ | -------------------------- | --------------------------------------- | ------------------------------ |
| Is a...                  | Standalone GUI application | Blender addon                           | Blender addon                  |
| Runs in/on...            | Windows, linux, mac        | Blender (on any platform)               | Blender (on any platform)      |
| Purpose                  | Full character modeler     | Full character modeler                  | Importer from MakeHuman        |
| Had first release...     | More than 15 years ago     | 2022                                    | 2018                           |
| Save file format         | MHM                        | JSON or Blend (but can read MHM)        | Blend                          |
| Morph target format      | .target                    | .target and gzipped .target             | Does not support morphs        |
| Clothes format           | MHCLO                      | MHCLO                                   | Baked mesh imported from MH    |
| Material format          | MHMAT                      | MHMAT, procedural skin, procedural eyes | MHMAT, procedural skin         |
| Base mesh                | hm08                       | hm08                                    | hm08                           |
| Export formats           | MHX, DAE, FBX, OBJ         | Anything blender can export to          | Anything blender can export to |
| Can model new characters | Yes                        | Yes                                     | No                             |
| Dynamically load assets  | Yes                        | Yes                                     | No                             |
