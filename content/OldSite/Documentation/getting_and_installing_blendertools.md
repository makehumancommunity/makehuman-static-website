---
title: "Getting and installing BlenderTools"
draft: false
---

The most up to date BlenderTools package (for 1.1.0) is available here: http://download.tuxfamily.org/makehuman/releases/1.1.0/blendertools-1.1.0-all.zip

BlenderTools roughly follows the releases of MakeHuman. So while it might work to use another version, it is probably better to upgrade BlenderTools whenever you upgrade MakeHuman.

BlenderTools should work with any modern version of Blender.

In practice, BlenderTools is a zip package consisting of three folders:

* MakeTarget (used to create targets)
* MakeClothes (used to create clothes, hair, proxies and other mesh items usable in MH)
* MakeWalk (used for BVH animation)

To install the addons, these **subfolders** must first be copied to a location where Blender can find it. Depending on the operating system being used, the addons destination directory where Blender will look for user-defined add-ons, is:

* Windows 7 and later: C:\Users\%username%\AppData\Roaming\Blender Foundation\Blender\%your blender version%\scripts\addons
* Linux: /home/%username%/.blender/%version%/scripts/addons
* OSX: /Users/%username%/Library/Application Support/Blender/%version%/scripts/addons

The directories should look something like:
 <nowiki>
/path/to/%version%/scripts/addons/maketarget/
/path/to/%version%/scripts/addons/makeclothes/
/path/to/%version%/scripts/addons/makewalk/
</nowiki>

**(you might need to create the '%version%/scripts' and '%version%/scripts/addons' directories if they don't already exist)**

''Note: that the AppData folder in Windows 7 and the .blender folder in Linux are hidden folders. The location may also be different depending on your choices for setting up your operating system and Blender. For more information see the Blender documentation.''

''Note: it won't work to use Blender's <code>Install from File...</code> UI to install these addons directly from the downloaded .zip file because the zip file has a top-level 'blendertools/' directory which shouldn't be kept.''

''Note: similarly on Windows it's not enough to use the <code>Extract all...</code> context menu option to unpack the zip file in the addons directory because that may create a top-level directory like 'blender-tools-1.1.0-all/' and the zip file also has its own top-level 'blendertools/' directory.''

To enable the MH addons, in Blender open the User Preferences window from the File > User Preferences menu, and go to the Addons tab. The Blendertools addons are located in the MakeHuman category. Enable them by checking the box in the upper-right corner, next to the running man symbol.   If you want Blendertools to start every time Blender is restarted, press the "Save User Settings" button.