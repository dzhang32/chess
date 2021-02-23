#!/usr/bin/env python3

"""
Created on Mon Feb 22 23:01:08 2021

@author: david_zhang
"""

import requests

def get_json(url):
    
    url_json = requests.get(url).json()
    
    return url_json

def get_player(user, type = "profile"):
    
    if type == "profile": 
        
        res = get_json('https://api.chess.com/pub/player/' + user)
    
    return res
    