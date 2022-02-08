---
title: "Releases:110"
draft: false
---

These are the final release notes for 1.1.0, which was released 2016-05-14.

## Highlights

See also the [release infographic](http://www.makehumancommunity.org/w/images/7/7a/Infographic_110.png).

* Many bugfixes and stability fixes

* Many targets improved and minor modeling corrections

* Completely new skeleton and posing system, with support for pose loading from BVH, and support for custom weight and proxies

* New pose system with auto-rigging, support for T-pose export, and initial support for special poses like high heel shoes

* New skin library with age variation

* New expression system now based on a face bone rig, including a library with facial expressions.

* Improved topologies/proxies

* FBX export now supports binary FBX and should work for most third-part applications which support FBX

## Important notes

If you are currently using 1.0.2, there are some things that may be confusing when upgrading to 1.1.0.

**Many assets are incompatible:** If you have a large set of manually added assets such as clothes and targets, please be aware that these may not work as expected with the new release. Targets should mostly work. Version 1.0.2 MHM files should be possible to open, but deprecated proxies and assets may not be available. MHM files made with earlier, unsupported nightly builds may produce very unexpected results.  In general, you should test your assets with the new release before trusting everything works as expected.

**New philosophy in which assets are included per default:** Previously all existing assets were included with the default distribution. This is no longer so. Instead, a small set of robust, full body clothing choices is supplied by default.  In addition, there is now a large online area for community-designed assets, to which everyone is welcome to upload their creations. Some previously included assets have been removed from the default distribution in favor of this area. The online area can be found at http://www.makehumancommunity.org/content/user_contributed_assets.html

**MHX has been deprecated, MHX2 is a plugin:** The old MHX format is deprecated. While it still remains in Blender's code base, users are strongly discouraged from using it. The successor is MHX2, which is a plugin which has to be installed for both MakeHuman and Blender (you will most likely want to install exactly the same version in both). More information can be found in [[FAQ:What happened to the MHX export in MH 1.1.x and later?]].

**Most information about MH, and services around MH, has been moved:** The server/domain setup has been changed for various legal reasons. The main homepage http://www.makehuman.org is now a skeleton page which mostly include download links. Other services such as forum, bugtracker, wiki and so on has been moved to http://www.makehumancommunity.org. Some links might still not have been updated.

## Errata

A few issues have been pushed until later releases. We are aware of these and will fix them later. 

* [#392](http://bugtracker.makehumancommunity.org/issues/392) - There are numerous issues with the BHV export
* [#899](http://bugtracker.makehumancommunity.org/issues/899) - FBX export dislikes non-ascii characters
* [#1001](http://bugtracker.makehumancommunity.org/issues/1001) - Collada export produces (skeleton) warnings on Maya import

## Detailed list of changes

This is a semi-structured list of changes between 1.0.2 and 1.1.0. The full list of changes (the commit list) [can be found at BitBucket](https://bitbucket.org/MakeHuman/makehuman/commits/branch/stable).

### UI
* Drag and drop of .mhm files in makehuman
* Improved text support for long right panel labels
* Nicer looking application icons by using SVG vector graphics (looks better on OSX retina displays)
* Gradient background
* Allow disabling/enabling grid
* Tag filters in all libraries

### File-Export
* Add support for binary FBX exporter
* Added support for optional export of helper geometry and facial pose units
* Added support for specifying bone orientation
* Removed export for old mhx, MD5 and skel formats

### Modeling
* Improved labeling and consistency of modelling sliders
* Add random model generation 
* Added nipple point and nipple size sliders
* Added head fat slider
* Added scale depth of parietal side slider
* Added additional sliders for shaping neck and double chin
* Added eye bag sliders
* Added support for laugh lines and dimples
* Add additional sliders controlling chin shape
* Break cheek support into left/right sections
* Add additional sliders to control pectoral and dorsal muscle
* Add additional control of waist position
* Add sliders controlling navel prominence and position
* Added sliders to control shoulder muscle mass
* Add additional sliders controlling upper arm shape
* Additional sliders to control size and muscularity of upper and lower legs
* Additional slider to control lower leg height
* Add separate measure control for knee

### Geometries
* Drop genital proxy support (these have been deferred to the user contributed assets area)
* Improve clothes tagging system
* Include default clothing outfits that clothe upper and lower body without mesh intersections
* Include more and improved hair styles
* Increase the number and richness of default topologies to include generic and muscle phenotypes
* Add additional eyelash choice

### Materials
* Extend included skin materials to middle age and older individuals
* Extend the available choices for eye color

### Pose Animate
* Redesign the entire rigging system for improved mesh control and pose support (2 skeleton system)
* Design basic rigs for new rigging system to support CMU animation and facial posing
* Add a pose tab with selectable poses including a T pose
* Add an expressions tab with 32 selectable facial expressions
* Allow mixing body pose and face pose, if face pose is set override face bones of body pose
* Support modeling while mesh is posed
* Removed specific rigs intended for commercial third part systems. These have been deferred to the user repos.

### System/code
* windows DLL dependency fix
* improvements and caching in proxy libraries for faster asset loading
* binary format for proxy files for faster loading and more compact data
* new fully data-driven modifier system
* rename of targets and modifiers for more consistency
* new skeleton API is much more understandable
* a lot of in-code documentation added
* many code cleanups and improvements
* refactors to improve re-usability of code and facilitate plugin development
* reduction of coupling between components
* makehuman can be started with a .mhm file passed as commandline argument

### Settings
* Add the ability to automatically return MakeHuman to the default settings