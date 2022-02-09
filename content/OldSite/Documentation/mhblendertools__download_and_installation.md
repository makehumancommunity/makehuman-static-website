---
title: "MHBlenderTools: Download and installation"
draft: false
---

**THIS PAGE IS OUTDATED**

The Blendertools package is available on the download page: http://www.makehuman.org/content/download.html

The current version is 1.0.0, designed to work with MakeHuman 1.0.0 and with Blender 2.69. It's a zip package of four folders:

* MakeTarget
* MakeClothes
* MakeWalk
* mhx_importer

To install the addons, these subfolders must first be copied to a location where Blender can find it. Depending on the operating system being used, the addons destination directory where Blender will look for user-defined add-ons, is

* Windows 7: C:\Users\%username%\AppData\Roaming\Blender Foundation\Blender\2.6x\scripts\addons
* Windows XP: C:\Documents and Settings\%username%\Application Data\Blender Foundation\Blender\2.6x\scripts\addons
* Vista: C:\Program Files\Blender Foundation\Blender\%blenderversion%\scripts\addons (this is valid at least for blender 2.69)
* Linux: /home/$user/.blender/$version/scripts/addons

Note that the AppData folder in Windows 7 and the .blender folder in Linux are hidden folders. The location may also be different depending on your choices for setting up your operating system and Blender. For more information see the Blender documentation.

To enable the MH addons, in Blender open the User Preferences window from the File > User Preferences menu, and go to the Addons tab. The Blendertools addons are located in the MakeHuman category. Enable them by checking the box in the upper-right corner, next to the running man symbol. If you want Blendertools to start every time Blender is restarted, press the "Save User Settings" button.

 !IMAGE!Pictures/mhx-pref.png!/IMAGE!