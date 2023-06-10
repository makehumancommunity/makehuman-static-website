---
title: "Helping out with coding"
draft: false
weight: 10
description: "These are coding tasks for MPFB."
---

Coding is fundamental in order to add features to MPFB. Here the limit is mainly your own fantasy.
If you don't have a specific idea, a good start is looking through the feature requests in the issue tracker in the repository: https://github.com/makehumancommunity/mpfb2/issues

The following are only a few suggestions.

## Larger endeavours

These are some planned features which have not been started due to lack of time. At some point they should be added, and any help is appreciated.

- Support for BlenRig. Right now there is no support at all. There is a feature request started at https://github.com/makehumancommunity/mpfb2/issues/100
- Support for retargeting animations. At the moment, this need to be done manually or using third part tools. In the best of worlds, there should be a button in the interface for remapping common downloadable animations to at least a few of the MPFB rig types.
- Load BVH-style MakeHuman pose files. This is one of the few remaining features from MakeHuman which is not supported at all in MPFB. This would be desirable, since there are a lot of poses available in the asset repo.
- Add support for geometry nodes hair. Currently only mesh style hair is supported. With blender 3.5 and later it should be possible to add support for automating at least some of the steps required to add geometry nodes hair. There is a feature request started at https://github.com/makehumancommunity/mpfb2/issues/80

## Easy but boring tasks

These are things which can be done when there is some time to spare, and which don't require starting a large project.

- Add unit tests. The test coverage isn't currently very impressive. While this might be an unthankful tasks with little visible benefit, it is very important for the future survival of the project. Blender often make changes in the python APIs, and without proper test coverage it is very difficult to know if everything still works when a new blender version is released.
- Add doc comments to methods, classed and modules. While it has been a design goal to have documented code, there are still parts of the code which need to be documented.
- Fix linting issues. If you run PyLint or SonarLint, you will get suggestions for code style issues that should be fixed in order to improve the code quality and readability. 
