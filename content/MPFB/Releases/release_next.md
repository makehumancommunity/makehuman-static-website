---
title: "MPFB 2.0-next"
draft: false
weight: 1
---

These are the release notes for what is to become the next release of MPFB. The release is most likely going to 
be called "MPFB 2.0 beta 1".

The changes listed on this page are feature additions and bug fixes since the release of [MPFB 2.0 alpha 3]({{% relref "release_20a3" %}}).

If you find a bug in MPFB2, take a look at [How do I report a bug?]({{% relref "../FAQ/how_do_i_report_a_bug" %}}).

If this is the first time you install MPFB2, you might want to take a look at the [textual getting started]({{% relref "../Docs/getting_started" %}}) guide
or the [Getting Started with MPFB2 youtube video](https://youtu.be/9jmTdhVjAsI).

If you came here wondering if these are the release notes for the next version of MakeHuman, take a look at [the differences between MPFB and MakeHuman]({{% relref "../FAQ/differences_between_mpfb2_and_makehuman" %}}).

## Downloads

See the [MPFB Downloads]({{% relref "../downloads" %}}) page for links to binaries. If you want the featured listed in these release notes,
you will need to download a nightly build.

## Release schedule

The next release is assumed to happen in the summer 2024. This is a prognosis, not a promise.

While development with MPFB2 moving forward in a steady pace, it is also occasionally a bit slow. We welcome more people to the 
project. If you want to engage in the development (or with testing, or with contributing art), take a look at
[Contributing]({{% relref "../Contributing" %}}).

For a list of still open features which are intended to be finished before the release, see [the milestone on github](https://github.com/makehumancommunity/mpfb2/milestone/1)

## Important breaking changes

MPFB2 is now Blender 4.1+ only. You will no longer be able to start it on, for example, Blender 3.6. 

Some shaders behave differently in Blender 4 compared to Blender 3. Because of this, a character preset made with Blender 3 might
not look exactly the same when opened in Blender 4. You should check your character presets and take a closer look at, for example, SSS.

## New features in summary

These are the new features in summary. See further down on the page for more details on some of the highlights. 

* GENERAL: The code base has been updated for Blender 4+. Lowest supported Blender version is now 4.1.0.
* RIGGING: There is a new game engine rig variant with breast bones (thanks to rmarma)
* RIGGING: Rigify is updated to use the new Blender 4 features, such as bone layers (thanks to angavrilov)
* ASSETS: Asset packs with targets are now supported
* ASSETS: Multiple directories with assets are now supported
* ASSETS: MakeClothes is now ported to and bundled with MPFB
* ASSETS: MakeSkin has better integration with the asset library (**this is still under development and not finished**)
* ASSETS: MakeTarget has better integration with the asset library (**this is still under development and not finished**)
* MATERIALS: The MakeSkin material model now supports all common PBR textures
* MATERIALS: There is a new Game Engine material (**this is still under development and not finished**)
* AI: There is a new function for exporting a pose to OpenPose
* DEVELOPER: Better handling of crashes related to UI operations
* DEVELOPER: Panel for quickly displaying version information

## Bug fixes / other changes

There has obviously been quite a lot of bug fixes and other changes, but these are a few examples:

* File paths where parent directories have mixed string encoding are now handled gracefully


## Target asset packs


## Multiple asset directories

UI, per-blend dir

## Full PBR model in MakeSkin materials


## New PBR-based game engine material model


## MakeClothes now bundled with MPFB


## MakeSkin has better integration with the asset library


## MakeTarget has better integration with the asset library


## Generative AI and OpenPose


## Better handling of crashes and error reporting


## Easily accessible version information


## Known issues

While much of the functionality in MPFB2 is in principle finished and working, some parts are still a bit rough around the edges. It is important to be aware of this to have a reasonable idea of what to expect from the addon.

Especially the following areas will need more work before being considered stable:

### Asset creation tools have had limited testing

While all asset creation tools (MakeClothes, MakeTarget, MakeSkin...) have now been merged into the MPFB code base, they have not been thoroughly 
tested yet. It is assumed there will be occasional bugs to stomp out. This said, they should work for most common use cases.

### The integrated MakeTarget lacks some features from the standalone version

The standalone MakeTarget had some features added after the then current version was merged into MPFB. These features remain to be ported.
These features are mainly convenience and efficiency stuff, and the version in MPFB is perfectly usable without them. But if you know you
are going to put in heavy work on targets, it might make sense to check the standalone version if there is something you want there.

The new features will be merged into MPFB at some point in the future.
