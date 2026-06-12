---
title: "Differences between MakeHuman 1 and MakeHuman 2"
draft: false
weight: 10
description: "How MakeHuman 2 differs from MakeHuman 1: a modern PySide6 foundation, additional base meshes, animation, PBR shading and glTF export, with shared MPFB2 assets."
---

MakeHuman 2 is a complete rewrite of MakeHuman 1. The goal is the same — quickly modelling 3D human characters
through a simple point-and-click interface — but the codebase, the rendering and several of the supported
standards are new.

The most important thing to know is that **MakeHuman 2 is still in alpha**. MakeHuman 1 remains the established,
production-ready option, and the two can be
[installed and run in parallel]({{% relref "downloads" %}}). That makes it easy to try MakeHuman 2 while keeping
MakeHuman 1 for day-to-day work.

Like MakeHuman 1, MakeHuman 2 shares its system assets with [MPFB2]({{% relref "../MPFB" %}}) — the same base
mesh (hm08) and the same asset packs.

## Overview of differences and similarities

|                          | MakeHuman 1                | MakeHuman 2                                     |
| ------------------------ | -------------------------- | ---------------------------------------------- |
| Status                   | Stable                     | Alpha                                          |
| GUI toolkit              | PyQt5 (Qt5)                | PySide6 (Qt6)                                  |
| Runs on...               | Windows, Linux, macOS      | Windows (Steam) or any platform from source    |
| Base meshes              | hm08                       | hm08, mh2bot (and support for more)            |
| Animation                | Limited                    | Full skeletal animation (BVH and poses)        |
| Shading                  | Phong                      | PBR and Phong                                  |
| Save file format         | MHM                        | MHM                                            |
| Morph target format      | .target                    | .target (compiled to .npz for speed)           |
| Export formats           | MHX, DAE, FBX, OBJ         | glTF 2.0, OBJ, STL, MH2B, BVH                  |
| Asset packs              | Shared with MPFB2          | Shared with MPFB2                              |
| Licensing                | AGPL code, CC0 assets      | AGPL code, CC0 assets                          |

## New in MakeHuman 2

- **A modern foundation.** The application has been rebuilt on PySide6 (Qt6) and OpenGL, replacing the older
  PyQt5-based stack of MakeHuman 1.
- **Additional base meshes.** Beyond the standard hm08 human mesh, MakeHuman 2 ships with the mh2bot mesh and is
  designed to support further base meshes.
- **Animation.** A full skeletal animation system with support for BVH and pose data.
- **PBR shading.** Physically-based rendering (metallic/roughness workflow) in addition to classic Phong
  shading.
- **glTF export.** Modern Khronos glTF 2.0 export, alongside OBJ, STL and the new MH2B binary format.

## Things to be aware of

- Because MakeHuman 2 is a rewrite, **some old MakeHuman 1 standards are no longer supported**.
- As an alpha, features and formats may still change. For anything you depend on, keep using MakeHuman 1 in
  parallel.
