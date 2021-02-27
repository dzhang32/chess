#!/usr/bin/env python3

"""
Created on Thu Feb 25 09:32:18 2021

@author: david_zhang
"""

import chessdotcom as cdc
import pandas as pd
import datetime as dt
import os
from tqdm import tqdm
import random

def main(iso, info, n, rel_results_dir):
    
    # use a relative path to the script
    # to determine output path, to allow transferability between machines
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    results_dir = os.path.join(script_dir, rel_results_dir)
    
    # convert this back to absolute path for printing
    results_dir = os.path.abspath(results_dir)
    
    print("Downloading %s players '%s' info to %s" % (iso, info, results_dir))
    
    players_info = get_country_players_info(iso, info, n)
    
    players_info.to_csv(results_dir + "/" + iso + "_players_" + info + "_" + 
                        dt.date.today().strftime("%d_%m_%Y") + ".csv", 
                        index = False)

def get_country_players_info(iso, info, n):
    """Retrieves one aspect of player profiles for all players in a country
    
    @type iso: str
    @param iso: ISO country code. 
    @type info: str
    @param info: A str of length 1, specifying the aspect of player info you 
    want to retrieve. 
    @rtype: DataFrame
    @returns: a DataFrame containing player info.
    """
    
    players = cdc.caller.get_country_players(iso).json["players"]

    players_info = []
    
    # select index of random n players
    player_indexes = random.sample(range(0, len(players)), n)
    
    for i in tqdm(player_indexes):
        
        player = cdc.caller.get_player_profile(players[i]).json
        players_info.append(player[info])
        
    players_info = pd.DataFrame({info: players_info})
    
    return players_info

if __name__ == "__main__":
    
    main(iso = "GB", info = "joined", n = 10000, rel_results_dir = "../data")
    main(iso = "IT", info = "joined", n = 10000, rel_results_dir = "../data")
    main(iso = "CO", info = "joined", n = 10000, rel_results_dir = "../data")
    main(iso = "CN", info = "joined", n = 10000, rel_results_dir = "../data")