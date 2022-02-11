#!/usr/bin/env python3

from _general import find_hugo, chdir_to_root
import subprocess, os

hugo = find_hugo()

chdir_to_root()
subprocess.run(["rm -rf dist/* build/*"], shell=True)
subprocess.run([hugo, "-D"])
os.chdir("build")
#subprocess.run(["tar", "cvzf", "../dist/static.tgz", "."])
subprocess.run(["rsync", "-avz", "-e", "ssh", "./", "joepal@static.makehumancommunity.org:~/static/"])

