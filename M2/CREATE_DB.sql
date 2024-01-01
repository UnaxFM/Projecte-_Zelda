DROP DATABASE IF EXISTS zelda;
CREATE DATABASE zelda CHARACTER SET utf8mb4;
USE zelda;

CREATE TABLE IF NOT EXISTS players(
	player_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(10),
    hearts_remaining INT,
    hearts_total INT,
    
    date_created DATETIME,
    date_modified DATETIME,
    user_modified INT
);


CREATE TABLE IF NOT EXISTS game(
	game_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fk_player_id_players_game INT UNSIGNED,
    date_started DATETIME,
    region VARCHAR(20),
    blood_moon_countdown INT,
    blood_moon_appearences INT,
    
    date_created DATETIME,
    date_modified DATETIME,
    user_modifies INT
);