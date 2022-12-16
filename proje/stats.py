# Creating data model



class Defensive:
    def __init__(self , playerId , year , team , games_played , total_tack , solo_tack ,ast_tack , pas_def ,ints ,yrd_per_int):
        self.playerId = playerId
        self.year = year
        self.team = team
        self.games_played = games_played
        self.total_tack = total_tack
        self.solo_tack = solo_tack
        self.ast_tack = ast_tack
        self.pas_def = pas_def
        self.ints = ints
        self.yrd_per_int = yrd_per_int

class Kickoff:
    def __init__(self , playerId , year , team , games_played , kickoff , kickoff_yrd , out_kickoff , yrd_per_kickoff , touchback):
        self.playerId = playerId
        self.year = year
        self.team = team
        self.games_played = games_played
        self.kickoff = kickoff
        self.kickoff_yrd = kickoff_yrd
        self.out_kickoff = out_kickoff
        self.yrd_per_kickoff = yrd_per_kickoff
        self.touchback = touchback

class Passing:
    def __init__(self , playerId , year , team , games_played , pass_Att , pass_comp , comp_percentage , passer_rating):
        self.playerId = playerId
        self.year = year
        self.team = team
        self.games_played = games_played
        self.pass_Att = pass_Att
        self.pass_comp = pass_comp
        self.comp_percentage = comp_percentage
        self.passer_rating = passer_rating

class Punting:
    def __init__(self , playerId , year , team , games_played , punts , gross_punting_yards , longest_punt , fair_catches):
        self.playerId = playerId
        self.year = year
        self.team = team
        self.games_played = games_played
        self.punts = punts
        self.gross_punting_yards = gross_punting_yards
        self.longest_punt = longest_punt
        self.fair_catches = fair_catches

class Receiving:
    def __init__(self , playerId , year , team , games_played , receptions, receiving_yrd , yrd_per_reception , yrd_per_game ):
        self.playerId = playerId
        self.year = year
        self.team = team
        self.games_played = games_played
        self.receptions = receptions
        self.receiving_yrd = receiving_yrd
        self.yrd_per_reception = yrd_per_reception
        self.yrd_per_game = yrd_per_game

class BasicStats:
    def __init__(self,playerId,age,birthPlace,birthday,college,curr_stat, curr_team,experience,height,highSchool,hS_location,name,number,position,weight,yearsPlayed):
        self.playerId = playerId
        self.age = age
        self.birthPlace = birthPlace
        self.birthday = birthday
        self.college = college
        self.curr_stat = curr_stat
        self.curr_team = curr_team
        self.experience = experience
        self.height = height
        self.highSchool = highSchool
        self.hS_location = hS_location
        self.name = name
        self.number = number
        self.position = position
        self.weight = weight
        self.yearsPlayed = yearsPlayed