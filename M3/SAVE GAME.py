# SE GUARDA PARTIDA AL OBTENER COMIDA O ALIMENTO + ABRIR SANTUARIO + CAMBIAR DE SECCIÓN
# POR LO TANTO, AL ABRIR SANTUARIO O COFRE, HAY QUE HACER UN INSERT, UPDATE DE DATOS DE SIEMPRE (info_jugador, comida, armas y enemigos)
# AL GUARDAR LA PARTIDA SE DEBE TENER EN CUENTA LO SIGUIENTE

key_primaria_partida = 3
"""
def save_game():
    #cursor.execute("query_delete")
    print(f"UPDATE game SET user_name = {datos_jugador_actual['nombre']}, "
          f"hearts_remaining = {datos_jugador_actual['vida_actual']}, "
          f"blood_moon_countdown = {datos_jugador_actual['blood_moon_countdown']}, "
          f"blood_moon_appearances = {datos_jugador_actual['blood_moon_appearances']}, "
          f"region = {datos_jugador_actual['region']} "
          f"WHERE game_id = {key_primaria_partida};")
    for alimento in info_alimento_partida:
        print(f"UPDATE game_food SET quantity_remaining = {info_alimento_partida[alimento]['cantidad']} "
              f"WHERE game_id = {key_primaria_partida} AND food_name = {alimento};")
    for arma in info_equipamiento_partida:
        print(f"UPDATE game_weapons SET equiped = {info_equipamiento_partida[arma]['equipado']}, "
              f"lives_remaining = {info_equipamiento_partida[arma]['usos']}, "
              f"quantity_remaining = {info_equipamiento_partida[arma]['cantidad']} "
              f"WHERE game_id = {key_primaria_partida} AND weapon_name = {arma};")
    for region in datos_partida_actual:
        if region == "castle":
            print(f"UPDATE game_enemies SET lifes_remaining = {datos_partida_actual[region][0]['vida']} WHERE game_id = {key_primaria_partida} AND region = {region} AND num = {0};")
        else:
            for enemigo in datos_partida_actual[region]["enemigos"]:
                print(f"UPDATE game_enemies "
                      f"SET xpos = {datos_partida_actual[region]['enemigos'][enemigo]['x']}, "
                      f"ypos {datos_partida_actual[region]['enemigos'][enemigo]['y']}, "
                      f"lifes_remaining = {datos_partida_actual[region]['enemigos'][enemigo]['vida']} "
                      f"WHERE game_id = {key_primaria_partida} AND region = {region} AND num = {enemigo};")
    #db.commit()
save_game()
"""
