---
title: "Running MakeHuman from source"
draft: false
weight: 4
---

## Before you start

This page describes running MakeHuman 1.1 running from source code hosted on Bitbucket. If you're looking for the upcoming MakeHuman 1.2 go to [https://github.com/makehumancommunity/makehuman](https://github.com/makehumancommunity/makehuman). You'll also find basic instructions on how to get started on this page.

## Overview

There are several reasons why you might want to run MakeHuman from a source snapshot from BitBucket rather than use one of the pre-built packages:

* This makes it easy to update and get the latest features
* You get full access to all assets (in the builds the assets are only available in compiled archives)
* It's possible there is no functional pre-built package for your platform. 

In order to run from source, you need the following:

* Get a source snapshot from BitBucket
* Install/setup a python environment with [python 2.7](http://www.python.org) (python later than 2.7 will not work) and the following dependencies installed:
** [NumPy](http://sourceforge.net/projects/numpy/files/NumPy/)
** [PyOpenGL](http://pyopengl.sourceforge.net/)
** [PyQT](http://www.riverbankcomputing.com/software/pyqt) (the required version is pyqt for qt4, qt5 is not supported)
* Run the script for downloading assets (this is described in a section at the bottom of the page, after the platform specific notes)
* (optionally) run the scripts for compiling assets

## Getting the source from Bitbucket

At this point in time it's recommended you run from the "stable" branch. If you're feeling adventurous, you can run "default", but in more cases than not this will crash for you.

The quickest way to get the source is to download is as a zip at https://bitbucket.org/MakeHuman/makehuman/get/stable.zip

However, if you plan to update in the future, you will want to install a [mercurial](https://www.mercurial-scm.org/) client and check out a source clone. This looks different depending on platform.

## Setting up the environment on Windows

Setting up the environment on Windows is normally somewhat cumbersome. 

There is a tutorial video on how to do this, but the links in the video are outdated. Rather than downloading all the dependencies in a big zip file, you will need to download them 
separately from the links above. However, in the video you can see what they should be named approximately.

{{#ev:youtube|3CCHGX-6Mtk}}

**IMPORTANT:** You ''must'' install the same architecture (32-bit or 64-bit) for all packages. While it's possible that you can find 64-bit packages for everything, it's probably easier to go for 32-bit packages even on a 64-bit system.

There are several mercurial clients for windows, but one of the more popular ones is [TortoiseHG](http://tortoisehg.bitbucket.org/).

## Setting up the environment on Linux

Running from source on Linux is generally trivial since all the dependencies are available via the package management. 

For Ubuntu and Debian, there is [stable&fileviewerfile-view-default a script](https://bitbucket.org/MakeHuman/makehuman/src/179e10c2b9440f73f6d154839e8720e1dccf39cd/buildscripts/deb/install_deb_dependencies.bash?at#) for installing all the required dependencies.

If you are not using a debian derivate, you will need to figure out that the dependencies are called on your platform. You will probably want at least:

* python 2.7
* python-numpy
* python-opengl 
* qt4
* python-qt4 
* python-qt4-gl

For example on ubuntu:

  sudo apt-get install python-numpy python-opengl python-qt4 python-qt4-gl

Usually it is not necessary to install python, since most Linux distributions have python preinstalled. Currently MakeHuman depends on python2.7 (a port to python3 has been started). In the future python2 might not be pre-installed anymore, so make sure python2 is on your system:

  python2 --version

The mercurial client is also available in most linux distributions. In ubuntu it's called "mercurial". For example:

  sudo apt-get install mercurial

To get a source snapshot from bitbucket run:

  hg clone https://bitbucket.org/MakeHuman/makehuman
  cd makehuman
  hg update -C stable

## Setting up the environment on MacOSX

To get the sources you need to either install hg or grab the very useful mercurial/git gui [SourceTree](https://www.sourcetreeapp.com).   

After you install the SourceTree app just go to the [MakeHuman project on BitBucket](https://bitbucket.org/MakeHuman/makehuman) and click on the download icon in the upper right corner who's mouseover says 'Clone in SourceTree'

Now that you have the source you need to get a python that supports the libraries/modules listed above.  The easiest way to get a working python and needed libraries installed on your mac is via [Brew](http://brew.sh).

After you install and/or update brew with the instructions on that site do the following:

 brew install python
 brew search qt

On my system that showed the a list of different things to install, what you are looking for is qt4 and pyqt4.   The entries that matched that for me were:

 brew install cartr/qt4/qt
 brew install cartr/qt4/pyqt

This will install dependencies like sip, etc as well if needed.   If it says it's missing dependencies ( say sip ) do a search on those dependencies and install the right versions.  Note that you do not run brew as root, it's files are all owned by you.

Once that is complete you should be able to follow the instructions to complete downloading, compiling the assets and pulling new versions from the repository ( via SourceTree if that is what you used ).

## Download and compilation scripts

Once you have an environment with the dependencies installed, and a source snapshot, there are a few scripts that should normally be run. They are available in the "makehuman" directory and
should probably be run in this order:

* download_assets.py (this is required, and will dowload all clothes etc)
* compile_targets.py (these three are optional but will make starting makehuman faster)
* compile_models.py
* compile_proxies.py

## Starting makehuman

With all the above, simply run the "makehuman.py" script either by double-clicking on it or by executing it from a console prompt.