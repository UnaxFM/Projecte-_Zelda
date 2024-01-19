import os
import platform
import random
import prints_menus as pm
import datos_juego as datos_importados

import mysql.connector

# Conexión con la BBDD
db = mysql.connector.connect(
    host="51.105.57.176",
    user="root",
    passwd="root",
    database="zelda"
)

cursor = db.cursor()

# LIMPIEZA DE PANTALLA
sistema = platform.system()

def limpiar_pantalla():
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# IMPORTACION DE DATOS DE datos_juego

def importar_datos_partida_sin_modificaciones():
    datos_partida = {}
    for key_mapa in datos_importados.datos:
        if key_mapa == "castle":
            datos_partida[key_mapa] = datos_importados.datos[key_mapa].copy()
        else:  # para evitar errores entre la diferente estructura castle / resto de regiones
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


# Estos son los datos sobre los que se interactua, puesto que son los mismos diccionarios importados.
info_alimento_partida = importar_datos_comida_sin_modificaciones()
info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
datos_partida_actual = importar_datos_partida_sin_modificaciones()


# CARGADO DE PARTIDAS
ver_todos = False  # RESET A FALSE CUANDO SE PASE DE PANTALLA !!!!! ojo hay que actualizarlo

def seleccionar_partidas_guardadas():
    if ver_todos:  # MODIFICAR AL CAMBIAR LA BBDD
        cursor.execute("SELECT game_id, date_modified, user_name, region, hearts_remaining, hearts_total "
                       "FROM game ORDER BY date_modified DESC")
    else:
        cursor.execute("SELECT game_id, date_modified, user_name, region, hearts_remaining, hearts_total "
                       "FROM game ORDER BY date_modified DESC LIMIT 8;")
    diccionario_partidas_guardadas = {}
    for partida_cargada_bbdd in cursor:
        partida = {"nombre_jugador": partida_cargada_bbdd[2],
                   "fecha_modificacion": partida_cargada_bbdd[1].strftime("%d/%m/%Y %H:%M:%S"),
                   "region": partida_cargada_bbdd[3],
                   "corazones_actuales": partida_cargada_bbdd[4],
                   "corazones_totales": partida_cargada_bbdd[5]}
        diccionario_partidas_guardadas[partida_cargada_bbdd[0]] = partida
    return diccionario_partidas_guardadas


def metodo_burbuja_ordenar_partidas_recientes(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if partidas_guardadas[lista[j]]["fecha_modificacion"] < partidas_guardadas[lista[j + 1]]["fecha_modificacion"]:  # Aqui se comprueba el parámetro
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Pero lo que se ordena es la lista de keys
    return lista

# PRIMERA CARGADA DE PARTIDAS DISPONIBLES  (permite cargar partida nada más iniciar el juego)
partidas_guardadas = seleccionar_partidas_guardadas()
lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))


# FLAGS
flag_general_juego = False
flag_main_menu = True
flag_about = False
flag_help_main_menu = False
flag_new_game = False
flag_help_new_game = False
flag_saved_games = False
flag_help_saved_games = False
flag_queries = False
flag_legend = False
flag_plot = False
flag_in_game = False
flag_ganon_castle = False
flag_help_inventory = False
flag_show_map = False
flag_zelda_saved = False
flag_link_death = False

# DATOS DE PARTIDA ACTUALIZABLES FUERA
key_primaria_partida = ""


# MENUS PRE-GAME

def print_main_menu():  # Se pone aqui por error (se produce circular import)
    print("* " * 40)
    eleccion_personaje_ascii = random.randrange(3)
    for i in range(len(pm.decoracion_personaje_1)):
        if i == 4:
            print("* " + " Zelda breath of the Wild".ljust(56) + pm.decoracion_main_menu[eleccion_personaje_ascii][i] + " " * 5 + "*")
        else:
            print("* " + " " * 56 + pm.decoracion_main_menu[eleccion_personaje_ascii][i] + " " * 5 + "*")
    if len(partidas_guardadas) != 0:
        print("* Continue, New Game, Help, About, Queries, Exit  " + "* " * 15)
    else:
        print("* New Game, Help, About, Queries, Exit  " + "* " * 20)


def print_saved_games():
    print("* " + "Saved games " + "* " * 33 + "\n" +
          "* " + " " * 76 + "* ")
    if len(lista_partidas) < 8:
        for i in range(len(lista_partidas)):
            print("*\t" + f"{i}: {partidas_guardadas[lista_partidas[i]]['fecha_modificacion']} - "
                          f"{partidas_guardadas[lista_partidas[i]]['nombre_jugador']}, "
                          f"{partidas_guardadas[lista_partidas[i]]['region']}".ljust(68) +
                  f"♥ {partidas_guardadas[lista_partidas[i]]['corazones_actuales']}/{partidas_guardadas[lista_partidas[i]]['corazones_totales']}".rjust(5) + " *")
        for i in range(8 - len(lista_partidas)):
            print("* " + " " * 76 + "* ")
    else:
        for i in range(len(lista_partidas)):
            print("*\t" + f"{i}: {partidas_guardadas[lista_partidas[i]]['fecha_modificacion']} - "
                          f"{partidas_guardadas[lista_partidas[i]]['nombre_jugador']}, "
                          f"{partidas_guardadas[lista_partidas[i]]['region']}".ljust(68) +
                  f"♥ {partidas_guardadas[lista_partidas[i]]['corazones_actuales']}/{partidas_guardadas[lista_partidas[i]]['corazones_totales']}".rjust(5) + " *")
    print("* " + " " * 76 + "* ")
    if not ver_todos:
        print("* " + "Play X, Erase X, Show All, Help, Back " + "* " * 20)
    else:
        print("* " + "Play X, Erase X, Show Recent, Help, Back  " + "* " * 18)


def asignar_nombre(nombre):
    global flag_new_game
    global flag_legend
    if nombre == "":
        nombre = "Link"
        lista_prompt.append(f"Welcome to the game, {nombre}")
        flag_legend = True
        flag_new_game = False
        return nombre
    elif 3 <= len(nombre) <= 10 and nombre.replace(" ", "").isalnum():
        lista_prompt.append(f"Welcome to the game, {nombre}")
        flag_legend = True
        flag_new_game = False
        return nombre
    else:
        lista_prompt.append(f"{nombre} is not a valid name")
        return ""


