#!/usr/bin/env python3

"""
Created on Sat Feb 27 12:39:34 2021

@author: david_zhang
"""

import os

def get_rel_dir(script_path, rel_path):
    """Get  path to directory relative to the current script 
    
    @type script_path: str
    @param script_path: path to script obtained through '__file__'
    @type info: str
    @param info: Relative path from script_path to directory of interest. 
    @rtype: str
    @returns: Absolute path to directory of interest. 
    """
    
    # use a relative path to the script
    # to determine output path, to allow transferability between machines
    script_dir = os.path.dirname(script_path)
    rel_dir = os.path.join(script_dir, rel_path)
    
    # convert this back to absolute path for printing
    rel_dir = os.path.abspath(rel_dir)
    
    return rel_dir