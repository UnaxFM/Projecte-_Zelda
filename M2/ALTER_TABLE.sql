USE zelda;


-- Taula players

ALTER TABLE players
    MODIFY user_name INT NOT NULL,
	MODIFY hearts_remaining NOT NULL,
    MODIFY hearts_total INT NOT NULL,
    MODIFY date_created DATETIME DEFAULT NOW(),
    MODIFY date_modified DATETIME DEFAULT NOW() ON UPDATE NOW(),
    
	ADD CONSTRAINT pk_players PRIMARY KEY (player_id);


ALTER TABLE game
	MODIFY fk_player_id_players_game INT UNSIGNED NOT NULL,
	MODIFY date_started DATETIME DEFAULT NOW(),
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY blood_moon_countdown INT NOT NULL,
    MODIFY blood_moon_appearences INT NOT NULL,
    
    MODIFY date_created DATETIME DEFAULT NOW(),
    MODIFY date_modified DATETIME DEFAULT NOW() ON UPDATE NOW(),
    
    ADD CONSTRAINT fk_game_fk_player_id_players_game FOREIGN KEY (fk_player_id_players_game) REFERENCES players(player_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT ck_game_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle'));
    

ALTER TABLE food
	MODIFY fk_game_id_game_food INT UNSIGNED NOT NULL,
    MODIFY quantity_remaining INT NOT NULL,
    
    ADD CONSTRAINT fk_food_fk_game_id_game_food FOREIGN KEY (fk_game_id_game_food) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT ck_food_food_name CHECK (food_name IN ('vegetables', 'fish', 'meat', 'salads', 'pescatarian','roasted'));


-- Taula weapons

ALTER TABLE weapons
	MODIFY weapon_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    MODIFY fk_game_id_game_food INT UNSIGNED NOT NULL,
    MODIFY weapon_name VARCHAR(15) NOT NULL,
    MODIFY equiped BOOLEAN DEFAULT FALSE NOT NULL,
    MODIFY lives_remaining INT NOT NULL,
    
    ADD CONSTRAINT ck_weapons_weapon_name CHECK (weapon_name IN ('wood sword', 'sword', 'wood shield', 'shield')),
    ADD CONSTRAINT fk_weapons_fk_game_id_game_food  FOREIGN KEY (fk_game_id_game_food) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Taula enemies

ALTER TABLE enemies
	MODIFY enemy_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    MODIFY fk_game_id_game_enemies INT UNSIGNED NOT NULL,
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY position INT NOT NULL,
    MODIFY lifes_remaining INT NOT NULL,
    
    ADD CONSTRAINT ck_enemies_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
    
    ADD CONSTRAINT fk_enemies_fk_game_id_game_enemies FOREIGN KEY (fk_game_id_game_enemies) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT pk_enemies PRIMARY KEY (enemy_id, fk_game_id_game_enemies,region);

    