# CREACION Y CARGA DE PARTIDA
def crear_nueva_partida(primary_key):
    sql = "INSERT INTO food (game_id, food_name) VALUES (%s, %s)"
    val = []
    for alimento in info_alimento_partida:
        temp = (primary_key, alimento)
        val.append(temp)
    print(val)
    cursor.executemany(sql, val)

    sql = "INSERT INTO weapons (game_id,weapon_name) VALUES (%s, %s)"
    val = []
    for arma in info_equipamiento_partida:
        temp = (primary_key, arma)
        val.append(temp)
    print(val)
    cursor.executemany(sql, val)

    sql = "INSERT INTO enemies (enemy_id, game_id, region, xpos, ypos, lifes_remaining) VALUES (%s, %s, %s, %s, %s, %s)"
    val = []
    lista_lugares = ["hyrule", "death mountain", "gerudo", "necluda"]
    for region_cargada in lista_lugares:
        print(region_cargada)
        for enemigo in datos_partida_actual[region_cargada]["enemigos"]:
            print(enemigo)
            temp = (enemigo, primary_key, region_cargada, datos_partida_actual[region_cargada]["enemigos"][enemigo]["x"], datos_partida_actual[region_cargada]["enemigos"][enemigo]["y"], datos_partida_actual[region_cargada]["enemigos"][enemigo]["vida"],)
            val.append(temp)
    print(val)

    val.append((0, primary_key, "castle", datos_partida_actual['castle'][0]['x'], datos_partida_actual['castle'][0]['y'], datos_partida_actual['castle'][0]['vida']))
    print(val)
    cursor.executemany(sql, val)
    db.commit()


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
    cursor.execute(f"SELECT weapon_name, equiped, uses, quantity FROM weapons WHERE game_id = {primary_key}")
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


def save_game(primary_key):
    print(
        f"UPDATE game SET user_name = '{datos_jugador_actual['nombre']}', hearts_remaining = {datos_jugador_actual['vida_actual']}, hearts_total = {datos_jugador_actual['vida_total']}, "
        f"blood_moon_countdown = {datos_jugador_actual['blood_moon_countdown']}, "
        f"blood_moon_appearences = {datos_jugador_actual['blood_moon_appearances']}, "
        f"region = '{datos_jugador_actual['region']}' "
        f"WHERE game_id = {primary_key};")
    cursor.execute(f"UPDATE game SET user_name = '{datos_jugador_actual['nombre']}', hearts_remaining = {datos_jugador_actual['vida_actual']}, hearts_total = {datos_jugador_actual['vida_total']}, "
                   f"blood_moon_countdown = {datos_jugador_actual['blood_moon_countdown']},"
                   f"blood_moon_appearences = {datos_jugador_actual['blood_moon_appearances']}, "
                   f"region = '{datos_jugador_actual['region']}'"
                   f"WHERE game_id = {primary_key};")
    for alimento in info_alimento_partida:
        cursor.execute(f"UPDATE food SET quantity_remaining = {info_alimento_partida[alimento]['cantidad']} "
              f"WHERE game_id = {primary_key} AND food_name = '{alimento}';")
    for arma in info_equipamiento_partida:
        cursor.execute(f"UPDATE weapons SET equiped = {info_equipamiento_partida[arma]['equipado']}, "
              f"uses = {info_equipamiento_partida[arma]['usos']}, "
              f"quantity = {info_equipamiento_partida[arma]['cantidad']} "
              f"WHERE game_id = {primary_key} AND weapon_name = '{arma}';")
    for region in datos_partida_actual:
        if region == "castle":
            cursor.execute(f"UPDATE enemies SET lifes_remaining = {datos_partida_actual[region][0]['vida']} WHERE game_id = {primary_key} AND region = '{region}' AND enemy_id = {0};")
        else:
            for enemigo in datos_partida_actual[region]["enemigos"]:
                cursor.execute(f"UPDATE enemies SET xpos = {datos_partida_actual[region]['enemigos'][enemigo]['x']}, ypos = {datos_partida_actual[region]['enemigos'][enemigo]['y']}, "
                               f"lifes_remaining = {datos_partida_actual[region]['enemigos'][enemigo]['vida']} WHERE game_id = {primary_key} AND region = '{region}' AND enemy_id = {enemigo};")
    db.commit()


# MAPAS

def generar_mapa(): # genera el mapa
    # GENERAR COPIA MAPA -----> a partir de esta se hace el mapa sobre el que interactuar
    mapa_a_cargar = []
    for fila in datos_importados.localizaciones[datos_jugador_actual["region"]]: # para cambiar de localizacion, cambia la region en info personaje
        fila_mapa_a_cargar = []
        for elemento in fila:
            fila_mapa_a_cargar.append(elemento)
        mapa_a_cargar.append(fila_mapa_a_cargar)
    # CARGAR ENEMIGO EN EL MAPA
    for enemigo in datos_partida_actual[datos_jugador_actual["region"]]["enemigos"]:
        if datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["vida"] > 0:  # Si vida > 0, hago print de E + vida
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["y"]] = "E"
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["y"] + 1] = \
            datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["vida"]  # Esto es la vida
    # CARGAR SANTUARIO EN EL MAPA
    for santuario in datos_partida_actual[datos_jugador_actual["region"]]["santuarios"]: # El santuario se carga siempre
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["y"]] = "S"
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["y"] + 1] = \
        datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["nombre"][1]
        if not datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["descubierto"]: # Pero si no esta descubierto
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["y"] + 2] = "?" # Se hace print de ?
    # CARGAR COFRE EN EL MAPA
    for cofre in datos_partida_actual[datos_jugador_actual["region"]]["cofres"]:
        if datos_partida_actual[datos_jugador_actual["region"]]["cofres"][cofre]["abierto"]:  # Si esta abierto, W
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["cofres"][cofre]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["cofres"][cofre]["y"]] = "W"
        else:  # Si esta cerrado, M
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["cofres"][cofre]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["cofres"][cofre]["y"]] = "M"
    # CARGAR ARBOL (conflicto si hay arboles juntos) EN EL MAPA
    for arbol in datos_partida_actual[datos_jugador_actual["region"]]["arboles"]:
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["arboles"][arbol]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["arboles"][arbol]["y"]] = "T"
        if datos_partida_actual[datos_jugador_actual["region"]]["arboles"][arbol]["vida"] <= 0:
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["arboles"][arbol]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["arboles"][arbol]["y"] + 1] = \
            datos_partida_actual[datos_jugador_actual["region"]]["arboles"][arbol]["turnos_restantes"]
    # CARGAR FOX
    if datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] and not datos_partida_actual[datos_jugador_actual["region"]]["fox"][0][
        "muerto"]:
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["y"]] = "F"
    #CARGAR JUGADOR
    mapa_a_cargar[xpos][ypos] = "X"
    return mapa_a_cargar


