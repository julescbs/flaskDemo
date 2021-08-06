import datetime
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/hello", methods=["POST"])
def compute_age():
    name = request.form.get('name')
    birthday = request.form.get('birthday')
    birthDatetime = datetime.datetime(int(birthday[0:4]), int(birthday[5:7]), int(birthday[8:10]))
    birthTimeDelta = datetime.datetime.now() - birthDatetime
    age = str(birthTimeDelta.days)+" days"
    #flask's templating system defangs user text inputs automatically
    #this method returns a rendered version of the template specified in profile.html
    return render_template(
        "profile.html",
        name=name,
        age=age)