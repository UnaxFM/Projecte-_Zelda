import datos_juego as datos_importados

def importar_datos_partida_sin_modificaciones():
    datos_partida = {}
    for key_mapa in datos_importados.datos:
        if key_mapa == "castle":
            datos_partida[key_mapa] = datos_importados.datos[key_mapa].copy()
        else:
            dato_por_mapa = {}
            if "spawn" in datos_importados.datos[key_mapa]:
                spawn = datos_importados.datos[key_mapa]["spawn"].copy()
            enemigos = {}
            if "enemigos" in datos_importados.datos[key_mapa]:
                for enemigo in datos_importados.datos[key_mapa]["enemigos"]:
                    enemigos[enemigo] = datos_importados.datos[key_mapa]["enemigos"][enemigo].copy()
            arboles = {}
            if "arboles" in datos_importados.datos[key_mapa]:
                for arbol in datos_importados.datos[key_mapa]["arboles"]:
                    arboles[arbol] = datos_importados.datos[key_mapa]["arboles"][arbol].copy()
            cofres = {}
            if "cofres" in datos_importados.datos[key_mapa]:
                for cofre in datos_importados.datos[key_mapa]["cofres"]:
                    cofres[cofre] = datos_importados.datos[key_mapa]["cofres"][cofre].copy()
            if "fox" in datos_importados.datos[key_mapa]:
                fox = datos_importados.datos[key_mapa]["fox"].copy()
            santuarios = {}
            if "santuarios" in datos_importados.datos[key_mapa]:
                for santuario in datos_importados.datos[key_mapa]["santuarios"]:
                    santuarios[santuario] = datos_importados.datos[key_mapa]["santuarios"][santuario].copy()
            dato_por_mapa = {"spawn": spawn, "enemigos": enemigos, "arboles": arboles,  "cofres": cofres, "fox": fox, "santuarios": santuarios}
            datos_partida[key_mapa] = dato_por_mapa
    return datos_partida


def importar_datos_armas_sin_modificaciones():
    datos_armas = {}
    for arma in datos_importados.weapons:
        datos_armas[arma] = datos_importados.weapons[arma].copy()
    return datos_armas


def importar_datos_comida_sin_modificaciones():
    datos_comida = {}
    for alimento in datos_importados.food:
        datos_comida[alimento] = datos_importados.food[alimento].copy()
    return datos_comida

def importar_datos_jugador_sin_modificaciones():
    datos_jugador = datos_importados.informacion_jugador.copy()
    datos_jugador["items_equipados"] = []
    return datos_jugador

info_alimento_partida = importar_datos_comida_sin_modificaciones()
info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
datos_partida_actual = importar_datos_partida_sin_modificaciones()

"""
for arma in info_equipamiento_partida:
    print(info_equipamiento_partida[arma])
for alimento in info_alimento_partida:
    print(info_alimento_partida[alimento])
comprobación
"""
#print(info_alimento_partida)
#print(info_equipamiento_partida)
#print(datos_jugador_actual)
#print(datos_partida_actual)

