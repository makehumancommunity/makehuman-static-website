---
title: "Releases:120b2"
draft: false
---

These are the release notes for 1.2.0-beta2, which was released 2020-07-27.

This is the second and final beta. From now on, nightly builds should in principle be considered release candidates for the final stable release.

If you wonder if this is something you should use, take a look at [[FAQ: Which version of MakeHuman should I download?]]

If you are already using a recent nightly build, there is no reason whatsoever to switch to a beta, unless you want a formal release build.

## General

In most cases, there should be no problem running versions 1.1.1 and 1.2.0 on the same system. They will not interfere with each other's files. You can find download links for 1.2.0 at the bottom of this page. 

"MakeHuman Community 1.2.0" is a major update of the underlying code, where the focus has been to replace outdated dependencies and modernize the system. Further, a shift in focus has been made to position MakeHuman as  a shared tool serving the larger community through integrated access to third party assets and extended functionality.

## Changes since beta 1

* CORE/UI: It is now possible to disable sample buffers via settings (on the general tab). This is the first thing to try on graphics cards which have trouble rendering the 3d canvas, see [[FAQ: The interface looks broken ]]
* CORE/UI: It is now possible to enforce "noshaders" via settings (on the general tab). This is the second thing to try on graphics cards which have trouble rendering the 3d canvas, see [[FAQ: The interface looks broken ]]
* CORE/UI: The UI should now scale properly on UHD/4K displays (thanks dennj). There is a setting ("use HDPI") for this under settings -> general.
* TARGETS: The core targets were reworked to assure left/right symmetry (thanks punkduck)
* WINDOWS: Another reason for makehuman silently not starting on windows was adressed
* WINDOWS: It should now be possible to "install for all users"

Due to the rapid evolution of the blender plugins (MPFB, MakeTarget, MakeClothes...) we're not listing these changes here. See the commit log in the respective git repositories instead:

