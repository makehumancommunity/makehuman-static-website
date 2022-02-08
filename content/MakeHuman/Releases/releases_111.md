---
title: "Releases:111"
draft: false
---

These are the release notes for version 1.1.1, which was released in March 2017.

This release is primarily a bug fix release where the major effort has been spent on addressing the unicode issues which made MakeHuman crash when using certain non-ASCII characters in filenames or usernames (in certain locales) on Windows platforms.

## Highlights

* It should now be possible to mix encodings (from recognized and valid codepages, see known issues below) on windows 7/8/10, for example when having a unicode file system, but a cp850-encoded filename. This will solve crashes when the user name or the installation path contains latin1 characters such as åäöüñé. 
* The UI will no longer crash when using translations.
* The release provides more consist management of undo and restore defaults
* Fix for glitches in the male formal suit (thanks to CallHarvey3d)
* Fix for glitches in the male worksuit (thanks to marco_105)

## Upgrading

In general, it should be possible to replace the 1.1.0 release with the 1.1.1 release without any noticeable downside. If you use the male worksuit, please note that it has had its UV layout redone from scratch (so third part textures relying on the old UV layout will no longer work).

## Useful extras

In [the release directory](http://download.tuxfamily.org/makehuman/releases/1.1.1) on tuxfamily, you will also find two zip files with extras that you may be interested in installing:

* **blender_plugins_for_1.1.1.zip**: These are blender plugins related to MakeHuman. This is what was called "blendertools" earlier (maketarget, makeclothes, makewalk), but now also includes the latest version of MHX2. 
* **makehuman_plugins_for_1.1.1.zip**: These are extras for MakeHuman as such. The zip contains the MakeHuman side of MHX2, the asset downloader plugin, the asset editor plugin, and the MHAPI dependency. 

## Known issues

While we believe we have now got a grip on all ''normal'' cases where non-ASCII characters are used in file names, it is still possible to break MakeHuman by copy/pasting characters from another codepage than the one windows is installed with. For example: if you have an US-english windows version and unzip MH in a folder named ру́сскийязы́к, chances are MH won't even start. 

However, any file name that you are able to write on the keyboard (as opposed from copying from the web) should now work.

Inside MakeHuman the use of unicode characters is more permissive. It is possible to save MakeHuman models in folders and with filenames containing characters that are not in the primary codepage. However, in case of doubt, we would recommend using only ASCII-characters, respectively characters from your active code page, for filenames. If you plan to save files with users from another locale, it is prudent to stick with ASCII names whenever possible.

Because of the cost, the release version of MakeHuman 1.1.1 is not code-signed. This means that some virus checkers, and the Windows OS may issue a warning on your initial start-up.  This should be safe to ignore if you downloaded your copy of MakeHuman directly from the official download site.  If you obtained your copy elsewhere please use due diligence.

A long standing bug, [#1054], was not possible to fix in time for the release. This causes shaders to glitch and look corrup on linux machines under the following conditions: 1. the machine runs on an integrated Intel graphics chipset and 2. the machine uses a newer graphics driver. This is known to affect Ubuntu 16.04, while older Ubuntu versions (such as 14.04) are not affected. For now, the workaround is to run MakeHuman with the parameter "--noshaders". For more info, see the [[FAQ:MakeHuman renders odd colours and weird transparency artefacts. Can you help me?|the appropriate FAQ item]](http://bugtracker.makehumancommunity.org/issues/1054).

## All fixes

* Bug #78: "Restore Default" button in settings
* Bug #195: "Undo" does not actually undo many commands
* Bug #354: Add package_name + date in window title
* Bug #662: New malesuit01 needs minor UV touch-up
* Bug #716: Translation choices
* Bug #718: Alternative distribution for windows
* Bug #764: SVG not supported on windows (but doesn't crash)
* Bug #771: Consistent handling of binary/ascii export choice
* Bug #831: Worksuit texture touch-up
* Bug #945: increasing eye bag slider breaks armature
* Bug #981: Makeclothes doesn't like eyes
* Bug #983: Modeling Face Mouth features slider images
* Bug #1004: RC and recent HG builds - file loader does not populate
* Bug #1027: MH 1.1.0 - Windows 10 PreRelease Build - File list Exceptions
* Bug #1028: MH 1.1.x - clean up / document status of genitals
* Bug #1029: Unicode in MH path still causing trouble
* Bug #1037: Using any translation crashes parts of the GUI
* Bug #1043: Possible issue in module3d
* Bug #1051: Assymetric foot vertex groups
* Bug #1053: Help About
* Bug #1057: ppa produced overwrite errorserrors
* Bug #1066: material_editor unicode warning MH 1.1.0 release
* Bug #1070: Sort filters dysfunctional - MH 1.1.0
* Bug #1073: Error loading a bvh pose created in Blender
* Bug #1076: MacOS Sierra - MakeHuman 1.1.0 data directory not loading
* Bug #1083: _cat_data["bodyproportion"] or _cat_data["bodyproportions"]?
* Bug #1088: Test cases for unicode issues
* Bug #1094: Update copyright to 2017
* Bug #1104: MakeWalk code has a trivial typo.
* Bug #1108: Replace splash screen
* Bug #1109: Investigate PPA errors
* Bug #1110: Update the README file.
* Bug #1111: Test Build r2066 (708f2b6d9545) issues
* Bug #1112: v1.1.1 can't load mhm created with v1.1.0
* Bug #1113: Link Help>About MakeHuman>Website to community
* Bug #1120: Error in language master file
* Bug #1124: PPA: the package description for makehuman-bodyparts is "test test"
* Bug #1126: PPA: makehuman-bodyparts should have "replaces makehuman-data"
* Bug #1135: File chooser in backgrounds tab does not populate when UI language set to russian
* Bug #1138: Missing bitbucket Item?
* Bug #1139: Missing comma in languages/master.json

* Feature #98: Regression suit to test the exported files.
* Feature #211: Conforming to debian python policy
* Feature #696: Increased support for rigid proxy assets
* Feature #1093: Easy way to copy version number to clipboard for bug reporting
* Feature #1107: Make sure it's possible to save all kinds of filenames on windows