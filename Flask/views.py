from flask import render_template
from datetime import datetime

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)
    
def buse_page():
    return render_template("buse.html")


def merve_page():
    return render_template("merve.html")


def pelin_page():
    return render_template("pelin.html")


def bora_page():
    return render_template("bora.html")


def atacan_page():
    return render_template("atacan.html")
