DROP DATABASE IF EXISTS zelda;
CREATE DATABASE zelda CHARACTER SET utf8mb4;
USE zelda;


CREATE TABLE IF NOT EXISTS players(
	player_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(10) NOT NULL,
    hearts_remaining INT NOT NULL,
    hearts_total INT NOT NULL
);

CREATE TABLE IF NOT EXISTS game(
	game_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    player_id INT UNSIGNED NOT NULL,
    date_started DATETIME DEFAULT NOW(),
    region VARCHAR(20) NOT NULL,
    blood_moon_countdown INT NOT NULL,
    blood_moon_appearences INT NOT NULL,
    
    CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
    
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

CREATE TABLE IF NOT EXISTS food(
	food_name VARCHAR(15) NOT NULL,
    game_id INT UNSIGNED NOT NULL,
    quantity_remaining INT UNSIGNED NOT NULL,
    
    CHECK (food_name IN ('vegetables', 'fish', 'meat', 'salads', 'pescatarian','roasted')),
    
    PRIMARY KEY (food_name, game_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS weapons(
	weapon_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    game_id INT UNSIGNED NOT NULL,
    weapon_name VARCHAR(15) NOT NULL,
    equiped BOOLEAN DEFAULT FALSE,
    lives_remaining INT NOT NULL,
    
    CHECK (weapon_name IN ('wood sword', 'sword', 'wood shield', 'shield')),
    
    PRIMARY KEY (weapon_id, game_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS enemies(
	enemy_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    game_id INT UNSIGNED NOT NULL,
    region VARCHAR(20) NOT NULL,
    position INT NOT NULL,
    lifes_remaining INT NOT NULL,
    
    CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),

	PRIMARY KEY (enemy_id, game_id,region),
    FOREIGN KEY (game_id) REFERENCES game(game_id)

);

CREATE TABLE IF NOT EXISTS chests(
	chest_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    game_id INT UNSIGNED NOT NULL,
    region VARCHAR(20) NOT NULL,
    position INT NOT NULL,
    state BOOLEAN DEFAULT FALSE,
    
    CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),

	PRIMARY KEY (chest_id, game_id,region),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS santuaries(
	sactuary_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    game_id INT UNSIGNED NOT NULL,
    region VARCHAR(20) NOT NULL,
    position INT NOT NULL,
    state BOOLEAN DEFAULT FALSE,
    
    CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),

	PRIMARY KEY (sactuary_id, game_id,region),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);