def show_map():
    mapa_show_map = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
        [" ", " ", "H", "y", "r", "u", "l", "e", " ", " ", " ", " ", " ", " ", " ", "S", 0, "?", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "D", "e", "a", "t", "h", " ", "m", "o", "u", "n", "t", "a", "i", "n", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", 2, "?", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", "S", 1, "?", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", 3, "?", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", "a", "s", "t", "l", "e", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", 4, "?", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", 5, "?", " "],
        [" ", " ", "G", "e", "r", "u", "d", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "S", 6, "?", " ", " ", " ", " ", " ", " ", "N", "e", "c", "l", "u", "d", "a", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

    lugares = ["hyrule", "death mountain", "necluda", "gerudo"]

    for i, fila in enumerate(mapa_show_map):
        for j, elemento in enumerate(fila):

            if isinstance(elemento, int):
                for lugar in lugares:
                    if elemento in datos_partida_actual[lugar]["santuarios"]:
                        if datos_partida_actual[lugar]["santuarios"][elemento]["descubierto"] == True:
                            mapa_show_map[i][j+1] = " "

    titulo = "Map" + " "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    if len(titulo) % 2 != 0:
        print("* " + titulo.title() + " " + "* " * calculo, end="")
    else:
        print("* " + titulo.title() + "* " * calculo, end="")
    print("* " * 10)
    for fila in mapa_show_map:
        print("*", end="")
        for elemento in fila:
            print(elemento, end="")
        print("* " + " " * 18 + "*")
    print("* " + "Back  " + "* " * 36)


def print_tablero(mapa):
    titulo = datos_jugador_actual["region"] + " "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    lista = ["Inventory", "Weapons", "Food"]
    titulo_2 = lista[0]
    calculo_secundario = int(((20 - len(titulo_2)) / 2) - 1)
    if len(titulo) % 2 != 0:
        print("* " + titulo.title() + " " + "* " * calculo, end="")
    else:
        print("* " + titulo.title() + "* " * calculo, end="")
    if len(titulo_2) % 2 != 0:
        print("* " * calculo_secundario + titulo_2.title() + " *")
    else:
        print("* " * (calculo_secundario - 1) + " " + titulo_2.title() + " *")
    for i in range(len(mapa)):
        print("*", end="")
        for elemento in mapa[i]:
            print(elemento, end="")
        print("* ")
    #print("* " * 40)

    # PRINT DINÁMICO
    global cocinar, pescar, santuario, cofre, equip, unequip, eat, atacar_general

    lista_acciones = ["attack", "equip", "unequip", "eat", "cook", "fish", "open",]
    lista_acciones_disponibles = ["exit", "go"]

    if atacar_general:
        lista_acciones_disponibles.append(lista_acciones[0])
    if equip:
        lista_acciones_disponibles.append(lista_acciones[1])
    if unequip:
        lista_acciones_disponibles.append(lista_acciones[2])
    if eat:
        lista_acciones_disponibles.append(lista_acciones[3])
    if cocinar:
        lista_acciones_disponibles.append(lista_acciones[4])
    if pescar:
        lista_acciones_disponibles.append(lista_acciones[5])
    if cofre or santuario:
        lista_acciones_disponibles.append(lista_acciones[6])

    # print(lista_acciones_disponibles)
    # print(", ".join(lista_acciones_disponibles))
    combinado = ", ".join(lista_acciones_disponibles)
    # combinado = "123456789"
    # print(len(combinado))
    calculo = int(((80 - len(combinado)) / 2) - 1)
    # print("* " * 40)
    if len(combinado) % 2 != 0:
        print("* " + combinado + " " + "* " * calculo)
    else:
        print("* " + combinado + "* " * calculo)


# --- funciones querys ---


# --- funciones inputs ---

# PROMPT
lista_prompt = []
def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)


def input_main_menu():
    global flag_main_menu
    opc = input("What to do now? ")
    if opc.lower() == "new game":
        global flag_new_game
        flag_new_game = True
        flag_main_menu = False
    elif opc.lower() == "help":
        global flag_help_main_menu
        flag_help_main_menu = True
        flag_main_menu = False
    elif opc.lower() == "about":
        global flag_about
        flag_about = True
        flag_main_menu = False
    elif opc.lower() == "queries":
        global flag_queries
        flag_queries = True
        flag_main_menu = False
    elif opc.lower() == "exit":
        global flag_general_juego
        flag_general_juego = True
        flag_main_menu = False
    # SI SOLAMENTE HAY UNA PARTIDA, CARGA DIRECTAMENTE //  SI HAY MÁS DE UNA, sale lista a elegir (input_save_game + flag_save_game)
    elif len(partidas_guardadas) > 0 and opc.lower() == "continue":
        if len(partidas_guardadas) == 1:
            global flag_in_game
            global key_primaria_partida
            key_primaria_partida = lista_partidas[0]
            cargar_partida(key_primaria_partida)
            flag_main_menu = False
            flag_in_game = True
            global ver_todos
            ver_todos = False
        else:
            global flag_saved_games
            flag_main_menu = False
            flag_saved_games = True
    else:
        lista_prompt.append("Invalid action")


def input_saved_games():
    global flag_saved_games
    global flag_in_game
    global lista_partidas
    global ver_todos
    global key_primaria_partida
    global partidas_guardadas
    opc = input("What to do now? ")
    if opc.lower() == "help":
        flag_saved_games = False
        global flag_help_saved_games
        flag_help_saved_games = True
    elif opc.lower() == "back":
        ver_todos = False
        flag_saved_games = False
        global flag_main_menu
        flag_main_menu = True
    elif ver_todos is False and opc.lower() == "show all":
        ver_todos = True
        partidas_guardadas = seleccionar_partidas_guardadas()
        lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
    elif ver_todos is True and opc.lower() == "show recent":
        ver_todos = False
        partidas_guardadas = seleccionar_partidas_guardadas()
        lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
    elif opc[0:4].lower() == "play":
        try:
            if int(opc[5]) == 0 and len(opc[5:]) > 1:
                raise ValueError                            # Me aseguro que no hayan espacios en blanco y sea un num
            indice_partida = int(opc[5:].replace(" ", "/")) # lista_partidas[indice_partida] == primary key == key del diccionario
            assert 0 <= indice_partida < len(lista_partidas)
            print(lista_partidas, lista_partidas[indice_partida])
            key_primaria_partida = lista_partidas[indice_partida]
            cargar_partida(key_primaria_partida)
            ver_todos = False
            flag_saved_games = False
            flag_in_game = True
        except (ValueError, AssertionError):
            lista_prompt.append("Invalid Action")
    elif opc[0:5].lower() == "erase":
        try:
            if int(opc[6]) == 0 and len(opc[6:]) > 1:
                raise ValueError
            indice_partida = int(opc[6:].replace(" ", "/"))
            assert 0 <= indice_partida < len(lista_partidas)
            del partidas_guardadas[lista_partidas[indice_partida]]
            print("eliminado del diccionario")
            query_delete = f"DELETE FROM game WHERE game_id = {lista_partidas[indice_partida]};"
            cursor.execute(query_delete)
            print("query realizada")
            db.commit()
            print("commit hecho")
            partidas_guardadas = seleccionar_partidas_guardadas()
            lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
            print("nuevas partidas guardadas")
        except (ValueError, AssertionError):
            lista_prompt.append("Invalid Action")
    else:
        lista_prompt.append("Invalid Action")


# --- funciones comprobacioens ---

def jugador_muerto(primary_key):
    global flag_link_death
    global flag_in_game
    global flag_ganon_castle
    if datos_jugador_actual["vida_actual"] < 1:
        lista_prompt.append("Nice try, you died, game is over")
        datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]

        #commit a la BBDD
        cursor.execute(f"UPDATE game SET hearts_remaining = {datos_jugador_actual['vida_actual']}, hearts_total = {datos_jugador_actual['vida_total']} WHERE game_id = {primary_key};")
        db.commit()

        flag_link_death = True
        flag_in_game = False
        flag_ganon_castle = False

