---
title: "What happened to the MHX export in MH 1.1.x and later?"
draft: false
---

**Short version (for MakeHuman 1.2.x):**

MHX2 is bundled and enabled per default in the latest alphas of MakeHuman 1.2.x, but you still need to install the addon in blender. The blender side of the addon, is shipped with the MakeHuman installation zip. 


**Short version (for MakeHuman 1.1.x):** 

MHX2 is now a plugin you download from https://bitbucket.org/Diffeomorphic/mhx2-makehuman-exchange

If you use Blender you will most likely want to install this. If you don't use Blender, there is not yet an importer available for your application.

For installation of the MakeHuman exporter component, you should save the ''9_export_mhx2'' folder into you MakeHuman plugins folder.  

The location of this plugins folder will vary with operating system.
* **MacOS X**:  Macintosh HD/Applications/MakeHuman.app/Contents/Resources/plugins
* **Windows 7/8/10**: C:\MakeHuman\plugins (Assuming you installed as C:\MakeHuman), or where MakeHuman was unzipped
* **Debian/Ubuntu Linux**: /usr/share/makehuman/plugins  (double check accuracy of this)
also see: [[FAQ:I downloaded a third party plug-in. How do I install it?]]
 

**Long version:** 

The old MHX format has been deprecated (both by MakeHuman and by its author, Thomas Larsson). 

Thomas Larsson has replaced MHX with MHX2 which is available as an external, separately maintained plugin. The major change from mhx to mhx2 is that it is now divided into separate exporter and importer components.  This means it is theoretically possible to use .mhx2 with any application for which there is a suitable importer.  Currently, the only importer available is for Blender.

For details on this MHX2 plugin (as well as download the MakeHuman Exporter and Blender Importer) see https://bitbucket.org/Diffeomorphic/mhx2-makehuman-exchange

MHX2 is not integrated into the core distribution because of separate maintenance and release cycles.  However, it remains one of the most high fidelity ways to move assets from MakeHuman to Blender (and other applications when suitable importers become available).  The alternative is to use the generic transfer formats: DAE and FBX. Because of their generic nature, however, these will not give you the full convenience of using .mhx2.

If you need the specific features of MHX2, visit the link above and follow the instructions. 

There is also a tutorial video on how to install MHX2 here: https://www.youtube.com/watch?v=3CCHGX-6Mtk