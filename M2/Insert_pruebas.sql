-- INSERT DE JUGADORES

INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('javier',2,2);
INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('marta',2,2);
INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('blanca',4,4);
INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('alvaro',2,4);


-- INSERT DE PARTIDAS

INSERT INTO game (fk_player_id_players_game,region) VALUES (1,'hyrule');
INSERT INTO game (fk_player_id_players_game,region) VALUES (2,'necluda');
INSERT INTO game (fk_player_id_players_game,region) VALUES (3,'hyrule');
INSERT INTO game (fk_player_id_players_game,region) VALUES (4,'necluda');
INSERT INTO game (fk_player_id_players_game,region) VALUES (1,'gerudo');
INSERT INTO game (fk_player_id_players_game,region) VALUES (2,'death mountain');
INSERT INTO game (fk_player_id_players_game,region) VALUES (1,'death mountain');

-- INSERT DE ARMAS

INSERT INTO weapons (fk_game_id_game_weapons