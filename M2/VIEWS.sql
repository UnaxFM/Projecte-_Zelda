
-- VISTA CONTEO ARMAS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_armas_partidas as
select g.user_name as 'NomUsuari',
	   g.game_id,
       w.weapon_name as 'NomArma',
       w.uses as 'Uses',
       g.date_started as 'DataPartida'

from game g join weapons w on g.game_id = w.game_id
group by g.user_name, g.game_id,w.weapon_name;



-- VISTA CONTEO COMIDA POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_comidas_partidas as
select g.user_name as 'NomUsuari',
	   g.game_id,
       f.food_name as 'NomMenjar',
       SUM(f.quantity_remaining) as 'QuantitatObtenida',
       g.date_started as 'DataPartida'

from game g join food f on g.game_id = f.game_id
group by g.user_name, g.game_id, f.food_name;


-- VISTA SANTUARIOS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_santuarios_partidas as
select g.user_name as 'NomUsuari',
       g.game_id,
       s.sactuary_id as 'SantuaryID',
       s.region as 'Region',
       s.xpos as 'xpos',
       s.ypos as 'ypos'

from game g join santuaries_opened s on g.game_id = s.game_id;


-- VISTA DE COFRES POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_chest_partidas as
select g.user_name as 'NomUsuari',
       g.game_id,
       c.chest_id as'ChestID',
       c.region as 'Region',
       c.xpos as 'xpos',
       c.ypos as 'ypos'

from game g join chest_opened c on g.game_id = c.game_id;


-- VISTA DE ENEMIGOS POR PARTIDA DE CADA USUARIO

CREATE OR REPLACE VIEW v_enemies_partidas as
select g.user_name as 'NomUsuari',
       g.game_id,
       e.enemy_id as 'EnemyID',
       e.region as 'Region',
       e.xpos as 'xpos',
       e.ypos as 'ypos',
       e.lifes_remaining as 'Lifes'

from game g join enemies e on g.game_id = e.game_id;
               

-- VISTES DE CONSULTES A LA BD

-- 1) usuaris que han jugat

CREATE OR REPLACE VIEW query_1_usuaris as
select user_name as 'NomUsuari',
	   MAX(date_started) as 'UltimaPartida'

from game
group by user_name
order by user_name;

-- 2) quantitat de partides jugades per usuari

CREATE OR REPLACE VIEW query_2_partides as
select user_name as 'NomUsuari', 
	   COUNT(game_id) as 'PartidesJugades'

from game
group by user_name
order by user_name;

-- 3) Armes usades per cada usuari i dades de la partida on n'ha gastat més: Consulta a través de la vista 

CREATE OR REPLACE VIEW query_3_armes as
SELECT
    g.user_name as 'NomUsuari',
    w.weapon_name as 'NomArma',
    w.quantity as 'QuantitatTotalObtenida',
    g.date_modified as 'DataPartida'
    
from game g join weapons w on g.game_id = w.game_id
where w.quantity > 0;

    
-- 4) Menjar consumit per cada usuari i dades de la partida on n'ha consumit més: consulta a través de la vista

CREATE OR REPLACE VIEW query_4_menjar as
SELECT
    g.user_name as 'NomUsuari',
    f.food_name as 'NomMenjar',
    f.quantity_remaining as 'QuantitatTotalObtenida',
	g.date_modified as 'DataPartida'

from game g join food f on g.game_id = f.game_id
where f.quantity_remaining >0;

    
-- 5) Estadística de "blood moons"

      -- mitjana blood moons
      
CREATE OR REPLACE VIEW query_5_mitjanabm as
select avg(blood_moon_appearences) as 'MediaBloodMoons'
from game;

      -- dades de la partida on han aparegut més

CREATE OR REPLACE VIEW query_5_mesbm as
SELECT
    date_started AS DataPartida,
    user_name AS NomUsuari,
    blood_moon_appearences AS QuantitatBloodMoons
from game 
order by blood_moon_appearences DESC
LIMIT 1;
