---
title: "Rigging and posing"
draft: false
weight: 10
---

These pages contain code hints related to rigging and posing.

## Relevant services and entities

The main service for rigging is [RigService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/rigservice.py), which contains logic for manipulating rigs and bones.

Paired with this, there is the [Rig](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/entities/rig.py) entity, which is used in the process for constructing a rig from 
a JSON definition.

For the specific cases of conversion rigs to IK rig or to rigify, there are also [righelpers](https://github.com/makehumancommunity/mpfb2/tree/master/src/mpfb/services/righelpers)
and [rigifyhelpers](https://github.com/makehumancommunity/mpfb2/tree/master/src/mpfb/services/rigifyhelpers). Note that rigifyhelpers is only for _converting_ a rig (such as the
game engine rig) to rigify. It is not relevant for setting up a pure rigify rig directly.

## Working with rigs (and weights)

There are some helper functions on the developer panel:

![rigging developer panel](rigging_developer_panel.png)

These can be used to load/save the data files mentioned below.

## Data files

Rigs are defined with two files:

* rig.\*.json is the JSON definition for the rig as such, including which bones it include and how these should be fitted to the base mesh.
* weights.\*.json is a file with vertex weight specifications for bones.

### Rig definition

This is the definition for the left upper arm for the default rig, picked from 
[its definition file](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/data/rigs/standard/rig.default.json):

    "upperarm01.L": {
        "head": {
            "cube_name": "joint-l-shoulder",
            "default_position": [
                0.1700395941734314,
                -0.019311200827360153,
                0.5021342039108276
            ],
            "strategy": "CUBE"
        },
        "inherit_scale": "FULL",
        "parent": "shoulder01.L",
        "rigify": {},
        "roll": 2.3827133178710938,
        "tail": {
            "default_position": [
                0.217001274228096,
                -0.017674963921308517,
                0.4479554295539856
            ],
            "strategy": "MEAN",
            "vertex_indices": [
                8057,
                17023
            ]
        },
        "use_connect": false,
        "use_inherit_rotation": true,
        "use_local_location": true
    },
    
The keys of this structure are:

* head / tail: Information on where the bones head and tails are located, as relative to the base mesh (see below).
* parent: Which bone is this bone a child of
* rigify: settings for rigify meta rigs. This is discussed further down.
* roll: This is the initial rotation of the bone around its Y axis
* use_connect: force this bone's head to be at the exact location of the parent bone's tail
* inherit_scale, use_inherit_rotation and use_local_location: Strategies for which transforms to inherit from the parent bone,
see [this section](https://docs.blender.org/manual/en/latest/animation/armatures/bones/properties/relations.html) of Blender's
documentation for information on what these do.

There are also the following possible keys, not shown in the example above:

* bendy_bone: sub-structure that contains a subset of B-Bone settings for the bone.
* constraints: array of structures defining constraints to add to the bone.
* layers: an array of 32 booleans determining on which bone layers the bone should be visible.
* roll_strategy: specifies a rule to compute the roll automatically.
* rotation_mode: specifies the rotation mode to use for animation, chosen out of QUATERNION (default), XYZ, etc.

The head / tail blocks specify where the head and the tail of the bone should be, in relation to the base mesh. The 
"default_position" is a coordinate specifying where the head/tail should be placed as a last resort if no matching
strategy can be used. 

There are four strategies possible for matching:

* CUBE: position should be at the exact center of the joint cube vertex group specified in the "cube_name" key
* VERTEX: position should be at the exact spot of a specific vertex specified by the "vertex_index" key
* MEAN: position should be at the geometric mean between two or more vertices specified as an array in the "vertex_indices" key
* XYZ: the three coordinate values of the position should be taken from three separate vertices specified as an array in the "vertex_indices" key

When saving the rig, MPFB can automatically choose one of CUBE, VERTEX, or MEAN of two vertices
based on the position of the bone. Other strategies must be manually configured by editing the json file.

When the rig is loaded from json using the Developer panel, the strategies used are stored in custom
properties of the bones, and reused on save unless the bone was moved and the automatically chosen
strategy would be a clearly better match. Saving a rig loaded via the non-developer Add Rig panel
will lose all original strategy data and re-create it from scratch.

There is only one possible roll strategy (must be manually assigned when needed):

* ALIGN_Z_WORLD_Z: aligns the local Z axis to be as close as possible to the world Z axis.

The bendy bone settings support the following properties, listed here with their default values:

    "bendy_bone": {
        "segments": 1,
        "custom_handle_start": null,
        "custom_handle_end": null,
        "handle_type_start": "AUTO",
        "handle_type_end": "AUTO",
        "handle_use_ease_start": false,
        "handle_use_ease_end": false,
        "handle_use_scale_start": [false, false, false],
        "handle_use_scale_end": [false, false, false],
        "easein": 1.0,
        "easeout": 1.0
    },

The constraint list uses property names from the Blender Python API, with name and type being mandatory. A real example:

    "constraints": [
        {
            "head_tail": 0.0,
            "influence": 0.5,
            "mix_mode": "REPLACE",
            "name": "Copy@DEF",
            "owner_space": "LOCAL",
            "remove_target_shear": false,
            "subtarget": "thigh.L",
            "target": true,
            "target_space": "LOCAL_OWNER_ORIENT",
            "type": "COPY_TRANSFORMS",
            "use_bbone_shape": false
        },
        ...
    ],

The rigify block is only relevant for creating rigify meta rigs. It has additional settings for rigify. A rigify block
may look like this:

    "rigify": {
        "rigify_parameters": {
            "fk_layers": [
                ...
            ],
            "tweak_layers": [
                ...
            ]
        },
        "rigify_type": "limbs.super_limb"
    },
        
The rigify_type specifies which type of bone this is, as expressed by a rigify type. See the documentation of rigify for 
more information on these.

The "rigify_parameters" block lists on which rigify layers the bone should be visible. Each sub-block is a 32 boolean array
specifying on which layer the bone should be visible. Possible blocks are "fk_layers", "tweak_layers" and "secondary_layers".

The actual rigify layers are defined independently of the rig in 
[a separate data file](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/data/rigs/rigify/rigify_layers.json).
\[THIS SHOULD BE DESCRIBED BETTER\].

### Weights definition

This is the top of the weights file for the default skeleton:

```
{
    "copyright": "(c) the guy who clicked the save weights button",
    "description": "Weights for a rig",
    "license": "CC0",
    "name": "MakeHuman weights",
    "version": 110,
    "weights": {
        "breast.L": [
            [
                1399,
                0.01600159890949726
            ],
            [
                1400,
                0.01799819990992546
            ],
            ...
```

The first keys are simple meta data, which is not actually used by the code. The relevant section is the "weights" block.

The weights block has one sub-block per bone name. This sub-block is an array of weights definition, each which is a
two cell array with vertex index and actual weight in the bone's vertex group.

In the code example above we can see that both vertex 1399 and 1400 belong to the "breast.L" vertex group. 
Vertex 1399 has a weight of 0.01600159890949726 and 1400 a weight of 0.01799819990992546

## Posing

To be written

