#!/usr/bin/env python3

from _general import get_mediawiki_db_page_list

pages = get_mediawiki_db_page_list()

for page in pages:
    print(str(page["id"]) + "\t" + str(page["category"]) + "\t" + page["title"])
    
