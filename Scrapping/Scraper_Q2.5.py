#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:26:00 2018

@author: JinMatthew
"""

#Scraper Q2.5

import json
import requests

from Yelp_Scrapper import read_api_key
from Yelp_Scrapper import yelp_api_fp

#data = """{
#  "total": 8228,
#  "businesses": [
#    {
#      "rating": 4,
#      "price": "$",
#      "phone": "+14152520800",
#      "id": "four-barrel-coffee-san-francisco",
#      "is_closed": false,
#      "categories": [
#        {
#          "alias": "coffee",
#          "title": "Coffee & Tea"
#        }
#      ],
#      "review_count": 1738,
#      "name": "Four Barrel Coffee",
#      "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
#      "coordinates": {
#        "latitude": 37.7670169511878,
#        "longitude": -122.42184275
#      },
#      "image_url": "http://s3-media2.fl.yelpcdn.com/bphoto/MmgtASP3l_t4tPCL1iAsCg/o.jpg",
#      "location": {
#        "city": "San Francisco",
#        "country": "US",
#        "address2": "",
#        "address3": "",
#        "state": "CA",
#        "address1": "375 Valencia St",
#        "zip_code": "94103"
#      },
#      "distance": 1604.23,
#      "transactions": ["pickup", "delivery"]
#    }
#  ],
#  "region": {
#    "center": {
#      "latitude": 37.767413217936834,
#      "longitude": -122.42820739746094
#    }
#  }
#}"""
#    
#data_json = json.loads(data)
#print(data_json)

def retrieve_json_from_yelp(api_key, term, location):
    headers = {'Authorization': 'Bearer %s' % api_key}
    yelp_api = 'https://api.yelp.com/v3/businesses/search'   
    params = {'term':term, 'location':location}
    
    response = requests.get(yelp_api, headers = headers, params = params)
    
    return response.content

# Scrap raw data from Yelp
raw_data = retrieve_json_from_yelp(read_api_key(yelp_api_fp), 'coffee', 'new york')
json_data = json.loads(raw_data)

url_list = [bs.get('url') for bs in json_data.get('businesses')]

