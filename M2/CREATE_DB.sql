DROP DATABASE IF EXISTS zelda;
CREATE DATABASE zelda CHARACTER SET utf8mb4;
USE zelda;

CREATE TABLE IF NOT EXISTS players(
	player_id INT,
    user_name VARCHAR(10),
    hearts_remaining INT,
    hearts_total INT,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);


CREATE TABLE IF NOT EXISTS game(
	game_id INT,
    fk_player_id_players_game INT,
    date_started DATETIME,
    region VARCHAR(20),
    blood_moon_countdown INT,
    blood_moon_appearences INT,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);


CREATE TABLE IF NOT EXISTS food(
	food_name VARCHAR(15),
    fk_game_id_game_food INT,
    quantity_remaining INT,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);


CREATE TABLE IF NOT EXISTS weapons(
	weapon_id INT,
    fk_game_id_game_weapons INT,
    weapon_name VARCHAR(15),
    equiped BOOLEAN,
    lives_remaining INT,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);


CREATE TABLE IF NOT EXISTS enemies(
	enemy_id INT,
    fk_game_id_game_enemies INT,
    region VARCHAR(20),
    position INT,
    lifes_remaining INT,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);


CREATE TABLE IF NOT EXISTS chest(
	chest_id INT,
    fk_game_id_game_chest INT,
    region VARCHAR(20),
    position INT,
    state BOOLEAN,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);


CREATE TABLE IF NOT EXISTS santuaries(
	sactuary_id INT,
    fk_game_id_game_santuaries INT,
    region VARCHAR(20),
    position INT,
    state BOOLEAN,
    
    date_created DATETIME DEFAULT NOW(),
    date_modified DATETIME DEFAULT NOW() ON UPDATE NOW()
);