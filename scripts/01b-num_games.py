#!/usr/bin/env python3

"""
Created on Sat Feb 27 09:44:40 2021

@author: david_zhang
"""
import utils
import chessdotcom as cdc
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
import os

def main(iso, start_date, n_months, rel_results_dir):
    
    # use the joined data downloaded in 01a-num_new_players
    # which contains player users 
    results_dir = utils.get_rel_dir(__file__, rel_results_dir)
    joined_data = [path for path in os.listdir(results_dir) 
                   if iso + "_players_joined" in path]
    
    # parse joined as date time
    dp = lambda x: dt.datetime.fromtimestamp(int(x))
    joined_data = pd.read_csv(results_dir + "/" + joined_data[0], 
                              parse_dates = ["joined"], 
                              date_parser = dp)
    
    # keep only user's that have joined before the start date
    joined_data = joined_data[joined_data["joined"] <= start_date].copy()
    usernames = list(joined_data["user"])
    
    print("Downloading N games of %s players to %s" % (iso, results_dir))
    
    n_games_all = list()
    
    for i in tqdm(range(len(usernames))):
        
        n_games = get_n_games_window(usernames[i], start_date, n_months)
        n_games_all.append(n_games)
        
    n_games_all = pd.concat(n_games_all).reset_index(drop = True)
    
    n_games_all.to_csv(results_dir + "/" + iso + "_n_games_" + 
                       dt.date.today().strftime("%d_%m_%Y") + ".csv", 
                       index = False)
    
    return n_games_all
        
def get_n_games_window(username, start_date, n_months):

    n_games = {}
    
    for i in range(n_months):
        
        date_of_interest = start_date + relativedelta(months = i)
        date_of_interest_str = dt.datetime.strftime(date_of_interest, "%Y_%m")
        
        games = cdc.caller.get_player_games_by_month(
            username, 
            datetime_obj = date_of_interest
            )
        games = games.json 
        
        n_games[date_of_interest_str] = len(games["games"])
        
    n_games = pd.DataFrame({"username": username, 
                            "month": n_games.keys(), 
                            "n_games": n_games.values()})
    
    return n_games

if __name__ == "__main__":
    
    # set start date as 1 month before QG release
    start_date = dt.datetime.strptime("2020-09-01", "%Y-%m-%d")
    
    main("GB", start_date, 5, "../data")
    