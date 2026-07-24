---
title: "Terminology"
draft: false
---

This is an attempt to make a small dictionary/glossary to introduce terms commonly used on the forums. It is still very much a work in progres.

## Terms specific to MakeHuman
To be written.

### Base mesh
To be written.

### Target
To be written.

### Modifier
To be written.

### Skin
To be written.

### Nightly / Nightly build
To be written.

### Hg / Bitbucket / Mercurial
To be written.

### Package
To be written.

### Build
To be written.

### MH Blender Ttools
To be written.

## General graphics-related terms

### Vertex / Vertices
A vertex is a single point in 3D space designated by a set of coordinates typically designated, by x, y, and z values relative to an origin designated with the spacial coordinates (0, 0, 0). Interpretation of a vertexes coordinates depend on the orientation of the coordinate system.  In MakeHuman, +Y is up in the viewport, +x is is the right side of the viewport, and +z is out of the screen [Note: verify this orientation]. Vertices are the plural form of vertex.

### Face
A face is a plane or surface in 3D space described by connecting three or more vertices.  A face that is created by only three vertices is called a "tri" and is strictly planar.  A face created by connecting 4 vertices is called a "quad" and need not represent a true, flat planar surface.  Faces in MakeHuman are "quads" by design,  MakeClothes requires that all faces be quads or this MakeHuman tool will fail. Faces created by more than 5 vertices are sometimes called "ngons". Faces can be "one-surfaced' (either side) or "two-surfaced', and the way light interacts with the surface of a face depends on how the  "surface normals" are defined.

### Edge
An edge is a line connecting exactly two vertices.  Edges that connect a series of vertices as a path of polygon edges is called an "edge loop". A path of polygon edges that are connected in sequence by their shared faces is called an edge ring.
   
### Mesh
A mesh is a collection of vertices, edges, and faces connected together to form a virtual 3D object.

### Normal
A normal is vector describing the direction that is othrogonal (at 90 degrees) to a surface.  The normal direction is often described by a "normal map" which can have a finer resolution than a single face.  This is done by using the value (magnitude) of individual pixels or pixel color channels in a bitmap image to describe the normal direction. Normals become importantin 3D graphics to describe how light reflects off objects in a virtual world.

### UV / UV unwrap / UV mapping
These terms relate to the process of flattening the surface of a 3d object so it can be laid out on a 2d image, a bit like a sewing pattern. "UV" is not an acronym. U and V is how you name
axes on the resulting 2d surface, instead of X/Y/Z. When someone sloppily just say "UV" they most likely mean a UV mapping. See https://en.wikipedia.org/wiki/UV_mapping.

### Texture
The term texture refers to a mechanism for describing surface characteristics of a 3D object.  A texture is only one component of a "material".  Textures are typically of one of two types.  The most common textures in MakeHuman are "bitmap images" used to represent skin or the color of clothing.  The other type of texture is a so-called "procedural texture" which is defined by a mathematical function for altering light-material interactions.  These procedural textures are uncommon in MakeHuman.

### Seam
A seam is one or more edges, typically end-to-end with each other, that define how a three dimensional mesh can be split to flatten it onto a planar surface.  Seams are used when creating a "UV map" for a mesh.  The need to create a UV map comes from a desire to create a mapping of the pixels in a bitmap texture to the faces of a 3D mesh.  Seams created manually allow this mapping to be created in a manner that allows discontinuities in the image to be hidden on the surface of the intact 3D object (e.g., human, hair, or clothing)

### Bump map
Bump mapping is a processing of defining the bumps and wrinkles on the surface of a 3D mesh.  It typically is done using a bitmap image to include the needed information.  Texture mapping, displacement mapping, normal mapping, height mapping, etc. are either forms of, or closely related to "bump mapping".

## File formats

### Obj file / Wavefront
To be written.

### Blend
To be written.

### Wavefront
To be written.

### FBX
To be written.

### MHX
To be written.