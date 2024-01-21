USE zelda;

-- Taula game

ALTER TABLE game
	MODIFY game_id INT UNSIGNED AUTO_INCREMENT,
    MODIFY user_name VARCHAR(10) NOT NULL,
	MODIFY hearts_remaining INT NOT NULL,
    MODIFY hearts_total INT NOT NULL,
	MODIFY date_started TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    MODIFY date_modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY blood_moon_countdown INT NOT NULL DEFAULT 0,
    MODIFY blood_moon_appearences INT NOT NULL DEFAULT 0,
    
	ADD CONSTRAINT ck_game_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),    
    
	ADD CONSTRAINT pk_game PRIMARY KEY (game_id);


-- Taula food
    
ALTER TABLE food
	MODIFY food_name VARCHAR(15) NOT NULL,
	MODIFY game_id INT UNSIGNED NOT NULL,
    MODIFY quantity_remaining INT NOT NULL DEFAULT 0,
    MODIFY date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
    
	ADD CONSTRAINT ck_food_food_name CHECK (food_name IN ('vegetables', 'fish', 'meat', 'salads', 'pescatarian','roasted')),

    ADD CONSTRAINT fk_game_food FOREIGN KEY (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
	ADD CONSTRAINT pk_food PRIMARY KEY (game_id,food_name);


-- Taula weapons

ALTER TABLE weapons
    MODIFY game_id INT UNSIGNED NOT NULL,
    MODIFY weapon_name VARCHAR(15) NOT NULL,
    MODIFY equiped BOOLEAN DEFAULT FALSE NOT NULL,
    MODIFY uses INT NOT NULL DEFAULT 0,
    MODIFY quantity INT NOT NULL DEFAULT 0,
    MODIFY date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
    
    ADD CONSTRAINT ck_weapons_weapon_name CHECK (weapon_name IN ('wood sword', 'sword', 'wood shield', 'shield')),
    
    ADD CONSTRAINT fk_game_weapons  FOREIGN KEY (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT pk_weapons PRIMARY KEY(game_id, weapon_name);


-- Taula enemies

ALTER TABLE enemies
	MODIFY enemy_id INT UNSIGNED NOT NULL,
    MODIFY game_id INT UNSIGNED NOT NULL,
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY xpos INT NOT NULL,
    MODIFY ypos INT NOT NULL,
    MODIFY lifes_remaining INT NOT NULL,
    MODIFY date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
    
    ADD CONSTRAINT ck_enemies_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
    
    ADD CONSTRAINT fk_game_enemies FOREIGN KEY (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT pk_enemies PRIMARY KEY (enemy_id, game_id,region);

    
-- Taula chest
    
ALTER TABLE chest_opened
	MODIFY chest_id INT UNSIGNED NOT NULL,
	MODIFY game_id INT UNSIGNED NOT NULL,
	MODIFY region VARCHAR(20) NOT NULL,
	MODIFY xpos INT NOT NULL,
    MODIFY ypos INT NOT NULL,
    MODIFY date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
	
	ADD CONSTRAINT ck_chest_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
	
	ADD CONSTRAINT fk_game_chest FOREIGN KEY (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
	ADD CONSTRAINT pk_chest PRIMARY KEY (chest_id, game_id, region);

        
-- Table santuaries

ALTER TABLE santuaries_opened
	MODIFY sactuary_id INT UNSIGNED NOT NULL,
    MODIFY game_id INT UNSIGNED NOT NULL,
    MODIFY region VARCHAR(20) NOT NULL,
    MODIFY xpos INT NOT NULL,
    MODIFY ypos INT NOT NULL,
    MODIFY date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE NOW(),
    
    ADD CONSTRAINT ck_santuaries_region CHECK (region IN ('hyrule', 'death mountain', 'gerudo', 'necluda', 'castle')),
    
    ADD CONSTRAINT fk_game_santuaries FOREIGN KEY (game_id) REFERENCES game(game_id) ON UPDATE CASCADE ON DELETE CASCADE,
    ADD CONSTRAINT pk_santuaries PRIMARY KEY (sactuary_id, game_id, region);
  
