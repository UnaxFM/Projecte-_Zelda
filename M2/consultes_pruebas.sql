-- 1) usuaris que han jugat

select p.user_name as 'NomUsuari',
	   MAX(g.date_started) as 'UltimaPartida'

from players p join game g on p.player_id = g.player_id
group by p.player_id,p.user_name
order by p.user_name;


-- 2) quantitat de partides jugades per usuari

select p.user_name as 'NomUsuari', 
	   COUNT(g.game_id) as 'PartidesJugades'

from players p join game g on p.player_id = g.player_id
group by p.player_id, p.user_name
order by p.user_name;


-- 3) Armes usades per cada usuari i dades de la partida on n'ha gastat més: Consulta a través de la vista --- mal ya que da solo la sum de esa partida

select NomUsuari, 
	   NomArma,
       SUM(QuantitatObtenida) as 'QuantitatTotalObtenida',
       DataPartida as 'DataPartidaMesUsada'

from v_armas_partidas
where (NomUsuari, NomArma, QuantitatObtenida) IN (select NomUsuari,NomArma,
															  MAX(QuantitatObtenida) as 'MaxQuantitatObtenida'
													  from v_armas_partidas group by NomUsuari, NomArma)
group by NomUsuari, NomArma, DataPartida;

-- respuesta del chatgpt

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

select NomUsuari, 
	   NomMenjar,
       SUM(QuantitatObtenida) as 'QuantitatTotalObtenida',
       DataPartida as 'DataPartidaMesUsada'

from v_comidas_partidas
where (NomUsuari, NomMenjar, QuantitatObtenida) IN (select NomUsuari,NomMenjar,
															  MAX(QuantitatObtenida) as 'MaxQuantitatObtenida'
													  from v_comida_partidas group by NomUsuari, NomMenjar)
group by NomUsuari, NomMenjar, DataPartida;

-- respuesta del chatgpt

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
select avg(blood_moon_appearences) as 'MediaBloodMoons'
from game;

      -- dades de la partida on han aparegut més

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



