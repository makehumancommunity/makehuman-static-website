---
title: "Releases:130"
draft: false
---

These are the release notes for 1.3.0, which was released 2023-04-28.

## General

The main selling points of this release are a set of body shapes by Elvaerwyn and a series of bug fixes for making MakeHuman work with windows 11 and newer linux releases. If you already use a nightly build which works for you and which has the body shapes, there is no reason to switch 
to the release build. 

## Downloading

* For windows, you can download the release binary from [here]({{% param "primaryFilesUrl" %}}/releases/makehuman-community-1.3.0-windows.zip) or [here]({{% param "secondaryFilesUrl" %}}/releases/makehuman-community-1.3.0-windows.zip).
* For linux, the recommended way to run MakeHuman is from source. See the [readme on github](https://github.com/makehumancommunity/makehuman/blob/master/README.md) for instructions. However, there are also new builds [in the PPA](https://launchpad.net/~makehuman-official/+archive/ubuntu/makehuman-community).

## Changes since 1.2.0

These are the main themes of the changes since 1.2.0. See the [commit log on github](https://github.com/makehumancommunity/makehuman/commits/master/) for details.

* Added a new set of targets with body shapes by Elvaerwyn
* Fixed several bugs which would cause the viewport to be empty, black or corrupted with newer versions of PyQt
* Fixed several bugs which would cause the viewport to be empty, black or corrupted with windows 11 or later.
* The relevant addons (asset downloader, mhapi, socket...) are now bundled with the main code


