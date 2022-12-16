from datetime import datetime
from flask import Flask, render_template
import views
from database import Database
import sqlite3 as dbapi2
import os
import pandas as pd


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)

    app.add_url_rule("/buse", view_func=views.buse_page)
    app.add_url_rule("/merve", view_func=views.merve_page)
    app.add_url_rule("/bora", view_func=views.bora_page)
    app.add_url_rule("/atacan", view_func=views.atacan_page)
    app.add_url_rule("/pelin", view_func=views.pelin_page)
    app.add_url_rule("/basicStats", view_func=views.basicStats_page)

    app.add_url_rule("/delete_basicstats/<player_id>", view_func=views.delete_basicstats)
    app.add_url_rule("/delete_receiving/<receiving_id>", view_func=views.delete_receiving)
    app.add_url_rule("/delete_defensive/<defensive_id>", view_func=views.delete_defensive)
    app.add_url_rule("/delete_kickoff/<kickoff_id>", view_func=views.delete_kickoff )
    app.add_url_rule("/delete_punting/<punting_id>", view_func=views.delete_punting )
    app.add_url_rule("/delete_passing/<passing_id>", view_func=views.delete_passing )

    app.add_url_rule("/add_receiving", view_func=views.add_receiving, methods=["GET", "POST"])
    app.add_url_rule("/add_punting", view_func=views.add_punting, methods=["GET", "POST"])
    app.add_url_rule("/add_passing", view_func=views.add_passing, methods=["GET", "POST"])
    app.add_url_rule("/add_kickoff", view_func=views.add_kickoff, methods=["GET", "POST"])
    app.add_url_rule("/add_defensive", view_func=views.add_defensive, methods=["GET", "POST"])

    app.add_url_rule("/bora/update/<passing_id>", view_func=views.update_passing, methods=["GET", "POST"])


    home_dir = os.getcwd()

    #if no DB exists create DB func

    db = Database(os.path.join(home_dir, "group2_nfl.db"))
    app.config["dbconfig"] = db

    return app

if __name__ == "__main__":
    app = create_app()

    port = app.config.get("PORT",5000)

    app.run(host="0.0.0.0",port=port)