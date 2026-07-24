---
title: "Big dump from drupal"
draft: false
---

## Introduction

MakeHuman (MH) is Open Source software (AGPL3.0) for creating lightweight, realistic 3D models of the human form. It is designed to be easy to use and flexible. The models are based upon real data for ethnicity, sex and body type and can produce an almost limitless range of human and human-like forms. The forms can be posed and rendered in the software itself or exported into other softwares for further manipulation.
It is developed by a community of programmers, artists, academics and enthusiasts interested in 3D computer models of human beings.
MakeHuman™ is used to create a 3D mesh with optimized topology representing human beings with a user-controlled mix of characteristics including race, sex, size, muscularity and other features. The models thus created are integrated into one of two typical pipelines or workflows.
In the first one, MakeHuman™ is integrated in a professional pipeline, where the A-posed mesh is exported into a full-featured 3D CGI system such as Blender, Maya, XSI, C4D, Zbrush etc.. in order to be included in complex scenes and renderings, or used for games.
In the second pipeline the mesh is posed and clothed directly in MakeHuman™, then rendered with an external engine, for 2D art or quick demo reel of a character.
This section contains high-level articles that describe the purpose and features of the MakeHuman software.
* Features-- describes the technical features of the program
* Evolution towards a Universal Model Topology: the HoMunculus-- gives an interesting background history of the development of the MakeHuman model
The MakeHuman User Documentation includes articles for installing the software and using it 'out of the box'  as well as extending and/or configuring MH for your own purposes. Beginners will want to begin with theInstallationsections for their computer systems and theGUI and Modellingsection for using the program. 

### Legal
The MakeHuman License
The MakeHuman license is a split AGPL/CC0 setup.!LINK!/content/license.html -- The full text of the license can be found here!/LINK!. There is also a!LINK!/content/license_explanation.html -- license explanation page!/LINK!. 
External Tools Licenses
From time to time the MakeHuman™ Team may release new external tools in various forms. Unless otherwise explicitly stated they are covered by the GNU AGPL 3.
Current tools are: 
* MakeTarget scripts for Blenderis distributed under the GNU AGPL 3. The MakeHuman morph target files that it generates are per default not covered by any license, since they are designed by you. However, if you make a morph target based on another pre-existing morph target (or a combination of pre-existing morph targets) you must fulfill the license terms of the pre-existing morph target.
  Note that all targets in the MakeHuman base distribution are licensed AGPL and that any target derived from these must also be licensed AGPLunless you get written permission by the author of the target file you derive from.
* MakeClothes script for Blenderis distributed under the GNU AGPL 3. If the user is the original author of the clothes, he is free to choose any license for them.
* MakeWalk script for Blenderis distributed under the GNU GPL 2. The license of output files generated using it is free to determine by the user, except when mocap data was used that enforces a specific license.
* MHX Importer.It is distributed under the GNU GPL 2.
* MakeTarget standaloneis distributed under the GNU AGPL 3. The MakeHuman morph target files that it generates are per default not covered by any license, since they are designed by you. However, if you make a morph target based on another pre-existing morph target (or a combination of pre-existing morph targets) you must fulfill the license terms of the pre-existing morph target.
  Note that all targets in the MakeHuman base distribution are licensed AGPL and that any target derived from these must also be licensed AGPLunless you get written permission by the author of the target file you derive from.
See the!LINK!http://www.gnu.org/licenses/agpl-3.0.html -- GNU Affero General Public License!/LINK!and!LINK!http://www.gnu.org/licenses/gpl-2.0.html -- General Public License!/LINK!for more details


### MakeHuman™ and its Purpose
MakeHuman™ is a tool designed to simplify the creation of virtual humans using a Graphical User Interface, also commonly referred to as a GUI. This is a specialized branch of the more general subject of 3D modelling. The MakeHuman Team is focused on this specific branch of the broader subject in order to achieve the best possible level of quality and ease of use in that area.  The ultimate goal is to be able to quickly produce a wide array of realistic virtual humans with only a few clicks of the mouse and be able to render or export them for use in other projects.
 !IMAGE!Pictures/gui_0.png!/IMAGE! 
Humans are created through the manipulation of controls that allow for the blending of different human attributes to create unique 3D human characters. The controls are intended to provide the user with a simple way to create characters that give expression to the widest possible range of human forms.The controllable attributes are broken into two groups: macro and detail. The macro targets deal with overall human characteristics like gender, age, height, weight and ethnicity. The detail targets allow for the character to be further refined by focusing on the low level details ofsuch things as the eye's shape or finger's length.
TheMakeHuman™project strives to provide a complete tool that allows for the management of all things needed to create realistic virtual humans. This includes some tools that have not yet been created or are in the early stages of development for things like poses, animation cycles, managing facial expressions, hair and clothes.With the exception of modelling, most of these tools follow a "point and click" approach by using the MakeHuman™'s Library. Via the MH Library, users preview and load poses, animation cycles, facial expressions, hair, shoes and clothes onto their character. MakeHuman™ also offers tools for exporting virtual humans to other software (such as the Blender 3D modeling suite) where further refinements can be made.


### Short and Long Pipeline
Makehuman was created to provide everyone with specialized software that strives to be the state of the art in a very specific field: the virtual human. The goal is to see it used in two different pipelines or workflows.

=### Short Pipeline

The short pipeline is intended for quick character prototyping and for 2D art. The user defines the character, adds clothes, hair, a pose and expressions, by selecting them from our libraries, and running the render to obtain an image of the character (future goal: indistinguishable from a real photo of him).This output can be used as a character preview, fineart, blueprints, storyboards, comics, illustrations, etc.. No special skill is required from the user.

=### Long Pipeline

The long pipeline is intended to create a 3D character in rest pose for export to external software (Blender, Maya, Max, C4D, etc..) in order to be tweaked, animated and rendered.  Another common usage of the rest-posed character is for games. The long pipeline requires the user to have professional skills and a good working knowledge of the external tools chosen to produce the desired final product.
 


### Professional mesh topology

=### The Homunculus

The principal aim of MakeHuman project is to develop an open source application capable to create realistic tridimensional humans. 
Since the early release in 2001, by pursuing this aim the MakeHuman Team have developed a model that can combine different anatomical parameters to transition smoothly from the infant to the elderly, from man to woman and from fat to slim. The vast wealth of potential combinations provides the artist an extraordinarily broad range of possibilities for artistic expression but presents many problems to the development team.
 !IMAGE!Pictures/age_1.png!/IMAGE! 
In particular it adds to the classical problems of 3D modelling (number of polygons, square or triangular faces, etc.) the problems of constructing a super mesh that can be transformed into any form of human while being sufficiently optimised to be able to be manipulated on desktop machines, yet still producing a professional quality of output. These discussions resulted in agreement that the initial mesh should occupy a middle ground, being neither pronounced masculine, nor pronounced feminine, neither young nor old and having a medium muscular definition. An androgynous form, the HoMunculus.
 !IMAGE!Pictures/hm01_0.png!/IMAGE! 
The Homunculus 00 (2002). No male, no female, nor young or old. A perfect neutral body.

=### Evolution of the topology

The current MakeHuman mesh has evolved through successive iterations of the project, incorporating lessons learned, community feedback and the results of considerable amounts of studies and experimentations.
  
The current version, known as the ‘Homunculus 08’ comprises a state of the art universal humanoid model, including:
* Light and optimized for subdivision surfaces modelling (14766 faces).
* Quads only. The human mesh is completely triangles free.
* Optimized for animation and sculpting (Zbrush, Mudbox)
* MInimal number of poles
* Max number of edges admitted for a pole: 5
 !IMAGE!Pictures/heads_0.png!/IMAGE! 
The Homunculus evolution through the heads
### Homunculus releases
* The first prototype of an universal mesh (head only) was done in 1999 in the makeHead script, and then adapted for the early MH (2000),
* The Homunculus00, was realized by Enrico Valenza in 2002.
* The Homunculus01 (or K-Mesh) was modelled by Kaushik Pal in 2005
* The Homunculus02 was modelled by Manuel Bastioni (Z-Mesh);
* The Homunculus03 was modelled by Gianluca Miragoli (aka Yashugan) in 2007 and builds upon the experience gained on the preceding versions (Y-Mesh)
* The Homunculus04 build upon the previous one by Gianluca Miragoli and Manuel Bastioni
* The Homunculus05 build upon the previous one by Gianluca Miragoli.
* The Homunculus06 released in 2010 (artists: Waldemar Perez Jr., André Richard, Manuel Bastioni).
* The Homunculus07 completely remodelled by Manuel Bastioni in 2011
* The Homunculus08 remodelled from scratch by Manuel Bastioni in 2013
 
 !IMAGE!Pictures/wip03_0.png!/IMAGE! 
An image from the "Making of" the Homunculus 08

=### Alternative topologies

The base mesh is capable to be morphed practically in any human character, but in some cases it is preferred to have a very specialized topology. For this reason, since the version 1.0 alpha 7, MakeHuman includes a function to change the mesh of the character, just selecting it from a simple chooser.
  
The makeHuman team is studying the requirements needed for different purposes (animation, games, crowd, closeups, etc..) in order to create a database of professional topologies. 
 !IMAGE!Pictures/topologies.png!/IMAGE! 
 



## General overview

 
Brief description of the various components which makeup the Makehuman Graphical User Interface (GUI).

### Install MakeHuman™

=### Installable versions of MakeHuman™ are available for Windows, Mac OS X and Linux.

The installable versions of the current!LINK!http://www.makehuman.org/content/download_makehuman_102.html -- stable !/LINK!!LINK!http://www.makehuman.org/content/download_makehuman_102.html -- release!/LINK!of MakeHuman are available for downlaod, as are!LINK!http://www.makehuman.org/content/download_nightlybuild.html -- nightly builds!/LINK! representing the latest deveopmental updates (not guaranteed stable) for the same platforms.

=### System Requirements

You will need about 250 MB of disk space.  In order to use some realtime materials and obtain the best from the internal rendering engine, it's required an average quality graphic card, produced after the year 2006.  In general, your graphics card should support OpenGL Shading Language (GLSL) version 1.2 or above.  There have been reports that the model colors are corrupted on some older Intel Graphics cards (often appearing blue and black).  If you experience this, a possible work-around is to start MakeHuman™ with the "-noshaders" command line switch.  On Windows, this switch can be added to your shortcut.

=### Choice of Installation Directory

The preferred install location location for MakeHuman is a directory simply named "MakeHuman", but in practice you can use another meaningful name. if it is constructed of ASCII characters.  On Windows, C:\Makehuman would make a good choice, and on Linux-alike OS's ~/MakeHuman would make a good choice.  Program data is written to the user's home directory by default, and not to the program install directory. Thus, it is not essential that users have write privledges to the program install directory.  
One caution on Windows systems is that the installation directory should not contain non-ASCII characters as this has been reported to cause problems for some users. This also implies that if your username includes non-ASCII letters that the desktop and Docuemts folders will not be appropriate places for installation because they would result in a path containing non-ASCII cahracters [e.g., C:\users\Åke\MakeHuman or C:\users\Desktop\Åke\MakeHuman are likely to cause problems). 

=### Windows

Download the zip file (or the installer, if available) from the from the download page (!LINK!http://makehuman.org/content/download.html -- http://makehuman.org/content/download.html!/LINK!).
* Installer (not available yet): just run it. The application will be accessible from the Start menu.
* Zip arhive: just to unzip it where you prefer, and double click on makehuman.exe to start the application.

=### Mac OS X

Download and run the installer (or the zip file) from the from the download page (!LINK!http://makehuman.org/content/download.html -- http://makehuman.org/content/download.html!/LINK!). Once downloaded, mount the disk image and drag the MakeHuman app into your Applications folder. MakeHuman™ supports Snow Leopard and newer.

=### Linux

Installers are avaiaible for debian (E.g Ubuntu, Debian etc.) and rpm based distributions (E.g Red-hat, Suse etc.).  Please use the appropriate package for your distribution.
If you do not want to use the prebuilt packages or are having trouble with the packages refer to "Installing from source" below.

=### Installing from source

If you want to install from source or are having trouble with the prepackaged binaries; Makehuman provides compressed source packages. These will work on all supported platforms provided all dependencies are satisfied. To execute MakeHuman simply run makehuman.py located in your unzipped makehuman source directory.
For dependencies and libraries, please read the section "!LINK!http://www.makehuman.org/doc/node/libraries_and_build_procedures.html -- Libraries and build procedures!/LINK!".


### The Interface and basic functions.

=### An Interface Overview:

 
 !IMAGE!Pictures/interface-labelled_new.png!/IMAGE! 
The application user interface comprises of the various elements. The core elements are :
1) the toolbar with its various partitions.
2) The tabs and sub-tabs which allow you to navigate the application, and utilise its various features in a coherent easy to understand manner.
3) The 3D view window which allows you to view the human as it is morphed, posed etc.
4) The left and right option panels whose options change depending upon the tab/sub-tab you are in.
5) Finally there is a progress Bar which shows the progress of an operation and the Information Bar providing useful information.
Note:Different views may contain different options. These options are described in more detail in the appropriate heads in the rest of the documentation. 
### The Toolbar
 
The "Main Toolbar" is actually made up of six separate partitions.
 !IMAGE!Pictures/the_toolbar.jpeg!/IMAGE! 
They are:
1) Files partition 2) The Edit partition 3) The View partition 4) The Symmetry partition 5) The Camera partition
### Files partition
 
 !IMAGE!Pictures/the_toolbar-file.jpeg!/IMAGE! 
This partition provides shortcut buttons that deal with saving or loading files (Save, Load, Export).
The save button performs the same action as pressing the Files tab and then the Save tab when there is no filename specified. If the file was given a name earlier and saved once this button performs a quick save over the file specified earlier.
The Load button takes you to the file loading window where you can choose the file to load.
The Export button takes you to the export tab and allows you to export your current MakeHuman project to one of the variety of export formats the MakeHuman program supports. Supported formats include mesh formats such as Filmbox (fbx),Wavefront obj, Sterolithography (stl), rig/rigging related formats such as Biovision Hierarchy and various maps such as Light Maps, and UV maps.
Load, Save and Export options are explained in more detail!LINK!http://www.makehuman.org/doc/node/load_save_and_export.html -- here!/LINK!.
### The Edit partition
 
 !IMAGE!Pictures/the_toolbar-undoredo.jpeg!/IMAGE! 
The Edit partitionof the toolbar, provides shortcut buttons that deal with editing actions.
  
The Undo button is to undo the last action that has been performed. Undo can be pressed to cancel actions until you have undone all of the actions taken during your current MakeHuman session.
The Redo button is related to the Undo button and will restore the last action that has been undone. Redo can be pressed until all undone actions performed during the current MakeHuman session have been restored.
The reset button will cancel all actions within the current MakeHuman session and restore the default settings for all MakeHuman controls. This effectively returns your MakeHuman session to the state shown when the program first opens.
### The View partition
 
 !IMAGE!Pictures/the_toolbar-smoothandwire.jpeg!/IMAGE! 
The View partitiontoolbar, provides buttons that manage the display mode of the character (Smooth, Wireframe, Background on/off).
Wireframe mode allows you to view the mesh in Wireframe mode like in many other 3D applications.
The Background option allows you to load a background reference image.
The pose button is used for posing. When a rig and pose is active this button is enabled and allows you to toggle between the selected pose and the default rest pose.
The "smooth" is particularly interesting since it subdivides the mesh. The image below shows the mesh smooth and normal, using the wireframe mode. This usesCatmull–Clarksubdivision to create a much more dense smoother mesh.
 !IMAGE!Pictures/nsmooth.png!/IMAGE! 
### The Symmetry partition
 
 !IMAGE!Pictures/the_toolbar-symmetry.jpeg!/IMAGE! 
The Symmetry partitiontoolbar, provides buttons that manage transferring settings applied to one side of the character to the other side of the character so that the character features become symmetrical.
 !IMAGE!Pictures/symm.png!/IMAGE! 
There are options for right to left symmetry, left to right symmetry and a general symmetry mode. Left to right symmetry applies all changes made on the left side to the right side of the human/character. Right to left  symmetry applies all changes made on the right side to the left side of the human/character. 
General symmetry mode behaves differently. When it is active all changes made are symmetrical when it is inactive any changes made to any one side affect that one side only. So this mode therefore allows the user to selectively apply symmetry.
In the above image the Left side of the character is made symmetrical with the right side of the character.
### The camera partition
 
 !IMAGE!Pictures/the_toolbar-cameraviews.jpeg!/IMAGE! 
The Camera partitionof the toolbar, manages the Camera placement within the scene so that the character can be viewed from different angles and zoom levels. (Front View, Back View, Left View, Right View, Top View, Bottom View, Global Camera, Face Camera and Reset Camera options are available).
### The help partition
 
 !IMAGE!Pictures/the_toolbar-screengrbhelp.jpeg!/IMAGE! 
The Help partition, allows you to save a quick screenshot of the view or to access to the help tab.
By default the toolbars are arranged in the order shown above horizontally next to each other along the top edge of the MakeHuman window. The four partition toolbars can each be moved to any area of your screen in Windows by clicking and holding the left mouse button on the left edge of the toolbar and dragging it to the location you desire.

=### The tabs

Most of the user controls of the MakeHuman™ application are accessed through the tabs panel. The tabs are organized intoMainTabsandSubTabs.TheMain Tabsoutline the broad category to which functionality belongs and theSub Tabsallow for more fine grained control over various aspects of the main category.ThereforeSub Tabskeep changing based on whichMain Tabhas been selected.
E.g. When you select the "Files" main tab all file associated functions are made accessible via subtabs such as saving, loading and exporting. In the below image Sub Tabs for the "Modelling" main tab are shown.
 !IMAGE!Pictures/maintab.png!/IMAGE! 
The Primary Tab groups are shown in the image above and from left to right are:
* Files:The Files Tab options provide access to the controls that manage saving, loading and exporting the MakeHuman™ project to or from files.
* Modelling:The Modelling Tab options provide access to the controls that shape and alter the appearance of the MakeHuman™ project model.
* Geometries:. The Geometries Tab options provide access to controls that add new geometries or change the human geometry within the MakeHuman™ project. E.g. Clothes, Eyes, Hair, Teeth, Genitals.
* Materials:The materials available for the human and the additional geometries.
* Pose/Animate:Options for posing animating and rigging a character.
* Rendering:Rendering options using the MakeHuman internal renderer. Currently external rendering is not supported from within the program.
* Settings:Provide options to configure settings of MakeHuman
* Utilities:Provide some additional more advanced utilities. E.g. Material Editor
* Help: The Help Tab's Help option provides access to controls that access the Help and support resources available for the MakeHuman™ project.

=### The sliders

MakeHuman is based on parametric modelling, controlled by sliders.
 !IMAGE!Pictures/wMgROK6FRzzyQAAAABJRU5ErkJggg# !/IMAGE! 
The meaning of each slider is generally self explanatory. Each slider controls the amount of a feature is expressed in the character from its minimum value to is maximum value.
For example, the slider "Age" will change the character from the minimum age, which is about 2 years old, to the maximum age of about 80. When multiple sliders are moved, the values are mixed to form a character that reflects the user's chosen settings using a special interpolation engine.
Each slider can be reset individually with right click on it.
A slider normally moves in increments of 3 or 4 setting values when dragged with the mouse; however, you can place the mouse cursor over the orange portion of the slider and use the mouse scroll wheel to make adjustments in smaller increments of 1.


### The Interace and File Formats
To be added soon.


### Load Save and Export

=### File Access Overview

The leftmost section of the Toolbar includes 3 quick action icons: 1)  for loading models from native .mhm files; 2) for saving the model as a native .mhm file; and 3) for exporting the model in various formats used by other 3D programs (e.g., dae, .fbx, .stl, .obj).
 !IMAGE!Pictures/lse_quick.png!/IMAGE! 
For more complete file access support (Load, Save, Export), the Files Tab options provides access to the controls that manage saving, loading, and exporting the MakeHuman™ project to or from files.
 !IMAGE!Pictures/lse_tabs.png!/IMAGE! 

=### Loading Files

Files are loaded using either the Quick Load icon or by directly choosing the File tab and the Load subtab.  
 !IMAGE!Pictures/load1.png!/IMAGE! 
By default, models that have beem saved in MHM format are retrieved from the user directory%HOMEPATH%/makehuman/v1/models/.   In the event that you have stored your MHM files in a different directory/folder, you can navigate to that directory/folder using the ellipsis at the top of the center panel.  The right hand panel will be populated with thumbnail images of all the MHM files found in the path specified in the path at the top of the center panel.  Simply click on the icon for the model you wish to load in the right panel. The model will load and refresh to its completed state in the center panel.  You can load different models sequentially, if you wish. They will simply replace the previous model in the center panel.   MakeHuman™ is designed so that all loaded models are loaded without changing the camera location.  Thus, you can zoom in on a particular area of the body and compare multiple saved models from a single camera perspective.

=### Saving Files (.mhm format)

