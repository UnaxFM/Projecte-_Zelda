USE zelda;

ALTER TABLE players
    MODIFY user_name INT NOT NULL,
	MODIFY hearts_remaining INT NOT NULL,
    MODIFY hearts_total INT NOT NULL,
    MODIFY date_created DATETIME DEFAULT NOW(),
    MODIFY date_modified DATETIME DEFAULT NOW() ON UPDATE NOW();


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