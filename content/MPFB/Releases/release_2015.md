---
title: "MPFB 2.0.15"
draft: false
weight: 1
description: "Release notes for MPFB 2.0.15 (2026-05-05): new Face operations panel for visemes and expressions, Lip Sync integration and improved custom rig support."
---

These are the release notes of MPFB 2.0.15 which was released 2026-05-05. The following are changes since [2.0.14]({{% relref "release_2014" %}}).

## General

This is a feature release adding the following:

- A new "Face operations" panel for loading viseme and expression shape keys
- A convenience layer for integrating with the [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/) from the Blender extension platform.
- Improved support for custom rigs
- UX improvements for certain scenarios related to asset pack installations

There are also code quality / documentation / developer changes.

Regarding bugfixes, there are some fixes related to asset creation for MakeClothes and MakeRig. 

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender.

## Face operations

A new "Face operations" sub-panel has been added under the **Operations** category in the N-panel. It provides two main sections
for working with facial shape keys and the Lip Sync addon.

![faceops](2015_faceops.png)

The upper section of the panel, **Facial shape key packs**, lets you select which packs of face shape keys to load onto the basemesh.
Three packs are available:

- **visemes01** — 22 Microsoft-style viseme shape keys (e.g. `aa_02`, `p_b_m_21`)
- **visemes02** — 15 Meta/VR-style viseme shape keys (e.g. `viseme_aa`, `viseme_CH`) 
- **faceunits01** — 54 ARKit face unit shape keys (e.g. `browDownLeft`, `eyeBlinkLeft`)

Select the shape key sets you need and click **"Load face shape keys"** to add them to the basemesh as shape keys with zero weight.

Note that you need to have installed the corresponding asset packs for this to work.

## Lip sync support

The lower section of the face operations panel, **Lip Sync shape keys**, handles integration with the [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/).

Once visemes02 are loaded and the Lip Sync addon has been initialised on the object, an **"Assign Lip Sync shape keys"** button becomes available.
Clicking it automatically maps all 15 viseme slots in the Lip Sync addon to the corresponding shape keys on the mesh, replacing what would
otherwise require around 15 manual dropdown selections in the Lip Sync panel.

The [visemes02]({{% relref "../../Assets/AssetPacks/visemes02" %}}) asset pack must be installed for the lip sync workflow.
The [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/) must be installed and enabled separately
via the Blender extension platform.

For a detailed walkthrough of the complete workflow, see the [lip sync documentation]({{% relref "../Docs/LipSync" %}}).

## Custom rigs

While there have been developer tools for creating rigs for quite some time now, there has been very limited support for actually using them.
In practice, users have been limited to the bundled rigs.

In this release, the UI for creating rigs have been moved to the "MakeRig" sub panel of "Create assets". Here there's a button for saving
the rig to the library. Once this has been done, the custom rig can be used as other rigs.

Paired with this, the logic related to rigs has been updated through the system so that custom rigs should be supported everywhere
through the entire life cycle of a character.

Note that this feature is still experimental and that there might be logical faults in how this is handled. Please report any problems
you encounter if using this.

## Asset pack installation UX

The prior logic for installing asset packs assumed that asset pack zips were downloaded and installed as is.

However, this ended up being confusing to some mac users. Safari has a default setting where it unzips the zip
files rather than saving them. Since there was no zip to install, these mac users would instead try to recreate
the asset pack by zipping the folder created by Safari. This would result in an invalid zip file with a bad
directory structure, such as one directory level too many.

Unfortunately, MPFB would accept such files and unpack them without protesting. Since the directory structure
was wrong, MPFB would then not find the installed assets. There was no obvious way for users to figure out
what had happened.

In the new logic, there is a drop-down in the asset pack installation panel, giving the user a choice on what
to do if an asset pack zip seems corrupt. The default option is to refuse to install it and, in the case of
mac metadata, tell the user to download and install a zip as is instead of trying to re-create it. There is 
also an option to _attempt_ to fix the zip, but with a clear warning that this might not work.

## MakeClothes: Fix tri/quad check

A logical flaw in the "check clothes" logic in MakeClothes prevented it from correctly detecting that a
clothes mesh had a mix of tris and quads. The check clothes button would report everything as ok, but then
the produce clothes button would crash with an incomprehensible error message.

Now check clothes will correctly report a mix of tris and quads to the UI.

## MakeClothes: Fix wrong EXACT match

A bug was fixed in MakeClothes. The matching logic will mark a clothing vertex which is within 0.001 from a
basemesh vert as an EXACT match. However, the logic failed to take into account that the vert might be in a
different vertex group, in which case it should not be a match at all. This has now been fixed.

(the bug caused spiky artifacts in dense meshes, particularly when posing)

## MakeClothes: New option to explicitly disable EXACT matches

In very dense meshes, vertex matches might end up being EXACT despite this not being intended. There was
no way for a user to avoid this. 

To solve this edge case, there is now a new UI option for explicitly disabling EXACT matches.

## MakeRig: Option to clear weights

When manually loading weights from a JSON file, the previous default was to combine these weights with
whatever existing weights was on the base mesh. If the loaded weights did not cover all verts or bones,
you would thus get a mix of weight paintings. 

There is now an option (defaulting to true) in the panel for whether to clear all bone weights before
loading new ones from json.

## Developer: Refactored UI layer directory structure

Previously, most UI panels/operator were located in a flat directory structure directly under src/mpfb/ui.

Now this structure has been cleaned up, with another level in the hierarchy. UI subdirs have been grouped into
new category dirs matching the top level panel they belong to. Thus, for example, the makeskin and makeclothes 
UI stuff is now in subdirs of src/mpfb/ui/create_assets.

## Developer: Significantly improved test coverage in the UI layer

An effort has been started to add unit testing of the UI layer. To achieve this, infrastructure with
fixtures and mocks have been added, and (lots) of energy has been spent on adding unit tests for at 
least the operators.

## Developer: New class decorator for poll

Since most poll() methods implement pretty much the same logic, with some minor variations, this logic
has been moved to a new class decorator `@pollstrategy`, which takes an argument for which type of poll
the operator or panel should use.

## Developer: Helper class for resolving objects from context

Pretty much every operator do one of a limited list of things, such as finding the basemesh and reading
scene properties. Since this is boilerplate, a new helper class `MpfbContext` has been added to automate
the common usage scenarios.

## Documentation: UI layer documentation

There is now technical [reference documentation for the UI layer](https://github.com/makehumancommunity/mpfb2/blob/master/docs/ui/index.md) 
in the [docs dir](https://github.com/makehumancommunity/mpfb2/blob/master/docs/index.md).
