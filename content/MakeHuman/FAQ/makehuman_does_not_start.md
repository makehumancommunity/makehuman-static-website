---
title: "MakeHuman does not start"
date: 2017-10-17T15:26:15Z
draft: false
weight: 10
alwaysopen: false
---

Before reading the following, also take a look at [What is the current status of MakeHuman?]({{% relref "current_status" %}}).

There are multiple reasons why MakeHuman does not start, and without some background information it is impossible to tell you what's wrong. 

In order to be able to give any kind of sensible answer, we will need to know:

* What does the log say? See [How to provide a log for a good bug report?]({{% relref "how_to_provide_a_makehuman_log_for_a_good_bug_report" %}})
* What graphics card are you using?
* If you have a laptop with dual graphics cards, are you sure that you are using the 3d-enabled one?
* What operating system are you using? Preferably including details about if it's 32 or 64 bit, what the system language is, exactly what OS version it is and so on.
* What version of makehuman did you download?

## It worked before / old settings

If you have been able to start a prior version of MH on the same machine, but a newer version does not start, something might be corrupt or incompatible in the user directory. Try deleting the DOCUMENTS/makehuman/v1py3 directory before launching MH.

See [Where are my MakeHuman files found (where is my HOME directory)]({{% relref "where_are_my_makehuman_files" %}})? for info on how to find this directory.

## Graphics card issues

The by far most common reason for MakeHuman silently failing during startup is a graphics card incompatibility. If you have an integrated intel graphics card for example, this is where we'd start looking. 

Another source of problems regarding graphics cards is when you try to start MakeHuman on a laptop with dual graphics cards. In this case, MH might get confused and pick settings for one card while in fact trying to run on the other. Usually, you can in these cases force MH to run on a specific graphics card. In later makehuman releases (1.2.0+) on windows, you will have to tell your laptop to run "pythonw.exe" on the discrete graphics card. In most cases this file will be inside c:\users\YOUR-USER-NAME\appdata\local\makehuman-community\python.