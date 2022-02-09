#!/usr/bin/env python3

from _general import chdir_to_root
import subprocess, sys, os, re

chdir_to_root()

if len(sys.argv) != 3:
    print("Wrong number of arguments")
    sys.exit(1)

page_file = sys.argv[1]
dest_dir = sys.argv[2]
source_dir = os.path.dirname(page_file)

if not os.path.exists(page_file):
    print(page_file + " does not exist")
    sys.exit(1)
    
if not os.path.exists(dest_dir):
    print(dest_dir + " does not exist")
    sys.exit(1)
    
print("Moving files from " + source_dir + " to " + dest_dir + "\n")

pattern = re.compile(r"!\[[^\]]+\]\((.*)\)")

with open(page_file, "r") as text_file:
    for line in text_file:
        if "![" in line:
            match = pattern.match(line)
            if match:
                image_file = os.path.join(source_dir, match.group(1))
                print(image_file + " -> " + dest_dir)
                subprocess.run(["git", "mv", image_file, dest_dir])
                
print(page_file + " -> " + dest_dir)
subprocess.run(["git", "mv", page_file, dest_dir])
                  