def mostrar_fox(): # FALTA EL INPUT DE MATAR + REINICIO AL MOVERSE DE REGION
    if not datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["intento"]:  # PERMITE QUE SOLO HAYA HABIDO UN INTENTO. SE DEBE REINICIAR AL SALIR DEL MAPA
        datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["intento"] = True
        visible = random.choice([True, False])  # 50% CHANCE
        if visible:
            lista_prompt.append("You see a Fox")
            datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] = True
        else:
            lista_prompt.append("You don't see a Fox")


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
                if datos_partida_actual[lugar]["cofres"][cofre]["abierto"]:
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


def actualizar_turnos_restantes_arboles(region_actual):
    for arbol_id, arbol_info in datos_partida_actual[region_actual]["arboles"].items():
        # para los árboles con algún turno para reaparecer
        if arbol_info["turnos_restantes"] > 0:
            datos_partida_actual[region_actual]["arboles"][arbol_id]["turnos_restantes"] -= 1
            # poner vida de cuatro para el respawn
            if arbol_info["turnos_restantes"] == 0:
                datos_partida_actual[region_actual]["arboles"][arbol_id]["vida"] = 4


# --- funciones inventario ----




# --- funciones movimiento ---

def verificar_alrededor(matriz, fila, columna):
    # guardar elementos
    alrededor = []

    # 3x3 alrededor del jugador
    for i in range(fila - 2, fila + 2):  # -1,0,1: range(-1,2)
        for j in range(columna - 2, columna + 2):  # -1,0,1 rrange(-1,2)
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]) and (i != fila or j != columna):
                alrededor.append(matriz[i][j])

    return alrededor


def permitir_acciones_jugador(mapa_cargado, xpos, ypos):
    global hierba, cocinar, talar, pescar, santuario, cofre, atacar_enemigo, equip, unequip, eat

    list_elementos = verificar_alrededor(mapa_cargado, xpos, ypos)

    hierba = True if " " in list_elementos else False
    cocinar = True if "C" in list_elementos else False
    talar = True if "T" in list_elementos else False
    pescar = True if "~" in list_elementos else False
    santuario = True if "S" in list_elementos else False
    cofre = True if "M" in list_elementos else False
    atacar_enemigo = True if "E" in list_elementos else False
    atacar_general = True if " " in list_elementos or "T" in list_elementos or "E" in list_elementos else False

    equip = True if any(info_equipamiento_partida[weapon]["cantidad"] > 0 for weapon in
                        ["wood sword", "sword", "wood shield", "shield"]) else False

    unequip = False if not datos_jugador_actual["items_equipados"] else True

    eat = True if any(info_alimento_partida[food]["cantidad"] > 0 for food in
                      ["vegetables", "fish", "meat", "salads", "pescatarian", "roasted"]) else False

    return hierba, cocinar, talar, pescar, santuario, cofre, atacar_enemigo, equip, unequip, eat, atacar_general


def encontrar_celda_vacia_adyacente(x, y, mapa):
    adyacentes = [
        (x, y - 1),  # arriba
        (x, y + 1),  # abajo
        (x - 1, y),  # izquierda
        (x + 1, y),  # derecha
    ]

    celdas_vacias = [(i, j) for i, j in adyacentes if
                     0 <= i < len(mapa) and 0 <= j < len(mapa[0]) and mapa[i][j] == " "]

    if celdas_vacias:
        return random.choice(celdas_vacias)
    else:
        return x, y


def obter_id_objeto_adyacente(diccionario):
    for id_objeto, info_objeto in diccionario.items():
        id_objeto_adyacente = None

        # 1)verificar arriba izquierda +1
        if info_objeto["x"] == xpos - 1 and info_objeto["y"] == ypos - 2:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 2)verificar arriba izquierda
        elif info_objeto["x"] == xpos - 1 and info_objeto["y"] == ypos - 1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 3)verificar arriba
        elif info_objeto["x"] == xpos - 1 and info_objeto["y"] == ypos:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 4)verificar arriba derecha
        elif info_objeto["x"] == xpos - 1 and info_objeto["y"] == ypos + 1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 5)verificar izquierda +1
        elif info_objeto["x"] == xpos and info_objeto["y"] == ypos - 2:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 7)derecha
        elif info_objeto["x"] == xpos and info_objeto["y"] == ypos + 1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 8)abajo izquierda +1
        elif info_objeto["x"] == xpos + 1 and info_objeto["y"] == ypos - 2:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 9)abajo izquierda
        elif info_objeto["x"] == xpos + 1 and info_objeto["y"] == ypos - 1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 10)abajo
        elif info_objeto["x"] == xpos + 1 and info_objeto["y"] == ypos:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        # 11)abajo derecha
        elif info_objeto["x"] == xpos + 1 and info_objeto["y"] == ypos + 1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente


def bajar_uso_cantidad_espada():
    if "wood sword" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["wood sword"]["usos"] -= 1
        # print("wood sw usos", info_equipamiento_partida["wood sword"]["usos"])

        if info_equipamiento_partida["wood sword"]["usos"] % 5 == 0:
            info_equipamiento_partida["wood sword"]["cantidad"] -= 1
            # print("wood sword cantidad", info_equipamiento_partida["wood sword"]["cantidad"])

    elif "sword" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["sword"]["usos"] -= 1
        # print("sword usos", info_equipamiento_partida["sword"]["usos"])

        if info_equipamiento_partida["sword"]["usos"] % 9 == 0:
            info_equipamiento_partida["sword"]["cantidad"] -= 1
            # print("sword cantidad", info_equipamiento_partida["sword"]["cantidad"])


def bajar_uso_cantidad_escudos():
    if "wood shield" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["wood shield"]["usos"] -= 1
        # print("wood sh usos", info_equipamiento_partida["wood shield"]["usos"])

        if info_equipamiento_partida["wood shield"]["usos"] % 5 == 0:
            info_equipamiento_partida["wood shield"]["cantidad"] -= 1
            # print("wood shield cantidad", info_equipamiento_partida["wood shield"]["cantidad"])

    elif "shield" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["shield"]["usos"] -= 1
        # print("shield usos", info_equipamiento_partida["shield"]["usos"])

        if info_equipamiento_partida["shield"]["usos"] % 9 == 0:
            info_equipamiento_partida["shield"]["cantidad"] -= 1
            # print("shield cantidad", info_equipamiento_partida["shield"]["cantidad"])

    else:
        datos_jugador_actual["vida_actual"] -= 1
        lista_prompt.append(
            f"Be careful {datos_jugador_actual['nombre']}, you only have {datos_jugador_actual['vida_actual']} hearts")


# --- funciones acciones ---

