---
title: "What should I do when switching to the extension platform version?"
draft: false
---

If this is the first time you install MPFB, then there's nothing specific you need to do.

However, if you have previously either installed a nightly build or an earlier release (such as beta 2), then the following 
are things you will most likely want to do:

Move your user data to a separate directory, see the "User data" section of [Which configuration settings should I adjust?]({{% relref "important_config" %}})

Completely remove all traces of the current MPFB installation:

* Go to the preferences -> addons section and disable MPFB
* Go to the preferences -> get extensions section and uninstall MPFB. The uninstall menu is on the arrow type of icon in the upper right part of the MPFB panel.
* Restart blender
* Go to the preferences -> addons section and make sure MPFB isn't visible anymore.

Now you can go ahead and install MPFB from the extension platform. Once installed, set the preference pointing to the "MPFB user data" to find your
user files.
