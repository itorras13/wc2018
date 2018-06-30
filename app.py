from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import socket
import sendgrid
import operator
from sendgrid.helpers.mail import *
from sendgrid import *
import ssl
import math


ssl._create_default_https_context = ssl._create_unverified_context

# SendGrid
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_KEY'))


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
from models import Submission


def addPlace(submissions):
    index = 0
    place = 0
    prevValue = 9999
    for submission in submissions:
        index += 1
        if submission['points'] != prevValue:
            place = index
        prevValue = submission['points']
        submission['place'] = place
    return submissions

def pointsPossible(sub):
    quarter_possibilities = [['Uruguay', 'Portugal'],
                             ['Brazil', 'Mexico'], ['Belgium','Japan'], 
                             ['Spain', 'Russia'], ['Croatia', 'Denmark'], 
                             ['Sweden', 'Switzerland'], ['Colombia', 'England']]
    semi_possibilities = [['Uruguay', 'Portugal', 'France'], 
                            ['Brazil', 'Mexico', 'Belgium', 'Japan'], 
                            ['Spain', 'Russia', 'Croatia', 'Denmark'],
                            ['Sweden', 'Switzerland', 'Colombia', 'England']]
    final_possibilities = [['Uruguay', 'Portugal', 'France'
                            ,'Brazil', 'Mexico', 'Belgium', 'Japan'], 
                            ['Spain', 'Russia', 'Croatia', 'Denmark',
                            'Sweden', 'Switzerland', 'Colombia', 'England']]
    all_left = ['Uruguay', 'Portugal', 'France'
                ,'Brazil', 'Mexico', 'Belgium', 'Japan', 
                'Spain', 'Russia', 'Croatia', 'Denmark',
                'Sweden', 'Switzerland', 'Colombia', 'England']
    quarters = [sub.r1, sub.r2, sub.r3, sub.r4, sub.r5, sub.r6, sub.r7, sub.r8]
    semis = [sub.q1, sub.q2, sub.q3, sub.q4]
    finalists = [sub.s1, sub.s2]
    winner = sub.final
    third = sub.third
    points = 0
    for rGame in quarter_possibilities:
        for team in rGame:
            if team in quarters:
                points += 6
                break
    for qGame in semi_possibilities:
        for team in qGame:
            if team in semis:
                points += 9
    for sGame in final_possibilities:
        for team in sGame:
            if team in finalists:
                points += 12
    if winner in all_left:
        points += 25
    if third in all_left:
        points += 6
    points += 18
    return points
            

@app.route('/')
def index():
    submissions = get_submissions("index")
    return render_template('index.html', submissions=addPlace(submissions), pot = len(submissions) * 50 - 100)


# @app.route('/show', defaults={'email': None})
@app.route('/show/<id>')
def show(id):
    sub = Submission.query.filter_by(id=id).first()
    submissions = get_submissions("index")
    placedSubs = addPlace(submissions)
    for placedSub in placedSubs:
        if placedSub['id'] == sub.id:
            place = placedSub['place']
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

            return render_template('show.html', sub=sub, place = ordinal(place))
    return render_template('show.html', sub=sub, place = " ")





@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))



def get_submissions(type):
    submissions = Submission.query.order_by(
        Submission.points.desc(),Submission.first_name.asc(),Submission.last_name.asc(),Submission.submission_number.asc()).all()
    if type == "show":
        return submissions
    else:
        updated_submissions = []
        for sub in submissions:
            new_sub = {}
            new_sub['email'] = sub.email
            sub_num = sub.submission_number
            if sub_num > 1:
                new_sub['name'] = sub.first_name + ' ' + \
                    sub.last_name + ' ' + str(sub_num)
            else:
                new_sub['name'] = sub.first_name + ' ' + sub.last_name
            new_sub['sub_num'] = sub_num
            new_sub['winner'] = sub.final
            new_sub['points'] = sub.points
            new_sub['paid'] = sub.paid
            new_sub['id'] = sub.id
            new_sub['left'] = pointsPossible(sub) + sub.points
            updated_submissions.append(new_sub)
        return updated_submissions





if __name__ == "__main__":
    # app.debug = True
    app.run()
