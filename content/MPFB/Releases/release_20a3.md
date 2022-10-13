---
title: "MPFB 2.0-alpha3"
draft: false
weight: 7
---

MPFB2-alpha3 has not yet been released, and these are preliminary release notes. If you see something in these notes you find interesting, 
there is a high probability you can already now test it out by downloading the nightly build though.

As 2.0-alpha3 is the third release in the MPFB2 series, the following are changes since 2.0-alpha2. For changes since MPFB1, 
see [release notes for alpha 1]({{< relref "release_20a1" >}}).

Before installing MPFB2, you should take a look at the [known issues](#known-issues) section at the bottom of this page.

## Downloads

Nightly builds of MPFB2 can be found on [Tuxfamily](https://download.tuxfamily.org/makehuman/plugins/) (look for the file named mpfb2-*.zip).

If this is the first time you install MPFB2, you might want to take a look at the [Getting started]({{< relref "../Docs/getting_started" >}}) guide.

## New features in summary

* ASSET LIBRARY: Make it possible to filter assets on asset pack name (requires new asset packs builds though, which have not yet been released)
* ASSET LIBRARY: Asset packs have been cleaned up, extended and gotten rendered thumbnails (again not really released yet)

(there will obviously be more stuff here before release)

## Bug fixes / other changes

* Pose names are now sorted alphabetically in the apply pose dropdowns
* Alternate material names are now sorted alphabetically in their dropdown
* Don't crash on character create if an alternate material has gone missing
* Fix whitespace in json files to avoid complex diffs in PRs

## Known issues

While much of the functionality in MPFB2 is in principle finished and working, some parts are still a bit rough around the edges. It is important to be aware of this
to have a reasonable idea of what to expect from the addon.

Especially the following areas will need more work before being considered stable:

### Rigify

While things have improved significantly in regards to rigify since 2.0-alpha1, there might still be places in the rigify code that are rough around the edges. If it works for you, all is well. However, you should not be surprised if you find a glitch. To help us hunt down these, please post feedback and bug reports on [the bug tracker](https://github.com/makehumancommunity/mpfb2/issues).

### MakeClothes port not really started

In the longer run, all the asset creation tools (MakeClothes, MakeSkin, MakeTarget...) will be merged with MPFB2. MakeSkin and MakeTarget have already
been ported, but the port of MakeClothes has hardly even started. The only actually working part of it is the clothes extraction. 

If you want to create clothes, you'll have to use the [separate MakeClothes addon](https://github.com/makehumancommunity/community-plugins-makeclothes).

### Things not ported from MPFB1

The following are functions which have not been ported from MPFB1:

* Everything related to mocap / kinect (I don't have a kinect setup, so can't test if things work or not)
* Rig amputations