def attack_enemy():
    # bajar stats armas
    bajar_uso_cantidad_espada()

    lista_prompt.append(f"Brave, keep fighting {datos_jugador_actual['nombre']}")

    # bajar stats escudo
    bajar_uso_cantidad_escudos()

    # bajar vida al enemigo de al lado
    id_enemigo_adyacente = obter_id_objeto_adyacente(datos_partida_actual[datos_jugador_actual["region"]]["enemigos"])

    datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["vida"] -= 1

    # si el enemigo llega a cero
    if datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["vida"] == 0:
        lista_prompt.append("You defeat an enemy, this is a dangerous zone")

    else:
        # mover enemigo a una celda aleatoria de al lado
        nueva_x, nueva_y = encontrar_celda_vacia_adyacente(
            datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["x"],
            datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["y"], mapa_cargado)

        datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["x"] = nueva_x
        datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["y"] = nueva_y

    # print(datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["x"],",",datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["y"])


def attack_fox():
    info_alimento_partida["meat"]["cantidad"] += 1
    bajar_uso_cantidad_espada()

    save_game(key_primaria_partida)
    lista_prompt.append("You got meat")

    # matar a la guineu
    datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"] = True


def attack_tree():
    # id del arbol adyacente
    id_arbol_adyacente = obter_id_objeto_adyacente(datos_partida_actual[datos_jugador_actual["region"]]["arboles"])

    #print(f"Enemigo {id_arbol_adyacente} es el de al lado")

    # el arbol está spawneando
    if datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["turnos_restantes"] > 0:
        lista_prompt.append("The tree is not ready yet")


    # se ataca SIN arma
    elif not "wood sword" in datos_jugador_actual["items_equipados"] and not "sword" in datos_jugador_actual[
        "items_equipados"]:


        # se gana una manzana
        if random.random() < 0.4:
            #print(info_alimento_partida["vegetables"])
            info_alimento_partida["vegetables"]["cantidad"] += 1
            #print(info_alimento_partida["vegetables"])

            save_game(key_primaria_partida)

            lista_prompt.append("You got an apple")

        # se gana un arma
        elif random.random() < 0.1:
            dado = random.randrange(0, 1)

            if dado == 1:
                #print(info_equipamiento_partida["wood sword"])
                info_equipamiento_partida["wood sword"]["cantidad"] += 1
                info_equipamiento_partida["wood sword"]["usos"] += 5
                #print(info_equipamiento_partida["wood sword"])

                save_game(key_primaria_partida)

                lista_prompt.append("You got a Wood sword")

            else:
                #print(info_equipamiento_partida["wood shield"])
                info_equipamiento_partida["wood shield"]["cantidad"] += 1
                info_equipamiento_partida["wood shield"]["usos"] += 5
                #print(info_equipamiento_partida["wood shield"])

                save_game(key_primaria_partida)

                lista_prompt.append("You got a wood shield")

        else:
            lista_prompt.append("The tree didn't give you anything")

    # se atca CON arma
    else:
        #print("con arma")
        if random.random() < 0.4:
            #print(info_alimento_partida["vegetables"]["cantidad"])
            info_alimento_partida["vegetables"]["cantidad"] += 1
            #print("cantidad vegetables", info_alimento_partida["vegetables"]["cantidad"])

            save_game(key_primaria_partida)

            lista_prompt.append("You got an apple")

        elif random.random() < 0.2:
            #print(info_equipamiento_partida["wood sword"]["cantidad"])
            info_equipamiento_partida["wood sword"]["cantidad"] += 1
            #print("cantidad wood s", info_equipamiento_partida["wood sword"]["cantidad"])

            save_game(key_primaria_partida)

            lista_prompt.append("You got a Wood sword")


        elif random.random() < 0.2:
            #print(info_equipamiento_partida["wood shield"]["cantidad"])
            info_equipamiento_partida["wood shield"]["cantidad"] += 1
            #print("cantidad wood shield", info_equipamiento_partida["wood shield"]["cantidad"])

            save_game(key_primaria_partida)

            lista_prompt.append("You got a wood shield")

        else:
            lista_prompt.append("The tree didn't give you anything")

        # quitar vida a la espada
        bajar_uso_cantidad_espada()

        # quitar vida al arbol adyacente
        datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["vida"] -= 1
        #print(datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["vida"])

        # añadir +9 turnos restantes si su vida es cero
        if datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["vida"] == 0:
            datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["turnos_restantes"] += 9


def attack_grass():
    if random.random() < 0.1:
        info_alimento_partida["meat"]["cantidad"] += 1

        save_game(key_primaria_partida)

        lista_prompt.append("You got a lizard")
    else:
        lista_prompt.append("It seems like there is nothing in the grass")


def fish():
    global pescar_mapa
    if random.random() < 0.2:
        info_alimento_partida["pescatarian"]["cantidad"] += 1
        pescar_mapa = False

        save_game(key_primaria_partida)

        lista_prompt.append("You got a fish")

    else:
        lista_prompt.append("You didn't get a fish")


def open_sacntuary():
    id_santuario_adyacente = obter_id_objeto_adyacente(
        datos_partida_actual[datos_jugador_actual["region"]]["santuarios"])

    # print(f"Santuario {id_santuario_adyacente} es el de al lado")

    # comprobar si ya está abierto
    if datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente][
        "descubierto"] == True:
        lista_prompt.append("You already opened this sanctuary")

    else:
        # actualizar santuario a true
        datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["descubierto"] = True

        # aumentar vida máxima
        datos_jugador_actual["vida_total"] += 1

        # restaurar vida al máximo
        datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]

        # commit a la BBDD

        sql = "INSERT INTO santuaries_opened (sactuary_id,game_id,region,xpos,ypos) VALUES (%s, %s, %s, %s, %s)"
        val = (id_santuario_adyacente,key_primaria_partida,datos_jugador_actual["region"],
              datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["x"],
              datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["y"]
              )
        cursor.execute(sql,val)

        save_game(key_primaria_partida)


        lista_prompt.append(f"Sanctuaire {id_santuario_adyacente} done")


def open_chest():
    # localizar cofre y ponerlo a true
    id_cofre_adyacente = obter_id_objeto_adyacente(
        datos_partida_actual[datos_jugador_actual["region"]]["cofres"])

    datos_partida_actual[datos_jugador_actual["region"]]["cofres"][id_cofre_adyacente]["abierto"] = True

    # hyrule y gerudo
    if datos_jugador_actual["region"] == "hyrule" or datos_jugador_actual["region"] == "gerudo":
        #print(info_equipamiento_partida["sword"])

        info_equipamiento_partida["sword"]["cantidad"] += 1
        info_equipamiento_partida["sword"]["usos"] += 9

        #print(info_equipamiento_partida["sword"])

        lista_prompt.append("You got a sword")

    # death mountain y necluda
    else:
        #print(info_equipamiento_partida["shield"])

        info_equipamiento_partida["shield"]["cantidad"] += 1
        info_equipamiento_partida["shield"]["usos"] += 9

        #print(info_equipamiento_partida["shield"])

        lista_prompt.append("You got a shield")

    # commit a la BBDD

    sql = "INSERT INTO chest_opened (chest_id,game_id,region,xpos,ypos) VALUES (%s, %s, %s, %s, %s)"
    val = (id_cofre_adyacente,key_primaria_partida,datos_jugador_actual["region"],
           datos_partida_actual[datos_jugador_actual["region"]]["cofres"][id_cofre_adyacente]["x"],
           datos_partida_actual[datos_jugador_actual["region"]]["cofres"][id_cofre_adyacente]["y"]
          )

    cursor.execute(sql,val)

    save_game(key_primaria_partida)


