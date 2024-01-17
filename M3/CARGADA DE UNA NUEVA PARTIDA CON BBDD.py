def cargar_partida(primary_key):
    # CARGAR PARTIDA
    # para datos jugador
    cursor = db.cursor()
    cursor.execute(f"SELECT user_name, hearts_remaining, blood_moon_countdown, blood_moon_appearences, region FROM game WHERE game_id = {primary_key}")
    for jugador in cursor:
        datos_jugador_actual["nombre"] = jugador[0]
        datos_jugador_actual["vida_actual"] = jugador[1]
        datos_jugador_actual["blood_moon_countdown"] = jugador[2]
        datos_jugador_actual["blood_moon_appearances"] = jugador[3]
        datos_jugador_actual["region"] = jugador[4]
    print("Info jugador cargada")
    # CARGAR COMIDA
    cursor.execute(f"SELECT food_name, quantity_remaining FROM food WHERE game_id = {primary_key}")
    for alimento_cargado in cursor:
        info_alimento_partida[alimento_cargado[0]]["cantidad"] = alimento_cargado[1]
    print("Info comida cargada")
    # CARGAR ARMAS
    cursor.execute(f"SELECT weapon_name, equiped, lives_remaining, uses FROM weapons WHERE game_id = {primary_key}")
    for arma_cargada in cursor:
        info_equipamiento_partida[arma_cargada[0]]["equipado"] = arma_cargada[1]
        info_equipamiento_partida[arma_cargada[0]]["usos"] = arma_cargada[2]
        info_equipamiento_partida[arma_cargada[0]]["cantidad"] = arma_cargada[3]
    # se comprueba si esta equipada y se añade al equipamiento dentro de items_equipados del usuario
    for arma in info_equipamiento_partida:
        if info_equipamiento_partida[arma]["equipado"]:
            datos_jugador_actual["items_equipados"].append(arma)
    print("armas cargadas")
    # CARGAR ENEMIGOS
    cursor.execute(f"SELECT region, enemy_id, xpos, ypos, lifes_remaining FROM enemies WHERE game_id = {primary_key}")
    for enemigo in cursor:
        if enemigo[0] == "castle":
            datos_partida_actual[enemigo[0]][0]["vida"] = enemigo[4]
        else:
            datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["x"] = enemigo[2]
            datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["y"] = enemigo[3]
            datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["vida"] = enemigo[4]
    print("cofres cargados")
    # CARGAR COFRES
    cursor.execute(f"SELECT region, chest_id FROM chest_opened WHERE game_id = {primary_key}")
    for cofre in cursor:
        datos_partida_actual[cofre[0]]["cofres"][cofre[1]]["abierto"] = True
    # CARGAR SANTUARIOS
    cursor.execute(f"SELECT region, sactuary_id FROM santuaries_opened WHERE game_id = {primary_key}")
    for santuario in cursor:
        datos_partida_actual[santuario[0]]["santuarios"][santuario[1]]["descubierto"] = True
        datos_jugador_actual["vida_total"] += 1  # SUMO LA VIDA