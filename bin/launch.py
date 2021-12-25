#!/usr/bin/env python3

from _general import find_hugo, chdir_to_root
import subprocess

hugo = find_hugo()

chdir_to_root()
subprocess.run([hugo, "server", "-D"])

