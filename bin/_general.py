#!/usr/bin/env python3

import shutil

def find_hugo(crash_if_not_found=True):
    loc = shutil.which("hugo1")
    if not loc and crash_if_not_found:
        print("\n\nHugo does not seem to be available. Download it from https://github.com/gohugoio/hugo/releases\n")
        print("Be sure to get the \"hugo extended\" binary from the bottom of the list of available binaries.\n\n")
        raise IOError("Hugo is not installed, see message above")
    return loc

