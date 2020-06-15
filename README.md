## ML Backed Betting
To install dependencies 

    pip3 install -r requitements.txt
    
At present we have 2 models for wicket prediction

 - Ball by ball wicket prediction running in flask app
 - Wicket prediction in +1, +2, +3, +4 over, given the current over

To run the flask app run

     python3 app.py
and go to `localhost:5050` as the webapp is running on port 5050. The prediction model had a ROC-AUC score of 60.54

## For Wicket prediction in +1, +2, +3, +4 over, given the current over (Will soon be added to the flask app)
Download the files from the WicketBetting folder

To install dependencies, run the following command

pip install -r requitements.txt

Then, run the following command: python predict.py

Input for this is: 
bowler='R Bhatia'
batsman='TS Mills'
non_striker='Yuvraj Singh'
over=5
tot_wicket_till_now=1
over_last_wicket=1


Output will look look this:

Probability of a wicket in  6  over is:  0.6
Probability of a wicket in  7  over is:  0.5
Probability of a wicket in  8  over is:  0.5
Probability of a wicket in  9  over is:  0.51
