#!/usr/bin/env python3

from _general import get_mediawiki_db_page_list, chdir_to_root
import json, re

pages = get_mediawiki_db_page_list()
chdir_to_root()

with open("exportmap.json", "r") as json_file:
    exportmap = json.load(json_file)
    
for page in pages:
    category = str(page["category"])
    
    if category.isnumeric() and exportmap["settings"]["ignorePagesWithNumericCategory"]:
        continue
    
    if category in exportmap["settings"]["ignoreCategories"]:
        continue
    
    id = int(page["id"])
    already_exists = False
    for existing_page in exportmap["pages"]:
        if int(existing_page["id"]) == id:
            already_exists = True
            continue
    
    if already_exists:
        continue
    
    newpage = dict()
    newpage["id"] = int(page["id"])
    newpage["category"] = category
    
    filename = re.sub(r'[^a-zA-Z0-9_:]', "", page["title"])
    filename = re.sub(r'\:', "_", filename) + ".md"
    
    newpage["filename"] = str(filename).lower()
    newpage["target"] = ""
    
    title = re.sub(r'_', " ", page["title"])
    newpage["title"] = title
    exportmap["pages"].append(newpage)

with open("exportmap.json", "w") as json_file:
    json.dump(exportmap, json_file, indent=4, sort_keys=True)
    
