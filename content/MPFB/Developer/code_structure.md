---
title: "Code structure"
draft: false
weight: 5
description: "A description of the general structure of the MPFB code"
---

This is a description of the general structure of the MPFB code.

## Overview

The code consists of a few different types of files:

* Data: these are not code files per se. Rather they are things such as JSON data files containing definitions of rigs or materials, or mesh objects.
* Service: this is either a stateless or singleton type of class with utility code. You will normally not manually instantiate these classes.
* Entity: this is a stateful class which is instantiated when performing an operation. Its instances might be long- or short lived. 
* Operator: in this case this is something that happens as a reaction to a click in the UI. While there could in theory be other types of operators in Blender, this is currently the only type implemented.
* Panel: this is a visible area in the interface. 

Outside of this there are some glue kind of files such as module descriptors and helper scripts. 

## Data

All system data that is bundled with MPFB is located under [src/mpfb/data](https://github.com/makehumancommunity/mpfb2/tree/master/src/mpfb/data). 

If you want to find where a rig or a material is defined, or where a target is loaded from, this is where you would look.

## Services

The bulk of the logic is to be found here. This is where you should start looking if you need to find code logic.

As said above, the services are either completely stateless, or are implemented as singletons. You will normally 
get access to it by simply importing its global instance. For example the HumanService:

    from mpfb.services.humanservice import HumanService
    
After which you can call methods defined on HumanService. From a coding point of view it should not make any
difference if the service is a singleton or a stateless class.

The following services are available:

* [AssetService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/assetservice.py) contains logic for locating and listing assets
* [ClothesService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/clothesservice.py) contains logic for loading MHCLO type assets and fitting them to the base mesh
* [HumanService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/humanservice.py) contains logic for constructing, serializing and deserializing humans.
It also contains logic for equipping assets on the human by calling relevant methods in other services.
* [LocationService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/locationservice.py) contains logic for resolving path location the the MPFB system and user data directories.
* [LogService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/logservice.py) contains logic for logging and profiling. 
* [MaterialService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/materialservice.py) contains logic for loading and manipulating materials. This includes both 
procedural materials and materials loaded from MHMAT.
* [NodeService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/nodeservice.py) contains logic for manipulating node trees, including serializing and deserializing them to/from json. It is closely related to the MaterialService.
* [ObjectService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/objectservice.py) contains logic for locating, selecting and activating objects. 
* [RigService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/rigservice.py) contains logic for manipulating rigs and bones, including serializing and deserializing them to/from json. Note that there is a lot of related logic in other parts of the code, particularly in [Rig](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/entities/rig.py)
and [righelpers](https://github.com/makehumancommunity/mpfb2/tree/master/src/mpfb/services/righelpers)
* [SocketService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/socketservice.py) contains logic for online imports from MakeHuman via a local socket connection. Note the 
related logic in [socketobject](https://github.com/makehumancommunity/mpfb2/tree/master/src/mpfb/entities/socketobject)
* [SystemService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/systemservice.py) contains some platform-specific utility calls, such as a method for opening a web browser 
a specific location.
* [TargetService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/targetservice.py) contains logic loading targets and manipulating shape keys
* [UiService](https://github.com/makehumancommunity/mpfb2/blob/master/src/mpfb/services/uiservice.py) contains logic for working with the user interface.

## Entities

To be written

## The user interface logic (Operators and panels)

The user interface is defined under [src/mpfb/ui](https://github.com/makehumancommunity/mpfb2/tree/master/src/mpfb/ui). The general principle is 
that each part of the user interface is placed in its own subfolder, although in some cases related panels are placed in the same subfolder.

The general structure of the ui folder is:

* There is an \_\_init\_\_.py file which imports all relevant parts (panels and operators) so that they become known to the system
* There is a file called *panel.py which contains the actual user interface definition
* The logic (what happens when you click a button etc) is placed in a subdirectory called "operators". Each button will have its own code file in this subdirectory.
* Relevant scene- and object properties are defined in json files in a subdirectory called "properties". These are, for example, text input boxes or checkboxes. 

As an example of the last bullet, here is the checkbox for "Fit to body" which is in the asset loading panel:

```
{
    "type": "boolean",
    "name": "fit_to_body",
    "description": "Adjust the shape of the imported clothes to fit the selected human",
    "label": "Fit to body",
    "default": true
}
```

To be written: describe how these are loaded via SceneConfigSet and BlenderConfigSet...
