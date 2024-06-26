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

See the [MPFB Downloads]({{% relref "../downloads" %}}) page for links to binaries. If you want the features listed in these release notes,
you will need to download a nightly build.

## Release schedule

The next release is assumed to happen in summer 2024. This is a prognosis, not a promise.

While development with MPFB2 is moving forward in a steady pace, it is also occasionally a bit slow. We welcome more people to the 
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
* ASSETS: MakeSkin has better integration with the asset library
* ASSETS: MakeTarget has better integration with the asset library (**this is still under development and not finished**)
* MATERIALS: The MakeSkin material model now supports all common PBR textures
* MATERIALS: There is a new Game Engine material (**this is still under development and not finished**)
* UI: There is a new option for preselecting group and material by name upon character creation
* UI: New filters for only showing active/equipped targets and assets
* AI: There is a new function for exporting a pose to OpenPose
* DEVELOPER: Better handling of crashes related to UI operations
* DEVELOPER: Panel for quickly displaying version information

## Bug fixes / other changes

There has obviously been quite a lot of bug fixes and other changes, but these are a few examples:

* File paths where parent directories have mixed string encoding are now handled gracefully


## Target asset packs

The asset pack functionality has been extended to also support packs with targets. Several new packs with targets 
have been added. You can find download links to these in [the asset packs section]({{% relref "../../Assets/AssetPacks" %}}).

![target packs](20b2_target_packs.png)

The currently active target in the image is "bear head" by JALdMIC, shared under CC-BY.

## Multiple asset directories

MPFB now supports specifying a second root for assets. This can be overridden on a per-blend basis (on the library settings panel),
making it possible to have asset directories which are specific to certain projects.

![secondary root](20b2_secondary_root.png)

Assets will need to be moved or copied to the second root manually using your operating system's file window or similar.

## Full PBR model in MakeSkin materials

The MakeSkin material model has been extended to support all common PBR textures. MakeSkin is the material used on, for example, all mesh assets such as clothes. It can also be used as skin on humans, if a PBR material is desired rather than one of the procedural alternatives.

You can create and persist MakeSkin materials on the MakeSkin panel:

![makeskin pbr](20b2_makeskin_pbr.png)

## MakeSkin has better integration with the asset library

The makeskin tool can now save materials directly to the asset library, making them available as alternate materials for the asset the material was
created on:

**There seems to be a bug with this, need to fix: [#188](https://github.com/makehumancommunity/mpfb2/issues/188)**

![makeskin pbr](20b2_makeskin_alternate.png)

## New PBR-based game engine material model (work in progress)

A specific game engine PBR material model has been added as an alternative to the MakeSkin model. When exporting to FBX, some aspects of the 
MakeSkin model do not translate gracefully. The game engine material model has been specifically tailored to translate well in an FBX export.

**(need illustration)**

**(this is still work in progress)**

## MakeClothes now bundled with MPFB

MakeClothes has now been reimplemented as a module inside MPFB. Previously the full functionality was only available as a standalone addon,
which had not been updated to work with Blender 4+.

![secondary root](20b2_make_clothes.png)

With the implementation being a part of MPFB, it is possible to save clothes directly to the asset library. Once a piece of clothing has been 
saved it is possible to equip it immediately without needing to restart Blender.

Note that the implementation is still a bit rough around the edges, particularly in regards to UX. It will need further testing before 
being completely stable. This said, it usually works when we play around with it.

## MakeTarget has better integration with the asset library


## Preselecting group and material

In the new human from preset and new human from scratch panels, there is now a new input box "preselect group".

![preselect group](20b2_preselect_group.png)

When containing the name of a vertex group, that group will be preselected in edit mode. Further, if there is a material
with a name that ends with the vertex group name, then that material will be set as active. The default value of the 
box is "body".

The reasoning behind the addition of this feature is that it was often unintuitive for users that the last created vertex
group and material were selected/active. This would, for example, cause problems when trying to texture paint.

## Filters for only showing active targets or assets

Both the "Apply assets" and the "Model" panels have gotten a new filter checkbox for toggling between showing all 
assets or targets and only showing those which are active on the currently selected character.

![only equipped](20b2_only_equipped.png)

![only active](20b2_only_active.png)

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
