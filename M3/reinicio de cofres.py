import datos_juego as datos_importados

def importar_datos_partida_sin_modificaciones():
    datos_partida = {}
    for key_mapa in datos_importados.datos:
        if key_mapa == "castle":
            spawn = datos_importados.datos[key_mapa]["spawn"].copy()
            ganon = datos_importados.datos[key_mapa][0].copy()
            datos_partida[key_mapa] = {"spawn": spawn, 0: ganon}
        else:
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

datos_partida_actual["hyrule"]["cofres"][0]["descubierto"] = True
print(info_equipamiento_partida["wood sword"]["cantidad"])
print(info_equipamiento_partida["sword"] ["cantidad"])

### PRUEBA INSERTS
sql = "INSERT INTO chest_opened (chest_id, game_id, region, xpos, ypos) VALUES (%s, %s, %s, %s, %s)"
val = []
lugares = ["hyrule", "death mountain", "necluda", "gerudo"]
for lugar in lugares:
    for cofre in datos_partida_actual[lugar]["cofres"]:
        temp = (cofre, key_primaria_partida, lugar, datos_partida_actual[lugar]["cofres"][cofre]["x"], datos_partida_actual[lugar]["cofres"][cofre]["y"])
        val.append(temp)
cursor.executemany(sql, val)
db.commit()

"""
sql = "INSERT INTO chest_opened (chest_id, game_id, region, xpos, ypos) VALUES (%s, %s, %s, %s, %s)"
val = temp = (key_del_cofre, key_primaria_partida, datos_jugador_actual["region"], datos_partida_actual[lugar]["cofres"][cofre]["x"], datos_partida_actual[lugar]["cofres"][cofre]["y"])
cursor.execute(sql, val)
db.commit()
"""

def reinicio_cofres(primary_key):
    if info_equipamiento_partida["wood sword"]["cantidad"] == 0 and info_equipamiento_partida["sword"] ["cantidad"] == 0:
        lugares = ["hyrule", "death mountain", "necluda", "gerudo"]
        for lugar in lugares:
            for cofre in datos_partida_actual[lugar]["cofres"]:
                if datos_partida_actual[lugar]["cofres"][cofre]["abierto"]:  # Si esta abierto, lo cambio a false
                    datos_partida_actual[lugar]["cofres"][cofre]["abierto"] = False
        sql = f"DELETE FROM chest_opened WHERE game_id = {primary_key}"
        cursor.execute(sql)
        db.commit()
        print("Cofres reiniciados correctamente ya que no te quedaban espadas")
        for lugar in lugares:
            for cofre in datos_partida_actual[lugar]["cofres"]:
                if datos_partida_actual[lugar]["cofres"][cofre]["abierto"]:  # Si esta abierto, lo cambio a false
                    print(datos_partida_actual[lugar]["cofres"][cofre]["abierto"])
    else:
        contador = 0
        lugares = ["hyrule", "death mountain", "necluda", "gerudo"]
        for lugar in lugares:
            for cofre in datos_partida_actual[lugar]["cofres"]:
                if datos_partida_actual[lugar]["cofres"][cofre]["descubierto"]:
                    contador += 1
        if contador == 7:
            sql = f"DELETE FROM chest_opened WHERE game_id = {primary_key}"
            cursor.execute(sql)
            db.commit()
            print("Cofres reiniciados correctamente ya que estaban todos abiertos")
            for lugar in lugares:
                for cofre in datos_partida_actual[lugar]["cofres"]:
                    if datos_partida_actual[lugar]["cofres"][cofre]["abierto"]:  # Si esta abierto, lo cambio a false
                        print(datos_partida_actual[lugar]["cofres"][cofre]["abierto"])

print(datos_partida_actual["hyrule"]["cofres"][0]["descubierto"])
