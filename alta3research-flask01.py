#!/usr/bin/env python3
""" A script to demonstrate proficiency with the flask library """
import json

import requests
from flask import Flask, jsonify  # python3 -m pip install flask
from flask import render_template
from flask import request  # python3 -m pip install requests
from datetime import date, datetime, time  # python3 -m pip install datetime

# create an app object from Flask
app = Flask(__name__)

sde_apprenticeship = [{'course': 'java',
                       'duration': 'six weeks',
                       'projects': 1,
                       'labs': 40,
                       'instructor': {'name': 'Nick',
                                      'email': 'nick@example.com'}
                       },
                      {'course': 'javascript',
                       'duration': 'four weeks',
                       'projects': 1,
                       'labs': 10,
                       'instructor': {'name': 'Nelly',
                                      'email': 'nelly@example.com'}

                       },
                      {'course': 'python',
                       'duration': 'two weeks',
                       'projects': 3,
                       'labs': 100,
                       'instructor': {'name': 'Jason',
                                      'email': 'jason@example.com'}

                       },
                      {'course': 'data structure and alg',
                       'duration': 'one week',
                       'projects': 0,
                       'labs': 0,
                       'instructor': {'name': 'Sang',
                                      'email': 'sang@example.com'}

                       }
                      ]


# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
# This is a landing point for users (a start)
@app.route("/")
def index():
    return render_template("home.html")


# flask endpoint to display available display greeting message for 'nm'
@app.route('/user', methods=['POST'])
def user():
    # grab the value of nm from the POST
    name = request.form['nm']
    # render the jinja template "username.html"
    # apply the value of name for the var name
    return render_template("username.html", name=name)


# flask endpoint to display available courses
@app.route("/course")
def course():
    # create a list of available courses
    courses = ["Java", "JavaScript", "Python", "HTML/CSS"]
    # render the jinja template "course.html"
    # apply the value of courses for the var courses
    return render_template("course.html", courses=courses)


# flask endpoint to display json data for current date and time
@app.route("/date")
def getdate():
    # jsonify current date and current time
    return jsonify({"current_date": date.today()}, {"current_time": datetime.now().strftime("%H:%M:%S")})


# flask endpoint to display json data for the list sde_apprenticeship
@app.route("/json", methods=["GET", "POST"])
def getjson():
    # if user generates a POST to our API
    if request.method == "POST":
        data = request.json
        if data:
            data = json.loads(data)
            course = data["course"]
            duration = data["duration"]
            projects = data["projects"]
            labs = data["labs"]
            instructor = data["instructor"]
            sde_apprenticeship.append(
                {"course": course, "duration": duration, "projects": projects, "labs": labs, "instructor": instructor})
    return jsonify(sde_apprenticeship)


# invoke the main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
