---
title: "Corrective shape keys"
draft: false
---

These are instructions for how to set up shape keys on a rigged makehuman model in blender. 

## Step by step to make it work.

On the character body armature modifier, activate the function "Display modifier in Edit Mode"



![Part_1_01.jpg](Part_1_01.jpg)



Create a basis shape key and then a deformation shape key, give it a suitable name. Pin the shape key to always show.



![Part_1_02.jpg](Part_1_02.jpg)



Select the bone you want shall control the shape key and pose it to the position where you want full shape key deformation.
Remember the bone name and wich axis you rotate it, in this example bone "lowerarm01.L" local X rotation - press key R then XX.



![Part_1_03.jpg](Part_1_03.jpg)



Select the body and edit the mesh until desired shape for that pose. Proportional edit is very useful.



![Part_1_04.jpg](Part_1_04.jpg)



Reset the bone to default position - press key ALT and R

Prepare the shape key to be driven by the bone.



![Part_1_05.jpg](Part_1_05.jpg)



The Value field color is now purple. Unpin the shape key and you will see the mesh transforms back to the default shape.



![Part_1_06.jpg](Part_1_06.jpg)



Open "Graph Editor" - "Edit Drivers"



![Part_1_07.jpg](Part_1_07.jpg)



Select the shape key to the left and the tab "Drivers", in the field "Object" select the skeleton and "Bone" in this example "lowerarm01.L" As this example want the bone local X rotation to control this shape key select "X Rotation" and "Local Space".

Finish by setting "Type:" to "Averaged Value".



![Part_1_08.jpg](Part_1_08.jpg)



If the shape key shall deform on the negative rotation axis, add the driver modifier "Generator" and value -1.000 as shown here.



![Part_1_09.jpg](Part_1_09.jpg)



Rotate the bone on local X axis (key R then XX) and the shape will deform the mesh.

Adjust the shape key until satisfied. The shape will always deform in a strait line.



![Part_1_10.jpg](Part_1_10.jpg)




## Mirror shape keys

Select the shape key you want to mirror and activate pin.



![Part_2_01.jpg](Part_2_01.jpg)



Make a copy of the shape key.



![Part_2_02.jpg](Part_2_02.jpg)



Give the new shape key a suitable name.



![Part_2_03.jpg](Part_2_03.jpg)



Mirror the new shape key. Choose either "Mirror Shape Key (Topology)" or "Mirror Shape Key"



![Part_2_04.jpg](Part_2_04.jpg)



If succed you have a new working shape key on the opposit side, and just need to assign it to be driven by, in this example, the bone "lowerarm01.R".



![Part_2_05.jpg](Part_2_05.jpg)



If both alternative generate an error message, the mirror process has failed, that occur when the mesh is non symetric and differs to much. Dont accept any error at all.



![Part_2_06.jpg](Part_2_06.jpg)



Instead read part 3 below ("Transfer shape keys to another character"). Import a symetrical MakeHuman character. Transfer the shape key to it, do the mirror, and transfer the shape key back to the original character, and give the shape key a suitable name. It is uncertain if the shape will look exactly the same but it wont generate any error message.

## Transfer shape keys to another character

Most important to know, the characters must have exactly the same topology. In some cases character specific adjustments has to be done afterwards. At this moment I only knows it possible to transfer shape key's one at a time.

Select the source character and the shape key to transfer.



![Part_3_01.jpg](Part_3_01.jpg)



Shift select the receiving character's body and transfer the shape key.



![Part_3_02.jpg](Part_3_02.jpg)



If not exist also a "Basis" shape key will automatically be created.



![Part_3_03.jpg](Part_3_03.jpg)

