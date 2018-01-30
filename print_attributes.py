#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:20:45 2018

@author: JinMatthew
"""

# Print Attributes of an object

def print_attributes(obj):
    for atr in vars(obj):
        print(atr, getattr(obj, atr))
        