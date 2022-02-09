---
title: "Do you have some quick tips on how to make a nice image with a makehuman toon?"
draft: false
---

Making a nice 3d image takes skill. There is no way around it: You'll need to know what to do, and be good at it. 

However, there are also some basic pointers which may be helpful when starting out. 

* Consider using a specific proxy for male/female (it particularly helps with the clavicle in female)
* Set the "default no toes" skeleton in MH before exporting
* Export/import using MHX2
* When importing using MHX2, override presets and set rig to "exported MHX". This way you get good weight painting *and* IK. 
* Use the cycles rendering mode in blender
* Enable at least two subdivisions on the body at render time
* Use lots of light with at least one narrow direct light source to provide interesting shadows, and plenty of indirectly bounced light in order to make things not too sharp
* Do not use light capping or filter glossy. Using these shortens render times significantly, but it also removes crispness from the final render. 
* Increase light bouncing to the preset "full global illumination"
* Consider mixing in SSS in the skin texture. Follow a tutorial from youtube to get a decent node setup 
* Read https://support.solidangle.com/display/NodeRef/skin to understand what else can be done for skins
* For materials on clothes and surroundings, consider using PBR rather than the normal diffuse-glossy-fresnel mix. See https://www.blenderguru.com/tutorials/pbr-shader-tutorial-pt1/ for an intro. There are plenty of plugins/materials to download, so you don't have to design them yourself.
* If you got lots and lots of patience, consider using particle hair. See http://www.blendernation.com/2016/08/09/blender-cycles-hair-tutorial/
* Most of what is true for photo composition is also true for making a good 3d still image, see http://www.techradar.com/how-to/photography-video-capture/cameras/10-rules-of-photo-composition-and-why-they-work-1320770