* [MakeHuman Plugin for Blender (MPFB)](https://github.com/makehumancommunity/makehuman-plugin-for-blender/commits/master)
* [MakeClothes 2](https://github.com/makehumancommunity/community-plugins-makeclothes/commits/master)
* [MakeTarget 2](https://github.com/makehumancommunity/community-plugins-maketarget/commits/master)
* [MakeSkin](https://github.com/makehumancommunity/community-plugins-makeskin/commits/master)

## Highlights

* The codebase has received a major overhaul to bring it up to date with modern versions of Python and Qt
* Third party assets can be downloaded from within MakeHuman with a simple point and click procedure
* There is a completely new Blender integration, with support for socket transfers, IK and Kinect
* There is a new randomization functionality for generating large sets of randomized characters
* Improved internationalization support for non-ASCII characters (backported)
* Plugins in user space
* Plugins activation at runtime
* Improved tag sorting capabilities (Hotkey: ALT-F), including sticky tag provisions
* Tags for models (with configurable tag count)
* Show Name Tags instead of file names in the file loader. 
* Saving model as target
* Real weight estimation
* Configurable location for the home folder
* MHX2 is bundled in the default installation
* Save thumbnails directly from the internal render engine
* There is a new installer for windows
* There is a new PPA for ubuntu. This PPA also offers builds of plugins. 
* Using Jupyter for the shell utility, if available on the system (currently not working for MakeHuman windows builds)
* There is a new tool MakeSkin for creating materials

## Known issues

* The FBX export is still incompatible with some third part software.
* While most of the graphics card incompatibilities should now be fixed, there may still be still parts of the program that cause problems with some integrated graphics cards.
* There is no build for OSX

## Upgrading

This version uses the same file formats as 1.1.x in almost all cases. The only exception is MHM files (which are produced when clicking "save model" in MakeHuman). 1.2.x is able to open MHM files produced in 1.1.x, and the result will look exactly the same as in 1.1.x. However, 1.1.x will not be able to open MHM files saved by 1.2.x.

For all other assets, things should work the same and look the same in both versions, using the same files.

### Running from source

The source code is available at [https://github.com/makehumancommunity/makehuman](https://github.com/makehumancommunity/makehuman). You'll also find basic instructions on how to use the source code on this page.

If you want to run MakeHuman directly from source (rather than downloading a binary build), you will have to replace almost all dependencies. It is also possible that not all dependencies will install smoothly beside the dependencies for 1.1.x. 

The following are the minimum required dependency versions for MakeHuman Community 1.2.0:

* Python: 3.6.4 or higher
* PyQt: 5.10.0 to 5.12.x. **5.14 will not work**
* NumPy: 1.13.0 or higher
* PyOpenGL: Any modern version will work, including the one used for MakeHuman 1.1.x

### Ubuntu

In order to fulfill the minimum dependency requirements listed above, you will need Ubuntu 18.04 or later. For earlier Ubuntu versions, you would have use backports of the dependencies, as they are not available in the default installation.

The PPA for this build is here: [ppa:makehuman-official/makehuman-community](https://launchpad.net/~makehuman-official/+archive/ubuntu/makehuman-community).

To enable it, run:

    sudo add-apt-repository ppa:makehuman-official/makehuman-community
    sudo apt-get update
    sudo apt-get install makehuman-community

### Mint

The instructions for Ubuntu apply, but you will have to also explicitly install all plugins (whereas these will be installed automatically on Ubuntu)

    sudo apt-get install makehuman-community-plugins-assetdownload makehuman-community-plugins-socket makehuman-community-plugins-massproduce mhx2-makehuman-exchange

## The upgraded codebase

The main focus of this release has been to modernize the code. In the prior version, large parts were written more than eight years ago, and relied on libraries and code structures which are no longer functional in a modern context. More in detail:

* The system was written for python 2.6 and then upgraded when needed to python 2.7. The expected end of life for python 2.7 is in a few months
* The user interface was implemented in Qt4, via PyQt4. Both Qt4 and PyQt4 got deprecated years ago, and Riverside (the authors of PyQt) removed all PyQt4 windows binaries, meaning we could no longer provide windows builds.

Thus, the need to bring the code up to modern times became critical. We realized that the system would soon not be possible to run or develop on several platforms. 

Going through the code to update it has taken some considerable time (years actually), but it has had the added benefit that we have also reviewed almost all sections of the code and fixed a lot of minor 
bugs and glitches.

Most users will probably not notice much difference: the user interfaces in 1.2.0 and 1.1.1 are almost identical. But it was work that needed to be done before we could move forward with implementing new features.

## Asset downloader



![12x-assetdownloader.png](12x-assetdownloader.png)



This version of MakeHuman bundles the asset downloader plugin. By using this you can access all the hundreds of user contributed assets that are available via the MakeHuman Community. 

Within the UI you can search for assets, show screenshots, read about details and download. Downloaded assets are automatically placed in your local asset directory so that you can
immediately go to the geometries tabs and, for example, equip the newly downloaded clothes.
<br clear=all>

## New blender integration



![12x-blender-import.png](12x-blender-import.png)





![12x-blender-ik.png](12x-blender-ik.png)



This release bundles a rich set of blender functionalitites, which can be added to blender in the form of an addon. Not all functionality will be listed here, but the following are 
some highlights.

### Import directly from MakeHuman

In blender it is now possible to fetch a toon directly from a running instance of MakeHuman, without having to first save the toon to a file. The importer will talk with the makehuman instance
and fetch all meshes (such as the body, hair clothes...), materials, rigs and poses. The process is almost instantaneous (a toon with a lot of clothes might take a few seconds to import).

The importer UI supports a wide range of settings and presets. By using a preset you can, for example, import a body mesh suitable for using together with MakeClothes. This will make it significantly easier
to develop assets aimed at a specific body type.

Note that for the importer to work, you will have to go to the Community -> Socket tab in MakeHuman and enable "Accept connections". Otherwise MakeHuman won't answer, and you will get an error in Blender.

### IK and amputations

The importer will use the skeleton set in MakeHuman to rig the resulting character in Blender. The rig can then be extended with the "IK rig" functionality: By clicking a button you can get extra 
IK controls, and IK chains set up for arms, legs and fingers.

Rigs can also be amputated in case detailed bones are not required. 

All rigs currently available to MakeHuman are supported. 

### Kinect

To be written

<br clear=all>

## A new windows installer

The windows version is now distributed as an executable installer that supports uninstall. After installing MakeHuman, it can now be found on the start menu like all other normal windows application. 

Note that it is no longer recommended to go to the installation folder and start MakeHuman manually there. In order to do so, you would have to manually set up an environment for python, something 
which is handled automatically by the start menu entry.

## Other bundled functionality

Apart from the above, some other functionality that previously had to be downloaded separately is now bundled:

### MHX2

MHX2 is now enabled per default in MakeHuman. The blender side of MHX2 can be downloaded from http://www.makehumancommunity.org/content/plugins.html

### MHAPI

MHAPI (a library with convenience calls for making addons for MakeHuman) is now included and enabled per default.

## Where to download

The following are links to where you can download beta 2:

You can [download the windows build here](http://download.tuxfamily.org/makehuman/nightly/makehuman-community-1.2.0-beta2-windows.zip).

For linux, [there is a new PPA](https://launchpad.net/~makehuman-official/+archive/ubuntu/makehuman-community).

## Providing feedback and bug reports

As always with a beta release, the important part is getting feedback and bug reports. 

If in doubt, feedback and bug reports can always be posted on the forums. But more formal information about bug trackers can be found here: http://www.makehumancommunity.org/content/bugtracker.html