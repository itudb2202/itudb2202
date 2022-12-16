from flask import Flask, render_template
from datetime import datetime
from flask import current_app, request
from database import Database

from stats import Defensive, Kickoff, Passing, Punting, Receiving, BasicStats


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
    db = current_app.config["dbconfig"]
    basicstats = db.get_all_basic_stats()
    return render_template("basicStats.html",basicstats_db = basicstats)

def delete_basicstats(player_id):
    db = current_app.config["dbconfig"]
    db.dlt_basicstats(player_id)
    basicstats = db.get_all_basic_stats()
    return render_template("basicStats.html", basicstats_db = basicstats)

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

def add_passing():
    if request.method == "GET":
        return render_template("bora_edit.html")
    else:
        form_player_id = request.form["Player_Id"]
        form_player_year = request.form["Player_Year"]
        form_team = request.form["Team"]
        form_games_played = request.form["Games_Played"]
        form_passes_attempted = request.form["Passes_Attempted"]
        form_passes_completed = request.form["Passes_Completed"]
        form_completion_percentage = request.form["Completion_Percentage"]
        form_passer_rating = request.form["Passer_Rating"]

        passing_stat = Passing(form_player_id, form_player_year, form_team, form_games_played, form_passes_attempted, form_passes_completed, form_completion_percentage, form_passer_rating)
        db = current_app.config["dbconfig"]
        db.add_passing_stat(passing_stat)
        passing = db.get_all_passing_stats()
        return render_template("bora.html", passing_db = passing)
