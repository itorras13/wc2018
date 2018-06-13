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


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        success = submit_quiniela(request)
        if success:
            print("success")
            from_email = Email(
                "itorras13sub@gmail.com", "Ignacio Torras")

            email = str(request.form['email'])
            to_email = Email(
                email, str(request.form['first_name']) + " " +
                str(request.form['last_name']))

            subject = 'World Cup 18 Submission Confirmed'

            submission = get_last_submission(email)
            html = render_template('email_template.html',
                                   sub=submission, email=email)
            content = Content("text/html", html)

            mail = Mail(from_email, subject, to_email, content)
            # mail.personalizations[0].add_to(Email("itorras13@gmail.com"))
            mail.personalizations[0].add_bcc(
                Email("itorras13+wc2018@gmail.com"))

            response = sg.client.mail.send.post(request_body=mail.get())
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


def get_last_submission(email):
    return Submission.query.filter_by(email=email).order_by(
        Submission.submission_number.desc()).first()


def get_submissions(type):
    submissions = Submission.query.order_by(
        Submission.publish_date.desc()).all()
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
            # new_sub['winner'] = sub.final
            new_sub['winner'] = '---'
            new_sub['points'] = sub.points
            new_sub['paid'] = sub.paid
            new_sub['id'] = sub.id
            updated_submissions.append(new_sub)
        return updated_submissions


def submit_quiniela(request):
    email = request.form['email']
    subs = db.session.query(Submission).filter(
        Submission.email == email).count()
    if subs < 3:
        new = Submission(
            request.form['first_name'], request.form['last_name'], email,
            subs + 1, request.form["residence"], request.form["a1h"],
            request.form["a1a"], request.form["a2h"], request.form["a2a"],
            request.form["a3h"], request.form["a3a"], request.form["a4h"],
            request.form["a4a"], request.form["a5h"], request.form["a5a"],
            request.form["a6h"], request.form["a6a"], request.form["b1h"],
            request.form["b1a"], request.form["b2h"], request.form["b2a"],
            request.form["b3h"], request.form["b3a"], request.form["b4h"],
            request.form["b4a"], request.form["b5h"], request.form["b5a"],
            request.form["b6h"], request.form["b6a"], request.form["c1h"],
            request.form["c1a"], request.form["c2h"], request.form["c2a"],
            request.form["c3h"], request.form["c3a"], request.form["c4h"],
            request.form["c4a"], request.form["c5h"], request.form["c5a"],
            request.form["c6h"], request.form["c6a"], request.form["d1h"],
            request.form["d1a"], request.form["d2h"], request.form["d2a"],
            request.form["d3h"], request.form["d3a"], request.form["d4h"],
            request.form["d4a"], request.form["d5h"], request.form["d5a"],
            request.form["d6h"], request.form["d6a"], request.form["e1h"],
            request.form["e1a"], request.form["e2h"], request.form["e2a"],
            request.form["e3h"], request.form["e3a"], request.form["e4h"],
            request.form["e4a"], request.form["e5h"], request.form["e5a"],
            request.form["e6h"], request.form["e6a"], request.form["f1h"],
            request.form["f1a"], request.form["f2h"], request.form["f2a"],
            request.form["f3h"], request.form["f3a"], request.form["f4h"],
            request.form["f4a"], request.form["f5h"], request.form["f5a"],
            request.form["f6h"], request.form["f6a"], request.form["g1h"],
            request.form["g1a"], request.form["g2h"], request.form["g2a"],
            request.form["g3h"], request.form["g3a"], request.form["g4h"],
            request.form["g4a"], request.form["g5h"], request.form["g5a"],
            request.form["g6h"], request.form["g6a"], request.form["h1h"],
            request.form["h1a"], request.form["h2h"], request.form["h2a"],
            request.form["h3h"], request.form["h3a"], request.form["h4h"],
            request.form["h4a"], request.form["h5h"], request.form["h5a"],
            request.form["h6h"], request.form["h6a"],
            request.form["a1"], request.form["a2"],
            request.form["b1"], request.form["b2"], request.form["c1"],
            request.form["c2"], request.form["d1"], request.form["d2"],
            request.form["e1"], request.form["e2"], request.form["f1"],
            request.form["f2"], request.form["g1"], request.form["g2"],
            request.form["h1"], request.form["h2"], request.form["r1"],
            request.form["r2"], request.form["r3"], request.form["r4"],
            request.form["r5"], request.form["r6"], request.form["r7"],
            request.form["r8"], request.form["q1"], request.form["q2"],
            request.form["q3"], request.form["q4"], request.form["s1"],
            request.form["s2"], request.form["third"], request.form["final"],
            request.form["golden_glove"], request.form["golden_boot"],
            request.form["golden_ball"])
        db.session.add(new)
        db.session.commit()
        return True
    return False


if __name__ == "__main__":
    # app.debug = True
    app.run()
