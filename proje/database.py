import sqlite3 as dbapi2
from stats import Defensive
from stats import Kickoff
from stats import Passing
from stats import Punting
from stats import Receiving


class Database:

    def __init__(self, dbfile):
        self.dbfile = dbfile


    # ------- GET ALL FUNCTIONS

    def get_all_punting_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM punting ORDER BY Punting_Id DESC LIMIT 30"
            punting_stats = cursor.execute(query).fetchall()
            return punting_stats

    def get_all_defensive_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM defensive ORDER BY Defensive_Id DESC LIMIT 30"
            defensive_stats = cursor.execute(query).fetchall()
            return defensive_stats

    def get_all_kickoff_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM kickoff ORDER BY Kickoff_Id DESC LIMIT 30"
            kickoff_stats = cursor.execute(query).fetchall()
            return kickoff_stats

    def get_all_receiving_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM receiving ORDER BY Receive_Id DESC LIMIT 30"
            defensive_stats = cursor.execute(query).fetchall()
            return defensive_stats

    def get_all_passing_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM passing ORDER BY Passing_Id DESC LIMIT 30"
            passing_stats = cursor.execute(query).fetchall()
            return passing_stats


    # ------- ADD FUNCTIONS

    def add_defensive_stat(self, defensive_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO defensive (Player_Id, Player_Year,Team, Games_Played, Total_Tackles, Solo_Tackles, Assisted_Tackles, Passes_Defended, Ints, Yards_Per_Int) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (defensive_stat.playerId, defensive_stat.year, defensive_stat.team, defensive_stat.games_played, defensive_stat.total_tack,
                            defensive_stat.solo_tack, defensive_stat.ast_tack, defensive_stat.pas_def, defensive_stat.ints, defensive_stat.yrd_per_int))
            connection.commit()
            defense_key = cursor.lastrowid
        return defense_key

    def add_receiving_stat(self, receiving_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            query = "INSERT INTO defensive (Player_Id, Player_Year,Team, Games_Played, Receptions, Receiving_Yards, Yards_Per_Reception, Yards_Per_Game) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (receiving_stat.playerId, receiving_stat.year, receiving_stat.team, receiving_stat.games_played, receiving_stat.receptions,
                            receiving_stat.receiving_yrd, receiving_stat.yrd_per_reception, receiving_stat.yrd_per_game))
            connection.commit()
            defense_key = cursor.lastrowid
        return defense_key


    # ------- DELETE FUNCTIONS

    def dlt_receiving(self, receiving_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM receiving WHERE (Receive_Id = ?)"
            cursor.execute(query, (receiving_key,))
            connection.commit()

    def dlt_defensive(self, defensive_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM defensive WHERE (Defensive_Id = ?)"
            cursor.execute(query, (defensive_key,))
            connection.commit()

    def dlt_kickoff(self, kickoff_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM kickoff WHERE (Kickoff_Id = ?)"
            cursor.execute(query, (kickoff_key,))
            connection.commit()

    def dlt_punting(self, punting_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM punting WHERE (Punting_Id = ?)"
            cursor.execute(query, (punting_key,))
            connection.commit()

    def dlt_passing(self, passing_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM passing WHERE (Passing_Id = ?)"
            cursor.execute(query, (passing_key,))
            connection.commit()

