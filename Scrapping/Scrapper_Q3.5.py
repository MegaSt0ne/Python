#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:15:47 2018

@author: JinMatthew
"""

from Scraper_Q3 import parse_page
from Scraper_Q2 import retrieve_html

# import url address
url = 'https://www.yelp.com/biz/phipps-conservatory-and-botanical-gardens-pittsburgh'

def extract_review(url):
    # Write solution here
    data = []
    while True:
        if url is None:
            break
        else:
            ndata, url = parse_page(retrieve_html(url)[1])
            data.extend(ndata)
    
    return data

print(extract_review(url))