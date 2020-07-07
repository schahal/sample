import datetime

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    """Default route for app

    Provides set of links to different routes and parts of the app

    Args:
        None

    Returns:
        Rendered homepage HTML
    """
    return render_template("index.html") 


@app.route("/isitnewyears")
def newyears():
    """Route to determine if it's New Year's

    Provides a prompt declaring whether or not it is New Year's Day 

    Args:
        None

    Returns:
        Rendered "Is It New Year's?" HTML
    """
    now = datetime.datetime.now()
    is_new_year = now.month == 1 and now.day == 1
    return render_template("newyears.html", new_year=is_new_year) 


@app.route("/<string:name>")
def cust_hello(name):
    """Catch-all route to print a greeting to passed-in route 

    Args:
        name - a string

    Returns:
        "Hello, <name>" salutation
    """
    name = name.capitalize()
    return f"Hello, {name}!"


@app.route("/greeting")
def greeting():
    """Route to provide form for a specific greeting 

    Prompts for your name 

    Args:
        None

    Returns:
        Rendered form HTML
    """
    return render_template("greeting.html") 


@app.route("/hello", methods=["GET", "POST"])
def hello():
    """Route to print specific salutation based on POSTed form

    Args:
        None

    Returns:
        Rendered "hello, <name>" HTML
    """
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)


@app.route("/notes", methods=["GET", "POST"])
def notes():
    """Note-taking route

    Keeps running list of all notes entered in the app's memory
    and displays them

    Args:
        None

    Returns:
        Rendered notes HTML
    """
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html", notes=session["notes"])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
