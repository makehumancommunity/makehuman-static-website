# makehuman-static-website

These are the sources for the new community website. The site as such is located under "content". Pages are markdown and can, if nothing fits better, be edited directly on github.

## The rendered site

Until finished, a rendered version of the site is available at http://static.makehumancommunity.org/

This will be updated manually once in a while, as an when there are changes.

At some point automatic building and updating will be implemented.

## Adding content (quick version)

Simply create a new markdown file in the appropriate location. Take a look at how existing pages are written in order to set page title etc.

## Working with Hugo

The site is rendered to HTML using [Hugo](https://gohugo.io/). You can download a self-contained instance of hugo from https://github.com/gohugoio/hugo/releases. 
Note that you need hugo **extended**, which is found at the bottom of the list of available files (which is located under the "assets" header).

The hugo theme is included as a git submodule. So when you clone the repo, be sure to include "--recursive", for example 

    git clone --recursive https://github.com/makehumancommunity/makehuman-static-website.git

To start a local hugo webserver on port 1313, run 

    hugo server -D 
    
.. in the root of the repo. This will automatically re-render all files when you make a change in the markdown code.
