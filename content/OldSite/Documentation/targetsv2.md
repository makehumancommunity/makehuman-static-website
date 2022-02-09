---
title: "TargetsV2"
draft: false
---

### Before using the program

MakeTarget Version 2 is created to work with new Blender. It is used to create custom targets for the body. A target is also called a morph or morphing which normally means the change of a shape in 3d. So it is used to create morphes or target of the basemesh. This program can also be used to correct targets made before.

The result of this target in MakeHuman is a table of changed vertices. It is an ASCII file containing 3 values how each vertex should be moved. It is obviously derived from Blender shape keys. So the workflow includes to create a new shape key in Blender as well.

There is a difference: Blender internally creates a copy of the complete mesh, even when you only change one vertex, the target of MakeHuman only contains the changed vertices.

Before a new target is created, the following questions should be answered:

* Should the target only change parts of the body like ears or lips not covered by clothes and where bones will not be stretched or located different?

   In this case is sufficient to work only with the body

* Does the target also change part clothes and bones?

   In this case body + helper mesh must be used

* Which mesh should be most likely used?

   You should decide between male or female mesh or the standard mesh used in MakeHuman, when started.


### Load the mesh


Best way is to load a human mesh using MPFB (MakeHuman Plugin for Blender). It has some presets which have to be used if you work with MakeTarget and it has a special help to work with the helper. You need to have MakeHuman in parallel using the socket connector (see image below).

In Blender, set MPFB "Settings" to "MakeTarget" and load settings. After that import the mesh.



![MTG](MTG)





To switch on the helper a modifier is added, just press the marked symbol and the helper will appear or disappear.




![MTG](MTG)




If you don't use MPFB, you can also load a human mesh with Makeclothes2. This will not include the toggle for the helper.

There are a few additional methods, you can load it via mhx2 .. but be careful the scale must be the same otherwise your target will either use 1/10 of the movement or 10 times as much later in MakeHuman (mhx2 export: use decimeter). So easiest way is either to use MPFB or MakeClothes


### Create a new target

As an example a target named lower-eyesbrows (should look a bit like an early human) should be created. It does not involve clothes and also no bones are changed. So in this case a mesh without
helpers would be sufficient.

The name lower-eyebrows is used to create the target. The result are two shape keys. An initial one "Basis" and the shape key which has to be changed.




![MTG](MTG)




Now the mesh is changed (make sure lower-eyebrows is selected in shape keys) so that the eyebrows are lowered. Best is to use proportional edit for your work. Be aware not to influence the eyelash region, otherwise the helper mesh must be changed for the eyelashes also.

Lets only change one eyebrow like in the picture.

The other side will be created by mirroring the target, here "copy +x to -x" is used. The copy command symmetrizes left and right side. A vertex in the middle will be set to x=0, so the mesh will stay totally symmetrical.




![MTG](MTG)



''Hint: symmetrizing is done with a table, so it will not fail as long as the table matches the mesh you load.''


### Save the target

The last step is to save the target. Search for your target path of MakeHuman (custom targets). You can create a sub-folder if you work with a lot of own targets, like in the picture.

In MakeHuman these folders must be scanned again. So press the rescan-button. Then a subfolder will be detected and the target is ready to use.




![MTG](MTG)




### Load a target

You can reload this target into MakeTarget2. As an example it is also easy to load a target made by someone else and change it or to load the official targets (only available on GitHub, the targets of the distribution are compressed). Especially if the helper was not changed, something that is sometimes neglected: load the mesh with helper, load the target, do the corrections and save it again.




![MTG](MTG)

