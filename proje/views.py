from flask import Flask, render_template
from datetime import datetime
from flask import current_app
from database import Database


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def buse_page():
    db = current_app.config["dbconfig"]
    punting = db.get_all_punting_stats()
    return render_template("buse.html", punting_db = punting)

def merve_page():
    db = current_app.config["dbconfig"]
    defensive = db.get_all_defensive_stats()
    return render_template("merve.html", defensive_db = defensive)

def pelin_page():
    db = current_app.config["dbconfig"]
    kickoff = db.get_all_kickoff_stats()
    return render_template("pelin.html", kickoff_db = kickoff)

def bora_page():
    db = current_app.config["dbconfig"]
    passing = db.get_all_passing_stats()
    return render_template("bora.html", passing_db=passing)

def atacan_page():
    db = current_app.config["dbconfig"]
    receiving = db.get_all_receiving_stats()
    return render_template("atacan.html", receiving_db = receiving)

def basicStats_page():
    return render_template("basicStats.html")

def delete_receiving(receiving_id):
    db = current_app.config["dbconfig"]
    db.dlt_receiving(receiving_id)
    receiving = db.get_all_receiving_stats()
    return render_template("atacan.html", receiving_db = receiving)

def delete_defensive(defensive_id):
    db = current_app.config["dbconfig"]
    db.dlt_defensive(defensive_id)
    defensive = db.get_all_defensive_stats()
    return render_template("merve.html", defensive_db = defensive)

def delete_kickoff(kickoff_id):
    db = current_app.config["dbconfig"]
    db.dlt_kickoff(kickoff_id)
    kickoff = db.get_all_kickoff_stats()
    return render_template("pelin.html", kickoff_db = kickoff)

def delete_punting(punting_id):
    db = current_app.config["dbconfig"]
    db.dlt_punting(punting_id)
    punting = db.get_all_punting_stats()
    return render_template("buse.html", punting_db = punting)

def delete_passing(passing_id):
    db = current_app.config["dbconfig"]
    db.dlt_passing(passing_id)
    passing = db.get_all_passing_stats()
    return render_template("bora.html", passing_db = passing)

