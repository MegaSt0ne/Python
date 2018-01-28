#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:59:59 2018

@author: JinMatthew
"""
import requests
import time

yelp_api_fp = '/Users/JinMatthew/Documents/CMU/18S/Practical Data Science/HW/HW1/yelp_api_key.txt'

def retrieve_html(url):
    # Send HTTP requests
    response = requests.get(url)
    # Return tuple status_code, HTML
    return (response.status_code, response.content)


def read_api_key(filepath):
    """
    Read the Yelp API Key from file.
    
    Args:
        filepath (string): File containing API Key
    Returns:
        api_key (string): The API Key
    """
    
    # feel free to modify this function if you are storing the API Key differently
    with open(filepath, 'r') as f:
        return f.read().replace('\n','')
 

def all_restaurants(api_key, query):
    """
    Retrieve ALL the restaurants on Yelp for a given query.

    Args:
        query (string): Search term

    Returns:
        results (list): list of dicts representing each business
    """
    # Write solution here
    # Parameters
    yelp_url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization':'Bearer %s' % api_key}
    
    # Initialize restaurant list
    restaurant_list = []
    
    # Send request to yelp API
    i = 0
    while True:
        params = {'term':'restaurant', 'location':query, 'limit': 20, 'offset': 20 * i}
        response = requests.get(yelp_url, headers = headers, params = params)
        
        # If requests are successfully sent
        if response.status_code == 200:
            restaurant_list.extend(response.json().get('businesses'))
            print(response.json().get('total'), i * 20)
        
            # If all the data have been scrapped, then exit loop
            if (response.json().get('total') < i * 20 ) or ((i + 1) * 20 >= 1000):
                break
            else:
                i += 1  
        else:
            break
    # Return results
    return restaurant_list
    
## Variables
#filepath = '/Users/JinMatthew/Documents/CMU/18S/Practical Data Science/HW/HW1/yelp_api_key.txt'
#api_key = read_api_key(filepath)
#restaurant_list = all_restaurant(api_key, 'restaurant', 'polish hill, pittsburgh')
##print(restaurant_list)
#print(list(map(lambda x: x['name'], restaurant_list)))
    
all_restaurants(read_api_key(yelp_api_fp), '5aushufosahdfa')
