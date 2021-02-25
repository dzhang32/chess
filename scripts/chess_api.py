#!/usr/bin/env python3

"""
Created on Mon Feb 22 23:01:08 2021

@author: david_zhang
"""

import requests

def get_json(url):
    """Retrieves JSON data from URL in a list format

    @type url: str
    @param url: URL of interest. 
    @rtype: list
    @returns: a list containing the queried JSON data.
    """
    
    url_json = requests.get(url).json()
    
    return url_json

def get_player(user, which = "profile"):
    """Obtains the chess.com data for a particular player

    @type user: user
    @param user: username of the player of interest. 
    @type which: str
    @param which: which kind of data to to be downloaded.
    @rtype: list
    @returns: a list containing the chess.com players info. 
    """
    
    if which == "profile": 
        
        res = get_json('https://api.chess.com/pub/player/' + user)
    
    return res
    