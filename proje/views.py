from flask import Flask, render_template
from datetime import datetime
from flask import current_app, request, abort
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
        values = {"Player_Id": "", "Player_Year": "", "Team": "", "Games_Played": "", "Passes_Attempted": "", "Passes_Completed": "", "Completion_Percentage": "", "Passer_Rating": ""}
        return render_template("bora_edit.html", values=values)
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


def add_kickoff():
    if request.method == "GET":
        return render_template("pelin_edit.html")
    else:
        form_player_id = request.form["Player_Id"]
        form_player_year = request.form["Player_Year"]
        form_team = request.form["Team"]
        form_games_played = request.form["Games_Played"]
        form_kickoffs = request.form["Kickoffs"]
        form_kickoff_yards = request.form["Kickoff_Yards"]
        form_out_of_bounds_kickoffs = request.form["Out_of_Bounds_Kickoffs"]
        form_yards_per_kickoff = request.form["Yards_Per_Kickoff"]
        form_touchbacks = request.form["Touchbacks"]

        kickoff_stat = Kickoff(form_player_id, form_player_year, form_team, form_games_played, form_kickoffs, form_kickoff_yards, form_out_of_bounds_kickoffs, form_yards_per_kickoff, form_touchbacks)
        db = current_app.config["dbconfig"]
        db.add_kickoff_stat(kickoff_stat)
        kickoff = db.get_all_kickoff_stats()
        return render_template("pelin.html", kickoff_db = kickoff)

def add_defensive():
    if request.method == "GET":
        return render_template("merve_edit.html")
    else:
        form_player_id = request.form["Player_Id"]
        form_player_year = request.form["Player_Year"]
        form_team = request.form["Team"]
        form_games_played = request.form["Games_Played"]
        form_total_tackles = request.form["Total_Tackles"]
        form_solo_tackles = request.form["Solo_Tackles"]
        form_assisted_tackles = request.form["Assisted_Tackles"]
        form_passes_defended = request.form["Passes_Defended"]
        form_ints = request.form["Ints"]
        form_yards_per_int = request.form["Yards_Per_Int"]

        defensive_stat = Defensive(form_player_id, form_player_year, form_team, form_games_played, form_total_tackles, form_solo_tackles, form_assisted_tackles, form_passes_defended, form_ints,form_yards_per_int)
        db = current_app.config["dbconfig"]
        db.add_defensive_stat(defensive_stat)
        defensive = db.get_all_defensive_stats()
        return render_template("merve.html", defensive_db = defensive)

def add_receiving():
    if request.method == "GET":
        return render_template("atacan_edit.html")
    else:
        form_player_id = request.form["Player_Id"]
        form_player_year = request.form["Player_Year"]
        form_team = request.form["Team"]
        form_games_played = request.form["Games_Played"]
        form_receptions = request.form["Receptions"]
        form_receiving_yards = request.form["Receiving_Yards"]
        form_yards_per_reception = request.form["Yards_Per_Reception"]
        form_yards_per_game = request.form["Yards_Per_Game"]


        receiving_stat = Receiving(form_player_id, form_player_year, form_team, form_games_played, form_receptions, form_receiving_yards, form_yards_per_reception, form_yards_per_game)
        db = current_app.config["dbconfig"]
        db.add_receiving_stat(receiving_stat)
        receiving = db.get_all_receiving_stats()
        return render_template("atacan.html", receiving_db = receiving)


def update_passing(passing_id):
    if request.method == "GET":
        db = current_app.config["dbconfig"]
        passing_stat = db.get_passing_stat(passing_id)
        if passing_stat is None:
            abort(404)
        values = {"Player_Id": passing_stat.playerId, "Player_Year": passing_stat.year, "Team": passing_stat.team, "Games_Played": passing_stat.games_played, "Passes_Attempted": passing_stat.pass_Att, "Passes_Completed": passing_stat.pass_comp, "Completion_Percentage": passing_stat.comp_percentage, "Passer_Rating": passing_stat.passer_rating}
        return render_template("bora_edit.html", values=values)
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
        db.update_passing_stat(passing_id, passing_stat)
        passing = db.get_all_passing_stats()
        return render_template("bora.html", passing_db = passing)

