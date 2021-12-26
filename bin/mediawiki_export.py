#!/usr/bin/env python3

from _general import get_mediawiki_db_page_list, chdir_to_root
import json, re, os, shutil
from datetime import datetime
from pathlib import Path

now = datetime.now()

pages = get_mediawiki_db_page_list()
chdir_to_root()

with open("exportmap.json", "r") as json_file:
    exportmap = json.load(json_file)
    
quarantine = exportmap["settings"]["quarantineRoot"]

for source_page in pages:
    dest_page = None
    for page_map in exportmap["pages"]:
        if int(source_page["id"]) == int(page_map["id"]):
            dest_page = page_map
            continue
    
    if dest_page is None:
        continue
    
    if "ignore" in dest_page and dest_page["ignore"] == True:
        continue
    
    if not "target" in dest_page or dest_page["target"] == "":
        if not "exportUnmatchedToQuarantine" in exportmap["settings"] or not exportmap["settings"]["exportUnmatchedToQuarantine"]:
            continue
        dest_page["target"] = os.path.join(quarantine, dest_page["category"])
    
    if dest_page["filename"] == "index.md":
        dest_page["filename"] = "wiki_index.md"
        
    filename = os.path.join(dest_page["target"], dest_page["filename"])
    
    print(filename) 
        
    with open(filename, "w") as markdown_file:
        markdown_file.write("---\n")
        title = re.sub(r'"', "\\\"", str(source_page["title"]))
        title = re.sub(r'_', " ", title)
        markdown_file.write("title: \"" + title + "\"\n")
        #markdown_file.write("date: " + now.strftime('%Y-%m-%dT%H:%M:%SZ') + "\n")
        markdown_file.write("draft: false\n")
        markdown_file.write("---\n\n")        
        
        content = str(source_page["content"]).strip()
        
        content = re.sub(r'=== (.*) =+', r'### \1', content)
        content = re.sub(r'===(.*)=+', r'### \1', content)
        content = re.sub(r'== (.*) =+', r'## \1', content)
        content = re.sub(r'==(.*)=+', r'## \1', content)
        content = re.sub(r'= (.*) =+', r'# \1', content)
        content = re.sub(r'=(.*)=+', r'# \1', content)
        
        content = re.sub(r'\'\'\'(.*)\'\'\'', r'**\1**', content)
        
        content = re.sub(r'\[http([^ ]+) (.*)\]', r'[\2](http\1)', content)
        
        images_pattern = re.compile(r'\[\[File:([^ \|]+).*\]\]')
        images = images_pattern.findall(content)
        if len(images) > 0:
            for image in images:
                found_file = False
                for match in Path(exportmap["settings"]["imagesSource"]).rglob(image):
                    if not "thumb" in str(match):
                        shutil.copy(str(match), os.path.join(dest_page["target"], image))
                        found_file = True
                        #print(" -- " + str(match))
                if not found_file:
                    for match in Path(exportmap["settings"]["imagesSource"]).rglob(str(image).capitalize()):
                        if not "thumb" in str(match):
                            shutil.copy(str(match), os.path.join(dest_page["target"], image))
                            found_file = True
                            #print(" -- " + str(match))
                if not found_file:
                    print("-- Found no match for " + str(image) + "!")
                        
            #print(images)
        
        content = re.sub(r'\[\[File:([^ \|]+).*\]\]', r'\n\n![\1](\1)\n\n', content)
                
        markdown_file.write(content)