Files are saved using either the Quick Save icon or by directly choosing the File tab and the Save sub tab.
The native file format for saving MakeHuman™ files is the .mhm format.  It is important to understand that this format does not save a pixel by pixel representation of your model nor does it save program objects like the actual clothes or hair.  Rather, it saves the necessary information for the program to reconstruct your model from its internally defined assets.  This means that if you move a .mhm file to another computer that lacks a piece of custom clothing, custom hair, or other custom object, the MakeHuman™ program on the new computer will be unable to provide a complete representation of your model unless you also move the custom asset(s) to the second computer.
By default, model files (in.mhm format) are saved to the user directory %HOMEPATH%/Documents/makehuman/v1/models/.   If you wish to save your files in a different location, you can use the ellipsis at the top of the center panel to navigate to the directory/folder of interest.  In addtion to the .mhm file, the save operation will generate a thumbnail image of the model as it appears in the viewport at save time.  Thus, you will want to move the camera to a meaningful and unique view of the model before saving so that the thumbnail image will be easy to identify visually.
CAUTIONARY NOTE:On windows OS (and perhaps on other OS's) there is a small gliche with saving to non-standard directories in MH 1.0.1 and  MH 1.0.2.  If you hit the ellipsis with a blank file name, use the system dialog to navigate to your directory of choice, enter a file name without extension in the system dialog, hit save, and watch the dialog close, the file will have been saved using the directory name rather than the filename you provided in the save box of the system dialog.  This directory name will now appear to the right of the ellipsis in the center panel.  It seems that you can avoid this problem by providing a full file name to the right of the ellipsis before you begin the save procedure, then using the system dialog to navigate to the desired directory, and supplying the same file name a second time in the filename blank of the save dialog.  This irratic behavior has been reported, and when fixed, this cautionary note should  be removed.  (Refer to bug 506 - RWB)

=### Exporting Files

 
 !IMAGE!Pictures/export_labelled.png!/IMAGE! 
The above illustration explains the typical user interface components of the Export tab. On the right you get to choose what to export be in the mesh, the rig or the maps. In the center you have the 3D preview to preview your model. On the right you have options which keep changing based on what format you have selected in the left panel. On the top below the tabs panel is the “Ellipsis” button which opens a file dialog, a text box to enter the file name of the file and an “Export” button to do the actual export and save the file in the desired format.
Below we outline the three main options in more detail i.e. Mesh formats, rig formats and Maps.
### Mesh Formats (.dae, .fbx, obj, Ogre3D, .MD5, .stl)
Files are Exported using either the Quick Export icon or by directly choosing the File tab and the Export subtab.
The Export window allows you to export your current MakeHuman project to one of a variety of export formats. Supported formats including Collada (DAE) Filmbox (fbx),Wavefront (obj), Id Software (MD5), and Sterolithography (stl).
By default, exported files (regardless of export format) are saved to the user directory%HOMEPATH%/makehuman/v1/exports/(to know yourHOMEPATHon your platform refer to this!LINK!http://www.makehuman.org/doc/faq/where_are_my_makehuman_files_found_ie_where_is_my_home_directory.html -- faq!/LINK!).
As is true for the load and save tabs, the ellipsis can be used to export to a non-standard directory/folder. After selecting a format and export options, type the name of your project in the input box at the center of the Export window and then click theExportbutton at the right hand side of the input box.
MakeHuman, itself, can not read any of the exported formats, so exporting is a one way transfer of information.  If you expect to do further refinement of your model, make sure you also save it in .mhm format.
The various export formats differ in the richness of the assets exported:
* Collada Dae (.dae):COLLADA™ is owned by the not-for-profit, open standards!LINK!http://www.khronos.org/ -- Khronos group!/LINK!. It defines an!LINK!https://www.khronos.org/collada/ -- XML-based schema!/LINK!standard for exporting 3D assets. MakeHuman™ is meant to adhere to version 1.4 of the standard. The resulting ASCII format files can become quite large which occassionally limits the use of this format with other programs. By default, MakeHuman™ exports DAE files with y-up, face-z and the decimeter scale chosen. When importing MakeHuman dae files into Blender, be sure to check "import units" at the bottom of the Blender left tool panel if you have not changed the units to meters.
* Wavefront Obj (.obj):OBJ is a very simple format to export the mesh, with vertices, faces and UV coordinates. Originally invented by Alias/Wavefront, all major 3D packages have OBJ importers, so this format allows you to export to the greatest range of applications. However, the character is not rigged but rather a static prop. Wavefront OBJ is a good choice when you need a simple mesh for an external renderer. It comes with an mtl file defining the material.
* Fbx:The default dialect currently used by the MakeHuman™ FBX exporter is FBX 2013 ASCII. Other FBX dialects exist, and if you need one of those dialects, you can use the AutoDesk™ FBX converter (!LINK!http://www.autodesk.com/products/fbx/overview -- http://www.autodesk.com/products/fbx/overview!/LINK!). For example, the Blender importer requires binary FBX files that can be generated in this fashion.
TheOptionsbox contains several export options for each of the formats.The export options available for each format can be selected or deselected by ticking (displayed in orange) and un-ticking off the box in front of them. You can either use the default options for a format or select and deselect options according to your goals and needs. Once an option is changed, it will remain in the changed state until you restart MakeHuman or change it again. They are unaffected by the reset button on the Toolbar.
A common option that is present for all formats isFeet on ground: the origin of the MakeHuman™ mesh is located in the hip area, but if this option is enabled, exported origin is moved to between the feet instead.
Another common option present in almost all formats is the Scale unit: decimeter, meter, inch, centimeter. The internal MakeHuman™ unit is decimeters (the base mesh is 16.8 dm tall), but this is a rather unique choice not shared by other applications. Setting the unit is not essential if the file is exported to a 3D suit like Maya, 3DSMax or Blender, because the character can be rescaled after import. However, Collada files can also be read by other types of applications, where choosing the right scale may be important. In particular, select meters for export to SecondLife.
### Rig formats (.bvh)
MakeHuman currently only supports one rig format.
* Biovision (.bvh):If BVH is selected, it is anticipated that built in animations will be saved to the export directory. As of the MakeHuman™ 1.0.2, there is no offical support for model animation from within MakeHuman™. Thus, selecting this export type is of limited value. If you are interested in using BVH files created by other programs with the MakeHuman model, you may wish to read the documentation on the!LINK!http://www.makehuman.org/sectionview/975 -- MHBlenderTools MakeWalk!/LINK! Addon. A good place to start is the!LINK!http://www.makehuman.org/doc/node/blendertools_makewalk_basic_workflow.html -- MakeWalk Basic Workflow!/LINK!chapter.
### Maps ( ligtmaps and UV maps)
* Lightmap:IfLightmapis checked, a grayscale image of the unwrapped A8 model is saved in the export directory as a 2048 x 2048 .png image.
* UV Map:IfUV mapis checked, a black and white UV unwrapped image of the model mesh on a black background is saved in the export directory as a 2048 x 2048 .png image.
 
 


### Zoom, pan and rotate using the orbital camera

=### Orbital camera

Starting with MH 1.0 there is a new orbital camera system that replaces the old still camera. This new camera addresses the issues where the old still camera made it hard to focus on body parts, for example hands. In the new system the human never moves. Rather, the camera travels on an imaginary sphere surrrounding the human.  The user "mouse picks" a focal point on the human by right clicking, and zooms in and out by dragging. This allows the user to easily rotate around this point to inspect it from all sides.

=### Right-click zoom picking

The default zoom button has been changed to the right mouse button and the use of the mouse wheel is depricated.
 !IMAGE!Pictures/mh_interface_cam.png!/IMAGE! 
Right clicking now serves two purposes, it picks the center of focus based on the location of the cursor when it is positioned over the human, and it lets you zoom in or out by dragging the mouse. Right clicking on the background and not on the human simply makes it zoom in or out straight ahead.

=### Auto-zoom

Another advantage of the orbital camera is that it will adapt the viewing distance based on the height of the human.
 !IMAGE!Pictures/mh_grid_interface2.png!/IMAGE! 
The camera will attempt to keep the current focus point in the center of the screen and maintain the same amount of visibility, independent of whether you are modeling a 1 year old child or a 2.5 m tall giant.

=### Panning

The panning function of the camera has been moved to the middle mouse button (which we suspect is not available to all users) to indicate its reduced importance. Panning will be limited based on camera zoom and will even be completely locked when the camera is zoomed back so that the entire human is visible. The reasoning for this is that panning in the context of MakeHuman is only useful to focus on a feature of the human mesh, not for moving the human around in the scene. In fact we discourage excessive use of the panning feature, and encourage you to use the right click zoom picking instead. Panning is only recommended for small corrections to the framing, as it is quite tricky to position the camera center yourself (you will notice this if you try rotating the camera after having panned over a larger distance, it might not rotate around the center you expected).

=### Grid

The grid helps with getting a better idea of the proportions of the human, and it provides a point of reference in the world when the camera is moved around.
 !IMAGE!Pictures/mh_grid_interface.png!/IMAGE! 
There are two detail levels which are activated when the camera is zoomed close enough. The grid adapts to the 'units' setting, which allows for metric and imperial units. The metric grid has subgrids each 2 cm and a main grid at 10 cm (1 dm) intervals, while the imperial grid has subgrids per inch, and a main grid with 1 foot as size.



## Define Human Characteristics

This section illustrates the modeling of the human using theparametric approach.
  
 

### Gender, Random, Measure and Custom
The gender plugin comprises sliders used to alter gender specific attributes of your human models.
Currently there are 2 categories under this:
* * Breast - this category, as the name suggests, comprises of sliders used to alter attributes related to the human female breasts such as firmness, size, pointiness etc.
* * Genitals - This category comprises of sliders used to alter attributes pertaining to male/female genitalia. Currently only male genitals are supported. (Note: male genitals have to be enabled under Geometries->Genitals for this to have any effect).

Note:For the upcoming MakeHuman 1.1 these sliders have been disabled and the Geometries->Genitals  subpanel no longer exists this is because we no longer have male genitals as a seperate mesh. Seperate male and female!LINK!http://www.makehuman.org/doc/node/makehuman_alternative_topologies.html -- alternate topologies/proxies!/LINK!exists with/without genitalia which are to be used instead.

=### Random modifier

 !IMAGE!Pictures/random2_2_0.png!/IMAGE! 
The random modifier is used to auto generate human beings with randomised parameters.
The interface comprises of 3 checkboxes, 2 sliders and 2 buttons.
* Macro checkbox -This checkbox is used to toggle whether "Macro" attributes such as age, tone/muscle, gender are randomised or not.
* Height checkbox -This checkbox is used to toggle whetherthe height attribute is randomised or not.
* Face checkbox -If this is enabled the facial features of the model are randomised.
* Symmetry slider -THis is used to introduce Assymmetry in the model.
* Amount -THis slider is used to control the amount of randomisation of the character done by the random plugin.
* Replace current -usede to replace current model with a new random model.
* Adjust current -this is used to alter the parameters of the current model.

=### Measure Panel

 !IMAGE!Pictures/measure_1.png!/IMAGE! 
The "Measure" tab facilitates the end user in more precise modelling of the human form. With the measure panel you are able to use the sliders as well as specify the units as sliders for more accurate adjustment of proportions. Various proportions can be edited here such as the proportions of the neck, waist , arms, legs and so on. One example of where this would be useful is in modelling characters like Michael Phelps who has an arm span longer than his height making him a better swimmer.

=### Custom modifier

 !IMAGE!Pictures/customtab_0.png!/IMAGE! 
The custom panel is primarily used for "custom morphs". Cusom morphs can be created by you using blender tools and then used inside makehuman. This tab will remain empty unless you make your own targets using blender scripts and import them for use inside blender. This would be used for instance if you wanted to make an "Elven ears" morph inside makeuman for a humanoid character. This tab is more relevant for advanced makehuman users.


### Using MakeHuman Hairstyles and Clothes

=### Hairstyles

The default MakeHuman™ humanoid model has no hair. However, you may want your model to have hair and a particular hairstyle. In MakeHuman™, you can choose from the available character hairstyles by first selecting the tabsGeometries > Hair.
 !IMAGE!Pictures/hair_1_0_0.png!/IMAGE! 
This opens the Hair library window.  The Hair library window, as usual, is arranged in three sections.  There is a left hand panel (currently empty, but that will include a tag filter), a center preview window showing your current character model, and a right hand panel containing a list of available hairstyles shown as a thumbnail with a label.  For the moment, the default hairstyles within MakeHuman™ are only few types. The library will be expanded release by release.
To be able to see your character with an available hairstyle, you must click on the thumbnail image with your mouse. 
### Changing or Removing Hairstyles and Hair
You can change an assigned hairstyle with another one by clicking on another thumbnail. For example, you can change the hairstyle "afro" of your model by clicking on the hairstyle "fhair" from the panel of thumbnails. Note that doing this will not combine the two hairstyles.
If you are unhappy with how the chosen hairstyle looks on your model and want to return to the previous state of your model, you can press the Undo button at the top left of the screen. In case you want to return to the original state of the model prior to applying any hairstyles, just find the thumbnail named "None" from the gallery of hairstyles and click on it. Your model will now revert to the state that it had before applying any hairstyles to it.
 

=### Clothes

 
The default MakeHuman™ model is barefoot and has no clothing on. However, if you would like to dress your model in MakeHuman™ it is possible by simply clicking and loading clothing and shoes from the library of clothing geometry objects that are fitted to the model automatically.
To dress your model press the tabsGeometries > Clothes.
 !IMAGE!Pictures/clothes_1_0.png!/IMAGE! 
 
The clothes interface is very similar to the hair one, with some differences:
* Clicking on more items in the right panel will combine them. To remove an item you have to re-click it.
* There is a tag filter in the left panel, useful to navigate through a big library.
* An option called "Hide Faces Under Clothes" is provided to prevent portions of the body from intersecting the clothing and creating holes during animating.
 
 
 


### Parametric Modelling
 !IMAGE!Pictures/main_labelled.png!/IMAGE! 
The Main controls are accessed by going to the 'Modelling' tab and selecting the “Main” sub-tab.
  
These controls define the major characteristics of a human being. controls are used to define the character's macro features. The first six corresponding to Gender, Age, Muscle, Weight, Height,  Proportions respectively and the last three ( African, Asian, and Caucasian) correspond to ethnicity.
 !IMAGE!Pictures/age_0.png!/IMAGE! 
 
* Gender:The gender tab is used to define what gender the human being poseeses. Male or female or a mixture of both characteristics with either being dorminant.
* Age:The age slider is used to alter the age of the human being as a whole. The above image shows human beings at various ages ranging from young to old.
* Muscle:The muscle sider is used adjust the amount of muscle possesed by the human character.
* Weight:The Weight silder is used to adjust the weight of the character. The default setting is the character with average weight. Used along with "Muscle" it can be used to specify the proportion of muscle and fat contributing to the weight.
* Height:The Height slider is used to adjust the height of the characters.
* Proportions:The proportions slider is used to adjust the the proportions, from "uncommon" to "idealistic".
Ethnicity sliders:THe ethinicity sliders (African, Asian, Caucasian) are used to alter the ethnic traits of the human being. These slidersare dependent on each other such that the sum of all three sliders is always 100 percent or a value on 1. This means that an increase in the value of "African" slider will lead to a decrease in the value of the "Caucasian" and "Asian" sliders. This is rational because if for instance a human being is of pure African origin then he/she is expected to possess only African traits whereas if he/she is of mixed decent the character is expected to have a fusion of ethnic characteristics. A human being cannot be hundred percent African and hundred percent Asian.

=### Face modifiers:

 !IMAGE!Pictures/face_modifier_labelled.png!/IMAGE! 
The makehuman face modifiers in makehuman are organised into several categories(eyes, nose , chine etc.) comprising of the morphs pertaining to varios facial features.  The morphs available on the right hand side pertain to the category currently active.
E.g. When the Head category is selected all morphs pertaining to the head such as head shape (oval ,round , triangular etc), angle and age are available. If the category was to be switched to Mouth size however all sliders related to that category would be visible and manipulatable.

=### Adjusting the Torso Shape:

 !IMAGE!Pictures/torso_cropped_labelled.png!/IMAGE! 
In order to alter the torso-related features of the human we have to select the "Torso" sub-tab located under the main "Modeling" tab. In the torso section we are able toalter various attibutes such as stomach (size, pregnancy shape), body height, width and so on.

=### Arms and Legs Shape:

 !IMAGE!Pictures/legs_modelling_2_0.png!/IMAGE! 
The "Arms and Legs" sub-tab is again located under the main "Modeling" tab. Here we can alter the various attributes related to the arms and legs such as hands, arms and feet.
 
 


### Makehuman alternative topologies
Makehuman provides a group of alternative topologies which replace the base mesh and are designed for special purposes. These are useful for various applications such as simulation (E.g. a car crash computer simulator), games and so on.
 !IMAGE!Pictures/topologies_0.png!/IMAGE! 
In order to use the alternative topologies provided by MakeHuman; go to Geometries -> Topologies.
For alternative topologies we follow a specific naming convention having the structureNameVertex-countE.g. proxy741 is a alternative topology named proxy with 741 vertices, female1605 is an alternative topology designed for females with 1605 vertices in the mesh.
For illustration purposes we show the wireframe/mesh view of female1605  with 1605 vertices in the figure below.
 !IMAGE!Pictures/Proxies1.png!/IMAGE! 


### Skin and other materials

=### Changing Skin Texture

By default the human has a texturless skin.  
Assigning a new skin material is very easy.  Go in Materials Tab.  You will now see a radio button option for "Skin" under the Human category choices section on the left side of the window. The right side will display available skin materials that can be applied to replace the default skin.  By clicking on one of them  your character will be displayed with the chosen material.
 !IMAGE!Pictures/materials_0.png!/IMAGE! 

=### Changing Hair Textures

Same process as the skin, but selecting the "hair" radio button instead. The materials available depend by the type of hair loaded.
 !IMAGE!Pictures/hair2_0_0.png!/IMAGE! 

=### Changing Clothes Textures

Changing clothes texture is exactly as the hair one, selecting the cloth type instead of hair.
 !IMAGE!Pictures/clothes2_0_0.png!/IMAGE! 



## Rendering Your Work

To write

### Quick rendering and advanced rendering

=### Introduction

MakeHuman™ has an internal rendering engine based on OpenGL technology: GLSL 1.2 for openGL 2.1 or superior.
For this reason some features will be available only for machine(s) build after semptember 2006.
  
For the same reasons, the results can vary a bit, depending the video cards.
 !IMAGE!Pictures/render_0.png!/IMAGE! 

=### Quick render and advanced render

MakeHuman™ uses two different rendering approaches, quick and advanced rendering. Both them produce images with transparent background, in order to be eaily mounted in Gimp or Photoshop.
The quick renderingis intended to for a click-and-see render. It uses fixed presets for lights and materials, studied to show the model in an optimal way. There are only ywo available options in that mode:
* Resolution, written in the form widthxheight
* Antialiasing(turn it on for quality rendering):  Aliasing happens when model edges look 'jaggy'. Raise this slider to filter these. It also help hair and thin stuff in general look better. However raising the AA level can have an equivalent performance hit.
The advanced renderinguse a different rendering technique. It gets the lights defined in "scene" and make complex calculations. In future it will supports shadows and more options to increase the realism.
In addition to the two existing options, there is the subsurface scattering one. Enabling it will produce a more realistic and impressive skin, to simulate the skin's behaviour when light passes through it.
When you have finished selecting the desired options, press the 'Render' button and see your model become a piece of 3D art!


### Scene and Viewer

=### Makehuman "Scenes":

MakeHuman™ provides a library of lighting presets, that will be used in the "advanced rendering" mode. This library is the "Scene" library which currently has only one lighting preset named "default".

=### The "Viewer":

The rendering result will be displayed in the "viewer". It's possible to zoom and move the image using the usual mouse buttons, and then save the image as png, using the "Save as" button.
 !IMAGE!Pictures/viewer_0.png!/IMAGE! 
 



## Settings

Setting the preferences in MakeHuman.

### Background
The Background tab allows you to add background/foreground images to use as a modelling reference or to create a scene within MakeHuman™ for the Short Pipeline.
When you open the Background tab you will see a "None" icon and a list of thumbnails of the files within the backgrounds folder in the!LINK!http://www.makehuman.org/doc/faq/where_is_my_home.html -- MakeHuman home folder!/LINK!, if they are present. The "None" icon is used to remove the background from the MakeHuman™ scene.
 !IMAGE!Pictures/background_0_0.png!/IMAGE! 

=### Different backgrounds for different sides

Prior to selecting an image you should first determine the side of the MakeHuman™ scene where you want the image to appear.  You can specify where you would like the background placed relative to your MakeHuman™ character with the Side control choices on the right hand side of the Background tab screen. 
  
The first six (6) options set the background in your scene using the standard Camera view positions. If you choose the last radio button option labeled "Other" you can add the background into the scene with the character and camera position however it was last set, as long as it was not in one of the predfined camera views. 
  
If you are placing an image to act as a reference image for modelling your character, you should select the side that matches your reference facing.
You can insert up to 7 different images into the MakeHuman™ scene by applying a different image to each Side option.  As the camera view changes into each side view or other view angle, the image shown will change as match your image side configuration for each of the camera side views shown in the modelling window.  The background image, in fact, will only appear while the camera remains in the side view specified.  Pressing one of the camera view options is the easiest way to get a background image to reappear if it disappears due to a camera view change.

=### Background opacity and position.

The Background Setting options allow you to set the background image's opacity using the Opacity slider control, which determines how transparent or opaque the image will appear in the scene, and to set the image as a background or foreground. These controls are particularly useful when you are using reference images to model your character.
The standard Opacity setting of 100 is equivalent to a 60% transparency level.  Setting the control to 0 will make the image invisible (100% transparency) and setting the opacity control to 250 will make the image fully opaque (0% tranparency).  
The "Show in Foreground" checkbox option allows you to place the image in front of the character in the scene so that the character will be obscured according to the opacity level setting of the background image.  This option should be checked if the image will be used as a reference image for modelling.
The background can be moved and resized to properly fit the character, checking the options in the left side and then clicking and dragging with leftbutton or rightbutton.


### General

=### General Settings

The general settings include important features that can make a huge difference in MakeHuman's performance.
 !IMAGE!Pictures/general.png!/IMAGE! 
### Slider behaviour
* Update realtime. This option recalculates the human shape in real time during the slider movements. This requires more CPU resources.
* Update normals real time. By enabling this option, the normals are updated during the slider movements in order to see a correct shading in real time. Computing the surface normals requires an intensive CPU calculation, so this can slow down old PCs.
* Fit objects in realtime. By enabling it, all objects (eyes, hair, clothes, teeth, etc..) are fitted in real time during the body transformations. This requires more CPU resources.
* Autozoom camera. Enabling it will automatically zoom in the camera to the zone of interest. For example, editing the head, it will zoom in to it, editing the hand, it will automatically zoom in to the hand, etc.. This can be useful in some cases, but it doesn't allow custom point of view, so this option is disabled by default.
* Slider images. Enable the images to illustrate the sliders' effect. Disable it for a more compact list of controls.
### Units
This setting is to choose the measurement system that will be used :
* Metric, to use meters, centimeters, etc
* Imperial, to use inch, feet,etc..
### Startup
* Preload macro targets. This option is very important for perfomance and startup loading time. Using the preload increases a lot the performance, but in the case when the targets are not compiled (for example the raw targets cloned from HG) it will considerably increase the loading time during startup.
* Restore windows size. This option is just to remember the custom windows size used for MakeHuman.
### Theme and languages.
These options areself explanatory. MakeHuman needs to be restarted for a change in the language settings to be effective.
 


### Mouse

=### Managing mouse configuration:

THe "Mouse" tab allows you to configure the behaviour of the mouse in makehuman.
 !IMAGE!Pictures/mouse_001.png!/IMAGE! 
The first wiidget in the left panel contains one slider labelled "3D viewport Speed".  This slider controls the how sensitive the viewport is to mouse movement. As you increase this parameter the viewport become increasingly sensitive to mouse movements, thereby moving faster.  Tweak this parameter with care.  A value of one is the default speed at which makehuman models rotate and move in response to the mouse. Increase this parameter if you feel that the movements are too slow for your liking.
The second widget inside the left panel is the "Camera" widget this widget allows you to configure the mouse settings used to control the camera.  This also allows you to invert the mouse wheel.
Note:With the orbital camera, panning is available only in certain situations. Therefore, the "Move" shortcut has been made available for configuration. If you cannot pan your model it may not a bug.


### Shortcuts
THe "Shortcuts" tab helps us to manage shortcuts in makehuman.
For your convinience shortcuts have been organised into 3 categories. The first category with the largest number of shrrtcuts available for configuration is the "Camera" category whose panel is located on the left hand side. THe other two categories are "Actions" and "Navigation". The "Action" panel helps us to alter shortcuts for actions such as undo and redo. The "Navigation" panel helps us to set shortcuts to quickly navigate between various frequently used tabs in Makehuman.
 
 !IMAGE!Pictures/shortcuts-mh_002.jpg!/IMAGE! 

=### How to use the Shortcuts Tab

Managing of shortcuts is very easy inside makehuman. Just select the appropriate box with the current shortcut key andf type in thenew shortcut key/key combination. Makehuman will warn you if there are duplicates.


### Plugins
Makehuman is designed using a modular approach. All features within makehuman belong to one module or the other. THese modules are called Plugins. With the help of the "Plugins" tab in makehuman we can enable or disable certain plugins thereby altering the feature set available.
This feature is useful when:
1) A particular feature is uneeded and you want to improve performance of makehuman by disabling it.
2) A particular plugin is giving problems on your machine and you would like to disable it to avoid accidently triggering the fault again.
 !IMAGE!Pictures/plugins-mh_002.png!/IMAGE! 
By default all plugins are enabled plugins can be disabled by clicking on the option buttons and removing the "x" next to the related plugin.



## Reporting a Bug

How to help MakeHuman development reporting a bug.

### Using the Makehuman log files for error reporting
Occassionally, MakeHuman will not behave as expected, or you will note an exception in the status line, You willingness to make a bug report.for such events goes a long way to help imrove MakeHuman.  For simple bugs,, it can often be enough to report the version of your operating system, the version of MakeHuman that you are using, and the steps to reproduce the problem.  However, the developers often need to know more detail to reproduce your problem in a different environment.
As long as MakeHuman has not "crashed" completely, the easiest way to learn the details is to use thebuilt-in log viewer.  This can be accessed by selecting theutilities taband then thelog subtab.  On the left, you will see alevel selectorthat is initially set to "default".  The center panel will show a very verbose set of all the actions that have happened inside MakeHuman since it was last restarted.  This entire set of information is seldom needed.
For bug reporting, you will be most interested in the messages that show when you set the level selector to "error".  If severe problems have occurred, the center window will show the errors logged in red.  If there are none, it may still be worth reporting the somewhat less severe "warning" level messages which resulted in code exceptions.  These messages will show in orange if you set the level selector to "warning".   Only seldom will levels of "notice" or "message" be of interest to developers.  Supply these only upon request.
When you find "errors" or "warnings" you can highlight the message(s) with the mouse and press the "copy" button in the left panel.  The message will be copied to your clipboard.  Simply paste  these messages at the end of your bug report.
In the event that MakeHuman crashes completely, or in the case of complex problems it may be better  or easier to upload more complete log information from the log files. MakeHuman  always creates 2 important files called "makehuman-debug.txt"  and "makehuman.log" in the user's home directory (under "My Documents/makehuman/v1" in Windows or "~/makehuman/v1" in your linux distribution).
makehuman-debug.txt:This provides some essential information about the system on which you have installed makehuman such as version information, machine architecture type, numpy versions and so on which is useful when reporting a bug as the bug may be applicable to your particular machine configuration.
makehuman.log:The makehuman.log file is another separate file. This file logs all events that take place from the beginning when makehuman is loading till the end when makehuman is closed. ALl regular events and error messages are logged in this file. It is important that you attach either this whole file or the last few signinficant lines indicating where the bug occured. This logs contains backtraces and other useful information like what plugins loaded, what plugins did not at which point did a python script fail and so on.
When reporting a bug in the makehuman bugtracker posting the contents of both these files is useful and will help us to debug and resolve the issue(s) more quickly. This is of course not needed when you are posting a feature request which is not a bug.


### Using the Makehuman bug tracker
Makehuman has introduced a new internal bug tracker based on redmine (!LINK!http://www.redmine.org -- www.redmine.org!/LINK!) this tracker allows us to easily handle bug reports and feature requests reported/requested by you. In order to use this new bug tracker a forum account is compulsory (even if you do not wish to use forums). Your forum ID becomes your makehuman bug tracker ID.
Following are some quick links related to makehuman bug tracker:
* Roadmaps:!LINK!http://bugtracker.makehuman.org/projects/makehuman/roadmap -- http://bugtracker.makehuman.org/projects/makehuman/roadmap!/LINK!
* Add a new issue and see the isues list:!LINK!http://bugtracker.makehuman.org/projects/makehuman/issues -- http://bugtracker.makehuman.org/projects/makehuman/issues!/LINK!
* Graph for a quick overview:!LINK!http://bugtracker.makehuman.org/projects/makehuman/issues/growth -- http://bugtracker.makehuman.org/projects/makehuman/issues/growth!/LINK!
* Activity:!LINK!http://bugtracker.makehuman.org/projects/makehuman/activity -- http://bugtracker.makehuman.org/projects/makehuman/activity!/LINK!
 



## Tools and contributing methods

Blendertools and contributing methods

### MakeTarget standalone

=### Making Wavefront .obj Files MakeHuman™ Compliant

The following procedures should be followed to create Wavefront .obj files that comply with the requirements of MakeHuman™ using modelling software programs such as 3dMax, Maya, XSI, etc. 
* * Download the 1.x base mesh  base.obj file from MakeHuman!LINK!https://bitbucket.org/MakeHuman/makehuman/src/c40af22cebf2d5372b931b485f60588f42f24480/makehuman/data/3dobjs/base.obj?at=default -- HG repository!/LINK!
* Import it into your preferred modelling software
* Modify it in order to create your final character
* Export it as .obj (of course with a different name than base.obj)
During editing of the base mesh be careful about 3 things!You have to pay attention that:
* The import/export does not alter the number of vertices, the faces, does not split the obj, etc. The topology has to be the same as the original one.
* When modifying the base, you do not delete or add vertices, do not add or remove faces, etc. The topology has to be the same as the original one.
* The 3D program used also preserves the exact order of the vertices.

=### There are no other limitations on the .obj files used.


=### Making Targets with MakeTarget™ StandAlone


=### Using the MakeTarget GUI program

To obtain the MakeTarget GUI program, download and install either the Windows version or the Linux version at the bottom of the download page of the MakeHuman website at: !LINK!http://makehuman.org/content/download.html -- http://makehuman.org/content/download.html!/LINK!
Looking at the GUI of MakeTarget, you can notice other elements: the (+) and (-) lists, the possibility to process whole directories and to have .obj as output.
These are batch tools, designed for MakeHuman developers. Let’s go on to describe an usual scenario.
  
Assuming you have 30 “chin”  targets modelled on the young caucasian female. These targets will create artifacts when applied on a young asian female. So our artists have to process 30 targets in order to create an asian version from all of them.
  
The steps are:
* For each chin target, do: asian-female-young.target + chin.target and save the result as .obj.
* Import each .obj in a modelling software, fix the artifacts by hand and export the corrected .obj.
* For each corrected .obj, subtract the asian-female-young.target and save the rest as asian version of the chin target.
For step (1) we will process an entire directory, choosing “Directory” as “input source” and targets as input type. Then we will “add” the asian-female-young.target, loading it in the (+) section. Then will choose “Obj” as “Output type”.
 !IMAGE!Pictures/image01.png!/IMAGE! 
Pressing the “Make” button, the entire folder will be processed, and in the same directory of targets we will see the newly created .objs. At this point, we can copy the folder, renaming it as “chin_fixed” and deleting the original targets.
For step (2), we have to import, edit and export each .obj individually, as showed previously for the single target. After completing step (2), all .objs in “chin_fixed” will be fixed and ready to be converted into targets.
So, it’s time for step (3). Again, we will process the entire directory, but this time the input type will be “Obj” and the output “Target”. Also, this time we will subtract the asian target, in order to obtain only the chin morph.
 !IMAGE!Pictures/image00.png!/IMAGE! 
Pressing the “make” button, this time we will obtain a series of .target, with the same name as the original objs, placed in the “chin_fixed” folder. That’s all!

=### Command Line Usage

This tool allows wavefront .obj files to be used that were edited using any 3D program. The only limitations are that the edit stems from the original base.obj file and that no vertices, edges or faces are added or removed. The 3D program used also needs to preserve the exact order of the vertices. There are no other limitations on the obj files used.
Usage:
There are a commandline version and a version with graphic user interface. Both do exactly the same thing.
Here follows the explanation of how to use the commandline version.
Options:
 -i --in     input obj or target
  
-o --out    output obj or target
  
-s --sub    target to subtract from obj
  
-a --add    target to add to obj
  
-d --dir    input folder to load all objs or targets from
  
--intype    type of file to be input, obj (default) or target  only applicable if --dir is used
  
--outtype   type of file that will be output, obj or target (default)
  
-h --help   this info
  
-v --verbose    verbose mode, shows extra information   
Usage scenarios: 
Load foo.obj as input, compare it with base.obj and output the  difference as foo.target.
Load foo.obj, subtract foo1.target from it, and output the difference  between the resulting obj and base.obj as foo.target.
Load foo.obj, add foo1.target to it, and output the difference  between the resulting obj and base.obj as foo.target.
Load all objs from myfolder, save the difference between the base.obj and each of the input objs to a target file with the same name as the input obj.
Load all objs from myfolder, subtract foo1.target from each of them, and save the difference between base.obj and each of the resulting objs to a target file with the same name as the input obj.
Load all objs from myfolder, add foo1.target to each of them, and save the difference between base.obj and each of the resulting objs to a target file with the same name as the input obj.
Load foo.target, apply it to base.obj and output the resulting obj as  foo.obj.
Load all target files from myfolder, apply each of them to base.obj and  save the result of each to obj with the same name as the target file.
Load all target files in myfolder, apply each of them to base.obj while also subtracting foo1.target from the result. Save each combination to   an obj with the same name as the input target.
Load all target files in myfolder, apply each of them to base.obj while also adding foo1.target to the result. Save each combination to an obj with the same name as the input target.
This is the usage information as can be obtained by running the "maketarget.py --help" command. Some additional scenarios that are not documented are possible with the tool.
  
The user is protected from issuing commands that make no sense (eg. do nothing) as the tool will warn you about this.
Also note that files are never overwritten. Upon encountering an already existing file this file is backed up as original_filename.bak. Additional backups of the same file are named in order original_filename.bak.0 original_filename.bak.1 etc.
The GUI version of the tool does exactly the same thing. The exact same options (except help and verbose) are available in the GUI. The only difference between commandline and GUI version is that the GUI demands you specify an --in or --dir parameter. With the commandline tool you can do without as long as you specify some --add or --sub targets.

=### Compiling Binaries

For the ease of distribution a pyinstaller configuration is supplied to create a self-contained binary executable for both windows and linux. (MAC OS might work but is untested). For running this executable, the user does not need to install python or any other libraries (such as wxwidgets) on his computer. For building the package, however, you need to have those dependencies
  
installed, and need to build the package on the target OS. There are two build files available:
* compilePyinstaller.bat,for building a windows executable
* compilePyinstaller.sh        for building a linux executable (might work for OSX   too)

In order to use them you need to create a folder called "pyinstaller" in the makehuman/tools/standalone/maketarget folder. The build configs were tested with pyinstaller 1.5.1, but might work on future or older versions too.
  
Additionally these dependencies are needed for the respective operating systems:
Windows:
* Python 2.7
  !LINK!http://python.org/ -- http://python.org/!/LINK!
  I recommend using python 2.7 as I had issues with 2.6 and pyinstaller. The tool works fine with python 2.6, however
* pywin32
  !LINK!http://sourceforge.net/projects/pywin32/ -- http://sourceforge.net/projects/pywin32/!/LINK!
  Python extensions for windows. Needed for pyinstaller to work.
* wxpython2.8
  !LINK!http://www.wxpython.org/ -- http://www.wxpython.org/!/LINK!
  WX Widgets libraries and python wrappers for windows. Installable as one singe package.I recommend using the wxPython2.8 win32 unicode package for python 2.7.
* UPX (optional)
  !LINK!http://upx.sourceforge.net/ -- http://upx.sourceforge.net/!/LINK!
  This is a tool for compressing the executable and reduce its size. Compression will happen automatically if UPX is installed.  To install UPX copy upx.exe to C:\WINDOWS\system32
  Note: you will need at least UPX 1.92 beta due to incompatibilites  with the Visual Studio compiler, with which newer versions of python are   compiled on windows.   
Linux:
* Python 2.6
  !LINK!http://python.org/ -- http://python.org/!/LINK!
  Version 2.7 works fine too.
* python-wxgtk2.8
* libwxgtk2.8
  !LINK!http://www.wxpython.org/ -- http://www.wxpython.org/!/LINK!
  !LINK!http://www.wxwidgets.org/ -- http://www.wxwidgets.org/!/LINK!
  WX Widgets libraries and python wrappers for wx
* UPX (optional)
  !LINK!http://upx.sourceforge.net/ -- http://upx.sourceforge.net/!/LINK!
  This is a tool for compressing the executable and reduce its size. Compression will happen automatically if UPX is installed
        
  
The pyinstaller script will create all the files that need to be distributed in a folder called dist/ (this will be an .xrc file, the executable, and a resources/ folder containing images used in the GUI).
  
You can archive the contents of the dist/ folder and distribute these freely as a standalone application.       
### wxWidgets specific information
The GUI of this tool has been made using the python version of wxWidgets. The GUI form itself is not created using application code, but is instead loaded from the maketarget.xrc file that declares the GUI. This file was built using wxFormBuilder (!LINK!http://wxformbuilder.org/ -- http://wxformbuilder.org/!/LINK!). The file maketarget_gui.fbp is the source file that can be opened in formbuilder. The xrc file is output generated using the formbuilder application. However, the xrc could be edited manually too (but this would cause fbp and xrc file to go out of sync).
### More information
For more specific details you can contact the author Jonas Hauquier at the makehuman.org website.
 


### MHBlenderTools: MakeTarget

=### What is a Target?  The MakeHuman Morphing Process.

The principle is simple. A target is a modifcation to a base mesh shape that does not alter the mesh itself but that stores information that permits the base mesh to be transformed into the target shape using ‘morphing’.  Targets are what allow the slider controls in MakeHuman™ to take a single base mesh for a character and morph the shape of that character based on a variety of different feature target files.  The many target files used by MakeHuman™ can alter a single human base form into characters with features as different as those distinguishing male from female to as subtle as varying the shape of a single earlobe.
 !IMAGE!Pictures/morph1.png!/IMAGE! 
A target contains the offsets by which vertices of the human base model (base.obj) deviate from the original to achieve a specific feature. eg. a long nose could be a target.  These targets can be combined and MakeHuman™ uses them by blending targets together and gradually applying them to the base mesh to create a nearly endless variety of human forms.  Below are examples of target blending obtained by choosing a target that defined the character as male and combining that target with the extreme settings for other targets that determned the muscle tone or weight of the character.
  
MakeHuman™ handles morphing with a special file format,.target.

=### Loading the Base Mesh

While it is possible to create targets using Blender without using the MakeTarget™ tool for Blender; that tool has many useful features that simplify the target creation process and will be explained by the help that follows.  Once the MakeTarget™ add-on has been enabled (see the previous "Get and Install MH Addons for Blender" section), a panel labelled MakeTarget™ version 1.xx appears in theBlender User Interface, to the right of the viewport. The visibility of the Blender User Interface can be toggled on and off with the N-key.
 !IMAGE!Pictures/maketarget131-area.png!/IMAGE! 
The MakeTarge™ Version 1.31 Panel (Initial Settings)
 !IMAGE!Pictures/maketarget131.png!/IMAGE! 
Prior to loading any targets, the initial the MakeTarget™ panel consists of three main buttons. The first two buttons load the base human mesh, respectively with and without the special fitting tools. The third button labeled "Set As Base" sets an existing mesh (that must be MakeHuman™compliant and derived from the A8_v74.obj file distributed with the MakeTarget™  release within the maketarget/data/ folder) as a human base mesh.  This third option is for users that have done editing of the base mesh in another 3D modelling program and that have saved or exported the model as a Wavefront .obj file
 !IMAGE!Pictures/helper_details.png!/IMAGE! 
Loading the "Human + Fit Tools" will import the base human +mesh helpers(image below, B). The "helpers" are special geometries, used in MakeHuman™ as a reference to correctly fit clothes, hair and accessories.  These helpers can be annoying during the modelling of the character, so usually our artists first work on the pure body, loading the human only with the first button (image below, A), and then, in a successive step, they fit the helpers.
 !IMAGE!Pictures/maketarget-base.png!/IMAGE! 

=### Basic usage

### The MakeTarget™ Version 1.09 Panel (After Loading The Target Mesh)
 !IMAGE!Pictures/MakeTarget_load.png!/IMAGE! 
After the mesh is loaded into the scene, the MakeTarget™panel layout will change, showing three new buttons that handle setting up the morphing targets. The first button creates a new empty target which will just be the original base mesh loaded in the previous step.
The second button loads the morphing from an existing target file. Do not attempt to load target files from the previous MakeHuman™versions, as these files are not compatible with the current base.
The third button creates a new target from an existing base mesh that is MakeHuman™compliant (derived from the A8_v74.obj file provided with the MakeTarget™release distribution), for example, a character modelled with an external tool (Maya, Max, C4D, etc..) and then saved or exported so that it can be imported into Blender as a wavefront obj file.  To correctly use the third button, it is necessary to first select the imported base, then the MakeHuman™base, and then press the Load Target From Mesh button.  When the steps have been done correctly and that button is pressed the imported base will disappear and its transformations will be transferred onto the MakeHuman™base.
### Editing The Target And The "Save Target As" Button
After a new empty target is initialized or an existing one is loaded/imported, the MakeTarget™ panel layout will change again, offering a rich set of new options (image below). For the basic use of the MakeTarget™ tool you may ignore all of these options except for the "Save Target As" button.
To create a custom target, the artist has to alter the base mesh, which is done in the usual way within Blender.  First start edit mode, and then select one or more vertices, moving them to reshape the mesh.  You may use the full power of Blender to create your morphing target design.The only rule, in order to create a valid morphing target, is to never add or delete a vertex, face or edge. The topology must be absolutely preserved.After the modelling process is completed, the MakeHuman™morphing target can be saved by pressing the "Save Target As" button on the MakeTarget™panel.  By default this will save all of the offset deviations of every vertice from the base mesh into the target file.

=### Advanced usage

### The MakeTarget™Version 1.09 Panel (After Loading A Target)
During the creation or the editing of a target, as mentioned previously, the MakeTarget™panel shows a new layout with a rich set of options. Depending on whether the mesh is loaded without the fit tools (image below, left) or with the fit tools (image below, right), the panel offers different options.
 !IMAGE!Pictures/maketarget131-panels.png!/IMAGE! 
At the top of the panel there is a numeric slider that determines the amount of morphing to apply from the target. The maximum value is 1.0, which means that the target morphing is fully applied. A value of 0 will show the original base mesh without any target morphing.  The minimum value of the slider is -1.0.  Using negative values usually creates weird effects as a projected inverse of the target morph is applied, but these settings are useful to subtract unwanted morphing results when multiple targets are combined. The effect is shown in the image below beginning on the left with the full inverse of the morphing target, to the original base mesh in the middle, and finally to the fully applied morph target design on the right.
 !IMAGE!Pictures/maketarget3.png!/IMAGE! 
### Load Target Section (After The First Target Is Loaded)
 !IMAGE!Pictures/MakeTargetLoadSecondaryTarget.png!/IMAGE! 
The three buttons that now in the "Load Target" section are used in exactly the same way as they were before any target was loaded, except that any targets that are now created or loaded with these buttons become a secondary target that can be applied to the previously loaded one.  These buttons are used to append one or more additional targets to the first target and combine them in various proportions.
### Discard And Apply Target Section
 !IMAGE!Pictures/MakeTargetDiscardAndApplyTarget.png!/IMAGE! 
 
The first two buttons under the "Discard And Apply Target" section will either discard all of the targets (returning you to the original base mesh) or only the last target appended (which will either be the last secondary target applied or the primary target if no secondary targets have been applied).  The button "Apply targets" under the "Discard And Apply Target" section is used to join all targets into a single unique morphing target combination.
### Symmetry Section
 !IMAGE!Pictures/MakeTargetTargetSymmetryButtons.png!/IMAGE! 
The two buttons in the "Symmetry" section are modelling tools, and are very useful.  They has been designed to produce very reliable target results. Using the symmetry buttons will cause the mesh to become symetrical on either side of the X axis, with the option to apply edits from the left side of the character to the right side (Left->Right), or vice versa (Right->Left).  Pressing these buttons will also align center vertices that have been unintentionally moved away from the center back to their center position.
### Save Target Section
 !IMAGE!Pictures/MakeTargetSaveTargetSection.png!/IMAGE! 
Finally, press the "Save Target As" button to save the .target file once all secondary targets and edits have been completed.
The checkbox labeled "Selected verts only" is a very important option.  This option when checked will permit you to select a set of vertices in edit mode and then save only those vertices into the target file. Such targets are useful when you want the target to only morph the selected vertices and leave all other vertices completely unaffected by the morphing target.  For example, an artist could design a morphing target that is limited to the hands only, a single hand only, or to the head only, and save a target containing vertices that will only morph those body parts, while having no effect on other parts of the body that were not explicitly chosen by the artist.
The checkbox labeled "Active Target Only" will cause the "Save Target As" button to only save the last target only.  This option normally applies when one or more secondary targets have been added using the Load Target section after adding the initial target.
### Additional Fit Helper Buttons
 !IMAGE!Pictures/MakeTargetFitTargetButton.png!/IMAGE! 
 !IMAGE!Pictures/MakeTargetSkirtEditingAffectOnly3.png!/IMAGE! 
When the fit helpers have been included as part of the target, the additional options of the MakeTarget™panel shown in the images above appear.  These buttons are included to work with the helper objects.  When the helpers have been loaded, an additional button labeled "Fit Targets" is available under the Load Target section.  This button should be pressed after making alterations to the body that disconnect it from the helper objects, but prior to making modifications to those objects.  This button will refit the clothing to the body, and if pressed when the default All option under the "Affect Only: section is selected, all clothing helpers will be refitted to the body.  However, the refitting process will cause any modifications previously made to a refitted helper objects to be lost.  To limit the Fit Target button behavior to a single helper object, you should specify the object that you want to have refitted under the Affects Only section appearing at the bottom of the panel.  This will cause the refitting to only affect the chosen helper (for example the Hair), while leaving all other helper objects unaffected, preserving your edit modifications to those helpers (for example, the Tights and Skirt helpers will not be refitted and your modifications to those helpers will be preserved if the Hair Affects Only option is set).
The additional helper options also include buttons that improve the fit of the skirt specifically by snapping the skirt to the character's waist ("Snap Skirt Waist" button) or straightening the skirt ("Straighten Skirt" button).  It is recommended that you still select the Skirt as the Affects Only option prior to pressing either of these buttons.


### MHBlenderTools: MakeClothes
### Overview
MakeClothes, as its name implies, is a Blender addon that is used to construct clothing assets for use in the MakeHuman program. Clothes can be modeled using any technique that is natural. For example, clothing can be modeled from scratch, or by altering either the human mesh or the “clothing helpers” (see below) provided by the MakeClothes tool. When designing and modeling a clothing item, there are two restrictions that should be kept in mind. First, the algorithm for mapping a clothing mesh to the human mesh requires that theclothing mesh consists entirely of quad faces. Second, it is important to know that MakeClothes supports only one material per item of clothing. 
Upon completing the MakeClothes workflow, a new folder will be created by the tool within %USER%/makehuman/v1/data/clothes. That folder will assume the unique name that the user provides for the clothing item. This folder will be populated with the assets necessary to make the item available in MakeHuman. The one additional, useful but not essential, item that the user must supply is a thumbnail icon for the clothing. The thumbnail icon can be created with any image editing program as a 128 x128 pixel image in .png format. The file should then be saved in the same folder as the other assets and the extension changed to .thumb.
### Using MakeClothes addon
MakeClothes is controlled by the MakeClothes panel in the N-shelf to the right of the viewport. It consists of the main buttons that are always visible, and several hidden sections that can be displayed by enabling a checkbox.
 !IMAGE!Pictures/mc2-010-main.png!/IMAGE! 
The main section contains the following:
* Type: Specifies the character to be used as a reference. It can be one of the following:
* Base Mesh: The MakeHuman mesh without any targets applied.
* Average Male: A caucasian young male.
* Average Female: A caucasian young female.
* Average Child: A caucasian young child.
* Average Baby: A caucasian young baby.
* Base Mesh with Helpers: The MakeHuman mesh without any targets applied.
* Average Male with Helpers: A caucasian young male.
* Average Female with Helpers: A caucasian young female.
* Average Childwith Helpers: A caucasian young child.
* Average Baby with Helpers: A caucasian young baby.

* Load Human mesh: the button to load the selected type into the scene.
Note:"helpers" in MakeHuman are a type of special, invisible geometry over the base mesh which can be loaded to help model clothes, for example, a helper sweater, helper tights etc. They have their own materials. It is important to note that no alterations should be made to the base mesh type after it is loaded otherwise the script will fail.
The picture below shows the result of pressing "Load Human Mesh", with type set to Base Mesh.
 !IMAGE!Pictures/mc2-011-main_0.png!/IMAGE! 
A human mesh is loaded into the viewport, and more tools are enabled:
* Mesh Type: MakeClothes divides meshes into two types: human and clothing. This button displays the mesh type (Human/Clothing) of the active mesh and is greyed out if the active object is not a mesh. (MakeHuman normally detects the items accurately, but in the event of an error, you can click the button to change the mesh type so that it is treated as a clothing item instead of human if it is a clothing item and wrongly detected as a human item)
* Create Vertex Groups From Selection: MakeClothes uses vertex groups to control the fitting.
* Make Clothes. This is the main entry point for the MakeClothes script. With one human and one piece of clothing selected, create an association between clothes vertices and human triangles, i.e. triplets of human vertices. Both meshes must have vertex groups with identical names, and each clothing vertex must belong to exactly one vertex group. The result of the association is saved in the file ObjectName/ObjectName.mhclo, in the default directory. This button is greyed out if the active object is not a mesh.
* Test Clothes. This buttons loads a piece of clothing (an .mhclo file) and fits it to the active mesh, which must be a human. Typically a second human is loaded on a different layer, and the quality of the clothes fitted to that character can immediately be checked in Blender. To test the clothes under the strictest conditions, the human model used for testing should be quite different from the human used for clothes-making. If the original character is an adult, Baby With Helpers is a good choice.
If, instead, the Human With Helpers button is pressed, the full MakeHuman mesh including the helper geometry is loaded. Different materials are assigned to each type of helper geometry. The materials are ordered in the order of the vertex number. This makes it easy to peel off one helper type at a time.
 !IMAGE!Pictures/makeclothes03.png!/IMAGE! 
### Glue clothes to the body
The clothes are meshes that  be done directly in Blender, or in another package and then imported into Blender as an obj file. Note that the mesh type is Clothing, which is the default unless the mesh has been declared to be a human. A simple method to obtain a starting point modelling is to duplicate part of the human mesh and separate it from the human. However, in this case the duplicated mesh will still be a human. To change the mesh type, press the toggle button Human. The status is now changed into Clothing.
After loading the human, next step is to "glue" the clothes to the human, in order that they will automatically fit the body changes. To control this association, MakeClothes uses vertex groups. Each clothing vertex must belong to exactly one vertex group, and a vertex group with thesame namemust exist in the human mesh as well. Only human vertices in the correct vertex group will be considered when making clothes.
Vertex groups speed up the clothes-making process by pruning the search tree, and can be used to control the appearance of clothes as well. However, assigning vertex groups can be quite tedious, and in many cases it is sufficient let MakeClothes create vertex groups automatically. This is done automatically when a human mesh is loaded. If a clothing mesh does not have any vertex groups, it is also done automatically, when the MakeClothes button is pressed.
### Automatic vertex groups
If vertex groups need to be reassigned, e.g. because a piece of clothing has been edited, the automatic vertex groups can be used. When the human is selected, there is a button, visible in the image above, called "Create Vertex Groups From Selection". Selecting a cloth, the button change in "Create Vertex Groups". Both the buttons do the same thing, but there is a little difference: in the human is possible to generate the vertex groups only for a sub set of the vertices (selected in edit mode), while for clothing the vertex groups must include all vertices.  This is because we need to associate onlya partof the human vertices withallvertices of the clothing. For example, we need to associate all the vertices of a skirt with the human torso only.
Pressing the button, the following vertex groups are created:
* Mid: Vertices on or very close to the center line (|x| < 0:001).
* Left: Vertices to the left of the center line (x > 0:001). For a human the Mid vertices are also included in the Left group.
* Right. Vertices to the right of the center line (x z 0:001). For a human the Mid vertices are also included in the Right group.
* Delete: An empty group only created for humans. Human vertices hidden by the piece of clothing can be added to this groups. These vertices are then optionally deleted when the clothing is applied in MakeHuman, thus avoiding that blotches of skin poking through the clothes. Note that when a vertex is deleted, so are all faces containing this vertex. Don't assign a vertex to the Delete group unless all faces containing it are hidden by the pieces of clothing.
In the image below, vertices assigned to the Mid and Left groups for a nude human.
 !IMAGE!Pictures/auto-vert.png!/IMAGE! 
### Generate the clothes file.
When both clothing and human has the vertex groups with same name, just press the MakeClothes button to generate the files.
  
They will be located in your HOME/makehuman/a8/data/clothes, in order to be inbcluded automatically in MakeHuman.

=### Advanced tools

Under the main buttons of Makeclothes, there are seven hidden panels that can be activated clicking the checkbox. Let's see their meaning.
### Show selection, Show Materials, Show UV projection
 !IMAGE!Pictures/options-01.png!/IMAGE! 
Show selection.This feature is just a shortcut to quickly select some part of the human. So, instead of classic Blender selection (go in edit mode, move the mous on a vert and press Lkey to select the linked vertices), you can just press these buttons.
Show Materials. This will show a button to export the materials only. It's useful in case there are not changes on geometry, but only on the material, in order to avoid to recompute all.
Show UV projection.This section is useful mainly for making proxy meshes.
* Recover seams.Creates a Seam object, which has edges where the selected mesh's UV layout has seams. The Seam object is intended to be reference for marking seams for the clothing.
* Auto seams.
* Project UVs.Automatically create an UV layout for the clothing, compatible with the human's UV coordinates. This is intended for the mask UV layer, which must be compatible with the body mesh for all clothes. The actual texture can use a different UV layer which can be laid out in any desirable manner.
* Reexport Mhclo file.The mhclo file must be resaved when the mask UVs have been defined. This can be done by pressing Make clothes again, but Reexport Mhclo file is faster.
### Show ZDepth, Show Offset scaling
 !IMAGE!Pictures/options-02_0.png!/IMAGE! 
Show ZDepth.This option is used to assign a depth to the cloth, in order to hide skin and clothes which are covered by clothes on top of it. The Z depth specifies the stacking order, which decides which clothes should hide others. Normally the Z depth ranges between 0 (skin) and 100 (external accessories such as backpacks).
* Depth name. Roughly indicates the preferred Z depth for various clothes types. The choices are: Body, Underwear and lingerie, Socks and stockings, Shirt and trousers, Sweater, Indoor jacket, Shoes and boots, Coat, Backpack.
* Set Z depth.Set the Z depth depending on the selected depth name.
* Z depth.The value of the Z depth. This is changed by the Set Z depth button, but can be dialledmanually for fine-tuning.
Show Offset scaling.The location of a clothing vertex depends on two data: a point on a body triangle, described in barycentric coordinates, and the offset from that point. The offset is scaled in the X, Y and Z directions depending on the size of a certain body part.
* Body part.Set this to the body part which is most affected. The choices are: Custom, Body, Genital, Head, Torso, Arm, Hand, Leg, Foot.
* Examine.Select the boundary vertices with Set boundary is invoked.
* Set boundary.Set the boundary to vertices determined by the selected body part.
* Custom Boundary.To manually set the bounday box.
* X1, X2, Y1, Y2, Z1, Z2.The vertex numbers of the six vertices which define the scaling boundary. The X scale is determined from the distance between vertices X1 and X2, the Y scale by Y1 and Y2, and the Z scale by Z1 and Z2.
### Show Setting, Show License
 !IMAGE!Pictures/options-03.png!/IMAGE! 
Show Setting.The setting include the author name and the export path. It's possible to save and restore the settings.
Show License.This set of options are to add theauthor name, the type of license and the tags for clothes. Licensing information to be put at the top of the exported mhclo file. It consists of three strings that can contain arbitary text.
* Author. Defaults to: Unknown.
* License. Defaults to: AGPL3
* HomePage. Defaults to:!LINK!http://www.makehuman.org/ -- http://www.makehuman.org/!/LINK!


### GUI languages and translations.
Our GUI is available in many languages, but translations are not yet complete. 
Anyway now contributing in order to add a new language is very easy, since the MakeHuman project is now available for translation on!LINK!http://www.transifex.com/organization/makehuman/ -- Transifex!/LINK!.
 !IMAGE!Pictures/languages.png!/IMAGE! 
Transifex is a web application for localization in an easy and agile way.
 !IMAGE!Pictures/transifex.png!/IMAGE! 
If you want to help the MakeHuman project by translating the GUI into your language, you first need to create an account on Transifex. Then, when logged in, you can go to!LINK!https://www.transifex.com/projects/p/makehuman/ -- the MakeHuman Transifex page!/LINK!and click on the appropriate language you want to translate. Then click the "Join team" button. Now you can click the current release name (for example  "Alpha 8") entry and click "Translate now".
If you want to make a translation in another language that is not yet listed, click "request language" on the!LINK!https://www.transifex.com/projects/p/makehuman/ -- MakeHuman transifex page!/LINK!. We will make sure to accept it as fast as possible, so you can start translating.
Translating is quick and easy. You can select the "Untranslated strings" filter to show only the things left to translate. Click the first word on the left, and in the center of the screen enter your translation in the input box. When done typing, simply press the TAB button on your keyboard, and it automatically goes to the next entry. Repeat this process untill everything is translated.
  
You can leave things open you are uncertain about, and leave them for later. Perhaps others know a good solution. You can interrupt your work at any time and continue working later, or leave it for others to finish.
If you already have a translated file on your hard disk (for example you made modifications to an already existing language .ini file of MakeHuman, or you have filled in a .missing language file), you can upload it as translation and Transifex will automatically include it in the translation.
You will be also able to download the json file of your language, in order to put it in makehuman/data/languages. On restarting MakeHuman, the new language will be available as an option under "Settings".
  
 


### MHBlenderTools: Download and installation
The Blendertools package is available on the download page:!LINK!http://www.makehuman.org/content/download.html -- http://www.makehuman.org/content/download.html!/LINK!
The current version is 1.0.0, designed to work with MakeHuman 1.0.0 and with Blender 2.69. It's a zip package of four folders:
* MakeTarget
* MakeClothes
* MakeWalk
* mhx_importer
To install the addons, these subfolders must first be copied to a location where Blender can find it. Depending on the operating system being used, the addons destination directory where Blender will look for user-defined add-ons, is
* Windows 7: C:\Users\%username%\AppData\Roaming\Blender Foundation\Blender\2.6x\scripts\addons
* Windows XP: C:\Documents and Settings\%username%\Application Data\Blender Foundation\Blender\2.6x\scripts\addons
* Vista: C:\Program Files\Blender Foundation\Blender\%blenderversion%\scripts\addons (this is valid at least for blender 2.69)
* Linux: /home/$user/.blender/$version/scripts/addons
Note that the AppData folder in Windows 7 and the .blender folder in Linux are hidden folders. The location may also be different depending on your choices for setting up your operating system and Blender. For more information see the Blender documentation.
To enable the MH addons, in Blender open the User Preferences window from the File > User Preferences menu, and go to the Addons tab. The Blendertools addons are located in the MakeHuman category. Enable them by checking the box in the upper-right corner, next to the running man symbol.   If you want Blendertools to start every time Blender is restarted, press the "Save User Settings" button.
 !IMAGE!Pictures/mhx-pref.png!/IMAGE! 
 


### MHBlenderTools: MakeWalk basic workflow
MakeWalk is a Blender add-on for retargeting mocap data (.bvh files) to a given armature.

=### Retargeting: how it works

The goal of retargeting is to transfer a motion from a source armature (e.g. from a BVH file) to a given target armature (e.g. the MHX rig). However, it is not straightforward to assign the source action to the target rig, even if the bones have identical names. The motion of each bone is specified in local coordinates, relative to the parent and the bone's own rest pose. If the rest poses of the source and target armatures differ, the source F-curves can not be used directly by the target armature.
 !IMAGE!Pictures/makewalk-1.png!/IMAGE! 
The picture above shows a transformation in the local coordinate system. Since the parent's local Y points along its axis and its local Z points up, the child bone is rotated around the local X axis. This is not very useful if the target armature has a diffent rest pose. To retarget the pose, we therefore reexpress the transformation in the global coordinate system, as shown below. The local X rotation corresponds to a global Y rotation, and by a different angle. Once the global transformation matrix is known, we can reexpress it in the target bone's local coordinate system.
  
The retargeting process thus consists of making two coordinate transformations:
Source local # > Global > Target local.
This will ensure that the source bone and the target bone will have the same global orientation.
 !IMAGE!Pictures/makewalk_2.png!/IMAGE! 
Unfortunately, things are a little more complicated. We do not always want the source and target bones to have identical orientation. In particular, the root or pelvis bone may point in entirely different directions in different  armatures. E.g. in the CMU armature rest pose the pelvis points forward-down, and in the MHX rig it points straight up.
 !IMAGE!Pictures/makewalk-3.png!/IMAGE! 
If we insisted that the root bone in the MHX rig would point in the same direction as in the CMU rig, the retargeting would not be very successful, as shown in the figure above. If we instead keep the rotation offset from the rest poses, the target pose becomes much better, as shown below.
To calibrate the source and target armature against each other, MalkWalk introduces extra keyframes at frame 0, where both armatures are posed in T-pose.
 !IMAGE!Pictures/mcp-ret-060-calibrate.png!/IMAGE! 
In the rest of the animation, bones in the target armature copy the global rotations of the source armature, apart from differences present in the T-poses. In this way we can transfer animations from CMU to the MHX rig, despite the fact that the rest poses are very different.
 

=### Basic Workflow

### Retargeting
The MakeWalk panels appear in the tool shelf whenever an armature is the active object. Select the armature and press the Load And Retarget button. In the file selector, select the .bvh file. We choose the file 90_04.bvh from the CMU database. It is a cartwheel animation.
 !IMAGE!Pictures/makewalk-4.png!/IMAGE! 
After a short wait, the armature is doing gymnastics.
 !IMAGE!Pictures/makewalk-5.png!/IMAGE! 
At frame 0 of the animation the armature has been placed in T-pose. This is not part of the originial .bvh file, but inserted by MakeWalk to calibrate the source armature (defined by the bvh file) and the target armature (the selected armature in the viewport) against each other.
### Supported armatures
MakeWalk works with most straightforward biped rigs with FK arms and legs, such as the Rigify meta-rig. There is also built-in support for some more complex rigs: the MHX advanced rig from MakeHuman, the MHX rig from MakeHuman and Rigify.
 !IMAGE!Pictures/makewalk-6.png!/IMAGE! 
It is often possible to use MakeWalk with other complex rig, but in that case the automatic bone identification may fail. If so, a bone map must be defined manually, see!LINK!http://makehuman.org/doc/node/defining_the_target_rig_manually.html -- Defining a Target Rig Manually!/LINK!.
### Troubleshooting
Retargeting is a rather involved subject, and it can sometimes result in poor motion. The process may even fail completely, usually because MakeWalk failed to automatically identify the bones of a complex rig. If this should happen, see!LINK!http://www.makehuman.org/doc/node/makewalk_errors_and_corrective_actions.html -- Errors and Corrective Actions!/LINK!.

=### Where to find BVH files

There are several different formats that mocap files can be stored in. MakeHuman's mocap tool can only deal with files in Biovision BVH format. BVH files can be bought from many commercial sources, but a large range of mocap files are also available for free download. Here are some sites I found useful.
* CMU Graphics Lab Motion Capture Database: Hosted at Carnegie-Mellon University, this is a huge library of mocap files which can be downloaded for free. The web address is!LINK!http://mocap.cs.cmu.edu/ -- http://mocap.cs.cmu.edu!/LINK!.  CMU hosts mocap files in three formats: tvd, c3d and amc. However, the mocap tool can only read BVH files, so none of these files can be used directly. Fortunately, B. Hahne at!LINK!http://www.cgspeed.com/ -- www.cgspeed.com!/LINK!has converted the CMU files to BVH. The converted files are located at!LINK!http://sites.google.com/a/cgspeed.com/cgspeed/motion-capture -- http://sites.google.com/a/cgspeed.com/cgspeed/motion-capture!/LINK!.
  
* Advanced Computing Center for the Arts and Design (ACCAD): Hosted at the Ohio State University, this is another great source of free mocap files. BVH files can be downloaded from!LINK!http://accad.osu.edu/research/mocap/mocap_data.htm -- http://accad.osu.edu/research/mocap/mocap_data.htm!/LINK! 
* Eyes Japan (mocapdata.com):This is a Japanese company that sells mocap data commercially, but they also offer a huge number of motions for free. According to their homepage, mocapdata.com provides 744 premium motion data and 4197 free motion data. The only catch is that downloading requires registration. Not surprisingly, the homepage of mocapdata.com has the address!LINK!http://www.mocapdata.com/ -- http://www.mocapdata.com/!/LINK!.
  
* The Trailer's Park: Free mocap data can also be found at the Trailer's Park,!LINK!http://www.thetrailerspark.com/ -- http://www.thetrailerspark.com!/LINK!. This site does not offer original data, but offer repacks of mocap data from other free sites for download. Free download is limited to some five packs per day, so some patience is required here.
  
* Hochschule der Medien, Universität Bonn (HDM):!LINK!http://www.mpi-inf.mpg.de/resources/HDM05/ -- http://www.mpi-inf.mpg.de/resources/HDM05!/LINK! 
* The Perfume global site project #001:!LINK!http://perfume-dev.github.com/ -- http://perfume-dev.github.com/!/LINK!


### MHBlenderTools: MakeWalk user interface

=### The user interface

The user > interface of MakeWalk is located in under the Armature tab, and becomes visible when an armature is selected. It consists of six panels; the first one is open by default and the others are closed.
 !IMAGE!Pictures/makewalk-7_0.png!/IMAGE! 
* Load And Retarget: Select a BVH file and retarget it to the active armature.
* Start Frame: The first frame in the BVH file to considered.
* Last Frame: The last frame to be considered, unless the animation stops earlier. The difference last_frame - first_frame is the maximal number of frames after retargeting. The number of frames in the BVH file may be larger, if some frames are skipped due to subsampling
* Detailed steps: When this options is selected, further buttons are show below
* Load BVH File (.bvh). Load a BVH file, and create an animated armature from it.
* Rename And Rescale BVH Rig. With the BVH armature active, and a target armature selected, rename and rescale the bones of the active armature to fit the target.
* Load And Rename BVH File (.bvh). A combination of the previous two buttons. With a target armature active, load a BVH file, and create an animated armature with renamed and rescaled bones.
* Retarget Selected To Active. Retarget the animation from a renamed and rescaled BVH armature to the active armature.
* Simplify FCurves. Simplify the F-curves of the active armature.
* Rescale FCurves. Rescale F-curevs of the active armature.What if retargeting fails?
MakeWalk is designed to retarget animations to a given armature with a minimum of user intervention. However, retargeting is a complex process, and entirely automatic retargeting may fail or result in suboptimal motion. Information about how to identify and correct problems is found in!LINK!/doc/node/blendertools_makewalk_troubleshooting.html -- Errors and Corrective Actions!/LINK!.
A common problem is that automatic identification of bones in the target armature fails. A bone map can then be assigned manually, cf.!LINK!/doc/node/blendertools_makewalk_troubleshooting.html -- Defining the Target Rig Manually.!/LINK!

=### Options panel

 !IMAGE!Pictures/makewalk-8.png!/IMAGE! 
* Use Default Subsample. Blender normally plays the animation in 24 fps or 25 fps, but the animation in the BVH file may be recorded at a different speed. In particular, the BVH files from CMU were filmed at 120 fps. Enable this option to have the animation play at natural speed, irrespective of the frame rate in the BVH file. Other subsample options are described below.
* Auto scale. Set the scale automatically based on the size of the left thigh. This choice has two motivations:
* Almost all character do have a left leg.
* The leg size is crucial for making walk cycles look good.

* Scale. The default MakeHuman scale is decimeters - 1 unit = 1 decimeter. Translations in a BVH file are expressed in different units; often the base unit is inches, meters or centimeters, but more obscure units can also occur, e.g. in BVH files from CMU. If the scale is set incorrectly, rotations will still be correctly retargeted, but the character will appear to take giant leaps or miniscule steps.
* Use Limits: If this option is enabled, MakeWalk honors any Limit Rotation constraints, and will not allow excessive rotations. If the animation in the bvh files exceeds some rotation limits, this makes the retargeted animation less faithful. On the other hand, the rig may not be built for excessive rotations, so unchecking this option can lead to other problems.
* Unlock Rotation: If this option is disabled, MakeWalk honors any rotation locks. If the animation in the bvh files bend around locked axes, this makes the retargeted animation less faithful. If Unlock Rotation is enabled, any X or Z rotation locks are disabled. Y rotation locks (bone twisting) are never disabled. The reason for this is that in the MHX and Rigify rigs, forearm rotation is handled by deform bones controlled by hand twisting.
* Auto source rig. The source rig (i.e. the armature defined by the BVH file) is specified in the!LINK!/doc/node/blendertools_makewalk_source_and_target_armature.html -- Source Armature panel!/LINK!. Enable this option if the mocap tool should attempt to automatically identify the source rig, based on the structure of the bone hierarchy.
* Auto target rig. The target rig (i.e. the armature in the blend file) is specified in the!LINK!/doc/node/blendertools_makewalk_source_and_target_armature.html -- Target Armature panel!/LINK!. Enable this option if the mocap tool should attempt to automatically identify the target rig, based on the structure of the bone hierarchy.
* Ignore Hidden Layers. Ignore bones on hidden layers when identifying the target rig.
### Subsample and Rescale
If the Use Default Subsample option is set, the mocap tool will rescale the animation to fit the current frame rate. However, there are at least two reasons why you may want to load an animation at a different frame rate:
* * To obtain a slow-motion or rapid-motion effect.
* To quickly load an animation to see if the gross features will work out.
If the Use Default Subsample option is disabled, the SubSample section becomes visible.
* Subsample. Enable subsampling.
* Subsample Factor. If the value of this property is n, only every n:th frame of the BVH animation is loaded.
* Rescale. Enable rescaling.
* Rescale Factor. If the value of this property is n, the time distance between keyframes is changed to n.
* Rescale FCurves. Apply the settings above to existing F-curves rather than to the loaded animation.
Rescaling differs from simply scaling F-curves in the F-curve editor.
### Simplification
* Simplify FCurves. Remove unnecessary keyframes.
* Max Loc Error. The maximal allowed error for location keyframes, in Blender units. A larger error results in fewer keyframes but less accuracy.
* Max Rot Error. The maximal allowed error for rotation keyframes, in degrees. A larger error results in fewer keyframes but less accuracy.
* Only Visible. Simplification only affect F-curves visible in the Graph editor.
* Only Between Markers. Simplification only affects F-curves between the two outermost selected markers. The timeline must have at least  two selected markers.

=### Edit panel

Loading and retargeting is normally only the first step in the creation of an animation from mocap data. There are many reasons why a loaded animation does not behave exactly the way you want it to: artifacts in the mocap data, differences in armature structure not compensated for correctly by the retargeting process, differences in body stature between the mocap actor and the target character, or simply that the filmed sequence does not do exactly what you intend.. It is of course possible to edit the action directly in the graph editor, but this is unpractical due to the amount of mocap data. The mocap tool offers several possibilities to edit an action at a higher level. These tools are colleted in the Edit Action panel which is located just below the Options panel.
 !IMAGE!Pictures/edit-action.png!/IMAGE! 
### Inverse Kinematics
* Transfer FK => IK: The load and retarget steps transfers an animation from a bvh file to the target character. However, only the FK bones are animated. Press this button to transfer the FK animation to the IK bones. Only works for the advanced MHX armature. If two markers are selected, only the animation between the markers is transferred.
* Transfer IK => FK: Transfer the animation back from the IK bones to the FK bones. Useful if the IK animation has been edited,
* Clear IK Animation: Remove all keyframes from all IK bones (arms and legs).
* Clear FK Animation: Remove all keyframes from all FK bones (arms and legs).
### Global Edit
* Shift Animation. Shift the keys for the selected bones at all keyframes.If two markers are selected, only the keyframes between the markers are deleted.
* X,Y,Z: F-curves affected by the next button.
* Fixate Bone Locations:Replace all location keys by their average. Only selected bones and keyframes between selected markers are affected.
* Rescale Factor: Factor used by next button.
* Rescale FCurves: Rescale all F-curves by the factor above. This is similar to scaling F-curves in the curve editor, but jumps are treated correctly. E.g., rotations of +180 degrees and -180 degrees are the same, but if we scale an F-curve with a factor two, the intermedate keyframe will have the average rotation 0 degrees, The Rescale FCurves button handles this case correctly.
### Local Edit
This section could be called "Poor man's animation layers". A loaded mocap animation usually has imperfections that must be edited, but without changing the overall feel of the motion. The Start Edit button creates a new animation layer where differences from the original motion are stored as keys, called delta keys since delta often denotes a difference.
* Start Edit: Start editing F-curves.
* Undo Edit: Quit F-curve editing, without modifying the original F-curves.
* Loc: Set a location delta keyframe.
* Rot: Set a rotation delta keyframe.
* LocRot: Set a location and rotation delta keyframe.
* Delete: Remove all delta keyframes at the current time.
* |<: Move to first delta keyframe
* <: Move to previous delta keyframe.
* >: Move to next delta keyframe.
* >|: Move to last delta keyframe.
* Confirm Edit: Modify the original F-curves and quit F-curve editing.
The delta keys are represented by markers in the timeline.
 !IMAGE!Pictures/mwe-315-local-keys.png!/IMAGE! 
A delta key can be added with the Loc, Rot and LocRot buttons, and removed with Delete. There is no way to view the delta keys directly. In the viewport and the curve editor, the final pose is shown, which is the sum of the original pose and the delta key.
A common use for delta keys is to correct for intersection with other objects or the character herself. The typical workflow is as follows:
* * Start Edit.
* Set a delta key at a good frame just before the intersection.
* Set a delta key at a good frame just after the intersection.
* Edit the pose a the frame(s) where intersection occurs.
* If the intersection has been removed, Confirm Edit. If not, set new delta keys until it has, or Undo Edit to remove the delta layer.
### Feet
* Left: Affect the left foot.
* Right: Affect the right foot.
* Hips: Affect the characters hip (COM) bone.
* Offset Toes: Ensure that the toe is below the ball of the foot at all keyframes. Primarily useful for rigs with a reverse foot setup as explained below.
* Keep Feet Above Floor: If a mesh object (typically a plane) is selected, shift the keyframes to keep the affected feet above the plane. The plane does not necessarily lie in the XY plane; if the plane is tilted, the feet are kept on the plane's upper side. If no plane is selected, the feet are kept above the XY plane (z = 0). The IK feet are affected if the rig has and uses IK legs, otherwise the FK feet are kept above the floor. If two markers are selected, only the keyframes inbetween are shifted.
In a rig with a reverse foot setup, such as the MHX rig, the foot can rotate around the toe, ball, and heel. The reverse foot and toe bones are completely fixed by the corresponding FK bones, but the IK effector can be placed arbitrarily, as long as it ends at the toe tip. The transfer tool uses this freedom to make the IK effector perfectly horizontal, provided that the toe is below the ball and heel.
 !IMAGE!Pictures/refoot.png!/IMAGE! 
  
To use this feature we must ensure that the toe is below the ball of the foot, which is done by the Offset Toes button.
### Loop And Repeat
!LINK! -- Loop Animation!/LINK!
Create a loop of the action between two selected time markers, by blending the keyframes in the beginning and end of the loop. This is useful e.g. to create walk and run cycles for games. For good results, the poses at the beginning and end of the selected region should be similar.
* Blend Range: The number of keyframes used for blending.
* Loop in place: Remove the X and Y components of the root bone's location.
* Loop F-curves: Loop the animation.
!LINK! -- Repeat Animation!/LINK!
  
Repeat the action between two selected time markers. The actions should preferably be looped before it is repeated, to make the beginning and end match seamlessly.
* Repeat Number: The number of repetitions.
* Repeat F-curves: Repeat the animation.
### Stitching
Create a new action by stitching two actions together seamlessly.
* Update Action List: Update the first and second action drop-down lists.
* First Action: The name of the first action.
* First End Frame: Last frame of the first action
* Set Current Action: Set the first action as the current action.
* Second Action: The name of the second action.
* Second Start Frame: First frame of the second action.
* Set Current Action: Set the second action as the current action.
* Action Target: Choose between creating a new action and prepending the second action.
* Blend Range: The number of keyframes used for blending. Same parameter as in Loop Animations section.
* Output Action Name:
* Stitch Actions: Stitch the actions together.


### MHBlenderTools: MakeWalk armatures

=### Source Armature panel

MakeWalk transfers an animation from a source armature, defined in a bvh file, to a given target armature. It uses an intermediate standard rig described in!LINK!http://makehuman.org/doc/node/defining_the_target_rig_manually.html -- Defining the Target Rig Manually!/LINK!. The bone map from the source armature to the target armature hence consists of two parts:
* A map from the source rig to the standard rig. It is defined in the MakeWalk: Source Armature panel.
* A map from the target rig to the standard rig. It is defined in the!LINK!http://makehuman.org/doc/node/makewalk_target_armature_panel.html -- MakeWalk: Target Armature panel!/LINK!.
 !IMAGE!Pictures/mws-010-panel.png!/IMAGE! 
When a new scene is opened, the  panel consists of the single button Initialize Source Panel. Once this button has been pressed, the following content is available:
 !IMAGE!Pictures/mws-020-auto.png!/IMAGE! 
* Reinit Source Panel: Reinitialization.
* Auto Source Rig: If this option is enabled, MakeWalk will try to identify the source rig automatically. It may happen that MakeWalk fails to identify the source rig automatically, but this is very unusual. If it should nevertheless happen, it is possible to define the bone map manually in analogy with !LINK!http://makehuman.org/doc/node/defining_the_target_rig_manually.html -- how it is done for target rigs!/LINK!.
* Source rig. A list of bvh rigs recognized by the mocap tool. This either defines the expected source rig (if Auto Source Rig is disabled) or to Automatic.
* Bones in the active source rig.

=### Target Armature panel

The second part of the mapping from source to target armatures is defined by the panel labelled MH Mocap: Target armature. It is the top-most of the mocap tool panels, and is closed by default.
When a new scene is opened, the  panel consists of the single button Initialize Target Panel. Once this button has been pressed, the following content is available:
 !IMAGE!Pictures/mwt-011-panel.png!/IMAGE! 
* Reinit Target Panel. Reinitialization.
* Target rig. A list of bvh rigs recognized by the mocap tool. This either defines the expected Target rig (if Auto Target rig guessing is disabled), or is set to a matching rig (if automatic target rig identificiation is enabled).
* Auto Target Rig. If this option is enabled, MakeWalk will try to identify the target rig automatically. However, automatic rig identification is not trivial for complex rigs, and it may fail. If so, the bone map may be specified manually, cf!LINK!http://makehuman.org/doc/node/defining_the_target_rig_manually.html -- Defining the Target Rig Manually!/LINK!. If the bone map is defined. The target rigs available by default correspond mostly to the rig presets that can be exported from MakeHuman
* MHX. An advanced rig from MakeHuman alpha 8.
* MH Alpha 7. The MHX rig from MakeHuman alpha 7.
* Rigify.

* Ignore Hidden Layers: Ignore bones on hidden layers during automatic rig identification.
* Reverse Hip. Select this option if the armature has an reverse hip. It is rather common that an armature has a reverse hip. In a normal hip setup, the armature root is the hip or pelvis bone, and the thighs and the rest of the spine are children of this bone. In a reverse hip setup, the first bone in the spine has been reversed. There is a separate root bone, and the two lowest bones in the spine are both children of thise root, whereas the thighs are children of the reversed hip.
* Identify Target Rig: Identify the target rig, i.e. find out how bone names in the active armature correspond to the internal names. This step is performed automatically during retargeting, but the identification can also be done separately for debugging purposes. The bone map appears in the area called FK bones below.
* Set T-pose. Pose the active armature in T-pose.
* Save T-pose. Option used by the next button.
* Save Target File. Save the current bone map as a .trg file. If the Save T-pose option is set, also save a json file defining the T-pose.
* FK bones. The bone map.
The picture below shows automatic rig identification of the Rigify meta-rig (Add > Armature > Advanced Human).
 !IMAGE!Pictures/mwt-020-metarig.png!/IMAGE! 
 


### MHBlenderTools: MakeWalk troubleshooting.

=### What if retargeting fails?

### Errors and Corrective Actions
This document will describe common errors and corrective actions.
It may happen that MakeWalk fails to retarget an animation to a given armature. In that case an error message is displayed.
 !IMAGE!Pictures/mwa-100-error.png!/IMAGE! 
The error message consists of the following:
Mocap error
  
Category
  
Detailed error message
  
A link to this page
MakeWalk errors are grouped into the following categories:
* Load Bvh File
* Rename And Rescale
* Identify Target Rig
* Automatic Target Rig
* Manual Target Rig
* Identify Source Rig
* Retarget
* General Error
Load Bvh File
  
Rename And Rescale
  
Identify Target Rig
### Automatic Target Rig
The most common problem is probably that MakeWalk fails to identify the target rig automatically. There are several possible reasons for this:
* The character is not oriented correctly. In the rest pose, the character should be standing with up being the positive Z axis and facing -Y.
* The armature is complex with extra bones not corresponding to a standard biped rig.
* The armature only has IK arms or legs. MakeWalk retargets animations to the FK limbs, so if no such bones exist, the program will not work.
 !IMAGE!Pictures/mwa-110-reverse-hip.png!/IMAGE! 
It is rather common that an armature has a reverse hip. In a normal hip setup, the armature root is the hip or pelvis bone, and the thighs and the rest of the spine are children of this bone. In a reverse hip setup, the first bone in the spine has been reversed. There is a separate root bone, and the two lowest bones in the spine are both children of thise root, whereas the thighs are children of the reversed hip.
 !IMAGE!Pictures/mwa-120-reversehip.png!/IMAGE! 
The advantage of such a setup is that the upper and lower body can be posed independently. However, MakeWalk failes to identify the bones, unless the Reverse Hip option has been enabled.
If automatic bone identification still fails, bone mapping has to be made manually. How this is done is described in the next section.
### Defining the Target Rig Manually
Internally, MakeWalk retargets animations to an armature with the following bone hierarchy.
Here is a visual illustration of the bone hierarchy:
 !IMAGE!Pictures/mwa-010-armature.png!/IMAGE! 
In order to retarget to an armature with different bone names, we must define a map between the given bones and the internal names. By default, MakeWalk attempts to do this automatically. However, automatic bone mapping may easily be confused for non-trivial rigs. If this happens, one can define the bone map manually.
A bone map for a target armature is defined by a .trg file located in the target_rigs folder under the makewalk directory. The folder already contains three files, for retargeting the MHX advanced rig, the MakeHuman, and Rigify. These rigs are too complicated to identify the bone map automatically, so MakeWalk recognizes these rigs and use the predefined bone map.
Create a .trg file using an existing file as a template. E.g., a .trg file could look like this:
Note that it is not necessary to define maps to all bones. Bone names must not contain spaces, since whitespace is used as a delimiter in the .trg file. If the bones in your armature do contain spaces, replace them by underscore ( _ ). MakeWalk treats space and underscore as equivalent, so this is not a problem, except for very strange naming convention.
 !IMAGE!Pictures/mwa-020-myrig.png!/IMAGE! 
Save the .trg file with the name my_rig.trg in the target_rigs folder and press the Reinit Target Panel button.  My_Rig should now appear in the Target rig list. Select it. In the FK bones sections, the My_Rig bone names are now listed. Make sure that the Auto Target Rig option is deselected, to override automatic bone mapping. Finally go to the main panel and press Load And Retarget. The animation should now be loaded.


### MHBlenderTools: MakeWalk utilities

=### Utilities panel

This panel contains material that does not naturally fit into the other panels.
 !IMAGE!Pictures/mwu-010-panel.png!/IMAGE! 
### Default Settings
* Save Defaults: Save current settings as the default settings.
* Load Defaults: Load the default settings from file.
### Manage Actions
* Actions: A list of all actions in the scene, at the time when the Update Action List button was last pressed.
* Filter: If selected, only actions belonging to the active character are included in the action list. When the mocap tool creates an action, the first four letters in the action name are taken from the rig name.
* Update Action List:
* Set Current Action: Set the action selected in the Actions list as the active action.
* Delete Action: Permanently delete the action selected in the Actions list. The action must have zero users. It is quite cumbersome to permanently delete actions in Blender. The reason is that creating an action with hand animation takes much work, which should not be lost accidentally. The situation is different with mocap, where it is easy to fill up a blend file with many irrelevant actions. This button makes it easier to clean out such junk motions.
* Delete Temporary Actions: Some tools create temporary actions, whose names start with a hash sign (#). Deletes all such actions.
### Temporary properties
* Delete Temporary Properties. MakeWalk creates some properties for relevant posebones during retargeting. Pressing this button removes these properties. However, be aware that some of the tools in the Edit panel may fail if the temporrary properties are deleted.
The temporary properties for the active posebone can be inspected in the N-panel.
 !IMAGE!Pictures/mwu-030-temp-props.png!/IMAGE! 
* McpBone: The name of this bone in the internal hierarchy.
* McpParent: The parent of this bone in the internal hierarchy.
* McpQuatW, McpQuatX, McpQuatY, McpQuatZ: The rotation of this bone in T-pose, represented as a quaternion.
### T-pose
* Set T-pose: Set the current pose to T-pose.
* Clear T-pose: Set the current pose to the default pose.
* Load T-pose: Load a T-pose from a .json file to the active armature.
* Save T-pose: Save the current pose as a .json file.
### Rest Pose
* Current Pose => Rest Pose: Set the current pose to rest pose.


### MHBlenderTools: MHX importer basic usage.
MHX (MakeHuman eXchange format) is a custom format used to transfer a rigged character from MakeHuman to Blender. Due to its tight integration with Blender's python API, it supports advanced features like constraints, drivers and properties that general-purpose formats like Collada or FBX do not support.

=### Export From MakeHuman

 !IMAGE!Pictures/mx010-export.png!/IMAGE! 
After the character has been designed in MakeHuman, go to the Files > Export tab and select Blender exchange (mhx) as the Mesh format. Type the character's name in the box at the top and press export. An mhx file has been exported.

=### Import Into Blender

Once the mhx importer has been enabled, we can import the mhx file. Select File > Import > MakeHuman (.mhx).
 !IMAGE!Pictures/mx070-import.png!/IMAGE! 
In the file selector, navigate to the file that we just exported from MakeHuman, i.e. John Doe.mhx in the export directory. After a short while, the character appears in the viewport, ready for posing.
 !IMAGE!Pictures/mx080-import.png!/IMAGE! 


### MHBlenderTools: MHX default rigging
If pose/animate > skeleton is set to 'None' when the character is exported from MakeHuman in .MHX format, the character is equipped with the default MHX armature. This is a rather complex rig with quite a few features.
The bones are grouped into bone layers. Bone layers can be turn on and off in the MHX Main panel that appears in the user interface pane (N-pane), which is found to the right of the viewport. N-pane visibility can be toggled on and off with N-key.
The Root Layer
 !IMAGE!Pictures/mx210-root.png!/IMAGE! 
There are two bones on the Root layer:
* master: the big bone located at the foot level. It is the ultimate parent of every other bone in the rig, and can be used to move the entire character, including ik effectors.
* root: the wiggly bone located at the character's center of mass. It also moves the entire character, but IK effectors remain at a fix position.
The Spine Layer
 !IMAGE!Pictures/mx220-spine.png!/IMAGE! 
The spine is an immedate child of the root bone.
* spine:
* spine-1:
* chest:
* chest-1
* neck
* head
On this layer the two clavicle bones are also found. They are children of chest-1 and also appear on the arm layers.
The Head Layer
 !IMAGE!Pictures/mx230-head.png!/IMAGE! 
This layers contains the bones of the head (not the Neck and Head bones, however).
* jaw: Jaw bone
* tongue_base: Inner part of tongue.
* tongue_mid: Middle part of tongue.
* tongue_tip: Outer part of tongue.
* eye.L: Left eye.
* uplid.L: Left upper eyelid.
* lolid.L: Left lower eyelid.
* eye.R: Right eye.
* uplid.R: Right upper eyelid.
* lolid.R: Right lower eyelid.
* gaze. Target that the left and right eyes are tracking.
The FK Arm Layers
 !IMAGE!Pictures/mx240-fkarm.png!/IMAGE! 
The left forward kinematics (FK) arm layer consists of:
* clavicle.L: Left clavicle.
* deltoid.L Left deltoid muscle.
* upper_arm.fk.L: Left FK upper arm (humerus).
* forearm.fk.L: Left FK forearm. Y rotation is locked on this bone. To twist the forearm, rotate the hand bone instead.
* hand.fk.L: Left FK hand.
The bones on the right FK arm layer are analogous.
Note that there are two shoulder bones: clavicle and deltoid. It is not trivial to pose the shoulder, and with two shoulder bones better deformation is possible. The drawback is that an additional bone must be posed. However, in the common case that the arm is well below shoulder level, the deltoid bone can often be ignored.
The FK Leg Layers
 !IMAGE!Pictures/mx250-fkleg.png!/IMAGE! 
The left FK leg layer consists of:
* thigh.fk.L: Left FK thigh.
* shin.fk.L: Left FK shin.
* foot.fk.L: Left FK foot.
* toe.fk.L: Left FK toes.
THe right FK layer is analogous.
The Finger Layers
 !IMAGE!Pictures/mx260-fingers.png!/IMAGE! 
The long fingers on the Finger layers give a quick way to pose the fingers; the poses can be fine-tuned with the individual finger links on the Links layer.  The bones on the left Finger layer are:
* thumb.L: Left long thumb.
* index.L: Left long index finger.
* middle.L: Left long middle finger.
* ring.L: Left long ring finger.
* pinky.L: Left long pinky.
The bones on the right Finger layer are analogous.
Rotating a long finger around the local X will cause all finger links to curl (rotate around local X). Rotation around local Z only affects the first finger link.
The Finger Link Layers
 !IMAGE!Pictures/mx270-links.png!/IMAGE! 
Each of the Finger Links layers contains fourteen bones; two for the thumb and three for each other finger. They are used to fine-tune the finger pose, once a rough pose is achieved with the long finger bones.
The Palm Layers
 !IMAGE!Pictures/mx280-palm.png!/IMAGE! 
The left Palm layer contain the meta-carpal bones:
* thumb.01.L: Parent of the left thumb bones.
* palm_index.L: Parent of the left index finger bones.
* palm_middle.L: Parent of the left middle finger bones.
* palm_ring.L: Parent of the left ring finger bones.
* palm_pinky.L: Parent of the left pinky bones.
The bones on the right Palm layer are analogous.
The IK Arm Layers
 !IMAGE!Pictures/mx300-ikarm.png!/IMAGE! 
The arms are controlled by FK by default, but inverse kinematics (IK) can also be used. To quickly switch between FK and IK, press the buttons labelled FK or IK in the MHX FK/IK Switch panel, which appears in the N-panel if an MHX armature is the active object.
* clavicle.L: Left clavicle. Same bone as on FK layer.
* deltoid.L: Left deltoid. Same bone as on FK layer.
* hand.ik.L: Left hand IK effector. Positions and rotates the hand. Also controls forearm twist.
* elbow.pt.ik.L: Left elbow pole target. Controls the location of the elbow, which lies in the plane spanned by the arm socket (head of upper arm), wrist (tail of forearm), and elbow pole target.
* elbow.link.L: A rubberband that connects the elbow to the elbow pole target. This bone is merely a visual cue; has no effect and can not be selected.
The bones on the right IK arm layer are analogous.
The IK Leg Layers
 !IMAGE!Pictures/mx310-ikleg.png!/IMAGE! 
The legs are controlled by FK by default, but IK can also be used. To quickly switch between FK and IK, press the buttons labelled FK or IK in the MHX FK/IK Switch panel, which appears in the N-panel if an MHX armature is the active object.
* foot.ik.L: Left hand IK effector. Positions and rotates the hand.
* toe.rev..L: Left reverse toe.
* foot.rev.L: Left reverse foot.
* knee.pt.ik.L: Left knee pole target. Controls the location of the knee, which lies in the plane spanned by the leg socket (head of thigh), ankle (tail of shin), and knee pole target.
* knee.link.L: A rubberband that connects the knee to the knee pole target. This bone is merely a visual cue; has no effect and can not be selected.
* shin.ik.L: The foot bones and the pole target control the thigh and shin rotation, except for the twist (local Y rotation) of the shin, which is handle by this bone instead. The IK shin bone does not affect the bending of the shin, only the twisting.
The bones on the right IK leg layer are analogous.
 !IMAGE!Pictures/mx320-revfoot2.png!/IMAGE! 
The IK leg has an reverse foot setup, which allows the foot to rotate around the toe, ball, and heel.
* foot.ik.L: Rotate around heel.
* toe.rev.L: Rotate around toe tip.
* foot.rev.L: Rotate around ball.
FK-IK Snapping
In a rig with both FK and IK, it is useful to be able to switch between the two seamlessly. To this end, the MHX FK/IK Switch panel contains buttons to snap the IK to FK and vice versa, in such a way that the character's pose remains unchanged.
 !IMAGE!Pictures/mx330-fkik2.png!/IMAGE! 
To snap the IK bones to the FK pose, press the buttons
* Snap L IK Arm
* Snap R IK Arm
* Snap L IK Leg
* Snap R IK Leg
respectively. Note that the FK buttons at the top of the panel change to IK.
 !IMAGE!Pictures/mx340-ikfk2.png!/IMAGE! 
To snap the FK bones to the IK pose, press the buttons
* Snap L FK Arm
* Snap R FK Arm
* Snap L FK Leg
* Snap R FK Leg
respectively. Note that the IK buttons at the top of the panel change to FK.
The Tweak layer
 !IMAGE!Pictures/mx360-tweak2.png!/IMAGE! 
This layer contains some rarely used bone that in some cases are useful to tweak a pose.
* breast.L: Controls rotation of left breast. Useful mainly for female characters.
* arm.socket.L: The left arm socket. Allows the left upper arm (FK and IK) to be moved away from the deltoid bone.
* leg.socket.L: The left leg socket. Allows the left thigh (FK and IK) to be moved away from the hip.
The right-side bones (with suffix .R) are defined analogously.
 !IMAGE!Pictures/mx370-markers2.png!/IMAGE! 
The Tweak layer also contains marker bones. They are used by MakeWalk to determine the location of the toe, ball and heel, so they can be moved up above floor level. Move these bones in Edit mode to fine-tune their locatation. The marker bones on the left side are:
* toe.marker.L: Left toe marker.
* ball.marker.L: Left ball marker.
* heel.marker.L: Left heel marker.
The marker bones on the right side are analogous.
The MHX Control Panel
The default behaviour of the MHX rig can be modified by changing some properties in this panel.
 !IMAGE!Pictures/mx410-gaze2.png!/IMAGE! 
* GazeFollowsHead: If 1.0, the gaze bone is parented to the head. If 0.0, the gaze bone remains fixed in space (it is parented to the master bone).
* RotationLimits: If 0.0, all Limit Rotation constraint is ignored. If 1.0, they are honored. Default = 0.8.
 !IMAGE!Pictures/mx420-hinge2.png!/IMAGE! 
* ArmHinge, Left and Right: Determines whether the arm rotates when the shoulder does.
* FingerControl, Left and Right: Determines whether the finger links are parented by the long fingers (the default), or if the long fingers are to be ignored.
 !IMAGE!Pictures/mx430-leghinge2.png!/IMAGE! 
* LegHinge, Left and Right: Determines whether the leg rotates when the hip does. 
 !IMAGE!Pictures/mx440-legik2ankle2.png!/IMAGE! 
* LegIkToAnkle, Left and Right: If turned on, the reverse foot setup is disabled, and the ankle bones on the Extra layers become the effectors for the IK legs.


### MHBlenderTools: MHX other rigging systems
By default (i.e., if Pose/Animate > Skeleton is set to 'None') a character is exported as an mhx file is rigged with the MHX rig, which is a rather complex rig with many options. Alternatively, the character can be rigged with a simpler and ligher armature by choosing an alternate Rig Preset under Pose/Animate > Skeleton.
 !IMAGE!Pictures/mx710-other-rig2.png!/IMAGE! 
To this end, select one of the rigs in the Pose/Animate > Skeleton tab. A skeleton is drawn. Export the character from MakeHuman as an mhx file.
To reselect the default mhx rig, press None in the Pose/Animate > Skeleton tab.
 !IMAGE!Pictures/mx720-other-blender2.png!/IMAGE! 
Import the mhx file into Blender. Note that there are fewer bone layers available in the MHX Main panel.

=### Using the Rigify rig

As an alternative to the mhx rig, MakeHuman characters can also be rigged with the popular Rigify add-on by Nathan Vegdahl. Links to documentation about Rigify in general:
!LINK!http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Rigging/Rigify -- Official Rigify documentation!/LINK!
!LINK!http://blenderartists.org/forum/showthread.php?200371-Rigify-Auto-rigging-system-new-and-improved -- Blenderartist thread!/LINK!
 !IMAGE!Pictures/mx810-rigify-export2.png!/IMAGE! 
To use Rigify, the character must first be prepared in MakeHuman. Select the Export for Rigify checkbox in the Options group and export the file. This checkbox overrides any other rig selected under the Skeleton tab.
 !IMAGE!Pictures/mx820-rigify-enable2.png!/IMAGE! 
In Blender, enable the Rigify add-on. It is found in the Rigging category. Press Save User Settings to remember the choice.
 !IMAGE!Pictures/mx830-rigified2.png!/IMAGE! 
Import the mhx file as usual. John Doe is now rigged with Rigify and ready for use.
 !IMAGE!Pictures/mx840-norigify2.png!/IMAGE! 
If the Rigify add-on is not enabled, an intermediate rig is imported and an error message appears. If this happens, open a new Blender file, enable Rigify, and try again. Alternatively, you may select the armature and press the Rigify MHX Rig button that appears in the N-panel (after you have enabled the Rigify add-on, of course).
Disclaimer: MakeHuman has no control of the Rigify add-on. Rigify support was tested with Blender 2.69. If the specification of Rigify changes in the future, mhx file exported for Rigify may cease to work.
 


### MHBlenderTools: MHX Layers and masks
The mhx importer creates objects on the first four layers.
 !IMAGE!Pictures/mx900-layers2.png!/IMAGE! 
* * This layer contains the body, including hair, eyes, etc.
* This layer contains the armature.
* This layer contains any clothes. Empty if the character is nude.
* This layer contains any proxy meshes. Empty if no proxy mesh was exported.
Note that a proxy mesh does not replace the original human mesh, but is added as a separate object. If you only want to use the proxy mesh, the body can be deleted. However, the proxy mesh (perhaps slightly edited) has several uses apart from simply replacing the body, e.g. as a deflection surface for cloth simulation, or to speed up viewport performance when animating. It is therefore up to the user to decide which meshes to delete.
 !IMAGE!Pictures/mx920-unmasked2.png!/IMAGE! 
Vertices beneath clothes are hidden, to avoid ugly penetration issues. The picture above illustrates what may happen if skin under clothes is not hidden.
 !IMAGE!Pictures/mx910-mask2.png!/IMAGE! 
However, skin beneath clothes is not removed, only hidden by masks. This becomes evident if in edit mode, where the entire body is visible. To undress the character, deselect the clothes layer (layer 3), and disable all mask modifiers. Don't forget to disable the mask modifier for rendering as well.
With the mask modifiers, it is possible to export a character from MakeHuman with several different outfits, and select the outfit and hidden body vertices in Blender.
If you wish to delete the hidden vertices permanently, e.g. to improve performance or for export to some other application, apply the relevant mask modifiers.


### MHBlenderTools: MakeClothes rigid fitting
The standard clothes fitting algorithm is suitable for flexible clothes, especially clothes that follow the body closely. However, is does not work well for rigid objects like shoes, Therefore, MakeClothes has a variant suitable for rigid shoes. Rigid fitting is used on a vertex group basis, so rigid and flexible fitting can be mixed in the same piece of clothing.
Rigid fitting is used for every vertex group whose name starts with a '*'. Each such vertex group in the human must contain exactly three vertices, that determine the triangle used for fitting in this group.
 !IMAGE!Pictures/rf-100-orig.png!/IMAGE! 
The use of rigid vertex groups is best explained by an example. Consider a pair of shoes, which is a rigid object. We used the standard MakeClothes settings and an adult human with the original shoe to the left. Then the mhclo file was loaded onto a baby, with the result to the right. The shoe is recognizable but it has been deformed in an undesirable way. However, even though the quality of the fitting is poor, make sure to save the mhclo file, because we will need it at the end of this tutorial.
 !IMAGE!Pictures/rf-110-projection.png!/IMAGE! 
Each clothing vertex v is associated with a triangle t in the human mesh, i.e. three human vertices v1, v2, v3. Letrdenote the location of v andr1,r2,r3the locations of the corners of the triangle. Further, let d be the perpendicular distance from the clothes vertex to the plane spanned by the triangle. MakeClothes assigns three weights w1, w2, w3, such that
    r= w1r1+ w2r2+ w3r3+d,
where the sum of weights w1+ w2+ w3= 1. When the clothing is loaded onto a different character, the new location becomes
    r'= w1r'1+ w2r'2+ w3r'3+d',
wherer'1,r'2,r'3are the locations of the three human vertices in the new character, and
    d' #  Sd (sxdx, sydy, szdz)
is obtained from the original offsetdby inhomogeneous global scaling with the diagonal scale matrix
    S = diag(sx, sy, sz).
The important observation is that the quality of the fitting depends crucially on the chosen triangle, i.e. the triple of human vertices the determines the clothes vertex location. The standard choice is to choose the human triangle closest to to clothing vertex. In rigid fitting the triangle is the same for all vertices, and is defined by the tree vertices in the vertex group.
 !IMAGE!Pictures/rf-120-vgroups.png!/IMAGE! 
Here we see the vertex groups used to fit the left shoe. The standard vertex group Left consists of all vertices close to the left shoe, in the tights helper. On the other hand, the rigid vertex group *Left only contains three vertices that define the single triangle used for all clothes vertices in this group.
 !IMAGE!Pictures/rf-130-triangles.png!/IMAGE! 
The next illustration shows the corresponding triangles used for fitting. The Left group uses many triangles obtained by triangulating the corresponding faces. Different shoe vertices are associated with triangles that are transformed differently, and the rigid character of the shoe is lost. The *Left group only has one single triangle, with corners at the three vertices in the vertex group. The same triangle is used by all left shoe vertices.
 !IMAGE!Pictures/rf-140-rename-vgroups.png!/IMAGE! 
Once the human vertex groups have been defined, we proceed with clothes-making. Rename the shoe vertex groups to *Left and *Right, to make the shoes use rigid fitting. Recall that the human can have several overlapping vertex groups, but in a piece of clothing each vertex must belong to exactly one group.
 !IMAGE!Pictures/rf-150-offset-scaling.png!/IMAGE! 
Next we open the Offset Scaling section and select Foot as the body part. In flexible fitting, the offsets are usually very small, and selecting the correct body part is not so important. In contrast, this step is very important in rigid fitting, because many vertices are far away from their triangles and the offsets must be scaled correctly. Press Examing Boundary for a visual inspection of which vertices define the global scale matrix..
 !IMAGE!Pictures/rf-160-baby-shoes.png!/IMAGE! 
This picture shows the shoe loaded on a baby, using flexible fitting (blue) and rigid fitting (red). Rigid fitting clearly maintains the shape of the shoe much better.
However, one problem remains: bone weighting. Start up MakeHuman and load the shoes under the Geometries > Clothes tab. Export the character with a rig in one of the formats that allows that, e.g. mhx, and import the character into Blender. Now try to pose the feet. As we see in the picture below, the shoe does not follow the foot but is squashed or stretched in strange ways.
 !IMAGE!Pictures/rf-170-bad-deformation.png!/IMAGE! 
The reason is that rigid fitting affects the bone weights as well as the vertex locations. The bone weights are interpolated between the three corners of the triangle, rather than using the information from the entire foot. To correct this we need to use two different associations between clothes and human vertices: rigid fitting for vertex locations, but flexible fitting for bone weights.
Fortunately, MakeHuman can handle this situation, although there is currently no elegant interface for it in MakeClothes. In a text editor, open the mhclo file obtained by standard fitting in the beginning of this tutotial (this is why you needed to save it), and copy everything after the line
verts 0
to the end of the new mhclo file obtained by rigid fitting. Before the copied section, insert the line
weighting_verts
Export the shoes again from MakeHuman and import into Blender. The shoes should now both maintain their rigid shape and deform correctly.
 !IMAGE!Pictures/rf-190-good-deformation.png!/IMAGE! 
Due to an unfortunate behavior in MakeHuman, it is possible that the updated mhclo file is not loaded after it has replaced the old one. This is because MakeHuman automatically compiles mhclo and obj files when loaded, so they can be loaded faster next time. Although this behavior is convenient for ordinary users, it is very confusing and frustrating for clothes makers. If MakeHuman insists on loading old versions of your clothes, you may need to delete the compiled files (*.mhpxy and *.npz), or restart MakeHuman, or both. After the compiled files are gone, the updated clothes should load without problems.
 !IMAGE!Pictures/rf-180-compiled-files.png!/IMAGE! 
 
 
 
 
 



## Developers' note

Some notes about how to obtain the source code, modify it and share it.

### Makehuman Plugin System

=### Plugins

Makehuman has a simple plugin framework which makes it easy to add and remove features. At startup, MakeHuman now looks for .py files in the plugins folder which are not starting with an underscore (which makes it easier to disable unwanted plugins). It loads them one by one and calls the load entry point passing a reference to the application. The plugin can use this reference to add the necessary GUI widgets or code to the application.
  
The rules for plugins are very simple:
* A plugin is a .py file in the plugins folder with a load entry point.
* A plugin only imports core files.
The reason a plugin cannot import other plugins is that it would make it difficult to know which files belong to which plugin. We still need to define a convention for shared files beyond the core MakeHuman files. To get started look at example.py or any of the other plugins to see how you can create your own feature in MakeHuman.

=### GUI

The main layout  is a two level tab control. The tabs at the top represent categories, like files. modelling, geometries, materials, etc. The ones at the bottom are the tasks in the current category and refine the more broad category in face, torso, gender, saving, loading, exporting etc.
So when creating your plugin, the first thought should be “In which category does it belong?”. From experience we know that it can be a though question to answer. Sometimes the only answer is adding a new category. This is what we initially did for measurement for example
Next you probably want your own task to implement your feature. While it’s possible to attach functionality to an instance of gui3d.Task, it’s often easier to derive your own class.
  
When you create an instance of your class, you pass the parent of your task, which can either be an existing category
or the new one which you added.
In your derived task you will then add the necessary controls to let the user interact. A good place to see how to use the different controls is the example plugin. You will see that even if you don’t add any controls, the model is already visible. This is because the model is attached to the root of the GUI tree. In the onShow event of your task you might want to reset the camera position, like we do in the save task, or hide the model, like we do in the load task. Just don’t forget to reset the state when your task gets hidden in onHide.

=### Undo-redo

It is important that every modification is undoable, since just one undo able modification would leave the user without the possibility to undo anything. So it’s crucial that if you write a plugin which modifies the model, you also make undo work.
  
The Application class has several methods to work with actions. An action is a class with two methods, do and undo. If the action itself does the modification you can use app.do to add it to the undo stack. If you did the modification yourself already during user interaction, you can add the action using app.did. The application won’t call the do method of the action in that case.
  
If you want to make your own undoredo buttons, you can use app.undo and app.redo. To illustrate, here is the action we use to change the hair color:
The postAction is a handy way to specify a method to keep your GUI in sync with the changes.

=### Asynchronous Calls and Animation

When doing lengthy operations it is important not to block the GUI from redrawing. Since everything runs in one thread, it is easy to block the event loop in your plugin. There are 4 ways to avoid this, depending on the need. If no user interaction is needed, a progressbar can be used. A progressbar uses the redrawNow() method of the application. This redraws the screen outside the event loop. Instead of creating your own progressbar, it is advised to use the progress method, which uses the global progressbar. Calling progress with a value greater than zero shows the progressbar, a value of zero hides it.
If user interaction is desired during the operation, either asynchronous calls, a timer or a thread can be used. Asynchronous calls are used when a lengthy operation can be split in several units. It is used for example in the startup procedure as well as for the plugin loading loop. The mh.callAsync(method) queues the calling of method in the event loop, so it will be called when the event gets processed. In case different methods need to be called after each other, as in the startup procedure, callAsync is used to call the next method.
In case of the plugin loading loop, it calls the same method until it is done.
This is not to be used for animations, as it takes very little time between calling callAsync and the event loop calling the method. Calling time.sleep(dt) to avoid this should not be done as it blocks the main thread. For animations use timers instead. An example of this can be found in the BvhPlayer plugin. The method mh.addTimer(interval, method) adds a timer which calls the given method every interval milliseconds. It returns a value to be used by removeTimer to stop the timer.
If a lengthy operation includes blocking on sockets or pipes, it is advised to use a python thread. However this has been shown to be problematic on Linux. To get around the problems on linux you should not access any makehuman structures from within your thread, but use mh.callAsync to call the methods from the main thread. See the clock plugin example for example code on how to use threads correctly.

=### A template for plugins

Looking in the makehuman source folder, in the "plugin" directory, you will notice a file called "7_example.py". This is an "Hello world" plugin. It includes all main controls and some nice example of mesh manipulation. It's designed to be used as template of new plugin.
To see how it works, you need to enable it in the Preferences->Setting. Then it will be located at Utilities-->Example.
 !IMAGE!Pictures/UtilitiesExampleTab3.png!/IMAGE! 

=### Example Controls

 !IMAGE!Pictures/UtilitiesExampleControls.png!/IMAGE! 


### OpenGL Notes
Most of the 3D mesh handling functionality is delivered using OpenGL embedded within the C application code. OpenGL is a 3D graphics library that enables a 3D world to be defined, with a camera, objects, lights, textures etc. It then enables that 3D world to be visualised as a 2D representation that can be displayed on a computer screen and provides functions to enable an application (in response to user input) to navigate around the scene.

=### Basics

OpenGL takes a 3D scene and draws it into a 2D viewing area on your screen known as the viewport. OpenGL can project the scene onto the viewport in a variety of different ways, but the most common are:
* Perspective projection, as you would get if you could place a camera in the scene
* Orthographic projection, as a draftsman may contstruct technical drawings such as plans and elevations.
MakeHuman only uses Perspective projection.

=### Projection Transformation

You tell OpenGL how to project 3D objects onto the 2D viewport by defining a projection transformation, which indicates whether you wish to use perspective or orthographic projection (or an alternative projection pattern) and specifies other projection settings. This can be imagined as being comparable to specifying the characteristics of a camera (field of view, aspect ratio etc.) where an orthographic projection is equivalent to a camera at an infinite distance. The main difference being that with OpenGL you can change the settings between drawing different objects, which is a bit like taking a photo, changing the lens and moving the camera, then taking another photo without winding the film on.
MakeHuman sets a perspective projection using the function gluPerspective(fovAngle,aspectRatio,near,far) where:
* fovAngle: is the vertical field of view angle (45 degrees)
* aspectRatio: is the viewport width divided by the viewport height which, by default, is 800/600 (4/3)
* near: is the distance to the centre of the viewing plane (0.1)
* far: is the distance to the centre of the rear clippling plane (100)

=### Modelview Transformation

For OpenGL to know what to display in the viewport it also needs to know where the camera is relative to the 3D model. For this you need to define a modelview which defines the position and orientation of the camera and the position and orientation of objects that go to make up the model inside a virtual 3D world.    You do this by moving through and around the 3D world and by creating objects relative to your current position. OpenGL keeps track of your current position and orientation in the 3D world by recording the modelview transformation.
  
Both the projection transformation and the modelview transformation are stored internally in 4x4 transformation matrices. You can modify these matrices by calling functions that apply direct transformations (translations and rotations) or by calling functions that calculate transformations (e.g. the gluPerspective function outlined above).
  
To apply transformations you need to first make one of these matrices the current matrix. Subsequent transformations are applied cumulatively to the current matrix. The glMatrixMode function is used to set the current matrix mode:
* glMatrixMode(GL_PROJECTION) makes the projection transformation the current matrix so that projection settings can be applied, such as the field of View angle and Aspect Ratio.
* glMatrixMode(GL_MODELVIEW) makes the modelview transformation matrix the current matrix so that subsequent translations and rotations move the current location through the 3D world.

=### Resetting a transformation matrix

Matrix transformations that you apply are applied cumulatively. It is therefore often necessary to reset the matrix to its default ‘no transformation’ state so that you can apply a fresh set of transformations. OpenGL uses the transformation and modelview matrices to transform coordinates by performing a matrix multiplication. If you multiply by an identity matrix then the result is the same as the thing you started with, so to reset one of these matrices to an initial state where the transformation has no effect you can simply load the identity matrix using the function glLoadIdentity(). This loads the identity matrix into whichever transformation matrix is currently active, resetting it to the default ‘no transformation’ state.

=### Coordinates

OpenGL world space coordinates are unitless, so 2 units can represent milimeters, inches or light years. Interpretation of world space coordinates is up to the application. OpenGL uses a right handed coordinate system, so, if you are looking at the origin with the +X axis stretching away to the right and the +Y axis pointing straight up, the +Z axis will be heading out of the screen straight towards you and the -Z axis will be dissapearing away from you into the distance.
  
MakeHuman uses the default OpenGL modelview camera settings which are equivalent to invoking gluLookAt(0,0,0, 0,0,-1, 0,1,0). This places the camera at the origin, looking straight into the model along the -Z axis with the +Y axis pointing straight up. This means that a 2 unit wide and 2 unit high object centred at <0,0,-1> will roughly fill the viewport, as will a 4x4 object at twice the distance from the viewpoint.

=### Drawing objects

MakeHuman contains multiple objects. The Humanoid object is the main object, but it is surrounded by a set of control objects. Each object is constructed using triangular faces. The position and orientation of each face is defined relative to the object of which it is a part. The positions and orientations of the vertices and normals of the faces are defined relative to the face they’re on. The sequence in which face vertices are defined is significant in OpenGL. If the face is viewed from the front, the sequence of points runs counter clockwise. If the face is viewed from the back the points run clockwise. Faces viewed from behind may be invisible or may have a different color/texture defined to the front face. This order is also called the "winding order" of vertices, and is used by MakeHuman to calculate the normal of each face. If the winding order is reversed, the normal will be flipped. The glPushMatrix and glPopMatrix functions can be used to store away a copy of a matrix that can subsequently restored. MakeHuman uses this before and after drawing each object to store a copy of the modelview matrix and restore it.
 


### Directory structure and core modules
Overview
There are 10 main source folders with the main MakeHuman folder in the SVN repository:
* apps
* core
* data
* docs
* icons
* lib
* licences
* plugin
* shared
Of these, two folders: (licenses and docs)  are associated with the general housekeeping and installation aspects of MakeHuman.  Details of the housekeeping  folders will be summarized, where relevant, elsewhere in the documentation.  The remaining folder are discussed below.
 
Directory Structure and the Build System
During the pyinstaller build process, only files in the makehuman/data/ directory are included as data files, which means that any other data files will be skipped, causing file not found errors. Thus, the developer should place all data files under the data/ folder. The idea is to be able to cleanly identify what is data to be loaded at run time.and what is code that can be compiled at build time. One exception here is target (data) files that can optionally be precompiled to binary files at build time even though their binaries will reside in the data/ directory. The rational for this is that target files are static data core assets and should therefore naturally reside in makehuman/data/, but by compiling target files at build time, the size of the build distribution can be reduced and program startup times can be minimized
The files in makehuman/plugins/ form a second exception to data is "loaded at runtime" and code is "comiled at build time". Files in the makehuman/plugins/ folder are kept as a "side effect" of the fact that the makehuman/plugins/ path is included as data. It is included as data to make it possible to load plugins at runtime by inspecting the folder. Plugins are compiled as well, though. This does not mean that data may be stored in makehuman/plugins/ as this practice threatens logical organization of code and data, and it is not guaranteed that this will keep working in the future.
Plugins should never be used as imported modules in other plugins or, even worse, in a core module. Currently, the core plugins of MakeHuman all start with a digit (e.g., import 9_export_mhx). This is done intentionally to prevent their improper import into other modules in the program because imports of a module starting with a digit will produce a syntax error. Core plugins that require data, for example those related to .mhx export, should make use of a subfolder in the makehuman/data/ path (makehuman/data/mhx/).
Third-party plugins might have slightly greater lattitude about including data than core assets, but the clean separation of code and data is strongly encouraged.  Therefore, third-party plugin developers should place data in makehuman/plugins/pluginName/data to make it easily identifiable.
makehuman/data/ folder
Most operating systems set aside separate storage space for code and data, and programs can generally not write data to their own directory structure.  In addition, most OS support the notion of multiuser login, and support separate writable data areas for each user to customize.  MakeHuman includes some "fixed data assets" that are intrinsic to the program.  These data assets are save in the programs data folder within the program itself.  However, MakeHuman also makes provision for third-party and user developed assets like additional clothes, additional hairstyles, etc.  These latter assets are not saved in the program area but rather are save in user writable areas under the path  userhome/makehuman/. For example, on Windows 7 systems this would be "Docuements/makehuman".   In populating asset lists, the library holdings are generated based on the fact that syspath/data/itemtype and userhome/data/itemtype can coexist.
Themakehuman/data/ folderdoes not contain any codeper se. As its name implies this folder contains the basic data resources that ship with MakeHuman.  Often, during the development and building of MakeHuman, a given resource may exist in multiple formats.  Many if not most resources initially exist as “text-based” files which are stored in the data directory with an appropriate extension (see section of file extensions).  When MakeHuman is built for distribution on supported platforms, these text-based data resources are compressed into .npy format to produce a smaller and more rapidly loading distribution package.  Typically, the original text-based data files do not ship with standard, downloadable installation builds but instead, the corresponding compressed versions are distributed.
The data folder contains many subfolders which correspond to unique data assets.  The details of these assets will not be discussed here, but the reader can get a general idea of asset types just by reviewing the folder names.
3dobjs, animations, bvhs, expressions, eyebrows, eyes, genitals, hair, icons, languages, litspheres, materials, mhx, poses, povray, proxymeshes, rigs, scenes, shaders, skins, targets, textures, themes, uvs, vertesgroups, visemes.
Many of these data subfolders have subfolders themselves, but generally, this organization is easily discovered just by looking.
Four of the data subfolders (eyes, hair, and clothes) are directed at important geometry assets of the MakeHuman model.  MakeHuman supplies a special tool that lets developers or even end-users design additional assets using the 3D modeling program Blender.  The name for this tool isMakeClotheseven though it supports the development of the other geometries as well.
 

=### /makehuman/apps/

* catmull_clark_subdivision.py- an implementation of the!LINK!http://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface -- catmull clark subdivision algorithm.!/LINK!
* devtests.py- testing and development use only, and can safely be ignored.
* human.py- contains the Human class, which is the core data structure for MakeHuman model.
* humanmodifier.py- contains the functions and classes that link the GUI sliders to their respective effects on the MakeHuman mesh.
* metadataengine.py- implements algorithms to handle MakeHuman metadata tags within large files.  It makes it possible to quickly and easily associate descriptive adjectives (tags) such as "eye" or "brown" with the complete file path to an object that has these characteristics.
* mh2proxy.py- (unknown)
* posemode.py- contains classes and functions relevant to entering and exiting posemode, and altering a figure's pose. Changing the pose of a figure will deform the mesh and require the vertex warps to be reset.
* warpmodifier.py- contains classes and functions to handle the source and target of a warp.
* which.py- checks to see whether or not a program exists (needed for the GUI controls).

=### /makehuman/core/

* algos3d.py- contains algorithms used to perform high-level 3D transformations on the 3D mesh that is used to represent the human figure in the MakeHuman application.
* aljabr.py- contains the most common 3D algebraic operations used in MakeHuman including vector, matrix, quaternion, and various other operations.
* animation3d.py- contains functions and classes to animate a wide range of objects. Includes support for rotation, scaling, translation, camera movement, and variety of interpolation methods.
* compat.py- (Unknown)
* download.py- contains classes and functions to download media from the web and import it into MakeHuman.
* events3d.py- contains classes to allow an object to handle events resulting from keyboard or mouse input, window resizing, and changes to the human model with MakeHuman.
* export.py- (Not fully implemented) contains classes to export the MakeHuman model.
* files3d.py- contains functions to convert other 3D file formats to and from the internal format used by MakeHuman.
* geometry3d.py- contains classes for commonly used 2D and 3d objects such as rectangles, cubes, and flat meshes.
* gui3d.py- contains classes defined to implement widgets that provide utility functions to the graphical user interface.
* mhmain.py- contains the operations and event handlers that provide the core functionality of MakeHuman.
* module3d.py- contains classes and functions to handle the appearance and behavior of 3D objects such as shading, texturing, visibility, transparency, and creating groups of faces.
* selection3d.py- contains classes and functions that allow users to select elements within a 3D scene by clicking on them with the mouse using a technique called "!LINK!http://www.opengl.org/archives/resources/faq/technical/selection.htm -- Selection Using Unique Color ID's!/LINK!"
* textures3d.py- contains functions to perform standard proccesses on bitmaps and translate UV coordinates to a pixel index in a bitmap.
* transformations.py- A library for calculating 4x4 matrices for translating, rotating, reflecting, scaling, shearing, projecting, orthogonalizing, and superimposing arrays of 3D homogeneous coordinates as well as for converting between rotation matrices, Euler angles, and quaternions. Also includes an Arcball control object and functions to decompose transformation matrices.
* warp.py- contains classes and functions to warp vertex locations from a source character to a target character. This makes it possible to correctly combine several morphs that affect overlapping regions of the body.

=### /makehuman/lib/

* camera.py -handles camera events such as changing focus, camera mode, and field of view.
* core.py -sets default global variables
* debugdump.py -handles creating a debug text file in the user's home directory and writing relevant debug information to that file.
* filechooser.py- a Qt based filechooser widget that allows the user to preview and select files as well as sort them by name, creation date, modification date, and size.
* getpath.py- Utility module for finding the user's home path.
* glmodule.py- contains classes and functions to render 3D objects with openGL in both draw mode and pick mode.
* gui.py -alias from gui.py to qtgui.py
* image.py- handles flipping and resizing images as well as converting between RGB, ARGB, and greyscale.
* imageqt.py- handles loading and saving RGB and ARGB images.
* inifile.py- contains functions for formatting and parsing .ini files.
* language.py- handles language file loading and translation.
* log.py- extends the functionality of Python's logging module. The logging module can be used to create log files of events for debugging, or to display information or warnings within MakeHuman. It is used instead of print statements.
* matrix.py- uses the NumPy package to define standard matrix operations.
* mh.py- Python compatibility layer that replaces the old C functions of MakeHuman.
* object3d.py- defines the object3d class
* profiler.py- defines functions to handle profiling (how long various parts of the program executed).
 


### File formats and extensions
This section briefly reviews the file accessed or manipulated within MakeHuman.  An attempt will be made to explain the function of each file format and where in MakeHuman’s modules it is used.  Or external formats links will be provided to more detailed descriptions.  Where it can help the developer better understand the overall organization of MakeHuman source code, some information on the module group or modules interaction with the various formats will be provided.  This section Is intended to be used with the previous section on directories (folders) to develop an overview of MakeHuman code structure.  This structural understanding is essential during the debugging process and is essential to expanding the programs functionality in structurally sound ways.

=### .obj files

This extension designates Lightwave object files. These OBJ files store mesh information and metadata needed for rendering in text-readable format. It was originally developed for the Lightwave 3D graphics program, but this file format is now broadly supported by many, if not most, 3D programs.  Internally, MakeHuman uses OBJ files (or formats directly based on OBJ files) for the canonical storage of its assets. Many of MakeHuman’s development utilities store newly generated assets in formats related to the Lightwave OBJ specification.  Examples of assets canonically stored in Lightwave OBJ format include the base human, and auxiliary geometry assets like eyes, hair, and clothes.
Each OBJ file has a record specifying the object’s name and records specifying one or more mesh objects.   Mesh objects, in turn, are composed of record groups specifying: points or vertices (v), vertex normal (vn), faces (f), and vertex textures (vt). In MakeHuman and most general purpose 3D programs (e.g., Blender) OBJ files are exported with an accompanying Wavefront material file having the .mtl extension. These MTL files provide the detailed material attributes necessary to get photorealistic rendering of Wavefront objects.  A more complete specification of Wavefront object format can be found at:!LINK!http://www.martinreddy.net/gfx/3d/OBJ.spec -- http://www.martinreddy.net/gfx/3d/OBJ.spec!/LINK!
OBJ files and MTL files have a direct internal analog in MakeHuman in the form of the object class, Object3D.  This class, along with its properties and methods, is defined in the object3D.py module(libs folder).  Object3D objects are central to the internal workings of MakeHuman. The resemblance of Object3D objects to OBJ files is not coincidental. Many of the core mesh assets in MakeHuman are developed in the open-source project, Blender, and moved to MakeHuman internals using OBJ format.  In fact, MakeHuman maintains a separate product [MHTools] designed to support development of new core internal assets

=### .mhpxy files

This extension designates compressed binary proxies and clothes.

=### .mtl files

This extension designates a Wavefront material file. Wavefront MTL files are referenced from within Wavefront OBJ files to specify the materials used in rendering. More complete information on Wavefront material files is available here:!LINK!http://paulbourke.net/dataformats/mtl/ -- http://paulbourke.net/dataformats/mtl/!/LINK!
MakeHuman’s use of MTL file has been limited, but with the increased support for POV rendering, more modules may access and utilize MTL files. Currently, MTL-related data and files is developmental.  Thedata foldercontains a cube.obj (3dobj) and a plane.obj (mitsuba folder) ostensibly associated with materials. 

=### .npz files

This extension designates compressed binary asset files in MakeHuman [think npz = numPy zip files]. Among the most important assets stored with this extension is target vertex information.  These target data determine the motion of each MakeHuman vertices (relative to landmark vertices?) as sliders are moved.
Thefiles3D.pymodule (core folder) tests for verifies existence of OS dependent locations of binary mesh files. The primary purpose of thefiles3D.pymodule is to transpose imported 3D data into a standard internal format for each of the 3D file formats supported by the MakeHuman import. Each importer function is written to return the 3d data in a standard format as a Python list:
 [verts, vertsSharedFaces, vertsUV, faceGroups, faceGroupsNames]
Thetargets.pymodule (lib folder) is where system assets stored with the NPZ extension are identified, decompressed, and turned into memory resident structured objects for use by MakeHuman.  This
Code related to NPZ files can also be found inalgos3d.pymodule (core folder).  This module has been part of MakeHuman for a long time, and is used for morphing related operations.  It works with loaded binary translation vectors and applies those translations to morphing targets. It may have some legacy capability to work directly with text-based .target files.
Thecompile_models.pymodule (lib folder) takes all object mesh files (.obj) and compiles them into binary compressed files (NPZ). Similarly, thecompile_targets.pymodule (lib folder) compiles target files (.target) into binary compressed (NPZ) files.  The latter module is referenced by Benjamin Lau inMakeHuman.specfile, likely for build purposes.
Important concept.  The root folder of MakeHuman contains a batch file calledcleanpz.bat(for Windows) and a corresponding shell script file calledcleanpz.sh(for Linux) whose function is to delete NPZ files between SVN builds. This “garbage collection” assures that each build is not working with out-of-date assets.  It also reminds the developer that most of the canonical assets are initially constructed in text readable format. Developers write appropriate constructors to recompile NPZ files during the MakeHuman startup sequence when missing.  For distribution versions of MakeHuman, pre-compiled assets in the form of NPZ files are distributed as stable assets. When start up code confirms their existence , no recompile is done, producing a better start-up experience for the user. This design greatly increases boot and runtime performance for stable distributions without hampering rapid testing of SVN versions in interpretative mode.

=### .thumb files

This extension designates thumbnail (image preview) files in MakeHuman. Underneath, they are actually images constructed in the .png file format. Thus, they can be edited by standard image editors like GIMP or displayed by most web browsers. The MakeHuman Save Tab code automatically generates a companion .thumb file each time it saves a .mhm file. The .thumb generation is currently done by capturing a rectangular in the center of the viewport window.  The MakeHuman Load Tab code uses .thumb images to provide previews of saved models.
The format for .thumb is defined inimage_qt.pymodule (GUI folder). Load and Save use or generation occur inguiload.pyandguisave.pymodules, respectively (lib folder).  Numerous plugin modules reference .thumb files (plugins folder) including:2_posing_expression.py,3_libraries_clothes_chooser.py,3_libraries_eye_chooser.py,3_libraries_material_chooser.py,3_libraries_polygon_hair_chooser.py,3_libraries_posing_chooser.py,3_libraries_proxy_chooser.py, 4_rendering_scene.py,7_material_editor.py,

=### .lmk files

This MH internal extension designates landmark files. [might be renamed .mhlmk for naming standard reasons.] There is one set of landmarks for the model body (and a second set of landmarks for the model head (data | landmarks folder).  These LMK files are written in text readable format.  Each line has a single integer which specifies a landmark vertex in the model geometry. Landmark vertices are used for relative (local) spatial reference during model morphing.    
Landmark files are used bywarpmodifier.py(apps folder) andwarp.py(utils | tools | warptarget folder).The landmarks in these files are used as references during the complex process of reshaping the human.

=### .mhclo files

This MH internal extension designates MakeHuman clothes files. These files define clothing vertexes and remove vertexes from the model to allow fitting of the model without skin showing through. They are created using the MakeHuman Blender toolset, specifically the MakeClothes tool.
A special empty MakeHuman clothes meta-file namedclear.mhclois is used to restore the default UV map that comes with the system.  In the lib folder, thefilechooser.pymodule has aMhcloFileLoader.Refresh()method to clear materials when the refresh button is clicked.
In the plugins folder,3_libraries_clothes_chooser.py,3_libraries_eye_chooser.py,and 3_libraries_polygon_hair_chooser.pyall access MHCLO files, but as of this writing, there are some file handling issues related to proxy clothes that means some of this code is commented out.  In the shared/export_utils folder, config.py accesses acage.mhclofile.  In the tools folder, the tool ‘MakeClothes’ accessws MHCLO files in both the  makeclothes.pyandmaterial.pymodules.  Similarly, the tool ‘MakeTarget‘ accesses MHCLO files in several of its modules:_init_.py, convert.py,import_obj.py,mt.py, andsettings.py.  Finally, two experimental tools in the utils folder, themakeface.pyandhelpers.pymodules access MCHO files.

=### .mhmat files

This extension designates MakeHuman material files.    Material files are text-readable files that share their syntax structure with Lightwave OBJ and MTL files.
In the app module group,human.pyapplies a default material andmh2proxy.pyhandles materials for proxies and may do some special material handling for MHX Blender export files. In the data folder, the MHCLO files for clothes, eyes, and hair each references an MHMAT files. In the plugins folder,7_material_editor.pyloads, edits, and saves MHMAT files.  In the shared folder,material.pyparses MHMAT files and sets material properties.  In the tools folder, there is another (independent)material.pymodule for the MakeClothes tool that writes materials to the output file while using that tool within Blender. 
### Description of the file format
The entries inside a .mhmat file are of the form:
Comments can be included in c-style line comment format, like
or in python-style line comment format, like
 
The properties of a makehuman material are numerous so that they can cover the most common needs of exporters and rendering engines, and may vary among the following.
name- The internal name of the material.
Colors- Their value can be in R G B format, like:colorProperty R G B,where R, G, B are floating point numbers between 0 and 1. They control the color of various material properties and effects. To adjust the intensity of an effect, you can simply edit its color value.
ambientColor -The ambient component of the material, which is usually added on the final color regardless of the surrounding lights.
  diffuseColor -The diffuse component of the material, which reacts to each light's relative position.
  specularColor -The color of the specular shine that is caused by the reflection of a light source on the material.
  emissiveColor- The color of the light that the material seems to emit like if it's a glowing light source.
  shininess- The sharpness of the shine spots created by the reflection of a light source on the material, which is how glossy its surface is.
  
 

=### .mhuv files

This MH internal extension designates UV map files in MakeHuman.  These text-readable files based on Lightwave OBJ syntax. They contain one or two lines of metadata and alternative UV data for the texture object to be applied to the model.
 
There does not currently appear to be a development tool for creating UV map files.  They can be created by creating and saving an OBJ file and then renaming it. However, files created in this manner should not be considered fit for the SVN or website because they contain way too much redundant information.  The OBJ files created in this manner not only contain the alternate UV set but also contain all vertices of the original mesh.

=### .mhp files

This MH internal extension designates pose files.  These files are used to store coordinates for the run and walk poses on the pose tab. The dance1 pose appears to be implemented as a pose file, but it also includes some additional .target files.  The dance1 pose is also associated wih a .bvh file whereas run and walk are not.  In A8 development there have been issues with the dance1 file behaving less well than run and walk. Hopefully, these will be long gone during subsequent development.

=### .mht files


=### This MH internal extension designates a theme (GUI color scheme) for the GUI as rendered by the  pyQt library.


=### .target files

This MH internal extension [which lacks the mh… prefix] specifies final extreme positions that can be achieved when moving the interface sliders in one direction or the other.  By definition sliders have a value of zero on the left end and 1.0 on the right end, but there is a software flag to reverse this behavior as desired.  With scripting it may be possible to exceed slider extremes, but this is currently undocumented and should not be built into production code.  There is one TARGET file for each extreme of each movement.  These files are hand-built by MakeHuman artist-developers, and they are the engine of the programs utility. Typically, rightward movement of a slider should increase size, and leftward movement of a slider should decrease size. When ‘left’ and ‘right’ are used as asset names, they should refer to the left and right body part on the model, regardless of the model’s orientation in the viewport.  When slider movement involves asymmetrical change in the x, y, and z direction, it should be programmed so that the sliders operate naturally using the default viewport view for that slider. For example, left movement of the slider need not cause deformation toward the model’s left side.  Such behavior would only be sensible if the default viewport view had the model facing the rear of the viewport (model’s back toward user).
Most MakeHuman modules use data from the TARGET files.
·        In the apps group, these modules includes: devtests.py, human.py, humanmodifier.py, posemode.py, and warpmodifier.py.
·        In the core group, these modules includes: algos3D.py which is the main program that works with .target files after they are compiled into  
·        In the apps group, these modules includes:
·        In the apps group, these modules includes:
### .proxy files
This MH internal extension designates proxy meshes.  They are structured text files.  Format and attributes include ...  TODO
.qrc file
This is a resource file need used when compiling for the MakeHuman GUI which uses the pyQt library.
### .qss file
This is the text-based file fomat used to store widgets associated with the GUI interface as rendered by the pyQt library
Appreciate help from current developers as what needs to go here.  Undoubtedly some confusion or mistakes on my part, but some of it might help orient others. -RWB
Glad to do the grunt work, but feedback on needed improvemrnt greatly appreciated :-)
---------------------------
Also in this section could possibly also loading, saving, exporting formats (but these formats should probably be addressed in context below)
The basic work done within MakeHuman is saved as a file with an .mhm extension.  The .mhm files can be loaded at the start of a new user session, and return MakeHuman to the state that it was in at the end of the previous session. 
 


### Libraries and build procedures
With each MakeHuman release, packages are created for MS Windows, Mac OS X, and Debian derivatives for linux. At present there is not an operating system independent package (although the raw repository will work on all platforms). Each platform has special considerations that are addressed by the designated mainainter for that platform.
### Dependencies
In order to run makehuman and/or build packages the following need to be installed on the system:
* Python (Python 2.7 (python 3.x will not work).!LINK!http://www.python.org/download/ -- http://www.python.org/download/!/LINK!)
* Python-numpy (!LINK!http://sourceforge.net/projects/numpy/files/NumPy/ -- http://sourceforge.net/projects/numpy/files/NumPy/!/LINK!)
* Python-opengl (!LINK!http://pyopengl.sourceforge.net/ -- http://pyopengl.sourceforge.net/!/LINK!)
* Python-qt4 (!LINK!http://www.riverbankcomputing.com/software/pyqt -- http://www.riverbankcomputing.com/software/pyqt!/LINK!)
* Python-qt4-gl (Package required by some linux distributions only)
For linux there are scripts (buildscripts/deb/install_deb_dependencies.bash and buildscripts/rpm/install_rpm_dependencies.bash) which will install all the necessary dependencies but please note that these scripts may not agree with all debian and rpm based distros so it may be worth reading the bash script contents prior to running them.
### Assets
For obvious reasons, the binary assets (characters, textures, clothes, etc..) are not stored on Mercurial repository, but in two different places:
* * Immutable single archive files of the assets of finished versions of MH are stored (disregarding patch version token) on bitbucket (!LINK!https://bitbucket.org/MakeHuman/makehuman/downloads -- https://bitbucket.org/MakeHuman/makehuman/downloads!/LINK!)
* Assets still under development are store on Tuxfamily ftp:!LINK!http://download.tuxfamily.org/makehuman/assets/ -- http://download.tuxfamily.org/makehuman/assets/!/LINK!
When a new version is released, the current ftp asset tree gets zipped and uploaded to bitbucket. In the tuxfamily asset store, the folder for that version's contents are replaced with an archive_url.txt file that points the download script to the right url.
A new folder gets created on the tuxfamily host containing the assets to be included in the next release. For a released version, assets will usually not change, unless to fix bugs (in which case the previous archive is best kept, and a new one is created alongside it with a slightly different name), and the archive_url.txt file is updated.
To download automatically the assets and place them in the correct folder on a local repository, it's sufficient to run the python script with the command:
### Other scripts
In the makehuman root, there are a few scripts which need to be run:
* cleannpz.sh (cleannpz.bat)
* cleanpyc.sh (cleanpyc.bat)
* compile_targets.py
* compile_models.py
* compile_proxies.py
Note that all these are called automatically in the correct order by the "build_prepare.py" script in "buildscripts" when running one of the pre-existing package building routines below. However, when running makehuman from a source checkout, you will need to run these scripts in the above order.
### General proceedings for making a package
On all platforms the following steps should be taken when making the package:
* Update from HG repository (!LINK!https://bitbucket.org/MakeHuman/makehuman -- https://bitbucket.org/MakeHuman/makehuman!/LINK!)
* Run the scripts in the makehuman root directory. These will for example compile target files to npz files
* Copy all that's relevant to a work directory, excluding at least *.target, the utils directory and the tools directory (strictly speaking there are more that is not necessary, but it will have a minor influence)
* Do platform-dependent stuff to the work directory
* Zip the directory into a suitable installable format for the platform.

=### Linux

### Debian
In order for makehuman to work on Debian the following dependencies are needed.
* python
* python-qt4
* python-numpy
* python-opengl
* python-qt4-gl
These can be installed by running the command below:
On Debian/derivatives (Ubuntu kubuntu etc.) the whole package building is automated through the buildDeb.py script found in the "deb" folder.
  
For Deb script see:!LINK!https://bitbucket.org/MakeHuman/makehuman/src/tip/buildscripts/deb/?at# default -- https://bitbucket.org/MakeHuman/makehuman/src/tip/buildscripts/deb/?atd...!/LINK!
  
To build a deb file, create an empty directory (for example /tmp/deb) and run:

When the script has finished, the deb file will be available in /tmp/deb/output.There are some settings in the head of the buildDeb.py script for tweaking the output.
 
### Fedora 19 64-biit RPM Packaging
These instruction have been written for and tested on Fedora 19 64-bit. You will never be able to run the MakeHuman HG version on distros such as RHEL/CentOS 6.4 or earlier, since they do not support python 2.7, not even if you enable RPMForge. The instructions may or may not work on other RPM-based distros.
* * Install a Mercurial client (Hg) and clone the!LINK!https://bitbucket.org/MakeHuman/makehuman -- Makehuman BitBucket Repository!/LINK!.
* Install required dependencies.
  As root, run the bash script for installing the required dependencies.
  buildscripts/rpm/install_rpm_dependencies.bash
  This script also installs optional but recommended dependencies. If you only want the really required  dependencies, run

* Run MakeHuman. Change working directory to the root of the makehuman tree:
  
Then run:
You will most likely want to do this as your normal desktop user, not as root.

=### Windows

* * Install an Mercurial client!LINK!http://tortoisehg.bitbucket.org/download/ -- (Tortoise HG client!/LINK!is a good choice on Windows) and clone the!LINK!https://bitbucket.org/MakeHuman/makehuman -- MakeHuman repository!/LINK!(see!LINK!http://www.makehuman.org/doc/node/development_infrastructure.html -- http://www.makehuman.org/doc/node/development_infrastructure.html!/LINK!)
* Install required dependencies
  If you are using a 64bit Windows version (only applies to 64-bit computers), you can choose to use either 32-bit python or 64-bit python. Howver it is important that your library dependencies (NumPy, PyOpenGL, and pyQT4) are 32-bit if you use 32-bit Python and 64-bit if you use 64-bit Python.
  
* Run MakeHuman.
  Start a command console (cmd.exe), change directory to the makehuman folder. Then run:


=### Mac OSX

To build MakeHuman for Mac OS X, you should:
* * Download the MakeHuman OSX Builder from: !LINK!https://bitbucket.org/MakeHuman/makehuman-osx-builder -- https://bitbucket.org/MakeHuman/makehuman-osx-builder!/LINK!
* Follow the included instructions (Instructions.rtf)
 


### Development infrastructure
The development of MakeHuman is based on two fundamental tools:
* Mercurial (HG), a stable and robust platform for distributed revision control, with the main repo hosted on!LINK!https://bitbucket.org/MakeHuman/makehuman -- Bitbucket!/LINK!
* A collaborative software!LINK!http://bugtracker.makehuman.org -- development platform!/LINK!, based on!LINK!http://www.redmine.org/ -- Redmine!/LINK!.

=### Get the code from BitBucket.

Obtain the code from BitBucket repository is very simple, but you need to have Mercurial installed on your system.
It's natively present on Linux systems, while for Microsoft Windows, a good software is TortoiseHG (!LINK!http://tortoisehg.bitbucket.org/ -- http://tortoisehg.bitbucket.org/!/LINK!).
To clone the repository to your PC, just use this command:
hg clone!LINK!https://bitbucket.org/MakeHuman/makehuman -- https://bitbucket.org/MakeHuman/makehuman!/LINK!
With tortoiseHG, you can do it visually, with:
right-click --> TortoiseHG --> clone

=### Using Redmine in MakeHuman development

Redmine is a very powerful tool.
[To expand with technical information about the roadmap organizations, the subprojects, and how to use it to accept experimental features]
 


### Development organization
 !IMAGE!Pictures/mh-hg-infographic01.png!/IMAGE! 
The Unstable branch is where the development happens. This is our working branch, and so we can refer to it as default branch too.
The Stable branch is used for official release only.
  
It's just for mainteinance of the current official version. It's rarely used, except in the case of very noticeable bugs that will cause a service release. Any bugfix in the Stable must be merged in Unstable.
When the Unstable is ready for the release, it's merged in the Stable and a tag (a sort of bookmark) is created on this exact revision.
 !IMAGE!Pictures/mh-hg-infographic02.png!/IMAGE! 
Working on experimental clone for new features in early development is a great comfort for the developer.
  
He doesn't have to keep his  code on the local drive since he  can commit it immediately.
  
It doesn't  matter if the code does not work yet or breaks the app, it is the private playground of the developer.
 !IMAGE!Pictures/mh-hg-infographic03.png!/IMAGE! 
To start up a new feature yet unproven or that is unsure how to implement it exactly, or for a big refactor that might make a lot of problems until solved, we will create experimental repos, cloning the main one. One repo for (large) feature.
 !IMAGE!Pictures/mh-hg-infographic04.png!/IMAGE! 
Once the developer has something to show, he can communicate with other team members so  they can:
* clone the experimental repo to a new folder on their local disk
* test it
* give feedback
* perhaps even commit fixes
Once a feature is proven to work  well enough and accepted by the rest of the team, it can be merged in official unstable branch, where it can be integrated in nighly build version and further finalized (it can now be tested by a broader audience and we will receive bugs reports from them)
 !IMAGE!Pictures/mh-hg-infographic05.png!/IMAGE! 
It is also possible that an external programmer, without commit rights on the official repo, make changes on his own personal clone (that he can make public on his own account if he desires).
  
This is a good way to test new team members, where we can accept changes after verifying them. When we trust a new developer, we can give him direct access to official repo.


### Getting started
The best way to start your experiments with MakeHuman code is to clone our official repository and start to modify it.
  
In order to procced easily. it is recommended you use the tools available at!LINK!https://bitbucket.org -- https://bitbucket.org!/LINK!.
The general procedure is:
* Go to!LINK!https://bitbucket.org -- https://bitbucket.org!/LINK!and sign up (if you don't already have an account)
* Go to !LINK!https://bitbucket.org/MakeHuman/makehuman -- https://bitbucket.org/MakeHuman/makehuman!/LINK!
* Click "fork" (it's hidden under "..." in the button menu)
 !IMAGE!Pictures/fork.jpg!/IMAGE! 
* Enter a name and description of your choice (the fork will end up on your account, so it doesn't matter what you call it). Use "fork at tip" and don't check "this is a private repository"
* You should be redirected to the new repository on bitbucket
* clone your new repository to your local harddrive (if you need a primer on how to clone or use bitbucket,!LINK!https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+201+Bitbucket+with+Git+and+Mercurial -- see their tutorial!/LINK!)
* Make your code changes locally. Do not make a feature branch, work directly on the default branch.
* Commit and push the changes to your repository on bitbucket
* Go to your repository on bitbucket and click "pull request" (in the button menu at the top right of the page)
* Write a good description for what your changes concern and click "create pull request"
Once you have done this, the makehuman team will get a notification that there is an incoming code changes. This will be reviewed and either merged or rejected. 
If you want to continue working with updates in the future, make sure your fork is up to date with changes in the makehuman repository. Go to your repository, click the "..." button in the button menu and choose "compare", click the compare button on the page you get to. Merge any incoming changes.
If your tree is hopelessly out of sync with the makehuman tree, just delete it and make a new fork. Better that than accidentally getting junk in your pull requests.
Before starting with any of the above, you might want to read up on how to run makehuman from a source checkout rather than from a binary download. The short story is that you need to install a few dependencies. More information can be found here:!LINK!http://www.makehuman.org/doc/node/libraries_and_build_procedures.html -- http://www.makehuman.org/doc/node/libraries_and_build_procedures.html!/LINK!


### Application design and Code overview

=### Structural Organization of MakeHuman

MakeHuman is organized hierarchically.  There is a root application (type gui3d.Application) that handles rendering of objects (guicommon.Object). These objects can be added/removed to/from the root application.  Objects added to root application are always visible in the canvas.[I'm wondering if this is really true? - There are object on hidden tabs and the skeleton or mesh can be visible or not.  Am I confusing the distinction between 'canvass' and 'view'? - RWB]  Every added object has an openGL counterpart.
mhmain.MHApplication inherits from root application to constructmain application. A view is a visual context. A tab is a view, for example, the main application is a view.[The main application IS a view or the main application HAS a view? "the "main application frame/window is a view?"- RWB]
The Root application[you do meanrootand notmain? - RWB]contains Categories. A Category (gui3d.Category) is a specialised view object which contains multple taskiew objects (gui3d.TaskView).   Taskview objects are specialised view objects with a panes and tab.  In context of MakeHuman interface, Category objects constitute the  upper row of tabs while taskview objects constitute the lower row of tabs. 
Objects (guicommon.Object) can be added/removed to/from a taskview.  Objects added to a taskview are only visible if the taskview is visible.  For example, a skeleton added to the skeleton chooser is only visible  when the skeleton chooser taskview is visible.  Objects added to root application[root not main? - RWB]are always visible.  Thus objects like human and all proxies such as clothes are added to theapplication,because they should always be visible. Visiblilty can be disabled by setting the visibility flag on objects but an object that is not added to a currently visible taskview, or the application, is not visible, even if its visibility flag is set positive. [Wording needs improving -- 'should always be visible' and a 'visibility flag' are mixed message - RWB]
An object can only be added to one context. So an object is either added to one taskview, or the application, not two different taskviews.
Apart from root application, there is another application (type qtui.Application) which implements MH gui structures using Qtlibraries. mhmain.MHApplication inherits from this application too for handling of gui content.e 
General structure in MH can be represented as: !IMAGE!Pictures/mh-inheritance.png!/IMAGE! 

###  
Basics of event handling in Makehuman: ### 

Makehuman is a GUI based, interactive, Qt application in which objects interact by sending messages to each other. The Qt class QEvent encapsulates notion of low level events like mouse events, key press events, action events, etc. A Qt application is event loop-based, which is basically a program structure which allows events to be prioritized, queued and dispatched to application objects.   
In a Qt based application, there are different sources of events. Some events like key events and mouse events come from window system, while some others originate from within application. When an event occurs, Qt creates an event object to represent it by constructing an instance of the appropriate QEvent subclass, and delivers it to a particular instance of QObject (or one of its subclasses) by calling its event() function. This function does not handle the event itself, but rather, it calls an event handlerbased on the type of event delivered, and sends an acknowlegement based on whether the event was accepted or ignored.
QCoreApplication::exec()method enters the main event loop and waits until exit() is called. It is necessary to call this function to start event handling. In MH, it is done in lib.qtui.Applicationwhich inherits fromQApplicationwhich in turn inherits fromQCoreApplication:
def start(self):
  
        self.OnInit()
  
        self.callAsync(self.started)
  
        self.messages.start()
  
        self.exec_()
  
    
  
In MH, event handling falls in two broad categories.
* Event handling forcontainers(application, categories, taskviews)
* Event handling forwidgets(contained in containers)

=### Event handling for containers:

MH is organized hierarchically in the context of containers.  At top is the main application (core.mhmain.MHMainApplication).  It contains categories (core.gui.Category), which in turn contains taskviews (core.gui.TaskView).
In a Qt-based application, there are five different ways of events processing, as listed below:
* * Reimplementing an event handler function like paintEvent(), mousePressEvent() and so on. This is the most common, easiest, but least powerful approach.
* ReimplementingQCoreApplication::notify( QObject * receiver, QEvent * event ).  This is very powerful, providing complete control; but only one subclass can be active at a time.  Qt's event loop and sendEvent() calls use this approach to dispatch events.
* Installing an event filter onQCoreApplication::instance().  Such an event filter is able to process all events for all widgets.  It's just as powerful as reimplementing notify(); furthermore, it's possible to have more than one application-global event filter. Global event filters even see mouse events for disabled widgets. Note that application event filters are only called for objects that live in the main thread.[I believe that MH is single threaded - implications?  RWB]
* ReimplementingQObject::event()(as QWidget does). If you do this you get Tab key presses[<--Explain what is special about TAB and shift-TAB presses ?- RWB], and you get to see the events before any widget-specific event filters.
* Installing an event filter on the object itself.  Such an event filter gets all the events, including Tab and Shift+Tab key press events[<--Explain what is special about TAB and shift-TAB presses ?- RWB], as long as they do not change the focus widget.
In MakeHuman, approaches 2 and 4  are used for extensively for event handling.  As part of strategy 2,inlib.qtui.Application (which extendsQApplication), notify has been reimplemented:[I don''t understand the implication of this? Expond? -RWB]
def notify(self, object, event):
  
        self.logger_event.debug('notify(%s, %s(%s))', object, event, event.type())
  
        return super(Application, self).notify(object, event)
  
        
  
object is the receiver object. Class implementing notify has to be singleton.  [Clarify? - RWB]
In MakeHuman,MHApplicationsubclasseslib.qtui.Application.MHApplicationobject is the main application object. It's notify function receives notification from the event loop in the underlying Qt layer about each[container only or widgets too?]event, which is then relayed to receiver object's event method. Thereceiver object's event method is either inherited from QObject or reimplemented. The Receiver object then either sends TRUE or FALSE, as the case may be, to[WHERE??] - RWB
lib.qtui.Applicationalso implements an event function, which is called if the receiver object isMHApplication objectitself.  Then,lib.qtui.Application.event()checks if its a user-defined event or not,and it is so true is returned, else we call super class's event().   In case of true being returned,Qt dispatches event to receiver object's callEvent function which determines which function to be called on object to handle the event. Called function then handles the event or propagate it to its parent(or to current task if its application object), as may seem fit.

=### Event handling for widgets

Most of MH widgets are wrappers around Qt widgets. These widgets (defined in module lib.qtgui) inherit from the respective Qt widgets and the Widget class (lib.qtgui.Widget).  MH makes use ofsignal and slot mechanismby making the connection between the signal originating from the Qt layer and the corresponding handler function. For example, class TabBase connects the signal 'currentChanged' to its function 'tabChanged' as follows:
class TabsBase(Widget):
  
    def __init__(self):
  
        super(TabsBase, self).__init__()
  
        self.tabBar().setExpanding(False)
  
        self.connect(self, QtCore.SIGNAL('currentChanged(int)'), self.tabChanged)
  
        ......................
  
        
  
Any class inheriting from TabsBase(e.g., lib.qtgui.Tabs or lib.qtgui.TabBar) also gets this facility.  So now whenever signal 'currentChanged' is emitted from Qt layer function 'tabChanged' is called. The result is that when a user clicks the mouse on a tab, the 'tabChanged' code  will be called,
Similarly, MH Slider widget connects various slider operations to its event handling functions as:
  
...........................
  
    self.connect(self.slider, QtCore.SIGNAL('sliderMoved(int)'), self._changing)
  
    self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self._changed)
  
    self.connect(self.slider, QtCore.SIGNAL('sliderReleased()'), self._released)
  
    self.connect(self.slider, QtCore.SIGNAL('sliderPressed()'), self._pressed)
  
...........................      
[-- EDITING/PROOFING ENDS HERE - RWB --]
 
 

=### Overriding vs event decorators:

The View, Category and Application classes inherit from events3d.EventHandler, hence they have callEvent() function.  The events that apply to this category are usually application-wide. If user make a change that impacts the whole application, and whole application must know about this change, then best way to do so is to call callEvent() for all the taskviews of the application,as follows:
for category in self.categories.itervalues():
  
    for task in category.tasks:
  
        task.callEvent('onMyEvent', params)
A good example is the event of makehuman's scene changing(core.qtui.MHApplication._sceneChanged).  So when callEvent is called on a taskview object and it has onMyEvent implemented,it is being called.  In core.gui3d.View too one can see that most of the events (onShow, onMouseDown,...) on the taskview are propagated by default to their parents - the categories. The categories also are views, so the events are propagated again to their parent, the application. If, again, the application or any category has an onMyEvent method, it is executed.
There are some events that affect the application, but only a single task at a time,for example onMouseDown event. It only happens to the active taskview
  
(the others are hidden, so they receive no mouse events). Once the mouse is pressed, an Application.currentTask.callEvent("onMouseDown", event)is issued. This causes the onMouseDown event to be received by the active Taskview, its parent Category, and finally the Application. This call executes any onMouseDown method in these objects.
Apart from the Category events described above, there are events used for local purposes.  Such events are handled withevent decorators.  Suppose we have a new Taskview, FooTaskView. This Taskview has a 'mybar' member variable, which is of type Bar(events3d.eventHandler).  The requirement is that when self.mybar executes code, we may want to communicate with its parent to inform it about an event that just happened. So, inside the code for Bar, is located a 'self.callEvent('onBaz', 42)' command.  Thus, in the Bar class, we emit a timely event signal and use the event decorator to let the parent Taskview know about the event.  In the  FooTaskView class, but below the place where self.mybar is created, we add:
@self.mybar.mhEvent
  
def onBaz(event):
  
    # code on event.
  
    # guess what, event #  42.
When now the self.mybar Bar reaches that callEvent, the above method, located in FooTaskView, will be executed.
core.mhmain.MHApplication's human is perfect example of this approach.Human has onMouseDown event handler and we need to relay it to application.
  
In loadMainGui function of MHApplication, we add decorator to human attribute as:
def loadMainGui(self):
  
        ..............
  
        
  
        @self.selectedHuman.mhEvent
  
        def onMouseDown(event):
  
          if self.tool:
  
            self.selectedGroup = self.getSelectedFaceGroup()
  
            self.tool.callEvent("onMouseDown", event)
  
          else:
  
            self.currentTask.callEvent("onMouseDown", event)
  
        .............    

Application.human.onMouseDown event is caught and it starts its trip from the Human; it is captured by the decorated method located in Application.loadMainGui (this is the place where the method is bound with the event), it is sent to the currentTask, propagated through the parent category, and finally reaches its destination, the Application.
A more intense process happens on Human.onChanged. This is emitted when a save/load happpens, so the whole application has to know. So it starts from the human, captured by the decorated method in app, sent to ALL the taskviews in MH, and finally through the categories again to the app.
 

=### The MakeHuman Graphical User Interface (GUI):

The MakeHuman GUI is based on the pyQt library which, in turn, is built on the Qt library.   Qt is a development framework for the creation of applications and user interfaces for desktop.
Important GUI classes in MakeHuman are:
lib.qtui.Canvas:This is the class in MakeHuman which takes care of rendering openGL graphics.It inherits from Qt's QGLWidget class which is a widget for rendering OpenGL graphics.  QGLWidget provides functionality for displaying OpenGL graphics integrated into a Qt application. It is very simple to use. You inherit from it and use the subclass like any other QWidget, except that you have the choice between using QPainter and standard OpenGL rendering commands.  
The Canvas class reimplements three functions from parent class to perform openGL tasks:
* paintGL() - Renders the OpenGL scene. It gets called whenever the widget needs to be updated.
* resizeGL() - Sets up the OpenGL viewport, projection, etc. Gets called whenever the widget has been resized (and also when it is shown for the first time because all newly created widgets get a resize event automatically).
* initializeGL() - Sets up the OpenGL rendering context, defines display lists, etc. Gets called once before the first timeresizeGL() orpaintGL() is called.
lib.qtui.Application:  This is the foundation class which manages GUI's control flow and main settings. It inherits fromQtGui.QApplicationandevents3d.EventHandler.  QApplicationcontains the main event loop, where all events from the window system and other sources are processed and dispatched. It also handles the application's initialization and finalization.Application class holds gui main window(instance of lib.qtui.Frame). Application class receives event notifications from underlying Qt user intrface framework and dispatches them to appropriateuser intrface elements in MakeHuman.
GUI architecture inMakeHumanMH can be depicted as follows:
 !IMAGE!Pictures/mh-uiarchitecture.png!/IMAGE! 


### Application Design Notes from IRC Chat with Thanassis
Thanasis comments on gaining the big picture of MH coding
* [16:12:57] <Thanasis> I would avoid describing the different parts of code as different entities
* [16:13:43] <Thanasis> ie. follow the object-oriented paradigm, and avoid thinking who is inherited by who etc.
* [16:13:48] <Thanasis> more specifically
* [16:15:03] <Thanasis> I mean, treat an object as a single object
* [16:15:08] <Thanasis> I'll show an example
* [16:15:45] <Thanasis> you have the application. Inheritance says it consists of three classes, QApplication, MHApplication, and mhmain.Application (names may differ a bit).
* [16:15:58] <Thanasis> but it is only one object
* [16:16:42] <Thanasis> We don't care if the QApplication activates a function in MH application, because it happens inside the same object
* [16:16:50] <Thanasis> the application
* [16:17:18] <Thanasis> we only pay attention to the interactions the application object has with other objects
* [16:17:43] <Doctor_Hell_> but if you need to find a function, you need to follow the inheritage chain...no?
* [16:18:24] <Thanasis> of course, in the code, yes. but in a diagram it will make it complex
* [16:21:02] <Thanasis> well, let's go top-down
* [16:21:29] <Thanasis> we have: QT, App, Tab, Task
* [16:21:56] <Thanasis> The event starts from QT, and activates a handler in App
* [16:22:22] <Thanasis> The App sends a new event to the current Task
* [16:22:46] <Thanasis> The task handles it, and sends a copy to the parent Tab
* [16:23:13] <Thanasis> And finally the Tab handles it and sends a copy to the App
* [16:23:35] <Thanasis> which handles it, and stops
* [Referring to how distrating it is to describe the big picture of MH, Thanasis comments ...]
* "Distract? no, this does not consume any brain energy"
* We love your help- the more the bettter -- Thanks [RWB]

Comments Regarding MacroTarget slider processing/handling based on naming conventions:
* [16:36:24] <Doctor_Hell_> [23:26] <Doctor_Hell_> another complex part to know is the engine coded by Jonas to automatically handel the targets using their name
* [16:37:58] <Thanasis> uh. yes, that's a tough one too. I think it does, but I don't remember why and how, because it was a long time ago and Jonas changed the human modifier class since then
* [16:38:18] <Thanasis> he simplified it, actually, but I haven't seen the new version yet
* [16:38:34] <Doctor_Hell_> where is the code?
* [16:38:49] <Thanasis> apps/humanmodifier.py, I think
* [16:39:01] <Doctor_Hell_> Jonas should be very busy recently, since I asked him but he didn't reply me yet.
* [16:42:37] <Thanasis> um by the way, reading humanmodifier alone won't help a lot. I would suggest starting from the macro plugin, to trace what happens when a slider is created, and when the user moves a slider. It might be easier this way
Difficulties in understanding relationships between folder names / module names and the object structure
* [16:39:36] <Doctor_Hell_> ANother thing to understand is why we have some code inapps, other incore, other in libs..the logic is not clear for me..
* [16:39:52] <Thanasis> ah, ignore logic in that part. :)
* [16:40:20] <Thanasis> as far as I know it is all because of mh history so far
* [16:40:29] <Thanasis> the way it developed.
* [16:40:56] <Doctor_Hell_> I know some of it
* [16:41:24] <Doctor_Hell_> in the early times,it was planned to have a core folder, with all important main files
* [16:42:03] <Doctor_Hell_> then anapps folder, to contain many application based on the core files: makeHuman, makeANime, MakeToon, etc..
* [16:42:29] <Doctor_Hell_> butsharedandlibswere added later...I don't know why
* [16:43:10] <Thanasis>libs, they are classes imported from c++ directly
* [16:43:48] <Doctor_Hell_> ah ..so only the "shared" folder is the mystery
* [16:44:04] <Thanasis> shared, they are later classes used by many different parts of the code at the same time
* [16:44:15] <Thanasis> classes created later*
* [16:44:28] <Thanasis> ie. material. It's used literally everywhere
* [16:44:32] <Thanasis> progress too
* [16:44:58] <Doctor_Hell_> ok..at least now it make sense, thank you
 
* Comments on New API project
* [16:45:39] <Doctor_Hell_> now that you have more time, will you look at the API?
* [16:46:55] <Thanasis> 'time' != 'creativity'. I expect it will be easier to me after the start of the semester
* [16:46:27] <Doctor_Hell_> if you are logged to MH site, you can see this:!LINK!http://www.makehuman.org/blog/the_makehuman_api_project_mhapi.html -- http://www.makehuman.org/blog/the_makehuman_api_project_mhapi.html!/LINK!
* [16:47:02] <Doctor_Hell_> Also Joel has already created this:!LINK!https://bitbucket.org/joepal1976/makehuman-api-project/overview -- https://bitbucket.org/joepal1976/makehuman-api-project/overview!/LINK!
* [16:48:52] <Doctor_Hell_> at the moment, you can just post a list of wished api in the issue 534
* [16:49:16] <Doctor_Hell_> we want to start the API in few weeks..they are fundamental, in order to have more contributors...
* [16:51:05] <Thanasis> oh, boy. I want to clean up this code!LINK!https://bitbucket.org/joepal1976/makehuman-api-project/commits/aa5c12953fb2c8a1723b21bb0b7d90667653d615 -- https://bitbucket.org/joepal1976/makehuman-api-project/commits/aa5c12953...!/LINK!* ​Go for it? [RWB]  :)

The Doc_Hell Diagram (green and red arrows that even Glynn couln't understand)
                    [Summary - concentrate on green arrows not red arrows to get the big picture]
* <Doctor_Hell_> this is an example of bad diagram:!LINK!https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl# 0 -- https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl0!/LINK!
* [16:52:48] <Thanasis> well, in your shape, the actual thing is about the green arrows
* [16:53:19] <Thanasis> the red arrows could have been implemented in hundreds of different ways
* [16:53:44] <Thanasis> but the important is their result, the green arrows
* [16:53:53] <Doctor_Hell_> talking about how to draw the objects?
* [16:54:26] <Thanasis> well, my idea was, do two shapes
* [16:54:36] <Thanasis> the first without code
* [16:55:10] <Thanasis> only showing the 5 steps like I explained above, ie, the green arrows
* [16:55:28] <Thanasis> the second can explain each step in detail using the red arrows
* [16:55:50] <Thanasis> but in any case the definition is the following
* [16:56:04] <Thanasis> an event is, you send the name of a method to someone
* [16:56:14] <Doctor_Hell_> ok...but also we have the description written by Manish. I'll show you it tomorrow
* [16:56:21] <Thanasis> and that someone executes that method of theirs
* [16:56:47] <Thanasis> sure, there are many ways to describe it
* [16:57:00] <Doctor_Hell_> I hope we can find the best one
* [16:57:07] <Thanasis> I think that they all match though in some certain key points
* [16:57:52] <Thanasis> if these are filtered out, the explanation may be more simple
And touching on API ideas ...
* [16:59:09] <Doctor_Hell_> since the core is too complex for average python programmers
* [16:59:36] <Thanasis> yes... perhaps the code could be organized in tiers.
* [17:00:00] <Thanasis> core, classes, plugins, scripts
* [17:00:27] <Doctor_Hell_> ah you are talking of the current code, not the simplified api
* [17:00:54] <Doctor_Hell_> yes, it's a good idea..but what group under "core" ?
* [17:01:25] <Thanasis> theapplication and its interfaces(ie.communication with the system and devices. QT, GL etc.)
* [17:01:59] <Thanasis> classes are abstract, they use the application by calling its methods
* [17:02:35] <Thanasis> the application uses the interfaces (QT, GL.these are actually harder than the application andcould be a sepparate tier)
* [17:02:54] <Thanasis> thepluginsuse the classes to create objects
* [17:03:26] <Doctor_Hell_> I see some possible confusion because:
* [17:04:24] <Doctor_Hell_> - not all core modules are into core folder (for example qtui and qtgui are in libs)
* [17:04:49] <Doctor_Hell_> - Classes are everywhere
* [17:05:07] <Thanasis> yes, libs folder consists of both core and classes... indeed
* [17:05:23] <Thanasis> andinterfacestoo
* [17:06:51] <Thanasis> but in general, this separation exists somehow. I'm not sure how, but the past programmers instinctively created it, perhaps for better manageability
* [17:08:14] <Thanasis> ie. Human is a class, Material too, Armature (probably making name wrong again), and to function I observe that they use callbacks of Application
* [17:08:38] <Thanasis> They never use interfaces directly
* [17:09:46] <Thanasis> Even for drawing the human, it is the Application that will give the Human's object3d to OpenGL, not the Human directly
* [17:10:31] <Thanasis> and plugins use classes ie. they use the callbacks that Human, Material etc. have
* [17:11:08] <Doctor_Hell_> Do you mean abstraction classes?
* [17:13:27] <Doctor_Hell_> Thanasis: about  new API:!LINK!http://bugtracker.makehuman.org/issues/534 -- http://bugtracker.makehuman.org/issues/534!/LINK!
* [17:13:42] <Doctor_Hell_> and!LINK!http://bugtracker.makehuman.org/projects/makehuman/wiki/Abstraction_API_for_plugins -- http://bugtracker.makehuman.org/projects/makehuman/wiki/Abstraction_API_...!/LINK!
* [17:13:57] <Doctor_Hell_> Feel free to add wished api calls
 


### Q & A with Glynn Clements
Question: For an event when user clicks on a tab, Tabs class  method tabChanged is called.
  
QTabWidget documentation.There is no such method. 
  Response: 
  
The tabChanged method is defined for qtgui.TabsBase (and overridden for qtgui.Tabs).
  
Both qtgui.Tabs and qtgui.TabBar inherit from qtgui.TabsBase. 
  
Tabs inherits from both TabsBase and QTabWidget  while TabBar inherits from both TabsBase and QTabBar.
  
Both QTabWidget and QTabBar define the currentChanged signal, which is emitted  whenever the current tab changes. 
  
The TabsBase initialiser connects this signal to the tabChanged method (lib/qtgui.py:109):
  
class TabsBase(Widget):
  
def __init__(self):
  
...
  
self.connect(self, QtCore.SIGNAL('currentChanged  int)'), self.tabChanged)
  
### ## # =================================================
Question:   is it true that qtui module: low level module, that handles signals directly from QtCore,  QtGui and QtOpenGL?
  Response:
  
qtui defines the classes for the application (QApplication subclass), main window  QMainWindow subclass), drawing canvas (QGLWidget subclass), and some associated  support classes. In other words, it implements the high-level UI, or at least the aspects which are tied to Qt.
Question:   is it true that  qtgui module: low level module, that define the basic widgets of the GUI as  buttons, radiobuttons, etc..
  Response:
  
Yes; qtgui is essentially a compatibility layer between the Qt widget classes and the legacy MH GUI toolkit. The classes provide methods which more closely mimic the behaviour of original gui3d widgets. Qt events are translated to MH events3d events.
Question:   Is it true that  gui3d module: high level module, that define the principal public classes  of MakeHuman: Application, Category, TaskView and View.
  Response:
  
This is what's left of the legacy MH GUI toolkit. Before the move to Qt, everything was  a "View". Now it's just the high-level containers (Application, Category, Task) which exist as somewhere to put event handlers.
Question: What is the purpose of the module guicommon.py?  Looking at the module name, it appears to be a sort of library for the GUI functions, but it's a completely different thing.  What is it really?
  Response:
  
Object used to be part of gui3d. Its primary function is to be the base class for Human. It's the other main subclass of events3d.EventHandler (the first being gui3d.View).
  
It's not really accurate to call it a "wrapper" around Object3D (although it can have instances of both module3d.Object3D and object3d.Object3D as members).
  
One of the main differences between guicommon.Object and module3d.Object3D is that the latter is a single mesh, while the former has up to four meshes (all of type module3d.Object3D): the base (or "seed") mesh, a proxy mesh, a subdivided mesh, and a subdivided proxy mesh.
  
It [guicommon.py or guicommon.Object ??RWB] also contains an object transformation (location, rotattion, scale) [method?], and optionally a display mesh (object3d.Object3D). As a subclass of EventHandler, it [guicommon.Object ??RWB] provides mouse handlers which propagate the event to the object's view (these are overridden for the Human within MHApplication.loadMainGui).
Question:   G.app is the singular mhmain.MHApplication instance; the callEvent  method (inherited from event3d.EventHandler) will end up calling  G.app.onMouseDownCallback.  How the function callEvent end up calling G.app.onMouseDownCallback?
  Response:
  
"direction" will be either onMouseDownCallback or onMouseUpCallback.  Note the "Callback" suffix.
  
So typical event flow for clicking on the human model is:
  
G.app.mainwin.canvas.mouseUpDownEvent   ("onMouseDownCallback")
  
    [Canvas.mouseUpDownEvent]
  
G.app.callEvent("onMouseDownCallback")                [EventHandler.callEvent]
  
G.app.onMouseDownCallback()                    [gui3d.Application.onMouseDownCallback]
  
G.app.selectedHuman.callEvent('onMouseDown', event)        [EventHandler.callEvent]
  
G.app.selectedHuman.onMouseDown()
  
    [local function in MHApplication.loadMainGui]
  
G.app.currentTask.callEvent("onMouseDown", event)        [EventHandler.callEvent]
  
G.app.currentTask.onMouseDown()                    [View.onMouseDown]
  
G.app.currentCategory.callEvent("onMouseDown", event)        [EventHandler.callEvent]
  
G.app.currentCategory.onMouseDown()    
  
    [View.onMouseDown]
  
G.app.callEvent("onMouseDown", event)                [EventHandler.callEvent]
  
G.app.onMouseDown()                        [MHApplication.onMouseDown]
  
Notes: 
  
    G.app.currentTask.parent #  G.app.currentCategory
  
    G.app.currentCategory.parent #  G.app
Question: is the eventType string (also called 'direction') originated by QT?
  Response:
  
No. "direction" is just so that code which is common to both mouse press and mouse release events can go into a single method (mouseUpDownEvent) rather than duplicating it in mousePressEvent() and mouseReleaseEvent(). Those functions are identical except for the name of the event passed to callEvent.
  
Bear in mind that self.callEvent("onMouseDown", event) is almost the same as self.onMouseDown(event), except that callEvent forces a redraw after the event has been dealt with, and has some support for logging and profiling. Once you strip that away, the guts of callEvent() is just:
  
    method = getattr(self, eventType)
  
    method(event)
  
### ## # =============================================================
  Question: Can the modularization of the code can be improved? 
  Response:
  
Modularisation is already quite good. Too much of it can make the code harder to understand.
  
Currently, we try to avoid importing OpenGL or Qt modules (directly or indirectly) into modules which don't inherently depend upon them (e.g. guicommon.Object imports object3d locally in the attachMesh and detachMesh methods, so it only gets imported if you actually need to render the object).
  
TODO ACTION.  One minor point which I noticed: lib/camera.py imports glmodule solely for the queryDepth() call in convertToWorld2D (the Z coordinate is obtained by retrieving a value from the depth buffer using the X,Y coordinates). This should probably be a local import in that method, so that camera.py could be used in e.g. import/export utilities.
  
### ## # =================================================================
  Question: [Referring to DocHell's red and green diagram (!LINK!https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl# 0] -- https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl0]!/LINK!]
  Response:
  
I have no idea; I can't follow that [diagram]. It would probably help if you simply ignore CallEvent(), and treat object.callEvent('method',event) as just object.method(event).
  
The two factors which make following the flow slightly complicated are:
  
 Methods aren't always defined within the class used to create an object, but may be inherited from one of its base classes.
  
 Event handlers may be dynamically added to an object with the mhEvent method (which is usually invoked using Python's decorator syntax).  This is done for the Human object in MHApplication.loadMainGui():
  
@self.selectedHuman.mhEvent
  
def onMouseDown(event):
  
....
  
If you aren't familiar with the decorator syntax, the above is equivalent to:
  
def onMouseDown(event):
  
        ...
  
self.selectedHuman.mhEvent(onMouseDown)
  
which in turn boils down to:
  
def onMouseDown(event):
  
        ...
  
self.selectedHuman.onMouseDown = onMouseDown
  
### ## # ========================================================================
  Question: Could you provide an explanation of what a weak reference is?  How might this impact MakeHuman?
  Response:
  
[Jonas Hauquier ]  A weak reference, one that is not accounted for by the garbage collection.  Garbage collection removes objects from memory that have no pointers to  them anymore. Weakrefs are not counted among those, so if the object has only weakrefs pointing to it, and not real pointers, it will be removed anyway.   This is to make sure that object A and B that always point to each other, are not kept in memory just because they keep referencing each other (I  believe the garbage collection does not do expensive graph traversals to check what is still referenced by the active context).
  
[Glynn Clements]  Sort of. Python uses both reference-counting (which can't handle circular references) and reachability-based garbage collection (which can). If an object's reference count reaches zero, it will be finalised immediately. But an object with a non-zero reference count can still be finalised if it can be determined that it isn't reachable during a garbage-collection sweep.
  
However: the garbage collector won't attempt to finalise reference cycles if any of the objects in the cycle have a __del__ method, as it can't determine a safe order in which to execute them. Instead, it adds them to a list, accessible as gc.garbage.  Application code can inspect this list, manually finalise the objects (which should break the cycles), then remove them from the list (otherwise their presence in gc.garbage will itself constitute a reference).
  
It's possible to have the garbage collector report such cases using gc.set_debug(gc.DEBUG_UNCOLLECTABLE).
  
Only a few MH classes contain __del__ methods. These will only present a problem if the object itself is part of a cycle (i.e. contains references to "complex" objects which themselves contain references which could lead back to the original object).
  
"Leaf-node" classes such as Texture and Shader shouldn't present a problem unless their creators attach additonal references to them.  This may be an issue for e.g. qtgui.Slider and qtgui.RadioButton, as these have __del__ methods and will naturally create circular references. Use of weakref may be advised here. Similarly for queue.Thread. SceneItem in plugins/7_scene_editor.py may also be a problem.
  
### ## # ====================================================================
  Question: Could you clarify wherther the following acurately describe the use of decorators?
  
A basic decorator is a function that:
  
1) Gets a function "A" as argument
  
 2) Modifies the behavior of "A"
  
 3) Returns a "decorated" version of "A"
Response:  Correct.
Question:  Topic: Decorators and side-effects.  When is a decorator not about generating a function?   So, if the above accurately descibes a decorator, consider the code:
  
@self.selectedHuman.mhEvent
  
def onMouseDown(event):
  
This should translate:
  
onMouseDown = self.selectedHuman.mhEvent(onMouseDown)
  
One would expect that  using mhEvent as decorator, it returns a function, but instead, it returns None:
  
 def mhEvent(self, eventMethod):
  
self.attachEvent(eventMethod.__name__, eventMethod)
  
How can it be used as decorator?
  Response:
  
Because the returned "function" isn't actually used anywhere. The definition is local to loadMainGui(), which doesn't reference the functions, so the fact that e.g. onMouseDown is None within loadMainGui() doesn't matter.  The mhEvent() method is used for its side-effects, not its return value. It attaches an event to the selectedHuman.  It is equivalent to:
  
self.selectedHuman.attachEvent(onMouseDown.__name__, onMouseDown)
  
### ## # =====================================================================



## Packager's notes

Notes for packagers of Makehuman stables and nightlies.

### Packaging RPM's for Suse/Fedora using Open Build Service (OBS)
The Open Build Service is a service formerly known as the Opensuse build service. OBS allows packagers to build packages for several targets. Here a target is a particular OS version E.g. Suse 13.1, Suse 12.3, Fedora 20 , Ubuntu 14.04 and so on. OBS being a build system by itself can be hosted anywhere even on local infrastructure. For MakeHuman packages we use the OBS instance hosted by Novell at build.opensuse.org
This document will briefly outline the typical packaging workflow for Suse and Fedora. Both distributions use the RPM format and subsequently adhere to RPM's packaging rules.
   !IMAGE!Pictures/obs-flow-chart-scaled.png!/IMAGE! 
### 1) Prepare source tarball:
OBS does not allow pulling from the internet once the rpm is being processed into a package so. When creating the source tarball you should assemble it either on your own computer or a server online (even a VPS will do).
There are several Important files and scripts which are of interest to us. One is build_prepare.py this assembles the main folder and all the common data which is needed by all OSes be it Mac or LInux distros or windows. This script is essential to run. Then there is build_rpm.py. We borrow some of the initial code in this and use it on our bash script but we do not build the whole RPM because OBS does that. Another third inportant file is build.conf (this stores the configuration used by build_prepare.py to make the source tarball). Using the above scripts/files I prepared a Bash script which is shown below.
The above script assumes the following:
* You have cloned MakeHuman's Mercurial (Hg) repo into your home directory and it is located at ~/makehuman (cloning into ~/ automatically makes the makehuman folder)
* You have python , numpy and pyQt4 installed (package names may vary from distribution to distribution)
* You are running on a LInux distribution.
* You want to prepare a source tarball from Hg tags.
* $VERS is the latest user specified stable tagged version
* makehuman-$VERS is your destination folder where all files are copied
* the final tarball uses bzip compression. How the tarball is compressed is significant as RPM accepts only certain compression algorithms. The resultant file is makehuman-$VERS.tar.bz2 (E.g. makehuman-1.0.2.tar.bz2)
* You use an FTP server whose file path is located at /var/ftp you can skip this step if the script is run locally by commenting the lines out.
​Explanation of the above script:
In the first section we use Hg and extract available tags and ask the user for input on which stable tag he/she wants to build against.
In the second section we automatically create the build.conf file which is used to specify if we want a release or development folder. Here we set isRelease=True
In the third section we use build.conf along with build_prepare.py this creates a basic non-OS specific folder in home (~/).
In the fourth section we copy extra files such as the .desktop file and the makehuman icon file, the shell wrapper for MakeHuman and remove the .bat file which is not needed in linux. Currently there is a bug where command line arguments are not passed by the shell wrapper to the python executable. We fix this by manually editing the file automatically in our bash script before copying it into the target folder to be tarballed. This is moved into the folder created earlier by build_prepare.py . With this we now have have a folder with all the basic requirements needed for packaging.
FInally the folder is then tarballed and it is ready for upload to OBS. If you are not using an FTP server then comment out the “mv” command which moves the tarball to /var/ftp in the shell script above. IN some distributions the FTP directory is /srv/ftp
### 2) Upload the tarball to OBS
The next step is to upload the tarball to OBS. Firstly you need to create a username and password. Then login to build.opensuse.org and create a project. On account creation you get your own home directory.
Two interfaces exist to OBS. One is the command-line interface which is available by installing the package "osc" it is available in most distributions. The other one is the Web User interface. Both are equally useful the command line interface is better for doing certain tasks however.
OBS also has a feature called “ services”. Several services are available such as services to pull from various sources e.g. FTP servers online, services to tarball the version controlled sources directly (tar_scm). You can make use of these _services (they are defined using XML notation in "_service" files). Read!LINK!”http://en.opensuse.org/openSUSE:Build_Service_Concept_SourceService” -- Source Services!/LINK!; or you can manually upload your tarball through the Web UI or use the "osc" command line utility. To learn how to use the "osc" utility use "man osc" or view the manpage online.
I would not recommend using _service files to pull the tarball as they can stop working. It is better to manually push the tarball to OBS. Either by pressing the upload button on the Web UI or placing the tarball in your project home directory created by using the “osc checkout” command. Then typing “osc ar” (add /remove) and finally “ osc commit -m ”put commit description here” “ to push and commit the changes you just made.
You can also automate the above process by adding lines to the shell script but It is better to administer osc separately and manually to allow for more control.
### 3) Prepare the spec file:
A .spec file is a special file which is used to build RPM's. It “contains information required by RPM to build the package, as well as instructions telling RPM to build it. The spec file also dictates exactly what files are a part of the package, and where they should be installed. The RPM specification is very well defined and it is fundamental than any packager develop a strong base in the fundamentals.” (taken from “Maximum RPM”)
A very important book detailing the various capabilities of RPM is!LINK!”http://www.rpm.org/max-rpm/” -- Maximum RPM!/LINK!. This is a must read for any packager and will help in understanding the spec file shown below. If you have not read it please bookmark the page and give the book a read. I cannot stress how important it is.
In OBS we have 2 main OS's which use RPM's as build targets Fedora and Suse. RPM provides macros to make packaging more standardised and easy. Most Macros are common however some are distribution specific. Below is the spec file used by the Makehuman project. For version 1.0.2.
The above .spec file follows the general structure and format of spec files as per the RPM specification. The spec file has been formatted for for OBS by running “osc service localrun format_spec_file” then reading the contents to ensure that nothing went wrong and committing the changes back to OBS. In the above spec file we have split MakeHuman into 2 subpackages and made them depend upon each other to ensure consistency. As you can see there are 2 sources one is the tarball we created with our bash script earlier and there is another file called "makehuman.1" this is a manpage. In the spec file instructions are issued to gzip it and put into the manual directory on install. The manpage (Source101 in the .spec file) is shown below.
How man pages are created is out of scope of this document. Man pages use gtroff. There are however ample resources online which can help with this.
The .spec file has been commented to provide you with a better understanding of what is done at various stages.
Once the .spec file has been updated on OBS it automatically triggers a rebuild duribg that time you can monitor the status of the build process and correct errors in your spec file or sources as they arise.
### 4)Pushing changes to the official repositories
Once you are satisfied that your package is stable you can make a submit request to submit the package from the Web User Interface or run the command below.
In the above command we submit the “makehuman” package to the OpenSuse “graphics” project. After this the package is reviewed by the maintainer of the graphics project and approved or rejected with comments given. You will receive an email after the project has been reviewed.
Notes:
* The .spec file and the manual page will change over time. The above is there for illustration purposes only.
* You can find copies of the most recent stable .spec file and makehuman.1 manpage!LINK!:https://build.opensuse.org/package/show/graphics/makehuman: -- here!/LINK!. This is the stable version after a "submit request" to the official Suse repositories.