---
title: "What is the current status of MakeHuman?"
date: 2017-10-17T15:26:15Z
draft: false
---

## Version 1.x of the MakeHuman GUI application

MakeHuman is by today's standard a rather old system. The core 3d engine is now somewhere around 15 years old, and it is using standards which 
are no longer relevant for modern graphics cards. Many graphics cards still support these outdated standards, but for some systems, there will
be difficulties running MakeHuman.

A few attempts at modernizing the 3d engine have been made, but they have ultimately failed. There are many reasons for this, but a root of the
problem is that program logic, UI logic and 3d logic are mixed in the code base. Further, the persons who wrote the code modules are long since
gone, and the documentation of the reasoning behind the design has been lost. Thus fixing any bug in the code base is labor intensive and very
complicated.

Because of this, the status of the MakeHuman 1.x GUI application has moved from being in maintenance mode to mostly being not modified at all.

This said, the application still works for most platforms. It will continue to work for most users. But bug fixes and updates should generally not be expected.

## A new version of the GUI application

Since the general conclusion is that the old code base is unmaintainable, an initiative to rewrite the code base from scratch has been initiated.

For more information about this, see [Is there a MakeHuman version 2?]({{% relref "makehuman_version_2" %}})

It should be noted that this as of yet is not a functional replacement of the old GUI application

## Other implementations

The above regards the standalone GUI application. There are also other implementations of the MakeHuman logic. For example,
[MPFB]({{% relref "../../MPFB" %}}) is updated and actively supported.
