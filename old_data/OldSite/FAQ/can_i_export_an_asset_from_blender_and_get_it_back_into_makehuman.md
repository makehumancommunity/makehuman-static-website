---
title: "Can I export an asset from Blender and get it back into MakeHuman?"
draft: false
---

Short answer: No, not for typical workflows.

The .mhx2 format, so far, has only one exporter (and it is for MakeHuman) and only one importer (and it is for Blender). You can go from MakeHuman to Blender, but not back again to MakeHuman with .mhx2. You can save what you do in Blender, of course, as .blend files, but MakeHuman can not read these either. If you want to use the .blend file on another computer, consider using the [ File | External data | pack all into .blend ] menu in Blender so that your textures follow you automatically to the second computer.

If you want to go from MakeHuman to Blender for the animator, then get feedback from her (the animator), and then make changes specified by the animator, you should save the MakeHuman file as both an .mhm file which saves what you have in the MakeHuman interface, and as .mhx2 which can be read by Blender. You can start from where you left off with the .mhm, make the changes specified by the animator, and then create a NEW .mhx2 for her. You cannot take changes the animator has made in Blender and get them back into MakeHuman. Not possible with any file format. That is not how MakeHuman works. It is not a regular 3D modeling program. It is the initial program in a workflow chain. Once you have moved to Blender (or Max or Maya) you are stuck there.

The one other thing you might want to do is make clothes that you can put on different characters in MakeHuman. This you CAN get back into MakeHuman with some work, but the format is NOT .mhx2. You use the MakeClothes plugin in Blender to produce the clothes, and they are saved from that plugin in a form that can be used directly by MakeHuman. There is documentation on the MakeClothes plugin here, and there are many user contributed assets made with it on the community assets page. See http://www.makehumancommunity.org/conte ... ssets.html for these assets. 

See this documentation for making your own assets: 
http://www.makehumancommunity.org/wiki/ ... new_assets
http://www.makehumancommunity.org/wiki/ ... _tutorials