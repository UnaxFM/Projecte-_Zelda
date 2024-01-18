DROP DATABASE IF EXISTS zelda;
CREATE DATABASE zelda CHARACTER SET utf8mb4;
USE zelda;


CREATE TABLE IF NOT EXISTS game(
	game_id INT,
    user_name VARCHAR(10),
    hearts_remaining INT,
    hearts_total INT,
    date_started TIMESTAMP,
    date_modified TIMESTAMP,
    region VARCHAR(20),
    blood_moon_countdown INT,
    blood_moon_appearences INT
);


CREATE TABLE IF NOT EXISTS food(
	food_name VARCHAR(15),
    game_id INT,
    quantity_remaining INT,
    
    date_created TIMESTAMP,
    date_modified TIMESTAMP
);


CREATE TABLE IF NOT EXISTS weapons(
    game_id INT,
    weapon_name VARCHAR(15),
    equiped BOOLEAN,
    uses INT,
    quantity INT,
    
    date_created TIMESTAMP,
    date_modified TIMESTAMP
);


CREATE TABLE IF NOT EXISTS enemies(
	enemy_id INT,
    game_id INT,
    region VARCHAR(20),
    xpos INT,
    ypos INT,
    lifes_remaining INT,
    
    date_created TIMESTAMP,
    date_modified TIMESTAMP
);


CREATE TABLE IF NOT EXISTS chest_opened(
	chest_id INT,
    game_id INT,
    region VARCHAR(20),
    xpos INT,
    ypos INT,
    
    date_created TIMESTAMP,
    date_modified TIMESTAMP
);


CREATE TABLE IF NOT EXISTS santuaries_opened(
	sactuary_id INT,
    game_id INT,
    region VARCHAR(20),
    xpos INT,
    ypos INT,
    
    date_created TIMESTAMP,
    date_modified TIMESTAMP
);