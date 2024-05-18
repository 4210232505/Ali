from proje import app
from flask import render_template
from proje.models import hassan


@app.route("/")
def home():
    return render_template("log.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")



@app.route("/weather")
def weather():
    return render_template("weather.html")



@app.route("/my")
def my():
    a = hassan.query.all()
    return render_template("my.html",a=a)