-- VITA INFO JUGADOR

CREATE OR REPLACE VIEW v_inf_player as
select p.player_id as 'PlayerID',
       p.user_name as 'NomJugador',
       p.hearts_remaining as 'HeartsRemaining',
       p.hearts_total as 'HeartsTotal',
       g.date_started as 'DataPrimeraPartida',
       g.date_modified as 'DataLastSave',
       g.game_id as 'GameID',
       g.region as 'Region',
       g.xpos as 'xpos',
       g.ypos as 'ypos',
       g.blood_moon_countdown as 'BM_countdown',
       g.blood_moon_appearences as 'BMappeareces'
       
from players p left join game g on p.player_id = g.player_id;

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
               

-- VISTES DE CONSULTES A LA BD

-- 1) usuaris que han jugat

CREATE OR REPLACE VIEW query_1_usuaris as
select p.user_name as 'NomUsuari',
	   MAX(g.date_started) as 'UltimaPartida'

from players p join game g on p.player_id = g.player_id
group by p.player_id,p.user_name
order by p.user_name;

-- 2) quantitat de partides jugades per usuari

CREATE OR REPLACE VIEW query_2_partides as
select p.user_name as 'NomUsuari', 
	   COUNT(g.game_id) as 'PartidesJugades'

from players p join game g on p.player_id = g.player_id
group by p.player_id, p.user_name
order by p.user_name;

-- 3) Armes usades per cada usuari i dades de la partida on n'ha gastat més: Consulta a través de la vista --- mal ya que da solo la sum de esa partida

CREATE OR REPLACE VIEW query_3_armes as
SELECT
    NomUsuari,
    NomArma,
    QuantitatTotalObtenida,
    DataPartida
FROM (
    SELECT
        NomUsuari,
        NomArma,
        QuantitatTotalObtenida,
        DataPartida,
        RANK() OVER (PARTITION BY NomUsuari, NomArma ORDER BY QuantitatTotalObtenida DESC) AS RankPartida
    FROM (
        SELECT
            NomUsuari,
            NomArma,
            SUM(QuantitatObtenida) AS QuantitatTotalObtenida,
            MAX(DataPartida) AS DataPartida
        FROM
            v_armas_partidas
        GROUP BY
            NomUsuari, NomArma
    ) AS SubconsultaTotal
) AS SubconsultaRankeada
WHERE
    RankPartida = 1;
    
-- 4) Menjar consumit per cada usuari i dades de la partida on n'ha consumit més: consulta a través de la vista

CREATE OR REPLACE VIEW query_4_menjar as
SELECT
    NomUsuari,
    NomMenjar,
    QuantitatTotalObtenida,
    DataPartida
FROM (
    SELECT
        NomUsuari,
        NomMenjar,
        QuantitatTotalObtenida,
        DataPartida,
        RANK() OVER (PARTITION BY NomUsuari, NomMenjar ORDER BY QuantitatTotalObtenida DESC) AS RankPartida
    FROM (
        SELECT
            NomUsuari,
            NomMenjar,
            SUM(QuantitatObtenida) AS QuantitatTotalObtenida,
            MAX(DataPartida) AS DataPartida
        FROM
            v_comidas_partidas
        GROUP BY
            NomUsuari, NomMenjar
    ) AS SubconsultaTotal
) AS SubconsultaRankeada
WHERE
    RankPartida = 1;
    
-- 5) Estadística de "blood moons"

      -- mitjana blood moons
      
CREATE OR REPLACE VIEW query_5_mitjanabm as
select avg(blood_moon_appearences) as 'MediaBloodMoons'
from game;

      -- dades de la partida on han aparegut més

CREATE OR REPLACE VIEW query_5_mesbm as
SELECT
    g.date_started AS DataPartida,
    p.user_name AS NomUsuari,
    g.blood_moon_appearences AS QuantitatBloodMoons
FROM
    game g
JOIN
    players p ON g.player_id = p.player_id
ORDER BY
    g.blood_moon_appearences DESC
LIMIT 1;