"""
cursor.execute("SELECT GameID, DataLastSave, NomJugador, Region, HeartsRemaining, HeartsTotal "
                       "FROM v_inf_player ORDER BY DataLastSave DESC LIMIT 8;")
    diccionario_partidas_guardadas = {}
    for partida_cargada_bbdd in cursor:
"""
"""
# CARGAR PARTIDA
# para datos jugador
# cursor.execute(f"SELECT nombre_usuario, vida actual, blood_moon_countdown, "blood_moon_appearances", region WHERE primary_key = {}")
print(datos_jugador_actual)
cursor = ("Pablo", 4, 17, 5, "death mountain")
datos_jugador_actual["nombre"] = cursor[0]
datos_jugador_actual["vida_actual"] = cursor[1]
datos_jugador_actual["blood_moon_countdown"] = cursor[2]
datos_jugador_actual["blood_moon_appearances"] = cursor[3]
datos_jugador_actual["region"] = cursor[4]
print(datos_jugador_actual)

# CARGAR COMIDA
# cursor.execute(f"SELECT comida, cantidad WHERE primary_key = {}")
print(info_alimento_partida)
cursor = (("vegetables", 0), ("fish", 34), ("meat", 1), ("salads", 7), ("pescatarian", 10), ("roasted", 5))
for alimento_cargado in cursor:
    info_alimento_partida[alimento_cargado[0]]["cantidad"] = alimento_cargado[1]
print(info_alimento_partida)

# CARGAR ARMAS
# cursor.execute(f"SELECT arma, equipado, usos, cantidad WHERE primary_key = {}")
cursor = (("wood sword", True, 3, 5),("sword", False, 3, 1), ("wood shield", True, 3, 2), ("shield", False, 3, 3))

print(info_equipamiento_partida)
for arma_cargada in cursor:
    info_equipamiento_partida[arma_cargada[0]]["equipado"] = arma_cargada[1]
    info_equipamiento_partida[arma_cargada[0]]["usos"] = arma_cargada[2]
    info_equipamiento_partida[arma_cargada[0]]["cantidad"] = arma_cargada[3]
print(info_equipamiento_partida)

# se comprueba si esta equipada y se añade al equipamiento dentro de items_equipados del usuario
for arma in info_equipamiento_partida:
    if info_equipamiento_partida[arma]["equipado"]:
        datos_jugador_actual["items_equipados"].append(arma)

print(info_equipamiento_partida)
print(datos_jugador_actual)

# CARGAR ENEMIGOS
print(datos_partida_actual["hyrule"]["enemigos"][0])
print(datos_partida_actual["death mountain"]["enemigos"][0])

# cursor.execute(f"SELECT region, numero, x, y, vida WHERE primary_key = {}")
cursor = (("hyrule", 0, 3, 8, 5), ("death mountain", 0, 3, 15, 8))
for enemigo in cursor:
    datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["x"] = enemigo[2]
    datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["y"] = enemigo[3]
    datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["vida"] = enemigo[4]

print(datos_partida_actual["hyrule"]["enemigos"][0])
print(datos_partida_actual["death mountain"]["enemigos"][0])

# CARGAR COFRES

print(datos_partida_actual["hyrule"]["cofres"][0])
print(datos_partida_actual["death mountain"]["cofres"][0])
# cursor.execute(f"SELECT region, numero WHERE primary_key = {}")
cursor = (("hyrule", 0), ("death mountain", 0))
for cofre in cursor:
    datos_partida_actual[cofre[0]]["cofres"][cofre[1]]["abierto"] = True
print(datos_partida_actual["hyrule"]["cofres"][0])
print(datos_partida_actual["death mountain"]["cofres"][0])

# CARGAR SANTUARIOS
print(datos_partida_actual["hyrule"]["santuarios"][0])
print(datos_partida_actual["death mountain"]["santuarios"][3])
# cursor.execute(f"SELECT region, numero WHERE primary_key = {}")
cursor = (("hyrule", 0), ("death mountain", 3), ("gerudo", 4))
for santuario in cursor:
    datos_partida_actual[santuario[0]]["santuarios"][santuario[1]]["descubierto"] = True
    datos_jugador_actual["vida_total"] += 1  # SUMO LA VIDA
print(datos_partida_actual["hyrule"]["santuarios"][0])
print(datos_partida_actual["death mountain"]["santuarios"][3])
print(datos_jugador_actual)
"""

