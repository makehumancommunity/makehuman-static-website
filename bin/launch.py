#!/usr/bin/env python3

from _general import find_hugo
import subprocess

hugo = find_hugo()

subprocess.run([hugo, "server", "-D"])

