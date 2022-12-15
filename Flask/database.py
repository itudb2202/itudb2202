import sqlite3 as dbapi2
from classes import Defensive  
from classes import Kickoff  
from classes import Passing  
from classes import Punting  
from classes import Receiving  


class Database:


    def __init__(self, dbfile):
        self.dbfile = dbfile  

    def get_all_kickoff_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT Kickoff_Id, Player_Id, PLayer_Year, Team, Games_Played, Kickoffs, Kickoff_Yards, Out_of_Bounds_Kickoffs, Yards_Per_Kickoff, Touchbacks FROM kickoff ORDER BY Kickoff_Id"
            kickoff_stats = cursor.execute(query).fetchall()
            return kickoff_stats