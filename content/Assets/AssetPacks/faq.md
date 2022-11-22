---
title: "Asset Packs FAQ"
draft: false
weight: 1
---

These are some common questions about asset packs

### How do I install an asset pack in MPFB2?

Under "apply assets", there should be a "library settings" panel with an "install asset pack" button. Click this to open a file browser. Find the zip file with the asset pack and select this.

Note that you might need to restart Blender in order for the new asset pack to be detected.

### How do I install an asset pack in MakeHuman?

Unzip it in you makehuman/v1py3/data directory. See [where are my Makehuman files](http://www.makehumancommunity.org/wiki/FAQ:Where_are_my_MakeHuman_files_found_(where_is_my_HOME_directory)%3F) for more information on how to find this directory. For example, if the asset zip file contains a subdirectory "hair", then make sure that the contents of that directory end up under makehuman/v1py3/data/hair.

### Are there any differences between asset packs and assets found in the repositories?

Not any significant differences, no. Asset packs are simply downloaded assets which are bundled together in a single zip file. Some files have been renamed to better fit a common naming pattern though, and standardized rendered thumbnails have been added.

### Do I need the "makehuman system assets" pack in MakeHuman?

No, it is already included in MakeHuman. The system assets pack is intended for use in MPFB2.

### Do I need an asset pack in MakeHuman if I already used the asset downloader to download most of the assets in the pack?

No, you already have the same assets in that case.

### Can I use an asset pack in MakeHuman if I already used the asset downloader to download some of the assets in the pack?

Probably, although it is possible an asset might clash due to different naming. To be safe, you are probably better off by using the asset downloader to download the remaining assets rather than downloading the asset pack.

### What does "checked" mean, i.e what quality can I expect?

The assets have been opened in both MPFB2 and MakeHuman, and a cursory inspection has been made to ensure that the asset isn't in any obvious way broken. Most assets will have functional delete groups. Some assets where the lack of a delete group wasn't deemed to be a problem has also been accepted. So "checked" means that at least this level of quality is ensured.

However, there will always be a range of usefulness stemming from the purpose the asset had originally. If an asset was made for a short skinny female character, it might not be viable for a tall fat male character. This will be particularly visible when a delete group is not present, or not fitting the current character. In these cases the character skin might peek through the clothes and require manual correction.

### There is something wrong with an asset. Should I report this as a bug?

Apart from the "makehuman system assets", the bundled assets are mostly from third part authors. The MakeHuman dev team will not modify their assets directly. If you wish to report that something is wrong, you should reach out to the asset's listed author, preferably on the forums. If you can't reach the author directly, writing a note in the 
[assets forum](http://www.makehumancommunity.org/forum/viewforum.php?f=20) will probably be most likely to get attention.

### What does CC0 and CC-BY mean?

"CC" is "Creative Commons", a set of standard copyright/license notices. There are several variations of these, but the two used here are:

CC0 (Creative Commons Zero, [see full text](https://creativecommons.org/publicdomain/zero/1.0/deed.en)) basically means that the author has donated this asset to the public domain. There are no restrictions on the use. In short: "do whatever you want with it".

CC-BY (Creative Commons Attribution, [see full text](https://creativecommons.org/licenses/by/2.5/se/deed.en)) means that you can do whatever you want with the asset as long as you give credit to the author. See [What do I need to do when I use a CC-BY asset?](http://www.makehumancommunity.org/wiki/FAQ:What_do_I_need_to_do_when_I_use_a_CC-BY_asset%3F) for a guide on how this can look in practice.
