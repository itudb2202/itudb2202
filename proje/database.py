import sqlite3 as dbapi2
from stats import Defensive  
from stats import Kickoff  
from stats import Passing  
from stats import Punting  
from stats import Receiving  


class Database:

    def __init__(self, dbfile):
        self.dbfile = dbfile  

    def add_defensive_stat(self, defensive_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO defensive (Player_Id, Player_Year,Team, Games_Played, Total_Tackles, Solo_Tackles, Assisted_Tackles, Passes_Defended, Ints, Yards_Per_Int) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (defensive_stat.playerId, defensive_stat.year, defensive_stat.team, defensive_stat.games_played, defensive_stat.total_tack,
                            defensive_stat.solo_tack, defensive_stat.ast_tack, defensive_stat.pas_def, defensive_stat.ints, defensive_stat.yrd_per_int))
            connection.commit()
            defense_key = cursor.lastrowid
        return defense_key
        
        
    def get_all_defensive_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT Defensive_Id,Player_Id,Player_Year,Team,Games_Played,Total_Tackles,Solo_Tackles,Assisted_Tackles,Passes_Defended,Ints,Yards_Per_Int FROM defensive ORDER BY Defensive_Id LIMIT 30"
            defensive_stats = cursor.execute(query).fetchall()
            return defensive_stats

    def get_all_kickoff_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT Kickoff_Id, Player_Id, PLayer_Year, Team, Games_Played, Kickoffs, Kickoff_Yards, Out_of_Bounds_Kickoffs, Yards_Per_Kickoff, Touchbacks FROM kickoff ORDER BY Kickoff_Id LIMIT 30"
            kickoff_stats = cursor.execute(query).fetchall()
            return kickoff_stats

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


    def get_all_receiving_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM receiving ORDER BY Receive_Id LIMIT 30"
            defensive_stats = cursor.execute(query).fetchall()
            return defensive_stats

    
