---
title: "Help edit this site"
draft: false
weight: 5
---

This web site could need a lot of love. There is always the need for new tutorials, updating old facts and making things more readable.

The technology behind the site is rather straight forward. All pages are text files in MarkDown format. These are converted to static web
pages via a program called [Hugo](https://gohugo.io/).

This procedure runs (or will, when I've gotten around to it) every once in a while, so changes made to the underlying pages will be reflected
on the web site within a few hours.

## Making basic editing

In theory you can edit pages directly on github. For example, if you want to edit the page you are watching now, simply go to ... and click edit.
If you do not have write access, this will automatically be converted into a "pull request", so that someone from the dev team can look at it.

If you have write access, you can simply commit it without further procedures. 

The "preview" tab on github will give a reasonable impression of how the page will look on the web.

## Making more advanced editing

If you want to do more structured editing and be able to see how it looks when rendered, you will need to clone the site repository and install 
Hugo locally.

You can download a self-contained instance of hugo from https://github.com/gohugoio/hugo/releases. 
Note that you need hugo **extended**, which is found at the bottom of the list of available files (which is located under the "assets" header).

The hugo theme is included as a git submodule. So when you clone the repo, be sure to include "--recursive", for example 

    git clone --recursive https://github.com/makehumancommunity/makehuman-static-website.git

To start a local hugo webserver on port 1313, run 

    hugo server -D 
    
.. in the root of the repo. This will automatically re-render all files when you make a change in the markdown code.

Then make your edits, commit them and either push or make a pull request.

