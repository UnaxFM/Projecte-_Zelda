-- 1) usuaris que han jugat

select p.user_name as 'NomUsuari',
	   MAX(g.date_started) as 'UltimaPartida'

from players p join game g on p.player_id = g.fk_player_id_players_game
group by p.player_id,p.user_name;


-- 2) quantitat de partides jugades per usuari

select p.user_name as 'NomUsuari', 
	   COUNT(g.game_id) as 'PartidesJugades'

from players p join game g on p.player_id = g.fk_player_id_players_game
group by p.player_id, p.user_name;


-- 3) Armes usades per cada usuari i dades de la partida on n'ha gastat més

