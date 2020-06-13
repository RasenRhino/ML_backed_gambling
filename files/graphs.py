import numpy as np # linear algebra
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as mlt
matches=pd.read_csv('matches.csv')   
delivery=pd.read_csv('deliveries.csv')
def toss_plot(team1,team2):
	toss_data1=matches[(matches['team1']==team1)]
	toss_data2=matches[(matches['team2']==team2)]
	mlt.subplots(figsize=(10,6))
	tossplot1=sns.countplot(x='season',hue='toss_decision',data=toss_data1)
	mlt.title(team1)
	fig=tossplot1.get_figure()
	fig.savefig("tossplot_team1.png")
	mlt.subplots(figsize=(10,6))
	tossplot2=sns.countplot(x='season',hue='toss_decision',data=toss_data2)
	mlt.title(team2)
	fig=tossplot2.get_figure()
	fig.savefig("tossplot_team2.png")
toss_plot('Sunrisers Hyderabad','Royal Challengers Bangalore')