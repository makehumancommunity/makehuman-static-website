---
title: "MakeHuman fails to start in windows, nothing seems to happen when I click the exe"
draft: false
---

## For any version

The number one reason for this is a user error: you double-clicked the zip file (without extracting it) and then double-clicked the .exe file ''inside the zip''. This will not work. You need to first extract 
the zip file to a directory and then click the .exe file there. 

However, if this is not what happened, read on for other possible explanations. 

## For nightly builds and 1.1.0

In more cases than not, this is a crash in your graphics card drivers rather than in MakeHuman as such. It is caused by a faulty or old implementation of OpenGL, something which is particularly 
common in integrated Intel graphics cards. You can try to upgrade the graphics card drivers to see if it helps. 

Another possible remedy is running MakeHuman with the --noshaders switch. See [[FAQ:MakeHuman renders odd colours and weird transparency artefacts. Can you help me?]].

In order to make sure that it is the indeed the graphics card that is causing the problem, look in your log (see [[FAQ:How to provide a makehuman log for a good bug report?]]). If the log file 
is only a few lines long rather than a screen page or more, but there is no particular error message at the end, then it is most likely the graphics card driver that crashed.

Unfortunately, there is not a whole lot MakeHuman can do about faulty graphics card drivers. 

**Alternative explanations**

Other possible reasons for this and similar problems may include:

* Your antivirus quarantined a particular library in the downloaded zip. We've got reports that norton antivirus dislikes numpy for example. If this happens, random consequences ensue. To solve this, you should whitelist the makehuman directory and/or files belonging to makehuman.
* You have a very odd character encoding in your system and an uninterpretable character in the pathname. We ''think'' we have fixed most of these issues, but to test if this is indeed the problem, try putting makehuman in a path with only ASCII (a-z) characters, such as c:\makehuman. Unfortunately this problem will also arise if the user has odd characters in the username, since that is included in the path for where MakeHuman stores it user files. Per October 2016, there is a new build which solves most of these problems. So if you think this is what causes the crash, try downloading a zip file called makehuman-stable-XXXXXX-win32.zip from http://download.tuxfamily.org/makehuman/nightly/

**Reporting the problem and asking for support**

If you are not able to solve the problem, report it on the [forum] but be sure to follow the instructions in [[FAQ:How to provide a makehuman log for a good bug report?]](http://www.makehumancommunity.org/forum/) in order to provide enough info.

## For version 1.0.2 and earlier

Under the following conditions:

# You are using any version of windows
# You have downloaded a zip file containing the release build 1.0.2 or earlier (ie, not a nightly build).
# You have previously installed python
# Other factors as yet unidentified (by seemingly more rare going forward)

... MakeHuman will crash before anything appears on screen. The reason is that there is a bundled python inside the build zips, but unfortunately a system-wide installation can, under certain circumstances, get detected first. This makes python look in the wrong place for DLLs etc, which causes the exe for the build to silently crash.

There are several alternative work-arounds proposed for this. However, the simplest solution is the first one.

# Upgrade to 1.1.0. The problem is fixed in that branch since years back.
# Temporarily rename your python directory to something other than its directory path in your path statement.
# Uninstall the existing python from the machine (fairly extreme). 
# Run source checkouts from bitbucket instead. In this case you must have python installed on the machine.