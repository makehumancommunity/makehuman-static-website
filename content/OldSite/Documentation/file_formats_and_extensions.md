---
title: "File formats and extensions"
draft: false
---

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

The targets.pymodule (lib folder) is where system assets stored with the NPZ extension are identified, decompressed, and turned into memory resident structured objects for use by MakeHuman.  This Code related to NPZ files can also be found in algos3d.py module (core folder).  This module has been part of MakeHuman for a long time, and is used for morphing related operations.  It works with loaded binary translation vectors and applies those translations to morphing targets. It may have some legacy capability to work directly with text-based .target files.

The compile_models.py module (lib folder) takes all object mesh files (.obj) and compiles them into binary compressed files (NPZ). Similarly, the compile_targets.py module (lib folder) compiles target files (.target) into binary compressed (NPZ) files.  The latter module is referenced by Benjamin Lau in MakeHuman.spec file, likely for build purposes.

Important concept.  The root folder of MakeHuman contains a batch file called cleanpz.bat (for Windows) and a corresponding shell script file called cleanpz.sh (for Linux) whose function is to delete NPZ files between repository (Bitbucket or GIT) builds. This “garbage collection” assures that each build is not working with out-of-date assets.  It also reminds the developer that most of the canonical assets are initially constructed in text readable format. Developers write appropriate constructors to recompile NPZ files during the MakeHuman startup sequence when missing.  For distribution versions of MakeHuman, pre-compiled assets in the form of NPZ files are distributed as stable assets. When start up code confirms their existence , no recompile is done, producing a better start-up experience for the user. This design greatly increases boot and runtime performance for stable distributions without hampering rapid testing of repository versions in interpretative mode.

=### .thumb files

This extension designates thumbnail (image preview) files in MakeHuman. Underneath, they are actually images constructed in the .png file format. Thus, they can be edited by standard image editors like GIMP or displayed by most web browsers. The MakeHuman Save Tab code automatically generates a companion .thumb file each time it saves a .mhm file. The .thumb generation is currently done by capturing a rectangular in the center of the viewport window.  The MakeHuman Load Tab code uses .thumb images to provide previews of saved models.
The format for .thumb is defined inimage_qt.pymodule (GUI folder). Load and Save use or generation occur inguiload.pyandguisave.pymodules, respectively (lib folder).  Numerous plugin modules reference .thumb files (plugins folder) including:2_posing_expression.py,3_libraries_clothes_chooser.py,3_libraries_eye_chooser.py,3_libraries_material_chooser.py,3_libraries_polygon_hair_chooser.py,3_libraries_posing_chooser.py,3_libraries_proxy_chooser.py, 4_rendering_scene.py,7_material_editor.py,

=### .lmk files

