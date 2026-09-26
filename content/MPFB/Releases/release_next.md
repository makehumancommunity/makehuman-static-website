---
title: "MPFB 2.0-next"
draft: false
weight: 1
description: "Preliminary release notes for the upcoming MPFB release."
---

These are the release notes of what is to become MPFB 2.0.18, which has not been released yet. 
The following are changes since [2.0.17]({{% relref "release_2017" %}}).

## General

This is a minor release focusing on new user UX, compatibility with Blender 5.2 and some documentation fixes.

There is also a set of bug fixes:

- An ink layer using the "full body" focus could no longer be saved, since MPFB looked for a UV map file
  for a focus which does not have one. The full body focus is simply the basemesh's default UV map, and no
  lookup is needed in that case.
- A `.target` file in the user data whose name was long enough to produce a blender property identifier of
  64 characters or more would abort the entire addon registration, so that MPFB did not start at all.
  Over-long targets and expressions are now skipped with an explanatory warning in the log naming the
  offending file, rather than taking the addon down with them.
- MPFB could no longer recognize a generated rigify rig or find its meta rig on current versions of rigify,
  which for example made it refuse to refit a character whose meta rig was hidden (which is what MPFB's own
  panel recommends). Rigify has moved several of its properties from ID-properties to RNA properties, and
  MPFB now checks both, so that older blender and rigify versions keep working too.
- A randomization preset saved before a target section existed would fail to load in its entirety. Sections
  which a preset predates are now restored as disabled rather than raising an error, which reproduces
  exactly the character the preset gave before.
- Topology proxies can now be unequipped, see below.

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender.

## Start here panel

The first time a user opens up this version of MPFB, a panel at the top will list some introductory
text and buttons for opening relevant places in the docs etc. This panel can be dismissed
with a button, and then be re-opened via preferences.

The background is that there are recurring complaints along the lines of "there are no tutorials for MPFB"
and "there aren't any assets for MPFB", although both in fact exist. The panel is an attempt at fixing
the discoverability rather than the contents: it says what to click first, links the getting started guide
and the video tutorials, states plainly whether an asset library is installed (and what to do if it is not),
and points at the community forum and the issue tracker.

The panel introduces no new functionality. Every button in it invokes an operator which is available
elsewhere in the UI too.

## Asymmetry targets

An entire section of bundled targets, the 62 files under `data/targets/asym`, has been unreachable since
they were added: no section in `target.json` pointed at them, so no panel was ever built for them. How this
went unnoticed for five years remains unexplained.

The section has now been added, and the 62 files pair up into 31 sliders under a new "asym" category in the
model panel, each running from full left asymmetry at -1 to full right at +1. The same sliders are also
available in the randomization panel.

The sliders also have icons. Since these targets typically move the mesh only a millimeter or two, which is
invisible at icon size, the deformation in the icons is deliberately exaggerated: the icon shows the place
and the direction of the asymmetry, not its magnitude.

Both of these were contributed by GitHub user ashledombos.

## Unequipping topology proxies

Clicking the button for an already loaded topology proxy did not unequip it, but instead attempted to load
it again and failed with an error about a missing file. Proxies now behave the same way as clothes and body
parts: an equipped proxy shows an "Unequip" button, which removes the proxy and also removes the mask
modifier which was hiding the base mesh underneath it.

As a part of this, a proxy loaded without rigging is now parented to the basemesh. Without that parenting
MPFB did not consider the proxy an equipped asset at all, and it could thus never be unequipped.

## Blender 5.2 compatibility

Blender 5.2 changed how the inputs of a geometry nodes modifier are accessed. Up to 5.1 they are
ID-properties on the modifier itself, and as of 5.2 reading them that way raises an exception. This broke
the entire hair editor, since applying hair failed outright.

Reading and writing node group inputs has been moved into `ModifierService`, which tries the old form first
and falls back on the new one, so the hair editor works on 4.2 through 5.2.

In the same area, hair did not render in EEVEE on blender 5.x, because the strip setting was only applied
when the render engine identified itself as `BLENDER_EEVEE_NEXT`. In 5.x the identifier is `BLENDER_EEVEE`
again, and both names are now accepted.

Both of these were contributed by GitHub user ashledombos.

## Documentation

As GitHub user Shatur has noted, the 
[target metadata documentation](https://github.com/makehumancommunity/mpfb2/blob/master/docs/fileformats/target_metadata.md) 
as well as a few other pieces of documentation are confusing and in some cases outright wrong. Some attempts have been made
to find these places and update them. 

This is quite far off from being able to promise that everything in the docs is correct (it is most likely not). Help with
proof reading and suggesting changes is very welcome.

The technical documentation in the `docs` directory has also been extended to cover the new functionality in
this release: the start here panel, the proxy unequip operator, and the new methods in `ObjectService`,
`ModifierService` and `UiService`.
