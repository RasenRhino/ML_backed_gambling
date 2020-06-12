import numpy as np 
import pandas as pd 
dele=pd.read_csv("deliveries.csv")
matches=pd.read_csv("matches.csv")
matches['match_id'] = matches['id']
matches = matches.drop('id', axis=1)
df = dele.merge(matches, on='match_id', how='left')
def player_list_batsman(team,season):
	players = set(df.batsman.unique()).union(set(df.bowler.unique())).union(set(df.non_striker.unique()))
	return list(players)
