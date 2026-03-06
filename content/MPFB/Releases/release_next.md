---
title: "MPFB 2.0-next"
draft: false
weight: 1
---

These are the release notes of what is to become MPFB 2.0.15. Since [2.0.14]({{% relref "release_2014" %}}) was just released,
there is not much here yet.

## General

This release adds initial support for lip sync animation, including a new "Face operations" panel for loading facial shape keys
and integrating with the [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/) from the Blender extension platform.

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender.

## Lip sync support

A new "Face operations" sub-panel has been added under the **Operations** category in the N-panel. It provides two main sections
for working with facial shape keys and the Lip Sync addon.

### Face operations panel

The upper section of the panel, **Facial shape key packs**, lets you select which packs of face shape keys to load onto the basemesh.
Three packs are available:

- **visemes01** — 22 Microsoft-style viseme shape keys (e.g. `aa_02`, `p_b_m_21`)
- **visemes02** — 15 Meta/VR-style viseme shape keys (e.g. `viseme_aa`, `viseme_CH`) — the recommended pack for lip sync
- **faceunits01** — 54 ARKit face unit shape keys (e.g. `browDownLeft`, `eyeBlinkLeft`)

Select the packs you need and click **"Load face shape keys"** to add them to the basemesh as shape keys with zero weight.

### Lip Sync integration

The lower section, **Lip Sync shape keys**, handles integration with the [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/).
Once visemes02 are loaded and the Lip Sync addon has been initialised on the object, an **"Assign Lip Sync shape keys"** button becomes available.
Clicking it automatically maps all 15 viseme slots in the Lip Sync addon to the corresponding shape keys on the mesh, replacing what would
otherwise require around 15 manual dropdown selections in the Lip Sync panel.

The panel shows contextual status messages throughout the workflow: it warns when the Lip Sync addon is not enabled, when visemes02 has not
been loaded, or when Lip Sync has not been initialised on the selected object.

For a detailed walkthrough of the complete workflow, see the [lip sync documentation]({{% relref "../Docs/LipSync" %}}).

### Prerequisites

The [visemes02]({{% relref "../../Assets/AssetPacks/visemes02" %}}) asset pack must be installed for the lip sync workflow.
The [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/) must be installed and enabled separately
via the Blender extension platform.
