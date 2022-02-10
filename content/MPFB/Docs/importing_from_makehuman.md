---
title: "Importing from MakeHuman"
draft: false
weight: 20
---

These are general instructions on how to import a model from MakeHuman.

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