---
title: "What are the differences between MPFB2 and MHX2?"
draft: false
description: "An overview of similarities and differences between MPFB2 and MHX2"
---

MPFB2 and MHX2 are conceptually very different things, and a comparison isn't really fair. However, since they have functionality that
overlap to some degree we can list some points where they can be compared. 

Before reading this, you should take a look at [What are the differences between MPFB2 and MakeHuman]({{< relref "differences_between_mpfb2_and_makehuman" >}}) and
[What are the differences between MPFB1 and MPFB2]({{< relref "differences_between_mpfb1_and_mpfb2" >}}). Points
that describe MPFB2 on those pages will not be listed here. 

## In short

_MPFB2_ is an addon for Blender. Its aim is to provide for all needs for character modeling inside Blender. It is not primarily an importer from MakeHuman, although it is
very capable of doing that too.

_MHX2_ is a very old and these days rather archaic importer/exporter set of addons intended for transferring MakeHuman models from MakeHuman to Blender. The MH dev team keeps a fork of the original MHX2 code within the scope of makehumancommunity on GitHub mainly in order to maintain support for old projects, but no-one is doing active development for it. The original project got lost when BitBucket dropped support for mercurial. 

## Overview of differences and similarities

|                               | MHX2                                                    | MPFB2                                                                                 |
| ----------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Is a...                       | Set of import/export addons for MH and Blender          | Full character modeler for blender, which includes import functionality for MH models | 
| Also provides...              | Custom IK rigs, expressions, some utilities             | Full character modeling, updated materials, equip/unequip assets (and so on)          |
| Main purpose                  | Import/export                                           | Full character modeler                                                                |
| Had first release...          | More than 10 years ago (MHX1 several years before that) | 2022 (MPFB1 was released 2018)                                                        |
| MH File format / mode support | MHX files (baked json structures)                       | MHM, direct socket import without the need to first export to a file                  |
| Development status            | Mostly considered deprecated, rare bugfixes             | Under active development                                                              |

