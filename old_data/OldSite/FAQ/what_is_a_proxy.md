---
title: "What is a proxy?"
draft: false
---

A proxy mesh is an alternative to MakeHuman's base mesh. You can think of it as a full body glove which occupies roughly the same space as the human, and deforms with the human. It may have a different amount of polygons, usually a lot fewer than the base mesh. 

There are several reason why you would want to export a character as a proxy mesh:

* Gaming: The base mesh has quite high poly-count. Use the "proxy741" if you are on a tight polygon budget, or "male1591" or "female1605" proxy if you can afford more polygons. Or if you want to be extreme, you can download the [very low poly](http://www.makehumancommunity.org/proxy/very_low_poly.html) proxy.
* ZBrush sculpting: "male1591" proxy is a suitable starting point.
* Topology change: There are specific topologies for various cases (for example a very muscular male).

Because of the last bullet, sometimes the words "topology" and "proxy" are used interchangeably on the forums.

If you have external data, for example from a 3d scan, then it is much more convenient to apply that as a proxy than try to convert it to a target working on the base mesh, since a proxy don't need to have the same number or vertices nor share the UV. 

See also [[FAQ:How can I create proxies or alternative topologies?]]