# -- funciones movimiento --


def mover_a_objeto(objeto, numero, mapa, xpos, ypos):
    # verificar si la posción en la que va a colocarse está vació o no
    def verificar_posicion_final(i, j):
        if 0 <= i < len(mapa) and 0 <= j < len(mapa[0]) and mapa[i][j] == " ":
            return True
        return False

    def encontrar_celda_vacia_adyacente(i, j):
        adyacentes = [
            (i, j - 1),  # abajo
            (i, j + 1),  # arriba
            (i - 1, j),  # izquierda
            (i + 1, j),  # derecha
        ]

        for x, y in adyacentes:
            if verificar_posicion_final(x, y):
                return x, y
        return i, j  # Si no hay celda vacía adyacente, devuelve la anterior posición

    # LO QUE BUSCA NO ES UN SANTUARIO
    if numero is None:
        # print("busca")
        for i, fila in enumerate(mapa):
            for j, elemento in enumerate(fila):
                # fox
                if objeto == "f" and elemento == "F":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                # tree
                elif objeto == "t" and elemento == "T":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                # water
                elif objeto == "water" and elemento == "~":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                # chest
                elif objeto == "m" and elemento == "M":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                # fire
                elif objeto == "c" and elemento == "C":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos


    # LO QUE BUSCA ES UN SANTUARIO
    elif numero.isdigit():
        # print("busca un santuario")
        for i, fila in enumerate(mapa):
            for j, elemento in enumerate(fila):

                # sanctuary
                if objeto == "s" and j + 1 < len(fila) and fila[j] == "S" and fila[j + 1] == str(numero):
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()}{numero} en la posición {xpos},{ypos}")
                    return xpos, ypos

                # enemy
                elif objeto == "e" and j + 1 < len(fila) and fila[j] == "E" and fila[j + 1] == int(numero):
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    # print(f"objeto {objeto.upper()}{numero} en la posición {xpos},{ypos}")
                    return xpos, ypos

    # NO HA ENCONTRADO NADA
    # print(f"No se encontró el objeto {objeto.upper()}{numero}")
    lista_prompt.append("Invalid option")
    return xpos, ypos


def move_region(region, region_to_go, xpos, ypos):
    global pescar_mapa

    pos_spawn = {  # revisar los puntos de spawn
        "hyrule": (datos_partida_actual["hyrule"]["spawn"]["x"], datos_partida_actual["hyrule"]["spawn"]["y"]),
        "death mountain": (
        datos_partida_actual["death mountain"]["spawn"]["x"], datos_partida_actual["death mountain"]["spawn"]["y"]),
        "gerudo": (datos_partida_actual["gerudo"]["spawn"]["x"], datos_partida_actual["gerudo"]["spawn"]["y"]),
        "necluda": (datos_partida_actual["necluda"]["spawn"]["x"], datos_partida_actual["necluda"]["spawn"]["y"]),
        "castle": (datos_partida_actual["castle"]["spawn"]["x"], datos_partida_actual["castle"]["spawn"]["y"])
    }

    #  restricciones entre tp
    restricciones_tp = {
        "hyrule": ["gerudo", "death mountain", "castle"],
        "death mountain": ["hyrule", "necluda", "castle"],
        "gerudo": ["hyrule", "necluda", "castle"],
        "necluda": ["death mountain", "gerudo", "castle"]
    }

    # cambias al mapa de castle: al dar al back se irá a la pos anterior
    if region_to_go == "castle" and region_to_go in restricciones_tp[region]:
        nuevas_pos = pos_spawn[region_to_go]
        lista_prompt.append(f"You are now in {region_to_go}")
        return nuevas_pos[0], nuevas_pos[1], region


    # puedes cambiar de región
    elif region_to_go in restricciones_tp[region]:
        nuevas_pos = pos_spawn[region_to_go]
        pescar_mapa = True
        datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"] = False
        datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] = False
        datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["intento"] = False
        lista_prompt.append(f"You are now in {region_to_go}")

        return nuevas_pos[0], nuevas_pos[1], region_to_go

    elif region_to_go not in pos_spawn:
        lista_prompt.append("Invalid Option")
        return xpos, ypos, region

    # no puedes
    else:
        lista_prompt.append(f"You can't go to {region_to_go} from here")
        return xpos, ypos, region


def mover_a_direccion(matriz, fila_personaje, columna_personaje, direccion, steps):
    # Guardar las posiciones originales, por siac
    fila_anterior = fila_personaje
    columna_anterior = columna_personaje

    for i in range(steps):
        # Verificar dirección y sumar o restar pasos
        if direccion == "left":
            columna_personaje -= 1
        elif direccion == "right":
            columna_personaje += 1
        elif direccion == "up":
            fila_personaje -= 1
        elif direccion == "down":
            fila_personaje += 1
        else:
            lista_prompt.append("Invalid option")
            return fila_anterior, columna_anterior

        # Verificar límites del mapa - si la nueva pos está dentro del mapa
        if 0 <= fila_personaje < len(matriz) and 0 <= columna_personaje < len(matriz[0]):

            # Si hay algún obstáculo
            if matriz[fila_personaje][columna_personaje] != " ":
                print("objeto de por medio")
                lista_prompt.append("You can't go there, is not a valid position")
                # print(f"obstáculo en el camino {fila_personaje},{columna_personaje}")
                return fila_anterior, columna_anterior

        # te sales del mapa - la nueva pos está fuera del mapa
        else:
            print("te sales del mapa")
            lista_prompt.append("You can't go there, is not a valid position")
            return fila_anterior, columna_anterior

    # actualizar los puntos restantes de espera de los arboles
    actualizar_turnos_restantes_arboles(datos_jugador_actual["region"])

    # el movimiento es correcto y se puede
    return fila_personaje, columna_personaje


def go_by_the_x(to_do, xpos, ypos):
    # print("tp")

    to_do = to_do[10:].lower()  # objeto
    # print(to_do)
    numero = None

    # el input es incorrecto: el objeto no es correcto
    if not to_do == "f" and not to_do == "t" and not to_do == "water" and not to_do[0:1] == "s" and not to_do[0:1] == "e" \
            and not to_do == "m" and not to_do == "c":
        lista_prompt.append("Invalid Option")

    else:
        if to_do[0:1] == "s" or to_do[0:1] == "e":
            objeto = to_do[0:1]
            numero = to_do[1:]
        else:
            objeto = to_do

        # moverse
        xpos, ypos = mover_a_objeto(objeto, numero, mapa_cargado, xpos, ypos)
        return xpos, ypos


