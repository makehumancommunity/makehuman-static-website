---
title: "MakeHuman does not start"
draft: false
---

See also [[FAQ: I have a problem with makehuman. How do I report it?]].

There are multiple reasons why MakeHuman does not start, and without some background information it is impossible to tell you what's wrong. 

In order to be able to give any kind of sensible answer, we will need to know:

* What does the log say? See [[FAQ: How to provide a makehuman log for a good bug report?]]
* What graphics card are you using?
* If you have a laptop with dual graphics cards, are you sure that you are using the 3d-enabled one?
* What operating system are you using? Preferably including details about if it's 32 or 64 bit, what the system language is, exactly what OS version it is and so on.
* What version of makehuman did you download?

## It worked before / old settings

If you have been able to start a prior version of MH on the same machine, but a newer version does not start, something might be corrupt or incompatible in the user directory. Try deleting the DOCUMENTS/makehuman/v1py3 directory before launching MH.

See [[FAQ: Where are my MakeHuman files found (where is my HOME directory)?]] for info on how to find this directory.

## Graphics card issues

The by far most common reason for MakeHuman silently failing during startup is a graphics card incompatibility. If you have an integrated intel graphics card for example, this is where we'd start looking. 

At the point of writing this, we have implemented several measures for avoiding these crashes, but they have not yet made it into a build. The fixes are specifically not included in 1.2.0 alpha 3. 

It is ''possible'' your problem is solved already, but to test this your only option is currently to run from source, see [[FAQ: How can I run the same code as the nightly build from source?]]. The other option is to wait for the next build to be released.

Another source of problems regarding graphics cards is when you try to start MakeHuman on a laptop with dual graphics cards. In this case, MH might get confused and pick settings for one card while in fact trying to run on the other. Usually, you can in these cases force MH to run on a specific graphics card. In later makehuman releases (1.2.0+) on windows, you will have to tell your laptop to run "pythonw.exe" on the discrete graphics card. In most cases this file will be inside c:\users\YOUR-USER-NAME\appdata\local\makehuman-community\python.