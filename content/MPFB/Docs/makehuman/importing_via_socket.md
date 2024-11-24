---
title: "Importing from MakeHuman"
draft: false
weight: 20
---

One way to import a character from MakeHuman is via a socket connection. This will import _baked_ meshes from MakeHuman. 

The limitation is that these imported characters will then not be possible to continue working on via MPFB. You will for example
not be able to equip more clothes or change target values. 

If you want a live character, see [Importing via MHM]({{% relref "importing_via_mhm" %}}), which is the currently recommended import path.

## Requirements and preparations

You need at least MakeHuman Community 1.2.0 for this to work. MakeHuman must be running. 

In order to do direct imports from MakeHuman, you must enable the "socket server" inside MakeHuman. This is disabled
per default. 

In MakeHuman, find the "Community" -> "Socket" tab.

![Enable socket server](enable_socket_server.png)

Check the "Accept connections" checkbox. The center column should indicate that the server socket is started.

You can change the port that the server socket listens on (under "advanced"), but it is unlikely that you want to do so. 

## Basic operation

The UI for importing from MakeHuman is located on the "N" shelf in Blender. 

![Import UI](import_ui.png)

If all you want to do is to import with defaults, simply click the "Import human" button.

## Import options

On the import panel you can specify that you want to use particular settings / overrides.

- **Presets to use**: These are settings for how the import should be done, for example if clothes should be imported or not. If you select "use ui settings" here, the importer will use what is set on the "importer presets" panel directly below the "import from makehuman" panel.
- **Skin settings to use**: If you have specified (in the presets) that you want to use the enhanced skin material, you can here choose which particular skin settings you want to use.
- **Eye settings to use**: If you have specified (in the presets) that you want to use the procedural eye material, you can here choose which particular eye settings you want to use. 