def go_direction(to_do, xpos, ypos):
    to_do = to_do[3:].lower()

    # la dirección que quiere tomar: left/...
    direction = to_do[:-2]

    # el número de pasos que quiere dar: 2
    steps = to_do[-1]

    print(direction,"-",steps)
    print(type(direction))
    print(type(steps))

    if not direction.isalpha() or not steps.isdigit():
        lista_prompt.append("Invalid Option")
        return xpos, ypos

    # la orden es correcta
    else:
        steps = int(steps)

        # print(f"steps: {steps}, dirección: {direction}")

        # Mover el jugador
        xpos, ypos = mover_a_direccion(mapa_cargado, xpos, ypos, direction, steps)

        return xpos, ypos


# --- funciones cheats ---


# --- funciones ganon ---

def generar_mapa_ganon(): # genera el mapa
    # GENERAR COPIA MAPA -----> a partir de esta se hace el mapa sobre el que interactuar
    mapa_a_cargar_ganon = []
    for fila in datos_importados.localizaciones["castle"]: # para cambiar de localizacion, cambia la region en info personaje
        fila_mapa_a_cargar = []
        for elemento in fila:
            fila_mapa_a_cargar.append(elemento)
        mapa_a_cargar_ganon.append(fila_mapa_a_cargar)

    # MAPA GANON
    mapa_a_cargar_ganon[xpos][ypos] = "X"
    return mapa_a_cargar_ganon


def print_tablero_ganon(mapa, vida):  # hace print del tablero # a la espera de la parte de unax
    vivo = [" ", " ", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "G", "a", "n", "o", "n", " ", f"{'♥' * vida}".ljust(8), " ", " ", " "]
    derrotado = [" ", " ", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "G", "a", "n", "o", "n", " ", "d", "e", "f", "e", "a", "t", "e", "d", " ", " ", " "]
    titulo = "Castle "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    lista = ["Inventory", "Weapons", "Food"]
    titulo_2 = lista[1]
    calculo_2 = int((17 - len(titulo_2)) // 2)
    if datos_partida_actual["castle"][0]["vida"] == 0:
        mapa[1] = derrotado
    else:
        mapa[1] = vivo
    if len(titulo) % 2 != 0:
        print("* " + titulo.title() + " " + "* " * calculo, end="")
    else:
        print("* " + titulo.title() + "* " * calculo, end="")
    if len(titulo_2) % 2 != 0:
        print("* " * calculo_2 + titulo_2 + " * ")
    else:
        print("* " * calculo_2 + " " + titulo_2 + " * ")
    for i in range(len(mapa)):
        print("*", end="")
        for elemento in mapa[i]:
            print(elemento, end="")
        print("* ")
    #print("* " * 40)

    lista_acciones = ["attack"]
    lista_acciones_disponibles = ["exit", "go"]

    if xpos == 8 and ypos == 20:
        lista_acciones_disponibles.append(lista_acciones[0])


    # print(lista_acciones_disponibles)
    # print(", ".join(lista_acciones_disponibles))
    combinado = ", ".join(lista_acciones_disponibles)
    # combinado = "123456789"
    # print(len(combinado))
    calculo = int(((80 - len(combinado)) / 2) - 1)
    # print("* " * 40)
    if len(combinado) % 2 != 0:
        print("* " + combinado + " " + "* " * calculo)
    else:
        print("* " + combinado + "* " * calculo)


def go_direction_ganon(to_do,xpos,ypos):
    to_do = to_do[3:].lower()

    # la dirección que quiere tomar: left/...
    direction = to_do[:-2]

    # el número de pasos que quiere dar: 2
    steps = to_do[-1]

    print(direction, "-", steps)
    print(type(direction))
    print(type(steps))

    if not direction.isalpha() or not steps.isdigit():
        lista_prompt.append("Invalid Option")
        return xpos, ypos

    # la orden es correcta
    else:
        steps = int(steps)

        # print(f"steps: {steps}, dirección: {direction}")

        # Mover el jugador
        xpos, ypos = mover_a_direccion(datos_importados.localizaciones["castle"], xpos, ypos, direction, steps)

        return xpos, ypos


def attack_ganon():
    global flag_ganon_castle,flag_zelda_saved
    frases_atacar_ganon = ["Ganon is powerful, are you sure you can defeat him?",
                "Ganon's strength is supernatural, Zelda fought with bravery.",
                "To Ganon, you are like a fly, find a weak spot and attack.",
                "Ganon will not surrender easily.",
                "Ganon has fought great battles, is an expert fighter.",
                f"{datos_jugador_actual['nombre']}, transform your fears into strengths.",
                "Keep it up, {datos_jugador_actual['nombre']}, Ganon can't hold out much longer.",
                f"{datos_jugador_actual['nombre']}, history repeats itself, Ganon can be defeated.",
                "Think of all the warriors who have tried before.",
                f"You fight for the weaker ones, {datos_jugador_actual['nombre']}, persevere."]

    # bajar vida jugador
    datos_jugador_actual["vida_actual"] -= 1

    # bajar vida ganon
    datos_partida_actual["castle"][0]["vida"] -= 1

    lista_prompt.append(random.choice(frases_atacar_ganon))

    # GANON MUERE
    if datos_partida_actual["castle"][0]["vida"] < 1:
        muerte_ganon()

    # LINK MUERE
    elif datos_jugador_actual["vida_actual"] == 0:
        jugador_muerto(key_primaria_partida)


def muerte_ganon():
    global flag_zelda_saved,flag_ganon_castle,flag_in_game

    if datos_partida_actual["castle"][0]["vida"] < 1:
        lista_prompt.append("It has been an exhausting fight, but with persistence, you have achieved it.")
        lista_prompt.append("You saved Zelda, you won the game")
        # GUARDAR PARTIDA
        datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]  #maximo de corazones
        datos_jugador_actual["region"] = "hyrule"  # primera region

        save_game(key_primaria_partida)

        # AL ZELDA SAVED
        flag_zelda_saved = True
        flag_ganon_castle = False
        flag_in_game = False



# VARIABLES --------

xpos = 7
ypos = 10

hierba = False
cocinar = False
talar = False
pescar = False
fox = False
santuario = False
cofre = False
atacar_enemigo = False
equip = False
unequip = False
eat = False
atacar_general = False

pescar_mapa = True



