-- VITA INFO JUGADOR

CREATE OR REPLACE VIEW v_inf_player as
select p.player_id as 'PlayerID',
	   g.date_started as 'DataPartida',
       p.user_name as 'NomJugador',
       g.region as 'Region',
       p.hearts_remaining as 'HeartsRemaining',
       p.hearts_total as 'HeartsTotal',
       blood_moon_countdown as 'BM_countdown',
       blood_moon_appearences as 'BMappeareces'
       
from players p join game g on p.player_id = g.player_id;

-- VISTA CONTEO ARMAS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_armas_partidas as
select p.user_name as 'NomUsuari',
	   g.game_id,
       w.weapon_name as 'NomArma',
       COUNT(distinct w.weapon_id) as 'QuantitatObtenida',
       g.date_started as 'DataPartida'
from players p join game g on p.player_id = g.player_id
	          join weapons w on g.game_id = w.game_id
group by p.user_name, g.game_id,w.weapon_name;



-- VISTA CONTEO COMIDA POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_comida_partidas as
select p.user_name as 'NomUsuari',
	   g.game_id,
       f.food_name as 'NomMenjar',
       SUM(f.quantity_remaining) as 'QuantitatObtenida',
       g.date_started as 'DataPartida'
from players p join game g on p.player_id = g.player_id
	          join food f on g.game_id = f.game_id
group by p.user_name, g.game_id, f.food_name;