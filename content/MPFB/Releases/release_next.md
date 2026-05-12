---
title: "MPFB 2.0-next"
draft: false
weight: 1
---

These are the release notes of MPFB 2.0.16, which not yet been released. The following are changes since [2.0.15]({{% relref "release_2015" %}}).

## General

This is a feature release focusing on adding a complete toolset for expressions.

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender.

## Expressions

MakeHuman had an "expression mixer" which let the user compose pose-based expressions by mixing face units. Up until now MPFB did not
have anything similar. 

With the advent of the `faceunits01` asset pack, there are now ARKit compatible face shapes available. The expressions functionality
uses these to provide a toolset for shape key based expressions.

### Defining expressions: MakeExpression

There is a new panel "MakeExpression" available under the "create assets panel.



