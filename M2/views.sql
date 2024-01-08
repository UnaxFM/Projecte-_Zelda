-- VITA INFO JUGADOR

CREATE OR REPLACE VIEW v_inf_player as
select p.player_id as 'PlayerID',
       p.user_name as 'NomJugador',
       p.hearts_remaining as 'HeartsRemaining',
       p.hearts_total as 'HeartsTotal',
       g.date_started as 'DataPartida',
       g.region as 'Region',
       g.xpos as 'xpos',
       g.ypos as 'ypos',
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

CREATE OR REPLACE VIEW v_comidas_partidas as
select p.user_name as 'NomUsuari',
	   g.game_id,
       f.food_name as 'NomMenjar',
       SUM(f.quantity_remaining) as 'QuantitatObtenida',
       g.date_started as 'DataPartida'

from players p join game g on p.player_id = g.player_id
	           join food f on g.game_id = f.game_id
group by p.user_name, g.game_id, f.food_name;


-- VISTA SANTUARIOS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_santuarios_partidas as
select p.player_id as 'PlayerID',
	   p.user_name as 'NomUsuari',
       g.game_id,
       s.sactuary_id as 'SantuaryID',
       s.region as 'Region',
       s.xpos as 'xpos',
       s.ypos as 'ypos'

from players p join game g on p.player_id = g.player_id
			   join santuaries s on g.game_id = s.game_id;


-- VISTA DE COFRES POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_chest_partidas as
select p.player_id as 'PlayerID',
	   p.user_name as 'NomUsuari',
       g.game_id,
       c.chest_id as'ChestID',
       c.region as 'Region',
       c.xpos as 'xpos',
       c.ypos as 'ypos'

from players p join game g on p.player_id = g.player_id
			   join chest c on g.game_id = c.game_id;


-- VISTA DE ENEMIGOS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_enemies_partidas as
select p.player_id as 'PlayerID',
	   p.user_name as 'NomUsuari',
       g.game_id,
       e.enemy_id as 'EnemyID',
       e.region as 'Region',
       e.xpos as 'xpos',
       e.ypos as 'ypos',
       e.lifes_remaining as 'Lifes'

from players p join game g on p.player_id = g.player_id
			   join enemies e on g.game_id = e.game_id;