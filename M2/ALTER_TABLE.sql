USE zelda;

-- Taula players

ALTER TABLE players
	MODIFY player_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    MODIFY user_name VARCHAR(10) NOT NULL,
	MODIFY hearts_remaining INT NOT NULL,
    MODIFY hearts_total INT NOT NULL,
    
	ADD CONSTRAINT pk_players PRIMARY KEY (player_id);


-- Taula game

ALTER TABLE game
	MODIFY game_id INT UNSIGNED AUTO_INCREMENT,
	MODIFY fk_player_id_players_game INT UNSIGNED NOT NULL,
	MODIFY date_started DATETIME DEFAULT NOW() NOT NULL,
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY blood_moon_countdown INT NOT NULL DEFAULT 0,
    MODIFY blood_moon_appearences INT NOT NULL DEFAULT 0,
    
	ADD CONSTRAINT ck_game_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),    
    
    ADD CONSTRAINT fk_game_fk_player_id_players_game FOREIGN KEY (fk_player_id_players_game) REFERENCES players(player_id) ON UPDATE CASCADE ON DELETE CASCADE,
	ADD CONSTRAINT pk_game PRIMARY KEY (game_id);


-- Taula food
    
ALTER TABLE food
	MODIFY food_name VARCHAR(15) NOT NULL,
	MODIFY fk_game_id_game_food INT UNSIGNED NOT NULL,
    MODIFY quantity_remaining INT NOT NULL,
    
	ADD CONSTRAINT ck_food_food_name CHECK (food_name IN ('vegetables', 'fish', 'meat', 'salads', 'pescatarian','roasted')),

    ADD CONSTRAINT fk_food_fk_game_id_game_food FOREIGN KEY (fk_game_id_game_food) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
	ADD CONSTRAINT pk_food PRIMARY KEY (fk_game_id_game_food,food_name);


-- Taula weapons

ALTER TABLE weapons
	MODIFY weapon_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    MODIFY fk_game_id_game_weapons INT UNSIGNED NOT NULL,
    MODIFY weapon_name VARCHAR(15) NOT NULL,
    MODIFY equiped BOOLEAN DEFAULT FALSE NOT NULL,
    MODIFY lives_remaining INT NOT NULL,
    
    ADD CONSTRAINT ck_weapons_weapon_name CHECK (weapon_name IN ('wood sword', 'sword', 'wood shield', 'shield')),
    
    ADD CONSTRAINT fk_weapons_fk_game_id_game_food  FOREIGN KEY (fk_game_id_game_weapons) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT pk_weapons PRIMARY KEY(weapon_id, fk_game_id_game_weapons);


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

    
-- Taula chest
    
ALTER TABLE chest
	MODIFY chest_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	MODIFY fk_game_id_game_chest INT UNSIGNED NOT NULL,
	MODIFY region VARCHAR(20) NOT NULL,
	MODIFY position INT NOT NULL,
	MODIFY state BOOLEAN DEFAULT FALSE NOT NULL,
	
	ADD CONSTRAINT ck_chest_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
	
	ADD CONSTRAINT fk_chest_fk_game_id_game_chest FOREIGN KEY (fk_game_id_game_chest) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
	ADD CONSTRAINT pk_chest PRIMARY KEY (chest_id, fk_game_id_game_chest, region);

        
-- Table santuaries

ALTER TABLE santuaries
	MODIFY sactuary_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    MODIFY fk_game_id_game_santuaries INT UNSIGNED NOT NULL,
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY position INT NOT NULL,
    MODIFY state BOOLEAN DEFAULT FALSE NOT NULL,
    
    ADD CONSTRAINT ck_santuaries_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
    
    ADD CONSTRAINT fk_santuaries_fk_game_id_game_santuaries FOREIGN KEY (fk_game_id_game_santuaries) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT pk_santuaries PRIMARY KEY (sactuary_id, fk_game_id_game_santuaries, region);
  
