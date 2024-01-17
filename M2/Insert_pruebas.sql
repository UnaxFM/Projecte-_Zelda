-- INSERT DE PARTIDAS

INSERT INTO game (user_name,hearts_remaining,hearts_total,region) VALUES ("javier",1,2,"hyrule");


-- INSERT DE ARMAS

INSERT INTO weapons (game_id,weapon_name,lives_remaining) VALUES (1,'wood sword',2);


-- INSERT DE COMIDA

INSERT INTO food (food_name,game_id,quantity_remaining) VALUES ("salads",1,2);
