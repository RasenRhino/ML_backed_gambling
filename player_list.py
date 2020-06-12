import numpy as np 
import pandas as pd 
dele=pd.read_csv("deliveries.csv")
matches=pd.read_csv("matches.csv")
matches['match_id'] = matches['id']
matches = matches.drop('id', axis=1)
df = dele.merge(matches, on='match_id', how='left')
def player_list_name(team1,team2,season):
	abc=df[(df['season']==season)&(((df['batting_team']==team1)&(df['bowling_team']==team2)) | ((df['batting_team']==team2)&(df['bowling_team']==team1)))]
	players = set(abc.batsman.unique()).union(set(abc.bowler.unique())).union(set(abc.non_striker.unique()))
	return list(players)
# print(len(player_list_name('Sunrisers Hyderabad','Mumbai Indians',2014)))