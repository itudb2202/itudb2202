DROP TABLE IF EXISTS basic_stats;
DROP TABLE IF EXISTS career_stats_defensive;
DROP TABLE IF EXISTS career_stats_defensive;
DROP TABLE IF EXISTS career_stats_kickoff;
DROP TABLE IF EXISTS career_stats_passing;
DROP TABLE IF EXISTS career_stats_punting;
DROP TABLE IF EXISTS career_stats_receiving;

CREATE TABLE basic_stats (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
	age INTEGER,
	birth_place VARCHAR(50),
	birthday DATE,
	college VARCHAR (50),
	current_status VARCHAR (50),
	current_team VARCHAR (50),
	experience VARCHAR(50),
	height INTEGER,
	high_school VARCHAR (50),
	high_school_location VARCHAR (50),
	name VARCHAR (50) NOT NULL,
	player_number INTEGER,
	position VARCHAR(50),
	weight INTEGER,
	years_played VARCHAR(50),
); 

CREATE TABLE career_stats_defensive (
    defensive_id INTEGER PRIMARY KEY AUTOINCREMENT,
	player_id INTEGER,
	player_year INTEGER,
	team VARCHAR (50),
	games_played INTEGER,
	total_tackles INTEGER,
	solo_tackles INTEGER,
	assisted_tackled INTEGER,
	passed_defended INTEGER,
	ints INTEGER,
	yards_per_int FLOAT,
	FOREIGN player_id REFERENCES basic_stats(player_id) 
	ON DELETE CASCADE
	ON UPDATE CASCADE	
);

CREATE TABLE career_stats_kickoff (
    kickoff_id INTEGER PRIMARY KEY AUTOINCREMENT,
	player_id INTEGER,
	player_year INTEGER,
	team VARCHAR (50),
	games_played INTEGER,
	kickoffs INTEGER,
	kickoff_yards INTEGER,
	out_of_bound_kickoffs INTEGER,
	yards_per_kickoff FLOAT,
	touchbacks INTEGER,
	FOREIGN player_id REFERENCES basic_stats(player_id) 
	ON DELETE CASCADE
	ON UPDATE CASCADE	
);

CREATE TABLE career_stats_passing (
    passing_id INTEGER PRIMARY KEY AUTOINCREMENT,
	player_id INTEGER,
	player_year INTEGER,
	team VARCHAR (50),
	games_played INTEGER,
	passes_attempted INTEGER,
	passes_completed INTEGER,
	completion_percentage FLOAT,
	passer_rating FLOAT,
	FOREIGN player_id REFERENCES basic_stats(player_id) 
	ON DELETE CASCADE
	ON UPDATE CASCADE	
);

CREATE TABLE career_stats_punting (
    punting_id INTEGER PRIMARY KEY AUTOINCREMENT,
	player_id INTEGER,
	player_year INTEGER,
	team VARCHAR (50),
	games_played INTEGER,
	punts INTEGER,
	gross_punting_yards INTEGER,
	longest_punt INTEGER,
	fair_catches INTEGER,
	FOREIGN player_id REFERENCES basic_stats(player_id) 
	ON DELETE CASCADE
	ON UPDATE CASCADE	
);

CREATE TABLE career_stats_receiving (
    punting_id INTEGER PRIMARY KEY AUTOINCREMENT,
	player_id INTEGER,
	player_year INTEGER,
	team VARCHAR (50),
	games_played INTEGER,
	receptions INTEGER,
	receiving_yards INTEGER,
	yards_per_reception FLOAT,
	yards_per_game FLOAT,
	FOREIGN player_id REFERENCES basic_stats(player_id) 
	ON DELETE CASCADE
	ON UPDATE CASCADE	
);