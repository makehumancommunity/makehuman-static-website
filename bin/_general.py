#!/usr/bin/env python3

import shutil, os, MySQLdb, json, re

def find_hugo(crash_if_not_found=True):
    loc = shutil.which("hugo")
    if not loc and crash_if_not_found:
        print("\n\nHugo does not seem to be available. Download it from https://github.com/gohugoio/hugo/releases\n")
        print("Be sure to get the \"hugo extended\" binary from the bottom of the list of available binaries.\n\n")
        raise IOError("Hugo is not installed, see message above")
    return loc

def chdir_to_root():
    loc = os.path.dirname(__file__)
    parent = os.path.join(loc, "..")
    root = os.path.abspath(parent)
    os.chdir(root)

def get_mediawiki_db_page_list():
    CATEGORIES = {
        0: "UNCATEGORIZED",
        6: "IMAGE",    
        3000: "DOCUMENTATION",
        3002: "FAQ"
        }
    
    db = MySQLdb.connect("localhost","mediawiki","mediawiki123","mediawiki")
     
    # This join will exclude images, since they have no content text
    sql = """
    select 
      page.page_id,
      page.page_namespace, 
      page.page_title,
      convert(text.old_text using utf8) as content_text
    from 
      page,
      revision,
      text 
    where 
      page.page_latest = revision.rev_id 
      and revision.rev_text_id = text.old_id 
    order by
      page_namespace,
      page_title;"""
    
    cursor = db.cursor()
    cursor.execute(sql)
    
    result = cursor.fetchall()
    
    pages = []
    
    for row in result:
        item = dict()
        item["id"] = row[0];
        item["category"] = row[1];
        if item["category"] or item["category"] == 0:
            if int(item["category"]) in CATEGORIES:
                item["category"] = CATEGORIES[int(item["category"])]
        item["title"] = row[2]
        item["content"] = row[3]
        pages.append(item)
    
    db.close()
    
    return pages