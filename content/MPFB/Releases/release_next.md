---
title: "MPFB 2.0-next"
draft: false
weight: 1
description: "Preliminary release notes for the upcoming MPFB release."
---

These are the release notes of MPFB 2.0.16, which not yet been released. The following are changes since [2.0.15]({{% relref "release_2015" %}}).

## General

This is a feature release focusing on adding a complete toolset for expressions.

There is now also a set of example standalone scripts demonstrating how to use MPFB as a scripting API.

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender.

## Expressions

MakeHuman had an "expression mixer" which let the user compose pose-based expressions by mixing face units. Up until now MPFB did not
have anything similar.

With the advent of the `faceunits01` asset pack, there are now ARKit compatible face shapes available. The expressions functionality
uses these to provide a toolset for shape key based expressions.

The implementation diverges from MakeHuman in one important way: where MakeHuman composes expressions from bone pose units (BVH frames),
MPFB drives Blender shape keys directly. The user-facing workflow should however still feel recognizable to anyone familiar with the
MakeHuman expression mixer and expression library.

Note that all of the expression functionality requires the [faceunits01]({{% relref "../../Assets/AssetPacks/faceunits01" %}}) asset pack
to be installed. 

### Defining expressions: MakeExpression

A new "MakeExpression" sub-panel has been added under the **Create assets** category in the N-panel. It functions as a composer for
new expression assets.

![MPFB MakeExpression panel composing facial expressions from ARKit face units](2016_makeexpression.png)

The panel presents one slider per ARKit face unit, grouped by face region (brow, eye, cheek, jaw, mouth, nose, tongue) so that the list
of 52 face units stays navigable. By dragging the sliders a complete expression can be formed.
 
Once a combination of face units is dialled in, the **"Save expression to library"** button writes the result as a `.json` file under
`<user_data>/expressions/`. 

The companion **"Load expression"** button reads back a previously saved `.json` and restores the sliders, so an existing expression can
be tweaked and saved under a new name. 

### Using expressions

A new "Expressions library" panel has been added under the **Apply assets** category. This is where saved expressions are applied to a
character.

![MPFB Expressions library panel applying saved expressions to a character](2016_expressionslibrary.png)

The panel renders one slider per available expression — one per `.json` file discovered under the `expressions` subdirectory of any of
the standard MPFB asset roots. 

Changing a slider applies the expression to the character immediately. Setting a slider back to `0.0` removes the expression from the
character. Expressions can be mixed freely: for example dialling "smile" to 0.7 and "surprise" to 0.3 simply layers the two on top of
each other, with the per-face-unit values clamped to a sensible range as a safety net.

The top of the panel provides a few controls to keep the list manageable:

- **Auto refit** — when on (the default), each slider change also runs a refit of clothes and body parts. On heavy rigs it can be
  convenient to turn this off while dialling in values and run a refit manually afterwards.
- **Only show applied** — hides every slider whose current weight is `0.0`. This makes it easy to see and adjust the currently active
  expressions without scrolling through the full list.
- **Filter** — a case-insensitive substring filter over the slider labels, again following the style of the model panel.

### Round-tripping through the character preset

Applied expressions are part of the character's persisted state. When a character is saved, the list of currently
applied expressions and their weights are written into the preset, and they are reapplied when the character is loaded back in.

If the save file is loaded on a system where `faceunits01` is not installed, the expression list is preserved verbatim but not
applied, so that the intent is not lost. Re-saving and reloading on a machine that does have the asset pack installed will restore the
expressions correctly.

### Limitations

While the technology as such works, there might still be some polishing left to do on the individual faceunit shape keys. If you 
happen to be an artist and have the time, take a look at the [extra targets](https://github.com/makehumancommunity/extra-targets) 
repository and the individual target files there. Pull requests with tweaks for the targets are welcome.

## Sample scripts

MPFB has always had as one of the main design goals that the code should be possible to use as an API for scripting. How to
do so might not be immediate apparent though.

There are now [script samples](https://github.com/makehumancommunity/mpfb2/blob/master/script_samples/index.md) in the git repo
with demonstrations on how to perform some common tasks via scripting.

