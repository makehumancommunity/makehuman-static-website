---
title: "How do I report a bug?"
date: 2017-10-17T15:26:15Z
draft: false
---

Before reading the following, there are two quick hints which might be useful:

- Using blender 4? Make sure you install the specific blender 4 build of MPFB. The alpha 3 release is not blender 4 compatible.
- Running into errors which are reported as fixed? Take a look at [How do I make sure I have the correct version installed?]({{< relref "ensure_correct_version" >}})

## Reporting bugs

But reports are vital in order to help improving the software. So don't hesitate to report anything you find strange or 
if you encounter an outright error. This said, it will be helpful if you report these things in a structured manner. 
The following are a few hints on how to provide a good bug report.

Bugs should be reported here [in the github issues section](https://github.com/makehumancommunity/mpfb2/issues)

In general, this information should always be included:

- What, in detail, happened? Did you see an error message? Did the end result look different than expected? Did nothing happen at all? 
- From when is the version you are using? I.e, did you download it today or is it a few days or weeks old?
- If you are using an old version, did you test if the problem remains in the latest version (ie, nightly build from [MPFB Downloads]({{< relref "../downloads" >}}))?
- On what platform are you running blender?
- Exactly which blender version are you using?
- Screenshots clearly showing what the problem is

Without this kind of details, it is often simply not possible to figure out what the error is. 

When creating an issue on GitHub, you should get a basic template where these questions are listed.

If you have the time, it would also be helpful if you took a look at [How can I provide more help with debugging?]({{< relref "help_debugging" >}}) and 
provided the information listed there.

## Log files

If closer examination is needed, you might be asked for log files. 

On the developer panel you can find panels for increasing the log level and for exporting a log file. 

If you want to help the process along, you could increase the log level to DEBUG, repeat the procedure that caused the bug, export the "default" log file, and
attach this to your bug report.

## Suggestions for improvements

If you have a suggestion which is not a bug but rather a feature request, then that is welcome too. There is a separate template for reporting these
in the github issues section.
