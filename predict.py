import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
dele=pd.read_csv("deliveries.csv")
matches=pd.read_csv("matches.csv")
matches['match_id'] = matches['id']
matches = matches.drop('id', axis=1)
df = dele.merge(matches, on='match_id', how='left')
teams = set(df.team1.unique()).union(set(df.team2.unique()))
players = set(df.batsman.unique()).union(set(df.bowler.unique())).union(set(df.non_striker.unique()))
players=list(players)
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
train_data=df[(df['season']!=2008)].copy()
X1=train_data[['batting_team_e','bowling_team_e','batsman_e', 'non_striker_e', 'bowler_e', 'over', 'ball',
	    'inning']]
prob_out=cross_val_score(forest, X1, train_data.will_be_out, cv=10, scoring='roc_auc',n_jobs=-1).mean()
prob_four=cross_val_score(forest, X1, train_data.four, cv=10, scoring='roc_auc',n_jobs=-1).mean()
prob_six=cross_val_score(forest, X1, train_data.six, cv=10, scoring='roc_auc',n_jobs=-1).mean()
def predict_out(bat_team,bowl_team,batsman,bowler,nonstriker,over_no,ball_no,inning_no):
	
	
	y1=train_data['will_be_out']
	
	X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2, random_state=40)
	forest.fit(X_train,y_train)
	inp={'batting_team_e':batenc.transform([bat_team])[0],
		 'bowling_team_e':bowlenc.transform([bowl_team])[0],
		 'batsman_e':player_encoder.transform([batsman])[0],
		 'non_striker_e':player_encoder.transform([nonstriker])[0],
		 'bowler_e':player_encoder.transform([bowler])[0],
		 'over':over_no,
		 'ball':ball_no,
		 'inning':inning_no}
	inp1=pd.Series(inp)
	pr=forest.predict([inp1])
	# prob_out*=100
	if (False in pr):
	 	a={'chance':prob_out}
	 	return a
	else :
		a={'chance':prob_out}
		return a
def predict_four(bat_team,bowl_team,batsman,bowler,nonstriker,over_no,ball_no,inning_no):
	train_data=df[(df['season']!=2008)]
	
	y1=train_data['four']

	X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2, random_state=40)
	forest.fit(X_train,y_train)
	inp={'batting_team_e':batenc.transform([bat_team])[0],
		 'bowling_team_e':bowlenc.transform([bowl_team])[0],
		 'batsman_e':player_encoder.transform([batsman])[0],
		 'non_striker_e':player_encoder.transform([nonstriker])[0],
		 'bowler_e':player_encoder.transform([bowler])[0],
		 'over':over_no,
		 'ball':ball_no,
		 'inning':inning_no}
	inp1=pd.Series(inp)
	pr=forest.predict([inp1])
	# prob_four*=100
	if (False in pr):
	 	a={'chance':prob_four}
	 	return a
	else :
		a={'chance':prob_four}
		return a
def predict_six(bat_team,bowl_team,batsman,bowler,nonstriker,over_no,ball_no,inning_no):
	train_data=df[(df['season']!=2008)]
	
	y1=train_data['six']
	X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2, random_state=40)
	forest.fit(X_train,y_train)
	inp={'batting_team_e':batenc.transform([bat_team])[0],
		 'bowling_team_e':bowlenc.transform([bowl_team])[0],
		 'batsman_e':player_encoder.transform([batsman])[0],
		 'non_striker_e':player_encoder.transform([nonstriker])[0],
		 'bowler_e':player_encoder.transform([bowler])[0],
		 'over':over_no,
		 'ball':ball_no,
		 'inning':inning_no}
	inp1=pd.Series(inp)
	pr=forest.predict([inp1])
	# prob_six*=100
	if (False in pr):
	 	a={'chance':prob_six}
	 	return a
	else :
		a={'chance':prob_six}
		return a
# print(predict_out('Kolkata Knight Riders','Royal Challengers Bangalore','BB McCullum','SC Ganguly','P Kumar',1,3,1))


