---
title: "MPFB 2.0-next"
draft: false
weight: 1
---

These are the release notes of MPFB 2.0.13, which has not yet been released. Listed below are the changes
since [2.0.12]({{% relref "release_2012" %}}).

## General

This is a feature release focusing on OpenPose support. 

## Downloads

MPFB is available from  [the extension platform](https://extensions.blender.org/add-ons/mpfb/), and the preferred way of installation is
to use the extension platform functionality inside blender. 

## Support for OpenPose

A new solution for OpenPose has been added, inspired by [com.io7m.visual.openpose_rig](https://github.com/io7m/com.io7m.visual.openpose_rig).

In this solution there is a new OpenPose rig, coupled with functionality for adding renderable colored bones and utilities for changing the
scene into something which is suitable for rendering an OpenPose image.

![OpenPose](2013_openpose_rig.png)

The current implementation supports BODY_25. 

It is currently not decided whether there will be a variation with hands.
