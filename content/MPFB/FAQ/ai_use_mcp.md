---
title: "Does MPFB have an MCP interface?"
draft: false
description: "No, MPFB as such does not have an MCP interface. But there are separate code bases for interacting with MPFB via MCP."
---

MPFB as such does not come with an MCP interface. It is unlikely we will ever bundle one in the future either, as that would be feature creep and most likely 
a violation of the guidelines for the extension platform.

This said, since MPFB is perfectly possible to script from other addons, you can use a generic MCP bridge for Blender to interact with MPFB.

Both [Blender lab's Blender MCP](https://projects.blender.org/lab/blender_mcp) and [Ahujasid's MCP for Blender](https://github.com/ahujasid/mcp-for-blender) should work for this.

There is also an early beta of a [dedicated MCP bridge for MPFB](https://github.com/makehumancommunity/mpfb-mcp/tree/master). It works but isn't complete.
