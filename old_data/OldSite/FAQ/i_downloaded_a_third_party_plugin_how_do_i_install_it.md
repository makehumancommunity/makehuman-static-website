---
title: "I downloaded a third party plug-in. How do I install it?"
draft: false
---

In contrast to all other third party stuff described in the topics above, new plug-ins are **not''' installed in the user-home folder of MakeHuman, but need to be directly installed in a subfolder called '''"plugins"** of the program folder. The plugins-folder can be found in the same folder where the MakeHuman executable is located. On Windows it is located where you unzipped MakeHuman, e.g. C:\MakeHuman\plugins. On Debian-like systems, when using a package management, the folder is found at /usr/share/makehuman/plugins. For MacOS X it is Macintosh HD/Applications/MakeHuman.app/Contents/Resources/plugins.
The plug-in names start with a number and can be a single file or multiple files in a folder. Now copy the third party plug-in file or folder to the correct subfolder **"plugins"** indicated above. On Unix-like OSs (Linux / MacOS X)  make sure the newly installed plug-ins have the same permissions/ownership as the other plug-ins. When installing to /usr/share/makehuman, one will usually need root privileges. And care for case sensitivity.
Often it is necessary to install a corresponding plug-in to Blender (e.g. exporter/importer plug-in like MHX2). Please refer to the official Blender documentation on how to install plug-ins in Blender.