from flask import Flask, render_template
from datetime import datetime
from flask import current_app
from database import Database

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)
    
def buse_page():
    return render_template("buse.html")


def merve_page():
    return render_template("merve.html")


def pelin_page():
    db = current_app.config["dbconfig"]
    kickoff = db.get_all_kickoff_stats()
    return render_template("pelin.html", kickoff_db = kickoff)


def bora_page():
    return render_template("bora.html")


def atacan_page():
    return render_template("atacan.html")
