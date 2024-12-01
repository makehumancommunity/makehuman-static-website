---
title: "How to provide a makehuman log for a good bug report?"
draft: false
---

Pretty much whatever error report you post on the forums will have the same response unless you do what is listed below. The reponse will be "What does the log say?"

To avoid this, always include the logs if you want to report an error, be it on the forums or in the bug tracker. 

When you run  MakeHuman, four (two if you are on Linux) files are created into your home/makehuman directory (see [Where are my MakeHuman files found (where is my HOME directory)?]({{% relref "where_are_my_makehuman_files" %}}))

* makehuman.log
* makehuman-debug.txt
* python-out.txt
* python-err.txt

If a crash has occurred, the makehuman.log file is usually the most interesting, but it doesn't hurt to include all of them.

As alternative (and if the bug doesn't prevent the start of the GUI) you can also look in "Utilities"-->"Logs". Select the error and use the button "Copy to clipboard" in order to paste it in the report message.