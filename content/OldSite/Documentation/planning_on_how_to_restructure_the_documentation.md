---
title: "Planning on how to restructure the documentation"
draft: false
---

These are random ideas on what should be done with the docs as and when someone has the time and energy

## General outline 

As it stands now, the first major sections as such (Introduction, general overview and working with the human) looks reasonable, although some content of the section looks pretty malplaced and is probably incomprehensible for someone reading it the first time (for example "professional mesh topology", which is more a kind of reference / technical notes than something that should be in introduction).

After the three first major sections, the following major sections make slightly less sense, and seem to be there in a bit of random order. 

A user would probably expect the general flow of the docs to be something rather along the lines of:

* Introduction
* General usage (now "General overview")
* Working with the human
* Getting and creating more assets
** Downloading more assets
** Installing blendertools
** Creating targets
** Creating clothes
** Creating skins
** .. (etc) ..
* Continuing your work in another application
** Short notes on exporting to blender
** Short notes on exporting to 3dsmax
** Short notes on exporting to maya
** Short notes on exporting to unity
** Short notes on exporting to UE4
* MakeHuman for developers
* All notes about MH vs blender, with pertinent subsections
* All notes about MH vs 3dsmax, with pertinent subsections
* All notes about MH vs maya, with pertinent subsections
* All notes about MH vs unity, with pertinent subsections
* All notes about MH vs UE4, with pertinent subsections

## Other sections

I'd like to move some of the stuff from the root of the wiki into the doc structure. 

* The "workflows" pages 
* The terminology page

## Style

Much of the text is written from a tech viewpoint rather than a usage viewpoint. Most users are interested how to use things rather than how things are built. Also, the language is occasionally completely incomprehensible for someone who is not informed about the internals of MakeHuman even if they are techies per se.

The docs should be written for the intended target audience.

(in practice, doc articles should be read through and reformulated when they deviate from this... mostly it's not needed to write completely new docs)

## Outdated content

Particularly the images could benefit from being redone vs 1.1.0. But in many places there are old information which might not be entirely correct anymore.