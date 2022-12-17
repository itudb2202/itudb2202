import sqlite3 as dbapi2

from stats import Defensive, Kickoff, Passing, Punting, Receiving, BasicStats


class Database:

    def __init__(self, dbfile):
        self.dbfile = dbfile


    # ------- GET FUNCTIONS

    def get_defensive_stat(self, defensive_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM defensive WHERE (Defensive_Id = ?)"
            cursor.execute(query, (defensive_key,))

            temp_defensive_id, playerId , year , team , games_played , total_tack , solo_tack , ast_tack , pas_def, ints, yrd_per_int= cursor.fetchone()

        defensive_stat = Defensive(playerId , year , team , games_played , total_tack , solo_tack , ast_tack , pas_def, ints, yrd_per_int)
        return defensive_stat
    
    def get_receiving_stat(self, receiving_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM receiving WHERE (Receive_Id = ?)"
            cursor.execute(query, (receiving_key,))
            temp_receiving_key_id, playerId , year , team , games_played , receptions, receiving_yrd , yrd_per_reception , yrd_per_game = cursor.fetchone()

        receiving_stat = Receiving(playerId , year , team , games_played , receptions , receiving_yrd , yrd_per_reception , yrd_per_game)
        return receiving_stat

    def get_passing_stat(self, passing_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM passing WHERE (Passing_Id = ?)"
            cursor.execute(query, (passing_key,))

            temp_passing_id, playerId , year , team , games_played , pass_Att , pass_comp , comp_percentage , passer_rating = cursor.fetchone()

        passing_stat = Passing(playerId , year , team , games_played , pass_Att , pass_comp , comp_percentage , passer_rating)
        return passing_stat

    def get_punting_stat(self, punting_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM punting WHERE (Punting_Id = ?)"
            cursor.execute(query, (punting_key,))

            temp_punting_id, playerId , year , team , games_played , punts , gross_punting_yards , longest_punt , fair_catches = cursor.fetchone()

        punting_stat = Passing(playerId , year , team , games_played , punts , gross_punting_yards , longest_punt , fair_catches)
        return punting_stat


    def get_kickoff_stat(self, kickoff_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM kickoff WHERE (Kickoff_Id = ?)"
            cursor.execute(query, (kickoff_key,))

            temp_kickoff_id, playerId , year , team , games_played , kickoff , kickoff_yrd , out_kickoff , yrd_per_kickoff, touchback= cursor.fetchone()

        kickoff_stat = Kickoff(playerId , year , team , games_played , kickoff , kickoff_yrd , out_kickoff , yrd_per_kickoff, touchback)
        return kickoff_stat

    def get_basic_stat(self, basic_stat_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM basic_stats WHERE (Player_Id = ?)"
            cursor.execute(query, (basic_stat_key,))

            age, birthPlace, birthday, college, curr_stat, curr_team, experience, height, highSchool, hS_location, name, number, playerId, position, weight, yearsPlayed = cursor.fetchone()

        basic_stat = BasicStats(playerId, age, birthPlace, birthday, college, curr_stat, curr_team, experience, height, highSchool, hS_location, name, number, position, weight, yearsPlayed)
        return basic_stat


    # ------- GET ALL FUNCTIONS

    def get_all_basic_stats(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM basic_stats ORDER BY Player_Id DESC LIMIT 30"
            basic_stats = cursor.execute(query).fetchall()
            return basic_stats

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

    def add_basic_stat(self, basic_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO basic_stats (Age, Birth_Place,Birthday, College, Current_Status, Current_Team, Experience, Height_inches, High_School, High_School_Location,Player_Name,Player_Number,Player_Id,Position,Weight_lbs,Years_Played) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? , ? , ? , ? , ? , ?)"
            cursor.execute(query, (basic_stat.age, basic_stat.birthPlace, basic_stat.birthday, basic_stat.college, basic_stat.curr_stat,
                            basic_stat.curr_team, basic_stat.experience, basic_stat.height, basic_stat.highSchool, basic_stat.hS_location,basic_stat.name,basic_stat.number,basic_stat.playerId,basic_stat.position,basic_stat.weight,basic_stat.yearsPlayed))
            connection.commit()
            
    def add_defensive_stat(self, defensive_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO defensive (Player_Id, Player_Year,Team, Games_Played, Total_Tackles, Solo_Tackles, Assisted_Tackles, Passes_Defended, Ints, Yards_Per_Int) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (defensive_stat.playerId, defensive_stat.year, defensive_stat.team, defensive_stat.games_played, defensive_stat.total_tack,
                            defensive_stat.solo_tack, defensive_stat.ast_tack, defensive_stat.pas_def, defensive_stat.ints, defensive_stat.yrd_per_int))
            connection.commit()

    def add_receiving_stat(self, receiving_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO receiving (Player_Id, Player_Year,Team, Games_Played, Receptions, Receiving_Yards, Yards_Per_Reception, Yards_Per_Game) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (receiving_stat.playerId, receiving_stat.year, receiving_stat.team, receiving_stat.games_played, receiving_stat.receptions,
                            receiving_stat.receiving_yrd, receiving_stat.yrd_per_reception, receiving_stat.yrd_per_game))
            connection.commit()

    def add_punting_stat(self, punting_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO punting (Player_Id, Player_Year,Team, Games_Played, Punts, Gross_Punting_Yards, Longest_Punt, Fair_Catches) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (punting_stat.playerId, punting_stat.year, punting_stat.team, punting_stat.games_played, punting_stat.punts,
                            punting_stat.gross_punting_yards, punting_stat.longest_punt, punting_stat.fair_catches))
            connection.commit()

    def add_passing_stat(self, passing_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO passing (Player_Id, Player_Year, Team, Games_Played, Passes_Attempted, Passes_Completed, Completion_Percentage, Passer_Rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (passing_stat.playerId, passing_stat.year, passing_stat.team, passing_stat.games_played, passing_stat.pass_Att,
                            passing_stat.pass_comp, passing_stat.comp_percentage, passing_stat.passer_rating))
            connection.commit()

    def add_kickoff_stat(self, kickoff_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO kickoff (Player_Id, Player_Year, Team, Games_Played, Kickoffs, Kickoff_Yards, Out_of_Bounds_Kickoffs, Yards_Per_Kickoff, Touchbacks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (kickoff_stat.playerId, kickoff_stat.year, kickoff_stat.team, kickoff_stat.games_played, kickoff_stat.kickoff,
                            kickoff_stat.kickoff_yrd, kickoff_stat.out_kickoff, kickoff_stat.yrd_per_kickoff, kickoff_stat.touchback))
            connection.commit()

    # ------- DELETE FUNCTIONS

    def dlt_basicstats(self, basicstats_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            query = "DELETE FROM basic_stats WHERE (Player_Id = ?)"
            cursor.execute(query, (basicstats_key,))
            connection.commit()

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


    # ------- UPDATE FUNCTIONS

    def update_defensive_stat(self,defensive_key, defensive_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE defensive SET Player_Id = ?, Player_Year = ?, Team = ?, Games_Played = ?, Total_Tackles = ?, Solo_Tackles = ?, Assisted_Tackles = ?, Passes_Defended = ?, Ints = ? , Yards_Per_Int = ? WHERE (Defensive_Id = ?)"
            cursor.execute(query, (defensive_stat.playerId , defensive_stat.year , defensive_stat.team , defensive_stat.games_played , defensive_stat.total_tack, defensive_stat.solo_tack , defensive_stat.ast_tack , defensive_stat.pas_def, defensive_stat.ints, defensive_stat.yrd_per_int, defensive_key))
            connection.commit()

    def update_passing_stat(self, passing_key, passing_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE passing SET Player_Id = ?, Player_Year = ?, Team = ?, Games_Played = ?, Passes_Attempted = ?, Passes_Completed = ?, Completion_Percentage = ?, Passer_Rating = ? WHERE (Passing_Id = ?)"
            cursor.execute(query, (passing_stat.playerId, passing_stat.year, passing_stat.team, passing_stat.games_played, passing_stat.pass_Att, passing_stat.pass_comp, passing_stat.comp_percentage, passing_stat.passer_rating, passing_key))
            connection.commit()

    def update_punting_stat(self, punting_key, punting_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE punting SET Player_Id = ?, Player_Year = ?, Team = ?, Games_Played = ?, Punts = ?, Gross_Punting_Yards = ?, Longest_Punt = ?, Fair_Catches = ? WHERE (Punting_Id = ?)"
            cursor.execute(query, (punting_stat.playerId, punting_stat.year, punting_stat.team, punting_stat.games_played, punting_stat.punts, punting_stat.gross_punting_yards, punting_stat.longest_punt, punting_stat.fair_catches, punting_key))
            connection.commit()

    def update_receiving_stat(self, receiving_key, receiving_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE receiving SET Player_Id = ?, Player_Year = ?, Team = ?, Games_Played = ?, Receptions = ?, Receiving_Yards = ?, Yards_Per_Reception = ?, Yards_Per_Game = ? WHERE (Receive_Id = ?)"
            cursor.execute(query, (receiving_stat.playerId , receiving_stat.year , receiving_stat.team , receiving_stat.games_played , receiving_stat.receptions, receiving_stat.receiving_yrd , receiving_stat.yrd_per_reception , receiving_stat.yrd_per_game, receiving_key))
            connection.commit()

    def update_kickoff_stat(self,kickoff_key, kickoff_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE kickoff SET Player_Id = ?, Player_Year = ?, Team = ?, Games_Played = ?, Kickoffs = ?, Kickoff_Yards = ?, Out_of_Bounds_Kickoffs = ?, Yards_Per_Kickoff = ?, Touchbacks = ? WHERE (Kickoff_Id = ?)"
            cursor.execute(query, (kickoff_stat.playerId , kickoff_stat.year , kickoff_stat.team , kickoff_stat.games_played , kickoff_stat.kickoff, kickoff_stat.kickoff_yrd , kickoff_stat.out_kickoff , kickoff_stat.yrd_per_kickoff, kickoff_stat.touchback, kickoff_key))
            connection.commit()
    
    def update_basic_stat(self,basic_stat_key, basic_stat):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE basic_stats SET Age = ?, Birth_Place = ?, Birthday = ?, College = ?, Current_Status = ?, Current_Team = ?, Experience = ?, Height_inches = ?, High_School = ?, High_School_Location = ?, Player_Name = ?, Player_Number = ?, Player_Id = ?, Position = ?, Weight_lbs = ?, Years_Played = ? WHERE (Player_Id = ?)"
            cursor.execute(query, (basic_stat.age, basic_stat.birthPlace, basic_stat.birthday, basic_stat.college, basic_stat.curr_stat, basic_stat.curr_team, basic_stat.experience, basic_stat.height, basic_stat.highSchool, basic_stat.hS_location, basic_stat.name, basic_stat.number, basic_stat.playerId, basic_stat.position, basic_stat.weight, basic_stat.yearsPlayed, basic_stat_key))
            connection.commit()

