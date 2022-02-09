---
title: "How can I run the same code as the nightly build from source?"
draft: false
---

Note that these instructions are for running the development code which resides on github. They are specifically ''not'' for running the old python 2 based code from bitbucket. 

To run the code you will in summary need:

* Python 3 (any python version, including Anaconda, from 3.5.0 and upwards)
* PyQT5
* PyOpenGL
* numpy

## Running from source on Linux

These instructions are written for Ubuntu 20.04. Other systems might need a slightly adapted procedure.

### Installing dependencies

All dependencies are available via apt:

    sudo apt-get install python3 python3-opengl python3-pyqt5 python3-numpy git 

### Getting the source

As we fetch source code from several repos, let's make a subdir in our home to store everything:

    cd ~
    mkdir makehuman-devel
    cd makehuman-devel

Fetch all source directories. For now we'll use a fork of MHX2, but once we're sure our py3 port works we'll send a pull request back to Thomas:

    git clone https://github.com/makehumancommunity/makehuman.git
    git clone https://github.com/makehumancommunity/community-plugins-mhapi.git
    git clone https://github.com/makehumancommunity/community-plugins-assetdownload.git
    git clone https://github.com/makehumancommunity/mhx2-makehuman-exchange

### Link plugins

We'll put symlinks in the plugin directory so that we can simply pull from the plugin repos and get the newest versions later on.

    cd makehuman/makehuman/plugins
    ln -s ../../../community-plugins-mhapi/1_mhapi
    ln -s ../../../community-plugins-assetdownload/8_asset_downloader
    ln -s ../../../mhx2-makehuman-exchange/9_export_mhx2

### Download core assets

Cd to the makehuman dir and run the download script

    cd ..
    python3 download_assets_git.py

You can also optionally run the compile*.py scripts to generate NPZ files, but this is strictly speaking not necessary

### Start makehuman

To start MH be sure to use python3:

    python3 makehuman.py

If you get a crash or no toon is visible in the window, try:

    python3 makehuman.py --noshaders

## Running from source on windows

These instructions should work independently of windows version. 

### Installing dependencies

The only thing you need to download manually is Python. Any python from version 3.6.0 and upwards should work, including versions such as Anaconda. 

You can get an official python here: https://www.python.org/downloads/

It should not matter if you download 32 or 64 bit versions. 

When installing python, opt to add python to PATH. 

After having installed python, start a command prompt (left windows key + r, enter "cmd"), run the following commands to install the dependencies:

    pip install numpy
    pip install pyopengl
    pip install pyqt5

If it says it cannot find the command "pip", you will have to specify the full path to it. This should be in the "scripts" dir where you installed python.

### Getting the source

Quickest and easiest is to download a zip file of the repository, although you will most likely want to use git. 

You can find the zip file here: https://github.com/makehumancommunity/makehuman/archive/master.zip

If you use git, the address to clone is https://github.com/makehumancommunity/makehuman.git

Unzip / clone the source at an appropriate location. 

### Download core assets

Again start a command prompt, "cd" to the "makehuman" subdir of where you put the source, and run the download script

    python download_assets_git.py

It is normal that this script takes a (very) long time to finish, but all subsequent updates should be more or less immediate. 

The above command requires that git is installed with support for git LFS, see https://git-lfs.github.com/. It it's not possible to use git with lfs, you can instead run

    python download_assets.py

But this is deprecated and will currently fetch outdated assets.

You can also optionally run the compile*.py scripts to generate NPZ files, but this is strictly speaking not necessary.

### Start makehuman

To start MH:

    python makehuman.py

If you get a crash or no toon is visible in the window, try:

    python makehuman.py --noshaders

## Running from source on Mac

To be written