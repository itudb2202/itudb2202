from datetime import datetime

from flask import Flask, render_template

import views


def create_app():
    app = Flask(__name__)

    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/buse", view_func=views.buse_page)

    app.add_url_rule("/merve", view_func=views.merve_page)
    app.add_url_rule("/bora", view_func=views.bora_page)
    app.add_url_rule("/atacan", view_func=views.atacan_page)
    app.add_url_rule("/pelin", view_func=views.pelin_page)
    return app

if __name__ == "__main__":
    app = create_app()

    port = app.config.get("PORT",5000)

    app.run(host="0.0.0.0",port=port)