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
INSERT INTO game (fk_player_id_players_game,region) VALUES (1,'death mountain');

-- INSERT DE ARMAS

INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (5,'wood sword',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (1,'sword',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (1,'shield',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (1,'shield',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (2,'sword',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (2,'shield',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (3,'shield',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (4,'wood sword',2);
INSERT INTO weapons (fk_game_id_game_weapons,weapon_name,lives_remaining) VALUES (9,'sword',2);


-- INSERT DE COMIDA

INSERT INTO food (food_name,fk_game_id_game_food) VALUES ('salads',1);
INSERT INTO food (food_name,fk_game_id_game_food,quantity_remaining) VALUES ('fish',1,0);
INSERT INTO food (food_name,fk_game_id_game_food,quantity_remaining) VALUES ('meat',1,6);
INSERT INTO food (food_name,fk_game_id_game_food,quantity_remaining) VALUES ('vegetables',5,7);
