---
title: "MPFB"
draft: false
---

# MakeHuman Plugin For Blender
This page is the "main" page for the Blender plugin - in effect an "index" for documentation and tutorials regarding MPFB2. 

::{{#ev:youtube|ANnn8qKJMpc}}   AfyEbJnB1rs

About loading assets to your character.

::{{#ev:youtube|AfyEbJnB1rs}} 

This page will internally hold links for MPFB2 tutorials and development. 

## Get MPFB2 here=
:: * **[18&t=19356&hilitMPFB#p53411 Makehuman forum about MHFB2 ](http://www.makehumancommunity.org/forum/viewtopic.php?f#)**
:: * '''[MPFB2 on github](https://github.com/makehumancommunity/mpfb2)
:: * '''[MPFB2 status om github](https://github.com/makehumancommunity/mpfb2/blob/master/docs/general/status.md)
:: * '''[MPFB2 download the addon](http://download.tuxfamily.org/makehuman/plugins/)

### =Full announcement from Joel, made on the forum:## 

::I have today opened up the git repo of MPFB 2, https://github.com/makehumancommunity/mpfb2, for public access.

::This is a complete rewrite of MPFB 1 with added features (rigify support, procedural eyes, rig helpers...) and much improved code structure and performance (imports are 3x faster for example). A list of changes can be found at https://github.com/makehumancommunity/mpfb2/blob/master/docs/general/changes.md

::While some parts of MPFB 1 has not been ported yet (see https://github.com/makehumancommunity/mpfb2/blob/master/docs/general/status.md) and the official status is pre-alpha, I have used MPFB 2 a lot myself lately, and found it to be reasonably stable.

::MPFB 2 should be able to co-exist alongside MPFB 1, but it requires at least Blender 2.90.

::Nightly builds of MPFB 2 can be found at: http://download.tuxfamily.org/makehuman/plugins/. Builds made when something relevant has changed can be found in the dist directory of the git repository. Most of the time the dist dir build and the nightly build will be exactly the same code.

## Tutorials for using MPFB2=
There are a few things you need know and do to get this running. Most importantly the current version of MPFB is depending on that you are running the MakeHuman program and Blender side by side. That is the blender version will try to reuse the assets and resources that are "provided" by the MakeHuman program. Also, at the time of writing, you must still use MakeHuman to download assets, that and other functionality is not yet ported to Blender.

## Developers resources=

I will start this by making some developers notes that could eventually compile into one or more tutorials.
I will keep adding more notes to this page, but I urge you to:

* Add comments
* Add tips and links to other tutorials
* Add your own code
* Request topics that you think would need to covered
* Add links to other addons that is useful for VSC and MBFP2

### Using VSCode# 
I would recommend that you use VS Code since there is a very handy Blender Extension. This will help you as an experienced developer - and as a novice that wants to learn about Python and Blender. 
Take a look at this tutorial to get a quick overview - and follow this link to install blender/ and VSCode. [tutorial on installing blender/ and VSCode.](https://www.youtube.com/watch?v=77mMpeoh3OI&t) 


::::{{#ev:youtube|q06-hER7Y1Q}}


Now - If that did not seem too bad, you can move on to the next pages dedicated to actually running MPFB2 from VS Code: 

**Go here >>>''' '''[[Documentation:MPFB2 getting started with VS code]]**