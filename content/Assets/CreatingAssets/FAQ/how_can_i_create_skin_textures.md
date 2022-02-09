---
title: "How can I create skin textures?"
draft: false
---

A skin texture is basically a normal image, usually a PNG file with large dimensions (in the span between 1024x1024 and 8192x8192), with a simple text file descriptor (see MHMAT section below).

To demonstrate which regions end up where on the body, there is a special skin ["Annotated Skin"](http://www.makehumancommunity.org/skin/annotated_skin.html) in the skin repository. 

The easiest way to start with a skin is probably to download this and paint on top of it. 

## Texture painting in blender

For a full tutorial on this see [[Documentation:Texture painting a skin in blender|Tutorial: Texture painting a skin in blender]]

If you want to paint directly on a body, you are probably best off doing this in blender. For various reasons, it's slightly easier/efficient to texture paint in "blender render" mode rather than in cycles mode.

First, load a makehuman body. If you have MakeTarget and/or MakeClothes installed, just click the "load human" button. It's also perfectly viable to simply use a toon you exported from MakeHuman.

Then create a material and assign a texture to it.

In the default view you should now be able to switch to "texture paint" mode and draw on the body.

## Making a MHMAT file for the skin

To use the skin in makehuman you will also need a "MHMAT" file. This is a simple text file:

  name my_cool_skin
  diffuseColor 0.5 0.5 0.5
  tag somekeywordthatfitsyou
  diffuseTexture MyCoolSkin.png

Set "name" to what you want to call it in the lists inside makehuman. "diffuseColor" you can just copy (it's the color for skins that don't have a diffuse texture). "tag" is a keyword used for filtering inside MakeHuman if there are many skins, use whatever keyword you want. "diffuseTexture" is the important part. This is the filename of the image file with the texture. The path is relative to the location of the MHMAT file, so to avoid path problems, just place them in the same directory.

Save the mhmat file as whatever but with the ".mhmat" extension. If you skin texture is called "MyCoolSkin.png", it might make sense to save the MHMAT file as "MyCoolSkin.mhmat". Place the mhmat and the image texture in the "skins" directory under data (see [[FAQ:Where are my MakeHuman files found (where is my HOME directory)?]]). Next time you open MakeHuman you should now be able to choose the new skin on the skins tab.