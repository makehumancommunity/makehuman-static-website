---
title: "How do I upgrade from addon to extension?"
draft: false
description: "How to upgrade MPFB from the legacy Blender addon format to the new extension format introduced in October 2024 without losing user data."
---

If you have a) installed a version of MPFB from october 11 2024 or earlier, including for example beta 1, and b) plan to upgrade to a nightly build or a new release from october 12 2024 or later, then these are some things you need to do.

You do not need to do these things again if you already have a version from october 12 or later.

## Make a backup of your user data

Theoretically, your user data should be left intact if following this procedure. However, it does not hurt to make a backup anyway.

See the instructions in [How can I create a backup of my user data?]({{% relref "creating_a_backup" %}})

## Completely remove the old addon

First you should remove all traces of the old installation. This is done by using the "uninstall" button in the preferences window.

![Uninstall button for the legacy MPFB addon in Blender preferences](upgrade_uninstall.png)

Confirm that you want to delete the relevant directory.

In the addons list, you should no longer see any trace of mpfb:

![Empty Blender addons list after uninstalling the legacy MPFB addon](upgrade_empty.png)

## Restart and make a new install

Before installing the new version, you should close and restart Blender.

To install the new version, follow the instructions in [How can I install MPFB2?]({{% relref "how_do_i_install" %}}) 

