---
title: "Lip sync"
draft: false
weight: 37
description: "How to set up lip sync animation in MPFB using the Lip Sync addon"
alwaysopen: false
---

MPFB supports lip sync animation through integration with the [Lip Sync addon](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/)
from the Blender extension platform. Rather than re-implementing phoneme-to-viseme mapping from scratch, MPFB focuses on providing the
facial shape keys that the Lip Sync addon needs, and on automating the configuration that would otherwise have to be done manually.

A "viseme" is a facial shape that represents a specific sound. In MPFB these are stored as shape keys loaded from the visemes02 asset pack,
which uses the 15-shape Meta/ARKit naming convention (e.g. `viseme_aa`, `viseme_CH`, `viseme_sil`).

<!-- TODO: add screenshot of a character with viseme shape keys visible in the shape key properties panel -->

## Prerequisites

Before you can use lip sync in MPFB you need two things installed:

### The visemes02 asset pack

The visemes02 asset pack provides the facial shape keys for MPFB characters. Without it the "Load face shape keys" step below
will have nothing to load for lip sync purposes.

See [visemes02]({{% relref "../../../Assets/AssetPacks/visemes02" %}}) for installation instructions.

### The Lip Sync addon

The actual phoneme-to-animation work is handled by the Lip Sync addon, which is a separate free addon available on the Blender
extension platform:

- [Lip Sync on the extension platform](https://extensions.blender.org/add-ons/iocgpoly-lip-sync/)
- [Lip Sync GitHub page](https://github.com/Charley3d/lip-sync)
- [Lip Sync manual](https://docs.cgpoly.io/lip-sync-documentation)

Install it the same way as any other Blender extension: open **Edit → Preferences → Get Extensions**, search for "Lip Sync", and install it.
Make sure it is enabled before continuing.

## The Face operations panel

The **Face operations** panel is found in the **N-panel** (the side panel that opens with the **N** key in the 3D viewport).
Navigate to the **Operations** tab and expand the **Face operations** section. You must have a MPFB character selected for the
panel to display its contents.

<!-- TODO: add screenshot of the Face operations panel in the N-panel, showing both sub-sections -->

The panel has two sub-sections:

- **Facial shape key packs** — for loading shape keys onto the basemesh
- **Lip Sync shape keys** — for configuring the Lip Sync addon once the shape keys are in place

## Step 1: Load the visemes02 shape keys

In the **Facial shape key packs** sub-section, check the **visemes02** checkbox and click **"Load face shape keys"**.

<!-- TODO: add screenshot of the Facial shape key packs sub-section with visemes02 checked -->

This loads 15 shape keys onto the basemesh, each representing a different mouth position:

| Shape key | Sound |
|-----------|-------|
| `viseme_sil` | Silence / neutral |
| `viseme_PP` | P, B, M sounds |
| `viseme_FF` | F, V sounds |
| `viseme_TH` | Th sounds |
| `viseme_DD` | D, T, N sounds |
| `viseme_kk` | K, G sounds |
| `viseme_CH` | Ch, J, Sh sounds |
| `viseme_SS` | S, Z sounds |
| `viseme_nn` | N, Ng sounds |
| `viseme_RR` | R sound |
| `viseme_aa` | Aa vowel |
| `viseme_E` | Eh vowel |
| `viseme_I` | Ih vowel |
| `viseme_O` | Oh vowel |
| `viseme_U` | Uu vowel |

You can also load **visemes01** (Microsoft-style) and **faceunits01** (ARKit) at the same time if your workflow requires them,
though only visemes02 is used for the Lip Sync integration described here.

## Step 2: Initialise Lip Sync on the basemesh

Before MPFB can assign the shape keys to the Lip Sync addon, the Lip Sync addon must be initialised on the basemesh object.
This is done inside the Lip Sync addon's own panel, not in MPFB.

With the basemesh selected, open the Lip Sync panel (its location depends on the addon version — refer to the
[Lip Sync quick-start guide](https://docs.cgpoly.io/lip-sync-documentation/quick-start-guides/quick-start-shape-keys) for details)
and click its initialise/setup button.

<!-- TODO: add screenshot of the Lip Sync addon panel with the initialise button -->

Once initialisation is complete the **Lip Sync shape keys** sub-section in the MPFB Face operations panel will stop showing
the "Initialise Lip Sync on this object first" message and will instead show the assignment button.

## Step 3: Assign the shape keys

With visemes02 loaded and Lip Sync initialised, click **"Assign Lip Sync shape keys"** in the **Lip Sync shape keys** sub-section.

<!-- TODO: add screenshot of the Lip Sync shape keys sub-section with the Assign button visible -->

MPFB will automatically map each of the 15 viseme shape keys to the corresponding slot in the Lip Sync addon. This replaces
the manual process of setting each viseme dropdown in the Lip Sync panel individually.

If the operation completes successfully you will see an info message at the bottom of the screen. If any shape keys could not
be mapped — for example because a specific shape key was not found on the mesh — a warning will list the missing entries.

## Continuing in the Lip Sync addon

After the shape keys are assigned, the Lip Sync addon is ready to drive the character's mouth from audio or a phoneme track.
Refer to the [Lip Sync documentation](https://docs.cgpoly.io/lip-sync-documentation) for the next steps, which cover things
like loading audio, baking the animation and rendering.

<!-- TODO: add screenshot showing the completed Lip Sync addon configuration with shape keys assigned -->

## Status messages

The **Lip Sync shape keys** sub-section shows different messages depending on what is and is not in place:

| Message | Meaning |
|---------|---------|
| "Lip Sync addon is not enabled" | Install and enable the Lip Sync addon in Blender preferences |
| "Load visemes02 to enable Lip Sync configuration" | Use the **Facial shape key packs** section above to load visemes02 first |
| "Initialise Lip Sync on this object first (use the Lip Sync panel)" | Run the Lip Sync addon's own initialise step on the basemesh |
| "Assign Lip Sync shape keys" button visible | All prerequisites met; ready to assign |

## Notes

- The lip sync workflow is intended to be used on the basemesh directly, not on an export copy. If you plan to export the character
  to another application, see [Export copy]({{% relref "../exporting/export_copy" %}}) for how to handle shape keys as part of
  the export workflow.
- visemes01 and faceunits01 can be loaded at the same time as visemes02. They are independent and do not interfere with the lip sync setup.
- Lip sync shape keys added to the basemesh can be interpolated to child meshes (clothing, hair, body parts) through the Export copy feature.
