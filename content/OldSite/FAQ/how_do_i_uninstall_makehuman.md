---
title: "How do I uninstall MakeHuman?"
draft: false
---

Here are some informations how to remove MakeHuman from your system. The information is mostly intended for version 1.1.0 of MakeHuman.

## Windows
Simply delete the folder where you unzipped the MakeHuman-package. ([[FAQ:Where can I unzip MakeHuman (in Windows)?]]). MakeHuman itself only creates one folder (see below). The bundled Python and Qt libraries aren't expected to create any temporary files. (In case the last statement is not true, the temporary files should be found in the usual temp-folders. Please inform the MakeHuman-Team if you find any further remainder of MakeHuman, so the FAQ can be adapted.)

## Linux
Uninstallating MakeHuman depends on the method you installed it. If you have just unzipped a MakeHuman-package, simply delete this folder. In other cases use the specific package management tools of your distribution.


* Ubuntu (/Debian): You can remove MakeHuman via apt:
   sudo apt-get remove --purge makehuman
Then remove the ppa:
   sudo add-apt-repository --remove ppa:makehuman-official/makehuman-11x

Another possible method is to use ppa-purge (universe):
   sudo ppa-purge ppa:makehuman-official/makehuman-11x
This will remove MakeHuman and the ppa from source.list. In case there was another installation of MakeHuman before, from other sources then from the ppa, ppa-purge will only perform a downgrade to the previous version. 

If you have copied additional files to the system folders of MakeHuman by hand, these files will not be removed by the methods above and need to be deleted by hand.


* OpenSuse/Fedora:
Currently MakeHuman doesn't provide official rpm-packages. Please refer to your system documentation how to uninstall software.



## Mac OS X
To be written.

## Additional information, for all operating systems
On first run MakeHuman will create a folder called makehuman in your HOME directory. ([[FAQ:Where are my MakeHuman files found (where is my HOME directory)?]]) This folder can be deleted, too. But keep in mind, this folder contains all your models and other stuff you created or downloaded. **These files will be lost, if you don't have a back-up!**


''If you like, you can leaf a comment in the community forum why you removed MakeHuman (http://www.makehumancommunity.org/forum/). This will help the MakeHuman-Team to improve the software.''