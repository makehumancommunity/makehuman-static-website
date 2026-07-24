---
title: "How do I export assets from MakeHuman to Blender?"
draft: false
---

There are two main pipelines for exporting stuff from MakeHuman to Blender:

* MPFB (see also [[FAQ: What is MPFB (MakeHuman Plugin For Blender)?]]). This is the new pipeline, which is suitable for MakeHuman 1.2.0 and Blender 2.80. This is generally recommended unless you really need a specific feature of MHX. MPFB will make blender able to communicate directly with MakeHuman rather than relying on file exports.
* MHX (MakeHuman eXchange). This is the traditional pipeline consisting of a file exporter for makehuman and a file importer for blender. This is recommended if you for some reason is stuck with MakeHuman 1.1.x and Blender 2.79 or older. MHX has several issues with Blender 2.80, and is generally considered superseded by MPFB in MakeHuman 1.2.x.