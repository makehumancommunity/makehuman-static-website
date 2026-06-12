---
title: "Getting started with MakeHuman 2"
draft: false
weight: 8
description: "A basic introduction to MakeHuman 2: first-run setup, choosing a base mesh, modelling a character, and saving and exporting your work."
---

This page walks through the first steps of using MakeHuman 2. If you have not installed it yet, see the
[downloads page]({{% relref "downloads" %}}).

## First run: workspace and assets

The first time you start MakeHuman 2 it asks you to configure a workspace folder. This keeps the program code
separate from your assets, so that updating or reinstalling the program does not force you to download the assets
again. Two asset locations are supported:

- a **system folder** (next to the installation), and
- a **user folder** for your own custom assets.

Your configuration is stored in a per-user location so it persists across reinstalls:

- **Windows:** `%APPDATA%/makehuman2/makehuman2.conf`
- **Linux:** `~/.config/makehuman2/makehuman2.conf`
- **macOS:** `~/Library/Application Support/MakeHuman2/makehuman2.conf`

When prompted, use the built-in download manager to fetch the asset packs. These are the
[same asset packs used by MPFB2]({{% relref "differences_mh1_mh2" %}}).

## Choose a base mesh

MakeHuman 2 can work with more than one base mesh. The standard human base mesh is **hm08** — this is what most
people use and what the system asset packs are built for. An alternative mesh, **mh2bot**, is also bundled. You
can preselect a base mesh on startup with the `--base` command-line option.

## Model your character

Characters are built up by manipulating sliders, grouped into two categories:

- **Macro** targets control overall characteristics — gender, age, height, weight and ethnicity.
- **Detail** targets refine low-level features such as the shape of the eyes, mouth or fingers.

You can also load library assets — hair, clothes, eyes, skins and poses — through the point-and-click browsers.

## Save and export

- **Save** your work-in-progress as an `.mhm` model file so you can reopen and keep editing it later.
- **Export** the finished character to other applications. Supported formats include glTF 2.0, Wavefront OBJ,
  STL, the MakeHuman 2 binary format (MH2B), and BVH for animation data.

To bring characters into Blender, MakeHuman 2 ships with a Blender exporter addon (found under
`extern/blender_addons/io_makehuman/` in the source tree) that can communicate with a running MakeHuman 2
instance.

## Tutorial video

A getting-started tutorial video is planned. It will be embedded here once available.