This MH internal extension designates landmark files. [might be renamed .mhlmk for naming standard reasons.] There is one set of landmarks for the model body (and a second set of landmarks for the model head (data | landmarks folder).  These LMK files are written in text readable format.  Each line has a single integer which specifies a landmark vertex in the model geometry. Landmark vertices are used for relative (local) spatial reference during model morphing.    
Landmark files are used bywarpmodifier.py(apps folder) andwarp.py(utils | tools | warptarget folder).The landmarks in these files are used as references during the complex process of reshaping the human.

=### .mhclo files

This MH internal extension designates MakeHuman clothes files. These files define clothing vertexes and remove vertexes from the model to allow fitting of the model without skin showing through. They are created using the MakeHuman Blender toolset, specifically the MakeClothes tool.
A special empty MakeHuman clothes meta-file named clear.mhclo is is used to restore the default UV map that comes with the system.  In the lib folder, the filechooser.py module has a MhcloFileLoader.Refresh() method to clear materials when the refresh button is clicked.
In the plugins folder,3_libraries_clothes_chooser.py, 3_libraries_eye_chooser.py, and 3_libraries_polygon_hair_chooser.py all access MHCLO files, but as of this writing, there are some file handling issues related to proxy clothes that means some of this code is commented out.  In the shared/export_utils folder, config.py accesses a cage.mhclo file.  In the tools folder, the tool ‘MakeClothes’ accesses MHCLO files in both the  makeclothes.py and material.py modules.  Similarly, the tool ‘MakeTarget‘ accesses MHCLO files in several of its modules:_init_.py, convert.py, import_obj.py, mt.py, ands ettings.py.  Finally, two experimental tools in the utils folder, the makeface.py and helpers.py modules access MCHO files.

The mhclo-file structure:

A MH clothing consists of two files, the mhclo file which determines the vertex locations and a standard obj file which defines the rest of the mesh: faces, uv coordinates, uv faces. MH automatically compiles these files the first time it uses them, so these are the binary mhpxy and npz files. The header in a mhclo file looks like this:

    # Exported from MakeClothes (TM)
    # author Unknown
    # license AGPL3 (see also http://www.makehuman.org/doc/node/external_tools_license.html)
    # homepage http://www.makehuman.org/
    uuid 59985471-ab08-479f-a32d-2d88411714ef
    basemesh hm08
    name Helmet
    version 110
    obj_file helmet.obj
    x_scale 5399 11998 1.3980
    z_scale 962 5320 1.8441
    y_scale 791 881 2.2028
    z_depth 50
    max_pole 4
    verts 0


 # starts a comment.
The uuid is a unique identifier for this file.

The basemesh is the version of the MH mesh. Today always hm08, but earlier versions of MC supported hm07 and alpha6.

Name of clothing.

Version of MC

The obj file contains all information about the mesh in obj format: original vertex locations, faces, UVs.

x_scale v1 v2 dist: Used for scaling of offsets (see below) in the x direction. dist is the distance between verts v1 and v2 in the character the clothes were made for.

y_scale, z_scale analogous

z_depth determines the render order in MH, I think. It was originally used in a different way by the MHX importer.

max_pole is the maximal pole number of any vertex in this mesh. Affects how large arrays must be allocated in MH.

verts 0. It was some kind of vertex number offset, but the author doesn't quite remember how it worked.

Then comes a bunch of lines which determine the vertex locations.

    16563 16602 16605 -2.77529 -3.02614 6.80143 -0.56369 0.10852 -0.06174


The three first are human vertex numbers which define a triangle.
The three in the middle are barycentric coordinates, which define a point in the triangle.
The three last is an offset from this point. However, the offset is scaled with factors determined by the x,y,z_scale lines in the header.

If the n:th line reads

    v1 v2 v3 w1 w2 w3 d1 d2 d3


then the location of clothing vertex n is

    w1*r1 + w2*r2 + w3 *r3 + (s1*d1, s2*d2, s3*d3)


where r1,r2,r3 are locations of human vertices v1,v2,v3, and s1,s2,s3 are scale factors

=### .mhmat files

This extension designates MakeHuman material files.    Material files are text-readable files that share their syntax structure with Lightwave OBJ and MTL files.
In the app module group,human.pyapplies a default material andmh2proxy.pyhandles materials for proxies and may do some special material handling for MHX Blender export files. In the data folder, the MHCLO files for clothes, eyes, and hair each references an MHMAT files. In the plugins folder,7_material_editor.pyloads, edits, and saves MHMAT files.  In the shared folder,material.pyparses MHMAT files and sets material properties.  In the tools folder, there is another (independent)material.pymodule for the MakeClothes tool that writes materials to the output file while using that tool within Blender. 
### = .mhmat file format Internals## 
The entries inside a .mhmat file are of the form:
Comments can be included in c-style line comment format, like
or in python-style line comment format, like
 
The properties of a makehuman material are numerous so that they can cover the most common needs of exporters and rendering engines, and may vary among the following.
name- The internal name of the material.

Colors- Their value can be in R G B format, like: colorProperty R G B, where R, G, B are floating point numbers between 0 and 1. They control the color of various material properties and effects. 

To adjust the intensity of an effect, you can simply edit its color value.
  ambientColor -The ambient component of the material, which is usually added on the final color regardless of the surrounding lights.
  diffuseColor -The diffuse component of the material, which reacts to each light's relative position.
  specularColor -The color of the specular shine that is caused by the reflection of a light source on the material.
  emissiveColor- The color of the light that the material seems to emit as if it's a glowing light source.
  shininess- The sharpness of the shine spots created by the reflection of a light source on the material, which is how glossy its surface is.

Here's a list of naming convention for the content of the mhmat-file (floats are between 0.0 and 1.0):

"name": string

"tag": string

"description": string

"ambientColor": 3 x float

"diffuseColor": 3 x float

"specularColor": 3 x float

"shininess": 1 x float

"emissiveColor": 3 x float

"opacity": 1 x float

"translucency": 1 x float

"shadeless": bool

"wireframe": bool

"transparent": bool

"alphaToCoverage": bool

"backfaceCull": bool

"depthless": bool

"castShadows": bool

"receiveShadows": bool

"autoBlendSkin": bool

"diffuseTexture": filename

"bumpmapTexture": filename

"bumpmapIntensity": 1 x float

"normalmapTexture": filename

"normalmapIntensity": 1 x float

"displacementmapTexture": filename

"displacementmapIntensity": 1 x float

"specularmapTexture": filename

"specularmapIntensity": 1 x float

"transparencymapTexture": filename

"transparencymapIntensity": 1 x float

"aomapTexture": filename

"aomapIntensity": 1 x float



"sssEnabled": bool

"sssRScale": 1 x float

"sssGScale": 1 x float

"sssBScale": 1 x float



"shader": filename

"uvMap": filename

"shaderParam":

['diffuse', 'ambient', 'specular', 'emissive', 'diffuseTexture', 'bumpmapTexture', 'bumpmapIntensity', 'normalmapTexture', 'normalmapIntensity', 'displacementmapTexture', 'displacementmapTexture', 'specularmapTexture', 'specularmapIntensity', 'transparencymapTexture', 'transparencymapIntensity', 'aomapTexture', 'aomapIntensity']

"shaderDefine":

['BUMPMAP', 'NORMALMAP', 'DISPLACEMENT', 'SPECULARMAP', 'TRANSPARENCYMAP']

"shaderConfig" "diffuse": bool

"shaderConfig" "bump": bool

"shaderConfig" "normal": bool

"shaderConfig" "displacement": bool

"shaderConfig" "spec": bool

"shaderConfig" "vertexColors": bool

"shaderConfig" "transparency": bool

"shaderConfig" "ambientOcclusion": bool


ambientColor, diffuseColor specularColor, emissiveColor are the standard colors as used in the rendering equation or in standard OpenGL. Their corresponding intensities are simple scalars with a value between 0 and 1 and are multiplied with the colors to dim them. Default these intensities are set to 1.

Colors are described as three floating point numbers, representing R G B, or red-green-blue values. 1 is the maximum, 0 the minimum. For example 1.0 0 0 means fully red, 1 1 1 means full white, 0 0 0 is full black. 0.5 0.5 0.5 will give you a grey middle color.

opacity determines the opaqueness of the object (alpha channel), with 1 being fully opaque, and 0 being fully transparent (invisible)

translucency is something that came from Blender but is unused

shininess or specular hardness is a number between 0 and 1 determining the shininess constant of the phong shading model.
Texture maps

Various standard texture maps can be defined on the material, like diffuseTexture, bumpmapTexture, normalmapTexture, displacementmapTexture, specularmapTexture, transparencymapTexture, aomapTexture. Each of these also has an associated intensity value, which is a scalar from 0 to 1 multiplied with the pixel value of that texture (unless a specific shader implements it differently). These textures only have an effect if their corresponding shaderConfig feature has been defined (see the table in Shaders section).
Render states

When wireframe is set to True, the model is drawn in wireframe mode. In this mode, most material properties have no effect, but you can enable the vertexColors shaderConfig to be able to change the color of the mesh using vertex colors (this requires access to the mesh programatically, obj meshes do not support vertex colors). This feature is used in some parts of MakeHuman, for example viewing bone weights in the skeleton debug plugin.

Set shadeless to True to disable shading, eg. the object is not affected by lights. Configured shader will have no effect

Set transparent to True to enable transparency rendering (usually needed when opacity is < 1) In itself this does not change the visual appearance of the model, but this setting should be enabled if your texture contains (semi-) transparent parts. This setting instructs the renderer to disable depth buffer writes (glDepthMask(false)) and enables alpha testing and blending so that transparent surfaces can overlap and to allow alpha blending.

alphaToCoverage Applies when transparent is set to True (otherwise does nothing). It requires that your GPU supports alpha to coverage (A2C) rendering. It enables the A2C feature which provides face order-independent alpha rendering. This works very well for complex transparent meshes, like hair. At the cost of a slightly dithered look, it solves all the problems with face sorting that are usually involved in rendering semi transparency. (This feature disables anti-aliasing for this object because the multisample buffer is used for alpha blending instead)

Set backfaceCull to False to disable backface culling (render the back side of polygons) By default, and in most cases, this should be set to True, but can be useful in some cases (for example, we disable back-face culling for the eyebrow materials).

Set depthless to True for depthless rendering (object is not occluded and does not occlude other objects). This disables OpenGL depth writes and tests. In practice, this makes object faces that should be occluded shine through others.

castShadows determines whether the object casts shadows on other objects.

receiveShadows determines whether the object receives shadows from other objects. For some features, like eyes, you probably want to disable shadow receiving.

Since MakeHuman does not (yet) implement shadow casting, the shadow settings have no effect in MakeHuman, but they do export to other engines.

Play around with these settings in the Material Editor plugin to see their effect, that's the best advise I can give you. The best way to find out which settings work for an asset, is simply to try them out.
autoBlendSkin

If True MakeHuman will set the diffuse color based on the ethnix mix set for the character. Any diffuseColor set in the material file will be overridden by this. Also the shaderParam litsphereTexture will be automatically set to a dynamically blended litsphere texture, which is a mix of three litsphere materials (afro, asian, caucasian) depending on the ethnic mix of the character. This latter is specifically intended to be used with the litsphere shader, and it is what you see as default material when you start MakeHuman This overrides whatever shaderParam litsphereTexture was set in the material file. This setting is intended only for skin materials.
shaderParam

Define a custom shader parameter (uniform), which might be required for some non-standard shaders. For example, the litsphere shader takes an extra type of texture map as input, a so-called litsphere texture. This generic system of mapping shader uniforms allows you to create specialised shaders that take new and different kind of inputs, and allow configuring the shader from the material file.

shaderParam can be a list of floating point numbers, in which case it will be interpreted as a vector, or it can be a file path, in which case it is assumed to be an image path. Internally in MakeHuman, shaderParams can also be assigned a texture object, which allows for dynamically passing a texture that is in memory, but perhaps not stored on disk.

Another example of a custom shaderParam is the X-ray shader that defines an edgefalloff and intensity uniform parameter. These could be changed from the material file with

 shaderParam edgefalloff 0.8
 shaderParam intensity 0.77

shaderDefine

shaderDefines allow enabling or disabling custom shading techniques in shaders. These allow to define new shading techniques, apart from the pre-defined ones such as normal mapping, specularity mapping, ... It's a generic system that allows new shaders to be added and configured from the material file, or from the material editor (which nicely auto-detects these features in the shader and shows a set of checkboxes for them).
uvMap

Load custom UV coordinates on the mesh to use this material. This makes the material completely dependent on the mesh it is used with.

Takes a path to a .mhuv file, which is actually just an .obj file, where the vertex positions can be deleted (they can remain in there, but they are ignored). Requirement for it to work is that the vertex order is the same as that of the mesh obj.

An example uv map for the basemesh can be found in data/uvs/a7.mhuv, which is a set of UV coordinates compatible with the old Alpha 7 mesh, allowing you to load A7 textures on the new basemesh used in MakeHuman v1+
SSS properties
These are the so-called sub-surface scattering shading properties, currently only used by the built-in offline renderer. They were decided on while trying to figure out the most generic way to define SSS shading properties, so that they could easily be translated into SSS properties for a different renderer (as no single renderer that I know of has a standard for these). It's uncertain whether the format we have landed on currently is the best, or whether this will remain permanently or is still likely to change. This setting should currently be considered experimental. The properties are sssEnabled, sssRScale, sssGScale and sssBScale.

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
 

## Proxy files

### Offset and bounds

MakeClothes uses a bounding box for scaling the offsets. It's controlled by the ''Offsets'' option in MakeClothes.

This is how this data is stored in the proxy file, so you can modify by hand if desired.
In the mhclo file at the top, these values appear as
  x_scale 5399 11998 1.4340
  z_scale 962 5320 2.0001
  y_scale 791 881 2.4098


Allowed values are:
  x_scale
  y_scale
  z_scale
  shear_x
  shear_y
  shear_z
  l_shear_x
  l_shear_y
  l_shear_z
  r_shear_x
  r_shear_y
  r_shear_z


scale options follow the format:
  x_scale v1 v2 den

with v1, v2 vertex indices on the human basemesh, den a denominator with which the scaling value is reduced
which results in the construction of a scale matrix that is applied to all the offsets of the proxy.
eg.
  [xscale 0 0 0]
  [0 yscale 0 0]
  [0 0 zscale 0]
  [0 0 0      1]

where xscale is determined from the option x_scale v1 v2 den as:
xscale = abs(coord_pos(v1).x - coord_pos(v2).x) / den

analog for yscale and zscale (.y or .z components of the position vector will be used instead)


shear options follow the format:
  shear_x v1 v2 x1 x2

which result in the creation of a shear matrix instead of a scale matrix (I don't know of any instance where this is used)
uses numpy's affine_matrix_from_points method to calculate a transformation matrix that fits all selected points
didn't go into detail understanding this, because it doesn't seem too relevant. Read the code if interested.

scale overrides shear which overrides l_shear which overrides r_shear, only one of them is used (so you either specify scale, shear, l_shear or r_shear but no combination of them)
If you specify one, it is expected you define the other 2 of the same type as well.


### max_pole

Proxy files can specify the pole count, which is the maximum number of edges that a vertex in the proxy mesh (the OBJ file) can have. If all faces around this vertex share their edges, this number also coincides with the maximum number of faces per vertex. If not specified, MakeHuman assumes this number is 8, which is a reasonable standard (more than 8 edges per vertex is probably a sub-optimal topology).
For example, the MakeHuman basemesh, which was modeled with high consideration of pole count, has a maximum of 5 edges per vertex.

MakeHuman intentionally is conservative about pole count to benefit performance (of the subdivision algorithm for example), for the same performance reasons it will not check the pole count when loading an OBJ, and instead relies on the user, or creation tool (MakeClothes) to set this number appropriately (at the moment MakeClothes does not do this).

Similarly, you can improve performance of MakeHuman by lowering this number if your proxy mesh has lower pole count. Eg for some meshes this can be set to 6 or 7

Proxy files have a property ''max_pole'' to change this number from the default setting of 8 to something else:
  max_pole 9


## Meshes

MakeHuman stores its meshes in the standard Wavefront OBJ format. It supports quad-only meshes, and by default allows up to 8 edges per vertex. This number can be increased (see proxy format).


## Material files

You can store more than one material for an asset. To do so, create a folder named "material" inside of the folder which also contains the mhclo- and mhmat file of that asset. Put your alternative textures and mhmat-files in there.

## Poseunit files

TODO


## Target files

TODO


## Modifier and slider definitions

TODO