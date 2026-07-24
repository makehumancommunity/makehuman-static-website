---
title: "Can I use the stable version and the nightly build at the same time?"
draft: false
---

Yes. Care has been taken to separate the home directories so that they do not interfere with each other. 

In practice, everything related to the nightly build will be placed in HOME/makehuman/v1py3 where as the stable release will place stuff under HOME/makehuman/v1. 

The downside is that assets downloaded for the stable version will not show up in the nightly and vice versa. If you copy stuff between the directories please take care to ''not copy the NPZ files''. These are generated the first time the asset is loaded, and are incompatible between the code versions.