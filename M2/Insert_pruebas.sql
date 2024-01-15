-- INSERT DE JUGADORES

INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('javier',2,2);
INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('marta',2,2);
INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('blanca',4,4);
INSERT INTO players (user_name,hearts_remaining,hearts_total) VALUES ('alvaro',2,4);

INSERT INTO game (user_name,hearts_remaining,hearts_total,region) VALUES ("javier",1,2,"hyrule");

-- INSERT DE PARTIDAS

INSERT INTO game (player_id,region,xpos,ypos) VALUES (1,'hyrule',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (2,'necluda',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (3,'hyrule',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (4,'necluda',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (1,'gerudo',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (2,'death mountain',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (1,'death mountain',1,1);
INSERT INTO game (player_id,region,xpos,ypos) VALUES (1,'death mountain',1,1);

-- INSERT DE ARMAS

INSERT INTO weapons (game_id,weapon_name,lives_remaining) VALUES (1,'wood sword',2);
INSERT INTO weapons (game_id,weapon_name,lives_remaining) VALUES (1,'sword',2);
INSERT INTO weapons (game_id,weapon_name,lives_remaining) VALUES (1,'shield',2);
INSERT INTO weapons (game_id,weapon_name,lives_remaining) VALUES (1,'shield',2);
INSERT INTO weapons (game_id,weapon_name,lives_remaining) VALUES (2,'sword',2);



-- INSERT DE COMIDA

INSERT INTO food (food_name,game_id,quantity_remaining) VALUES ('fish',1,0);
INSERT INTO food (food_name,game_id,quantity_remaining) VALUES ('meat',1,6);
INSERT INTO food (food_name,game_id,quantity_remaining) VALUES ('vegetables',5,7);