def cargar_partida():
    # CARGAR PARTIDA
    # para datos jugador
    # cursor.execute(f"SELECT nombre_usuario, vida actual, blood_moon_countdown, "blood_moon_appearances", region WHERE primary_key = {key_primaria}")
    cursor = ("Pablo", 4, 17, 5, "necluda")
    datos_jugador_actual["nombre"] = cursor[0]
    datos_jugador_actual["vida_actual"] = cursor[1]
    datos_jugador_actual["blood_moon_countdown"] = cursor[2]
    datos_jugador_actual["blood_moon_appearances"] = cursor[3]
    datos_jugador_actual["region"] = cursor[4]
    # CARGAR COMIDA
    # cursor.execute(f"SELECT comida, cantidad WHERE primary_key = {key_primaria}")
    cursor = (("vegetables", 0), ("fish", 34), ("meat", 1), ("salads", 7), ("pescatarian", 10), ("roasted", 5))
    for alimento_cargado in cursor:
        info_alimento_partida[alimento_cargado[0]]["cantidad"] = alimento_cargado[1]
    # CARGAR ARMAS
    # cursor.execute(f"SELECT arma, equipado, usos, cantidad WHERE primary_key = {key_primaria}")
    cursor = (("wood sword", True, 3, 5), ("sword", False, 3, 1), ("wood shield", True, 3, 2), ("shield", False, 3, 3))
    for arma_cargada in cursor:
        info_equipamiento_partida[arma_cargada[0]]["equipado"] = arma_cargada[1]
        info_equipamiento_partida[arma_cargada[0]]["usos"] = arma_cargada[2]
        info_equipamiento_partida[arma_cargada[0]]["cantidad"] = arma_cargada[3]
    # se comprueba si esta equipada y se añade al equipamiento dentro de items_equipados del usuario
    for arma in info_equipamiento_partida:
        if info_equipamiento_partida[arma]["equipado"]:
            datos_jugador_actual["items_equipados"].append(arma)
    # CARGAR ENEMIGOS
    # cursor.execute(f"SELECT region, numero, x, y, vida WHERE primary_key = {key_primaria}")
    cursor = (("hyrule", 0, 3, 8, 5), ("death mountain", 0, 3, 25, 8))
    for enemigo in cursor:
        datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["x"] = enemigo[2]
        datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["y"] = enemigo[3]
        datos_partida_actual[enemigo[0]]["enemigos"][enemigo[1]]["vida"] = enemigo[4]
    # CARGAR COFRES
    # cursor.execute(f"SELECT region, numero WHERE primary_key = {key_primaria}")
    cursor = (("hyrule", 0), ("death mountain", 0))
    for cofre in cursor:
        datos_partida_actual[cofre[0]]["cofres"][cofre[1]]["abierto"] = True
    # CARGAR SANTUARIOS
    # cursor.execute(f"SELECT region, numero WHERE primary_key = {key_primaria}")
    cursor = (("hyrule", 0), ("death mountain", 3))
    for santuario in cursor:
        datos_partida_actual[santuario[0]]["santuarios"][santuario[1]]["descubierto"] = True
        datos_jugador_actual["vida_total"] += 1  # SUMO LA VIDA


print(info_alimento_partida)
print(info_equipamiento_partida)
print(datos_jugador_actual)
print(datos_partida_actual)
print(datos_partida_actual["hyrule"]["enemigos"][0])
print(datos_partida_actual["death mountain"]["enemigos"][0])
print(datos_partida_actual["hyrule"]["cofres"][0])
print(datos_partida_actual["death mountain"]["cofres"][0])
print(datos_partida_actual["hyrule"]["santuarios"][0])
print(datos_partida_actual["death mountain"]["santuarios"][3])

cargar_partida()

print(info_alimento_partida)
print(info_equipamiento_partida)
print(datos_jugador_actual)
print(datos_partida_actual)
print(datos_partida_actual["hyrule"]["enemigos"][0])
print(datos_partida_actual["death mountain"]["enemigos"][0])
print(datos_partida_actual["hyrule"]["cofres"][0])
print(datos_partida_actual["death mountain"]["cofres"][0])
print(datos_partida_actual["hyrule"]["santuarios"][0])
print(datos_partida_actual["death mountain"]["santuarios"][3])

