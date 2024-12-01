---
title: "What happened to MHX?"
date: 2017-10-17T15:26:15Z
draft: false
---

In ancient times, the preferred way to import makehuman data into Blender was by using MHX (MakeHuman eXchange). MHX was a project which was
maintained separately from the MakeHuman main code.

This was a very complicated export method which included serializing all MakeHuman data to json and then deserializing it in Blender. Further, it
depended on auto-running a lot of python logic in order to get rigs working properly.

MHX was largely abandoned about a decade ago. The MakeHuman dev team keeps
[a fork of the original code](https://github.com/makehumancommunity/mhx2-makehuman-exchange) around, but it isn't maintained. Thus it 
will not work with, for example, Blender 4.x.