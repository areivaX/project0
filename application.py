from flask import Flask, render_template, request, session
from flask_session import Session
from datetime import date

app = Flask(__name__)


#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


#@app.route("/", methods=["GET", "POST"])
#def index():
#    if request.method == "POST":
#        note = request.form.get("note")
#        notes.append(note)
#
#    return render_template("index.html", notes=notes)

#I want to learn better ways to display data!

@app.route('/')
def index():
    today = date.today()
    return render_template("index.html", today=today)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/aprender')
def aprender():
    temas=['math','cs','French','Spanish','Japanese','German']
    return render_template("aprender.html",temas=temas)


@app.route('/covid')
def covid():
    #would be nice to have a form here that shows geographically relevant resources?

    return render_template("covid.html")
