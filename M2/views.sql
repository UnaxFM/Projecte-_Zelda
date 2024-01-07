CREATE OR REPLACE VIEW v_inf_players as
select p.user_name, g.game_id, g.region

from players p join game g on p.player_id = g.fk_player_id_players_game;

