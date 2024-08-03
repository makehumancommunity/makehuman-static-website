---
title: "Blender crashes with an error about bpy.ops.import_scene.obj missing"
date: 2017-10-17T15:26:15Z
draft: false
---

The symptoms are as following: The addon seems to install correctly, and panels open and contain a user interface. However, 
when trying to create a human, a crash arises. In the bottom of the error message, there is an "AttributeError" complaining
that an operator "bpy.ops.import_scene.obj" is missing.

The most likely reason for this is that you are trying to use an old (as in earlier than march 2024) version of MPFB together
with Blender 4.x. This won't work, as Blender 4 removed support for the wavefront obj importer addon, in favor of the new
built-in wavefront support. 

The solution to the problem is using an up to date version of MPFB instead than the old version. 

If you have installed a new version and it still does not exist, you might also want to take a look at [How do I make sure I have the correct version installed?]({{% relref "ensure_correct_version" %}}).
