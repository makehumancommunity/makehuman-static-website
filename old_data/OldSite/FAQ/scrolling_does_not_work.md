---
title: "Scrolling does not work"
draft: false
---

When starting MakeHuman, everything looks fine. But when you try to scroll a panel, it either does not work at all, or the contents in the panel is compressed.

This happens when you use a PyQt version later than 5.12. Something in the MakeHuman UI code is incompatible with the latest PyQt versions. At this point, the only solution we have is to downgrade PyQt to 5.12.

Note that if you run from source, you can do so in [[a python venv]](https://docs.python.org/3/tutorial/venv.html) and install a a specific version of PyQt there. That way you don't need to touch the system-wide installed PyQt. Running in venv is our currently recommended 
approach for Ubuntu 20.10 (Ubuntu 20.04 and earlier should not have the problem).

On ubuntu the commands are these:

    apt-get install python3-virtualenv
    virtualenv makehuman-env
    source makehuman-env/bin/activate
    pip install PyQt5# 5.12.1 numpy pyopengl

Now you have a python command which will use pyqt 5.12, and can follow the instructions for running from source, see http://www.makehumancommunity.org/wiki/FAQ:How_can_I_run_the_same_code_as_the_nightly_build_from_source%3F (skip the parts about apt-get installing dependencies.. This is what you did with pip above here).