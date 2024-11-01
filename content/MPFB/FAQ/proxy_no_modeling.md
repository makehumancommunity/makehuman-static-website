---
title: "Model sliders stops working when using a proxy"
date: 2017-10-17T15:26:15Z
draft: false
---

When having applied a proxy/topology, it might seem as if model sliders stop working. This is actually not the case. What is happening is that
the basemesh indeed does change with the sliders, but since it is hidden by the proxy, the change is not visible. 

On the model tab, there is a button "refit assets to basemesh" and a checkbox "auto refit assets". Either click the button after a model change
to update it to the latest shape. Or, if you have enough power in your machine, check the checkbox and have the change apply automatically. The last
option might become cumbersome if you have clothes with dense meshes equipped.
