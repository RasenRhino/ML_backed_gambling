import numpy as np 
import pandas as pd 
dele=pd.read_csv("matches.csv")
def teamname_list():
	teams = set(dele.team1.unique()).union(set(dele.team2.unique()))
	return list(teams)