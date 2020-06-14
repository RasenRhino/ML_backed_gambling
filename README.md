## ML Backed Betting
To install dependencies 

    pip3 install -r requitements.txt
    
At present we have 2 models for wicket prediction

 - Ball by ball wicket prediction running in flask app
 - Wicket prediction in current over

To run the flask app run

     python3 app.py
and go to `localhost:5050` as the webapp is running on port 5050. The prediction model had a ROC-AUC score of 60.54

For wicket prediction in current over , run the project in jupyter notebook and open `predict.ipynb` and enter your inputs in the function. Will soon be added to the flask app.

