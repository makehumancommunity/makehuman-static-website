---
title: "What changed regarding the license in 2020?"
draft: false
---

In september 2020, the overall license of MakeHuman was clarified and made more permissive. The full and updated license text can be found at https://github.com/makehumancommunity/makehuman/blob/master/LICENSE.md

In summary, the goal was to remove any lingering doubts about whether the output from makehuman could be used freely and without license restrictions. 

These were the main changes: 


* BEFORE: Bundled assets are a part of the application
* AFTER: Bundled assets are something the application uses, but which are otherwise considered standalone entities


* BEFORE: Assets are per default covered by AGPL
* AFTER: Assets are per default released as CC0


* BEFORE: Exports become covered by CC0 upon export via the GUI
* AFTER: Exports only consist of things which were CC0 to start with


* BEFORE: Targets, proxies and the base mesh are considered source code, covered by AGPL (unless exported via the GUI)
* AFTER: Targets, proxies and the base mesh are considered graphical assets, covered by CC0


* BEFORE: Trying to "reverse engineer" or recreate the targets is prohibited
* AFTER: Targets are CC0 no matter how you got hold of them


We believe we have caught most places where the old license setup is mentioned. But if you find remaining strangenesses, particularly where assets are listed as AGPL, please report these.