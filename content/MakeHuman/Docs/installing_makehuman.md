---
title: "Installing MakeHuman"
draft: false
weight: 2
---

MakeHuman can be downloaded here [Later in the development life cycle, it might make sense to download nightly builds, which are found here: [http://download.tuxfamily.org/makehuman/nightly/](http://www.makehuman.org/download.php].).
Nightly represent the latest deveopmental updates and are not guaranteed to be stable.

## System Requirements

You will need about half a gigabyte of free disk space. 

In order to use some realtime materials and obtain the best from the internal rendering engine, it's required an average quality graphic card, produced after the year 2006. In general, your graphics card should support OpenGL Shading Language (GLSL) version 1.2 or above. There have been reports that the model colors are corrupted on some older Intel Graphics cards (often appearing blue and black).  If you experience this, a possible work-around is to start MakeHuman™ with the "--noshaders" command line switch.  On Windows, this switch can be added to your shortcut. See also [[FAQ:MakeHuman renders odd colours and weird transparency artefacts. Can you help me?]]

## Windows

Download the zip file from the from the download page [download page](http://www.makehuman.org/download.php). Then simply unzip it where you prefer, and double click on makehuman.exe to start the application. No installation is needed.

## Mac OS X

Download the DMG file from the download page [download page](http://www.makehuman.org/download.php). Once downloaded, mount the disk image and drag the MakeHuman app into your Applications folder. MakeHuman supports Snow Leopard and newer.

## Linux

At the point of writing this, the newest stable release is only available via PPA, see [https://launchpad.net/~makehuman-official/+archive/ubuntu/makehuman-11x]. This should work on all debian derivatives.
Other Linux distributions will need to run from source.

## Installing from source

If you want to play around with the code, follow the latest development, or are having trouble with the prepackaged binaries you can run from a source clone from BitBucket. This requires that you have installed python 2.7 and a set of other 
dependencies. See [[Documentation:Running_MakeHuman_from_source]] for more information.