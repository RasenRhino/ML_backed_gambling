import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.preprocessing import LabelEncoder
dele=pd.read_csv("deliveries.csv")
matches=pd.read_csv("matches.csv")
matches['match_id'] = matches['id']
matches = matches.drop('id', axis=1)
df = dele.merge(matches, on='match_id', how='left')
#encoders
batenc = LabelEncoder()
bowlenc=LabelEncoder()
player_encoder = LabelEncoder()
venue_encoder = LabelEncoder()
batenc.fit(df['batting_team'])
bowlenc.fit(df['bowling_team'])
player_encoder.fit(players)
venue_encoder.fit(df.venue)
#adding encoded values to data
df['batting_team_e']=batenc.transform(df['batting_team']).copy()
df['bowling_team_e']=bowlenc.transform(df['bowling_team']).copy()
df['venue_e'] = venue_encoder.transform(df.venue)
df['batsman_e'] = player_encoder.transform(df.batsman)
df['non_striker_e'] = player_encoder.transform(df.non_striker)
df['bowler_e'] = player_encoder.transform(df.bowler)
y = df.total_runs * ((~df.player_dismissed.isnull()).map({True: -1, False: 1}))
#making classes
df['will_be_out'] = y<0
df['four']= (y==4)
df['six']= (y==6)
forest = RandomForestClassifier(n_jobs=-1)

def predict(bat_team,bowl_team,season,batsman,nonstriker,bowler,over,bowl,inning):
	match_data=df[(df['batting_team']==bat_team)&(df['bowling_team']==bowl_team)&(df['season']==season)]
	players = set(match_data.batsman.unique()).union(set(match_data.bowler.unique())).union(set(match_data.non_striker.unique()))
	player_encoder = LabelEncoder()
	venue_encoder = LabelEncoder()
	batenc = LabelEncoder()
	bowlenc=LabelEncoder()
	player_encoder.fit(players)
	venue_encoder.fit(df.venue)