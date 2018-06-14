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


@app.route('/')
def index():
    submissions = get_submissions("index")
    return render_template('index.html', submissions=addPlace(submissions))


# @app.route('/show', defaults={'email': None})
@app.route('/show/<id>')
def show(id):
    sub = Submission.query.filter_by(id=id).first()
    return render_template('show.html', sub=sub)





@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))



def get_submissions(type):
    submissions = Submission.query.order_by(
        Submission.first_name.asc(),Submission.last_name.asc(),Submission.submission_number.asc()).all()
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
            updated_submissions.append(new_sub)
        return updated_submissions





if __name__ == "__main__":
    # app.debug = True
    app.run()
