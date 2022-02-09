---
title: "MH4UE"
draft: false
---

On this page you will find links to various things you will need when you want to use Makehuman characters in Unreal engine!

Please add your own pages, comments and tips where ever you find it is needed!  


## Introduction= 
When working with MakeHuman in Blender you will have some high quality characters to play with and you will see that the community addons can help you a lot. There are a few primary **[must have Blender addons](http://www.makehumancommunity.org/content/plugins.html)''' please use '''Blender 2.8** (or higher?) - these are the tree you will need to have and initially know about to full use of blender:

* Makehuman the community addon, that will allow you to fetch your character from MakeHuman to Blender directly!
* MHX2 Runtime, that will allow you to the import MHX2 files you made in MakeHuman 
* [[Documentation:MHBlenderTools:_MakeTarget|MakeTarget]] that will help you to make new Targets to be used from within MakeHuman.

### Into Blender and Unreal# 

When you want to use your characters in Blender, or when you want to export them to a game engine - UE4 or Unity - you even get some shape keys, also called morph targets. These are however not always "included" in the files exported from MakeHuman - specifically the shape keys are added by the MHX2 runtime addon. ( Also the community Blender addon contains some kind of shape key/pose functionality, but I have not been able to find any explanations for what they are doing! )

You can also take a look at this page for more on how to work with Blender: [[Moving Assets into Blender]].

Rather than making your characters in MakeHuman with one fixed expression/shape/pose, you would probably want to have the same options available in Blender. So I investigated the above addons and made MakeShapes as a small extension to MakeTartarget2. The general idea is have been to to transfer the Targets, expressions and the expression builder "sliders"... as-is, so they can be used as shape keys. 

There are, currently, two pages for this, one describing the process of getting MH to Blender and then into Unreal. And one describing the addon that will add more "shape keys" to your characters (while in blender). 

* [[Documentation:Saving_models_for_Unreal_Engine_and_how_to_import_them_there|Saving models for Unreal Engine and how to import them there]].
* [[Documentation:Saving_models_for_Unreal_Engine_Materials|How to setup Unreal materials]].
* [[Documentation:Unreal_MHC|Unreal MakeCustomization]].
* [[Documentation:MHBlenderTools: MakeShapes|MakeShapes - getting more shape keys/morph targets]]

### Inside Unreal# 

When your character(s) are inside Unreal you want to take full advantage of all the options. For this I am working on some character customize tools that will allow you to set up your characters either as "hand customized" or randomized.

## Additional resources=
And I also made these pages: 
* [[Documentation:Unreal Engine ALS V4]]
* [[Documentation:Unreal Engine Vehicle Variety Pack]]