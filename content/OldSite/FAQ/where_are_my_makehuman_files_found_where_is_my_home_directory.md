---
title: "Where are my MakeHuman files found (where is my HOME directory)?"
draft: false
---

TL;DR: 

* On windows, your files are usually in "MY DOCUMENTS"\makehuman\v1py3
* On linux, your files are usually in "~/Documents/makehuman/v1py3" or "~/makehuman/v1py3"

The longer story, with special cases:

The [BASE] folder location for saving MakeHuman user data depends on your operating system (Windows, Linux, OSX, etc..).  In the guide below, replace <username> with your actual login name. Typically, your <root> will be 'c:\\' (without quotes) on Windows machines, and just  plain "/" (without quotes) on Linux and Mac OSX. Take in account that your operating system might be case sensitive on filenames (Unix-like OSs !). In case of doubt use lower case directory names.

Here is the basic guide to finding the [BASE] folder on your operating system:
* Microsoft Windows Vista, 7, 8, 8.1 and 10: c:/Users/<username>/Documents/
* Linux: /home/<username>/ or simply ~/ (in 1.2.0 alpha 2 and later, the base folder has been moved to /home/<username>/Documents)
* Mac OSX: /Users/<username>/Documents/
* MakeHumanPortable (all Windows versions): X:\PortableApps\MakeHumanPortable\AppData (where X: is the drive letter of your removable device)

Your [BASE] folder, by default, contains an "asset folder" called **"makehuman"''' which will, in turn, contain a subfolder named 'v1' for MH version 1.X.X releases. The ./makehuman/v1/ subfolder contains a series of additional subfolders containing your personal MakeHuman asset files:  '''backgrounds, cache, data, exports, grab, models, and render**. 

The ./models/ folder will contain the .mhm **model''' files you "save". The ./exports/ folder will contain the files you "'''export'''" in .dae (collada), .fbx, .mhx2, .obj, or .stl formats. The ./backgrounds/ folder is where you can place '''background reference images''' to use in model construction. The '''data folder''', itself, contains many subfoders.  The ./data/... subfolders are where you will find '''clothes and other proxy objects** that you import using the asset manager.

**Notes:**
* On Windows systems, "Documents" is subject to internationalization.

For older/deprecated versions of Windows you may find the [BASE]/makehuman/v1/ subfolder here:
* Microsoft Windows 2000, XP and 2003: c:\\Documents and Settings\<username>
* Microsoft Windows NT:  <root>\WINNT\Profiles\<username>