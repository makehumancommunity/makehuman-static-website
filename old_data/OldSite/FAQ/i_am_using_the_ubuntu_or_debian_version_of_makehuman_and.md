---
title: "I am using the ubuntu or debian version of MakeHuman and..."
draft: false
---

The problem here is that you probably got your hands on MakeHuman alpha 6. This is a ''four years old alpha release''. There is no way we can maintain this. 

Unfortunately someone at Debian made a package of MH back then, and put it in the official repositories. After that it was not touched for years, despite our repeated pleas to either upgrade or at least remove this extremely archaic and completely unsupported version.

As per summer 2015, the Debian representative in charge of the MakeHuman package did a version bump on the package. It has since got posted in debian Sid ("unstable") and will slowly start to trickle down to new releases of Debian-derived distributions. However, the earliest possible actual release that might contain this package is ubuntu 15.10. Everything before that will still contain the alpha 6 release.

There is a perfectly functional official DEB release available from the MakeHuman download page. That will give you an up to date version of MH. If you are using ubuntu, see also [[FAQ:I'm using ubuntu. Is there a PPA?]]