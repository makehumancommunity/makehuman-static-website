---
title: "Why quadrilaterals?"
draft: false
---

Because quad > triangle conversion is trivial, while the other way around can be more complex (especially since it allows degraded topologies when quads and tris are mixed).
Quads have advantages in subdivision, and define deterministic edge loops, they are just much more convenient to work with in a modeling and animating environment.

In fact, MakeHuman does not impose the use of quads, you can use tris for proxies too. The only limitation is that you do not mix quads and tris, it's either one or the other. Note that subdivision does not work in MH when using tris.

In any case, the only reason you would use triangles is for reducing the polycount, which is a progress that should happen very late in your pipeline, not in the middle of the modeling process (and should only be done when you know exactly what polycount ratio you're aiming for). As vertex counts are becoming less of a limitation with recent graphics hardware, triangles are getting less and less used. In fact many recent (and even previous generation) games use only quads for their character meshes. It just performs much better in animation, and produces a much cleaner topology.