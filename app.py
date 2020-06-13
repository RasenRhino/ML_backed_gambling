import os
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

# util functions
from predict.team_list import teamname_list
from predict.player_list import player_list_name
from predict.prediction import predict_four, predict_six, predict_out

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello its me'

# create app instance
app = Flask(__name__)
app.config.from_object(Config)

# some init functions
teams = teamname_list()

# forms
class PreForm(FlaskForm):
    team1 = SelectField('Batting Team', validators=[DataRequired()])
    team2 = SelectField('Bowling Team', validators=[DataRequired()])
    season = IntegerField('Season', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])

class PredictionForm(FlaskForm):
    batsman = SelectField('Batsman Name', validators=[DataRequired()])
    batsman_ns = SelectField('Non-Striker Batsman Name', validators=[DataRequired()])
    bowler = SelectField('Bowler Name', validators=[DataRequired()])
    over = IntegerField('Over', validators=[DataRequired()])
    ball = IntegerField('Ball', validators=[DataRequired()])
    inning = IntegerField('Innings', validators=[DataRequired()]) 
    submit = SubmitField('Submit', validators=[DataRequired()])

# routes
@app.route('/', methods=['GET', 'POST'])
def home():
    form = PreForm()
    form.team1.choices = [(team) for team in teams]
    form.team2.choices = [(team) for team in teams]
    if form.is_submitted():
        print(form.errors)
        return redirect(url_for('predict', 
                season=form.season.data, team1=form.team1.data, team2=form.team2.data))
    # TODO : validations
    # if form.validate_on_submit():
    #     print(form.season.data)
    #     print(form.team1.data + form.team2.data)
    #     return redirect(url_for('predict', 
    #             season=form.season.data, team1=form.team1.data, team2=form.team2.data))
    return render_template('home.html', form=form, teams=teams)

# TODO: encode strings in request
@app.route('/predict/<int:season>/<team1>_<team2>', methods=['GET', 'POST'])
def predict(season, team1, team2):
    form = PredictionForm()
    players = player_list_name(team1, team2, season) 
    form.batsman.choices = [(player) for player in players]
    form.batsman_ns.choices = [(player) for player in players]
    form.bowler.choices = [(player) for player in players]
    # TODO: validations
    if form.is_submitted():
        predictions = {
            'four': predict_four(team1, team2, form.batsman.data, form.bowler.data, form.batsman_ns.data, form.over.data, form.ball.data, form.inning.data),   
            'six': predict_six(team1, team2, form.batsman.data, form.bowler.data, form.batsman_ns.data, form.over.data, form.ball.data, form.inning.data),   
            'out': predict_out(team1, team2, form.batsman.data, form.bowler.data, form.batsman_ns.data, form.over.data, form.ball.data, form.inning.data),   
        }
        return render_template('predict.html', 
                form=form, season=season, team1=team1, team2=team2, predictions=predictions)
    return render_template('predict.html', form=form, season=season, team1=team1, team2=team2)

# start server
if __name__ == '__main__':
    print(teamname_list())
    app.run(host='0.0.0.0', port=5050, debug=True)

