---
title: "MPFB 2.0-alpha2"
draft: false
weight: 6
---

**2.0-alpha2 has not yet been released, these are preliminary notes**

As 2.0-alpha2 is the second release in the MPFB2 series, the following are changes since 2.0-alpha1. For changes since MPFB1, 
see [release notes for alpha 1]({{< relref "release_20a1" >}}).

Before installing MPFB2, you should take a look at the [known issues](#known-issues) section at the bottom of this page.

## Downloads

The 2.0-alpha2 addon can be found on [Tuxfamily](https://download.tuxfamily.org/makehuman/plugins/) (look for the file named mpfb2-*.zip).

If this is the first time you install MPFB2, you might want to take a look at the [Getting started]({{< relref "../Docs/getting_started" >}}) guide.

## New features in summary

* SCULPT: There is a new panel for quickly setting up a sculpt project from a mesh
* SHAPE KEYS: There is a new button for baking all shape keys into the basemesh
* HELPERS: There is a new button for deleting the helpers from the basemesh
* MATERIALS: There is a new button for updating an existing material with a normal map
* ANIMATION: Add (highly experimental) code for creating walk cycles
* MAKESKIN: Implement texture path normalization, so that image files automatically get placed in the appropriate location and with appropriate names

## Bug fixes

* Do not crash on a context state mismatch when loading a wavefront object while in pose mode
* Update MakeSkin to correctly create template materials
* Update rig identification code so that it correctly can differentiate between "default" and "default no toes"
* Warn rather than crash if the rigify addon isn't enabled
* Warn rather than crash if the wavefront obj io addon isn't enabled
* Fix crash when creating a human of age "child" in combination with certain other macro target settings


## Sculpting: Setting up a sculpt project


## Shape keys: Baking all shape keys into the basemesh


## Helpers: Easily removing helpers from the basemesh


## Materials: Updating existing materials with a normal map


## Animation: Highly experimental code for walk cycles


## Known issues

While much of the functionality in MPFB2 is in principle finished and working, some parts are still a bit rough around the edges. It is important to be aware of this
to have a reasonable idea of what to expect from the addon.

Especially the following areas will need more work before being considered stable:

### Rigify

The rigify code is highly experimental and known to sometimes produce strange results. The weight painting is crude, bone sizes ends up looking strange, teeth and eyes object have crude 
workarounds. If it works for you, all is well. However, you should not be surprised if the rigify functionality does not work as desired. If you want to participate in the bug reporting, see
the following issues on the bug tracker:

* [MPFB issues with Rigify 3.1 features bug](https://github.com/makehumancommunity/mpfb2/issues/21)
* [Some models do not import correctly when importing via "Import MHM"](https://github.com/makehumancommunity/mpfb2/issues/20)
* [MPFB should check if a name is already taken before using it in rigify generate](https://github.com/makehumancommunity/mpfb2/issues/17)
* [Rigify generated rig does not move lower jaw teeth](https://github.com/makehumancommunity/mpfb2/issues/10)
* [The rigify meta rig needs to be weight painted](https://github.com/makehumancommunity/mpfb2/issues/9)
* [4 Problems I found when adding Rigify Rig bug](https://github.com/makehumancommunity/mpfb2/issues/6)

If you happen to know your way around the rigify API and have some spare time, help would be much appreciated with getting the rigify functionality up to par.

### MakeClothes port not really started

In the longer run, all the asset creation tools (MakeClothes, MakeSkin, MakeTarget...) will be merged with MPFB2. MakeSkin and MakeTarget have already
been ported, but the port of MakeClothes has hardly even started. The only actually working part of it is the clothes extraction. 

If you want to create clothes, you'll have to use the [separate MakeClothes addon](https://github.com/makehumancommunity/community-plugins-makeclothes).

### Things not ported from MPFB1

The following are functions which have not been ported from MPFB1:

* Everything related to mocap / kinect (I don't have a kinect setup, so can't test if things work or not)
* Rig amputations
