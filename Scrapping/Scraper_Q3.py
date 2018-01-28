#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:24:44 2018

@author: JinMatthew
"""

#Scraper_Q3

import requests
from bs4 import BeautifulSoup
#import re

html = 'https://www.yelp.com/biz/central-park-new-york?osq=central+park+coffee'

def parse_page(html):
    """
    Parse the reviews on a single page of a restaurant.
    
    Args:
        html (string): String of HTML corresponding to a Yelp restaurant

    Returns:
        tuple(list, string): a tuple of two elements
            first element: list of dictionaries corresponding to the extracted review information
            second element: URL for the next page of reviews (or None if it is the last page)
    """
    
    # Write solution here
    par_html = BeautifulSoup(html, 'html.parser')
    
    nlist = []
    for div in par_html('div', 'review review--with-sidebar'):
        ndict = {}
        ndict['review_id'] = div.get('data-review-id')
#        ndict['user_id'] = re.search(r'(user_id:)(\w*)', div.get('data-signup-object'))[2]
        ndict['user_id'] = div.get('data-signup-object').replace("user_id:", "")

        for img in div('img', 'offscreen'):
            ndict['rating'] = float(img.get('alt').split()[0])
        for span in div('span', 'rating-qualifier'):
            ndict['date'] = span.text.strip()
        for div in div('div', 'review-content'):          
            for p in div('p'):
                ndict['text'] = p.text.strip()   
        nlist.append(ndict)
    
    # Get the last page number
    for div in par_html('div', 'review-pager'):
        for subdiv in div('div', 'page-of-pages arrange_unit arrange_unit--fill'):
            npg = int(subdiv.text.strip().split()[-1])
        for subdiv in div('div', 'arrange_unit page-option current'):
            cpg = int(subdiv.text.strip())
            print('Parsing', cpg, 'page')

    # if current page number equals the last page number
    if npg == cpg:
        url = None
    else:
        for subdiv in div('div', 'arrange_unit page-option'):
            if int(subdiv.text.strip()) == (cpg + 1):
                url = subdiv.a.get('href')
                
    # Return results
    return (nlist, url)  

#mylist, myurl = parse_page(html)
#print(mylist[:2], myurl)

    
    