# INICIO JUEGO WHILE
while not flag_general_juego:

    # MAIN MENU
    while flag_main_menu:
        # limpiar_pantalla()
        print_main_menu()
        prompt(lista_prompt)
        input_main_menu()

    '''
     QUERIES MENU
    while flag_queries:
      limpiar_pantalla()
    '''

    # HELP MENU
    while flag_help_new_game:
        # limpiar_pantalla()
        pm.print_help_new_game()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_new_game = False
            flag_new_game = True
        else:
            lista_prompt.append("Invalid action")

    # ABAOUT MENU
    while flag_about:
        #limpiar_pantalla()
        pm.print_about()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_about = False
            flag_main_menu = True
        else:
            lista_prompt.append("Invalid action")

    # HELP MAIN MENU
    while flag_help_main_menu:
        #limpiar_pantalla()
        pm.print_help_main_menu()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_main_menu = False
            flag_main_menu = True
        else:
            lista_prompt.append("Invalid action")

    # NEW GAME MENU
    while flag_new_game:
        # limpiar_pantalla()
        pm.print_new_game()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_main_menu = True
            flag_new_game = False
        elif opc.lower() == "help":
            flag_help_new_game = True
            flag_new_game = False
        else:
            nombre_jugador = asignar_nombre(opc)

    # SAVED GAMES MENU
    while flag_saved_games:
        print(lista_partidas)
        #limpiar_pantalla()
        print_saved_games()
        prompt(lista_prompt)
        input_saved_games()

    # HELP SAVED GAMES MENU
    while flag_help_saved_games:
        #limpiar_pantalla()
        pm.print_help_saved_game()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_saved_games = False
            flag_saved_games = True
        else:
            lista_prompt.append("Invalid action")

    # LEGEND MENU
    while flag_legend:
        # limpiar_pantalla()
        pm.print_legend()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "continue":
            flag_legend = False
            flag_plot = True
        else:
            lista_prompt.append("Invalid action")
    # PLOT MENU
    while flag_plot:
        # limpiar_pantalla()
        pm.print_plot(nombre_jugador)
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "continue":
            lista_prompt.append("The adventure begins")
            datos_jugador_actual["nombre"] = nombre_jugador
            sql = "INSERT INTO game (user_name, hearts_remaining, hearts_total, region) VALUES (%s, %s, %s, %s)"
            val = (datos_jugador_actual['nombre'], 3, 3, "hyrule")
            cursor.execute(sql, val)
            key_primaria_partida = cursor.lastrowid
            print(f"Key primaria de partida creada = {key_primaria_partida}")
            crear_nueva_partida(key_primaria_partida)
            flag_plot = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")

    # GAME MENU
    while flag_in_game:
        # limpiar_pantalla()

        # COMPROBACIONES
        mostrar_fox()
        reinicio_cofres(key_primaria_partida)
        actualizar_turnos_restantes_arboles(datos_jugador_actual["region"])

        # MAPA
        mapa_cargado = generar_mapa()
        (hierba, cocinar, talar, pescar, santuario, cofre,
         atacar_enemigo, equip, unequip, eat, atacar_general) = permitir_acciones_jugador(mapa_cargado, xpos, ypos)
        print_tablero(mapa_cargado)
        # PROMPT
        prompt(lista_prompt)
        # INPUT
        to_do = input("What to do now?")

        if to_do.lower() == "exit":
            flag_in_game = False
            flag_main_menu = True


        # orden: SHOW MAP

        elif to_do.lower() == "show map":
            flag_in_game = False
            flag_show_map = True

        # orden: ATTACK

        elif to_do.lower() == "attack" and atacar_enemigo:
            attack_enemy()

        elif to_do.lower() == "attack" and fox:
            attack_fox()

        elif to_do.lower() == "attack" and talar:
            attack_tree()

        elif (to_do.lower() == "attack"
              and hierba and ("wood sword" in datos_jugador_actual["items_equipados"]
              or "sword" in datos_jugador_actual["items_equipados"])):
            attack_grass()

        # order: FISH

        elif to_do.lower() == "fish" and pescar and pescar_mapa:
            fish()

        # orden: OPEN

        elif to_do.lower() == "open sanctuary" and santuario:
            open_sacntuary()

        elif to_do.lower() == "open chest" and cofre:
            open_chest()

        # orden: GO BY THE [f,t,water,sX,eX,m,c]

        elif to_do[0:9].lower() == "go by the":
            xpos, ypos = go_by_the_x(to_do, xpos, ypos)

        # ordern: GO TO [REGION]

        elif to_do[0:5].lower() == "go to":
            region_to_go = to_do[6:].lower()

            xpos, ypos, datos_jugador_actual["region"] = move_region(datos_jugador_actual["region"], region_to_go, xpos,
                                                                     ypos)

            if xpos == 8 and ypos == 2:
                flag_in_game = False
                flag_ganon_castle = True

            save_game(key_primaria_partida)

        # orden: GO [DIRECCIÓN]

        elif to_do[0:2].lower() == "go":
            xpos, ypos = go_direction(to_do, xpos, ypos)

        # orden INCORRECTA

        else:
            lista_prompt.append("Incorrect Option")

        # si link ha muerto
        jugador_muerto(key_primaria_partida)

    # SHOW MAP MENU
    while flag_show_map:
        show_map()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_show_map = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")

    # HELP INVENTORY MENU
    while flag_help_inventory: # FALTA INPUT en in_game para ir a este flag
        pm.print_help_inventory()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_inventory = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")

    # GANON CASTLE MENU
    while flag_ganon_castle:

        mapa_cargado_ganon = generar_mapa_ganon()
        (hierba, cocinar, talar, pescar, santuario, cofre,
         atacar_enemigo, equip, unequip, eat, atacar_general) = permitir_acciones_jugador(mapa_cargado_ganon, xpos, ypos)
        print_tablero_ganon(mapa_cargado_ganon,datos_partida_actual["castle"][0]["vida"])
        # PROMPT
        prompt(lista_prompt)
        # INPUT
        to_do = input("What to do now?")

        # order: BACK

        if to_do.lower() == "back": #vuelve a la región anterior

            #reset vida ganon
            datos_partida_actual["castle"][0]["vida"] = 8

            flag_ganon_castle = False
            flag_in_game = True

        #order: GO [LEFT/RIGHT]

        elif to_do[0:7].lower() == "go left" or to_do[0:8] == "go right":

            xpos,ypos = go_direction_ganon(to_do,xpos,ypos)

            if xpos == 8 and ypos == 20:
                datos_jugador_actual["vida_actual"] -= 1


        #order: ATTACK
        elif to_do.lower() == "attack" and xpos == 8 and ypos == 20 and datos_partida_actual["castle"][0]["vida"] > 0 : #ganon
            attack_ganon()

        else:
            lista_prompt.append("Incorrect Option")

    # LINK DEATH MENU
    while flag_link_death:
        pm.print_personaje_death(datos_jugador_actual["nombre"])
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "continue":
            # restart de los datos de partida
            info_alimento_partida = importar_datos_comida_sin_modificaciones()
            info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
            datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
            datos_partida_actual = importar_datos_partida_sin_modificaciones()
            key_primaria_partida = ""
            # Vuelve al main menu
            flag_link_death = False
            flag_main_menu = True
        else:
            lista_prompt.append("Invalid action")

    # ZELDA SAVED MENU
    while flag_zelda_saved:
        pm.print_zelda_saved(datos_jugador_actual["nombre"])
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "continue":
            #reset datos
            info_alimento_partida = importar_datos_comida_sin_modificaciones()
            info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
            datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
            datos_partida_actual = importar_datos_partida_sin_modificaciones()
            key_primaria_partida = ""
            # menu principal
            flag_main_menu = True
            flag_zelda_saved =  False
        else:
            lista_prompt.append("Invalid action")


