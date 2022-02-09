---
title: "How can I create extra bodyparts?"
draft: false
---

If you wish to add extra body parts (wings, genitalia, horns...) you have three options:

* Deform the base mesh. In practice, you are making a new target, see [[FAQ:How can I create targets?]]. For small modifications, this is the most portable options, but it becomes nonviable for large body parts.
* Make a proxy which has the body part. See [[FAQ:How can I create proxies or alternative topologies?]]. For modifications that requires larger mesh densities in some areas, but which still follow the basic shape of the base mesh, this is the best option. This is the recommended approach for, for example, genitalia. The upside of this is that you don't get any seams between the body part and the main body. 
* Add the body part as if it was a piece of clothing, see [[FAQ:How can I create clothes?]]. Body parts that are essentially separate from the body (think angel wings) would probably benefit from being done this way. The downside is that you will most likely get visible seams/transitions between the extra body part and the main body.

In the latter two cases, it might become interesting to work with rigid vertex groups. These are discussed in [[Documentation:Controlling_the_result_with_vertex_groups]]