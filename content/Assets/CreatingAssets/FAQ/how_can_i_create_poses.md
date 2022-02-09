---
title: "How can I create poses?"
draft: false
---

A pose is a BVH file. This is a standard format which is supported by most 3d editors. 

In general the work flow is this:

* Assign the "default" skeleton to a toon in MH
* Export it
* Import in your favorite 3d editor
* Move around some bones
* Export the pose as a BVH file (be sure to only export one frame, in blender the default is to export the whole frame range)
* Save the BVH file in v1/data/poses

At the time of writing this, [there is a problem](http://bugtracker.makehumancommunity.org/issues/1032) with the collada export which makes it unsuitable for the above workflow. Blender users will want to export using MHX2 and import without any overrides.