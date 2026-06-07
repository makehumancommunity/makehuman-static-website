---
title: "MakeTarget in MPFB2"
draft: false
weight: 30
---

# MakeTarget in MBPFB2

**Disclaimer: This is a guide by someone new to makehuman and modeling providing advice on the workflow which got him started successfully. It is probably not the only way to do things.**

The MakeTarget workflow in MPFB v2.0.15 differs slightly from those in MakeHuman version.

As with previous versions of MakeTarget
1. create a new human
2. create a new target/blendshape
3. edit the human mesh
4. save the target

However, to *create a new base human* is no longer a one-click process.
1. Open a new blender project to clear all blendshapes
2. Press "n" if needed to bring up the item/add-ons menu
3. Navigate to "New human > From scratch"
4. Under "Phenotype" uncheck "Add phenotype" and set "Phenotype influence" to 0
5. Under "Breast" uncheck "Add breast targets" and set "Breast influence" to 0
6. Optionally uncheck options in "Create".
7. Select the "Human" in Blender's outliner.
8. Navigate to "Create assets > MakeTarget"
9. Under "Initialize", name your target and press "Create target"
10. Ensure the options under "Symmetrize" are not grayed-out.

Steps 4 and 5 are meant to remove elements from the model which introduce slight asymmetries that seem to prevent MakeTarget's symmetrize operations from working. Sometimes the options still seem to be unavailable, in which case I would try rebooting Blender.

There is additionally some nuance regarding editing and symmetrizing the created blendshape.
* Edit in Blender's Edit mode.
* Symmetrization in Blender's Object mode.

The latter two points are where the operations worked for me, but other Blender modes may work as well.
