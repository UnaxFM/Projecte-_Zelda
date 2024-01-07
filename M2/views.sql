-- VISTA CONTEO ARMAS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_armas_partidas as
select p.user_name as 'NomUsuari',
	   g.game_id,
       w.weapon_name as 'NomArma',
       COUNT(distinct w.weapon_id) as 'QuantitatObtenida',
       g.date_started as 'DataPartida'
from players p join game g on p.player_id = g.fk_player_id_players_game
	          join weapons w on g.game_id = w.fk_game_id_game_weapons
group by p.user_name, g.game_id,w.weapon_name;



-- VISTA CONTEO COMIDA POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_comida_partidas as
select p.user_name as 'NomUsuari',
	   g.game_id,
       f.food_name as 'NomMenjar',
       SUM(f.quantity_remaining) as 'QuantitatObtenida',
       g.date_started as 'DataPartida'
from players p join game g on p.player_id = g.fk_player_id_players_game
	          join food f on g.game_id = f.fk_game_id_game_food
group by p.user_name, g.game_id, f.food_name;