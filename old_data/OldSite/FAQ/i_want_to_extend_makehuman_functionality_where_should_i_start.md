---
title: "I want to extend MakeHuman functionality. Where should I start?"
draft: false
---

In almost all conceivable scenarios, you'll want to write a plugin rather than change the MakeHuman code as such.

While writing a plugin isn't trivial either, it is far more easy than digging into the MH core code. 

A good start for plugins is by building on MHAPI, which can be found here: https://github.com/makehumancommunity/community-plugins-mhapi

An example of a plugin using MHAPI is the asset downloader, which is available here: https://github.com/makehumancommunity/community-plugins-assetdownload