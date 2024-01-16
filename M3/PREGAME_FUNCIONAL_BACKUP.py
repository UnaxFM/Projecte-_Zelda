import os
import platform
import random
import prints_menus as pm
import mysql.connector
import datos_juego as datos_importados

# Conexión con la BBDD
db = mysql.connector.connect(
    host="localhost",  # IP
    user="root",  # root
    passwd="Cacadevaca48_",  # root
    database="zelda"  # la BBDD que sea
)

cursor = db.cursor()

# LIMPIEZA DE PANTALLA
sistema = platform.system()

def limpiar_pantalla():
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# PROMPT
lista_prompt = []
def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)

# IMPORTACION DE DATOS

import datos_juego as datos_importados
def importar_datos_partida_sin_modificaciones():
    datos_partida = {}
    for key_mapa in datos_importados.datos:
        if key_mapa == "castle":
            datos_partida[key_mapa] = datos_importados.datos[key_mapa].copy()
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

# se cargan datos de partida
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

# Esto permite obtener lista con las PK de las partidas cargadas
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
flag_help_inventory = False
flag_show_map = False
flag_zelda_saved = False
flag_link_death = False

# DATOS DE PARTIDA ACTUALIZABLES FUERA
key_primaria_partida = ""

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
    # SI SOLAMENTE HAY UNA PARTIDA, CARGA DIRECTAMENTE //  SI HAY MÁS DE UNA, sale lista a elegir
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
                raise ValueError
            indice_partida = int(opc[5:].replace(" ", "/")) # lista_partidas[indice_partida] == primary key == key del diccionario
            assert 0 <= indice_partida < len(lista_partidas)
            print(lista_partidas[indice_partida])
            key_primaria_partida = lista_partidas[indice_partida]
            cargar_partida(key_primaria_partida)
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
              f"lives_remaining = {info_equipamiento_partida[arma]['usos']}, "
              f"uses = {info_equipamiento_partida[arma]['cantidad']} "
              f"WHERE game_id = {primary_key} AND weapon_name = '{arma}';")
    for region in datos_partida_actual:
        if region == "castle":
            cursor.execute(f"UPDATE enemies SET lifes_remaining = {datos_partida_actual[region][0]['vida']} WHERE game_id = {primary_key} AND region = '{region}' AND enemy_id = {0};")
        else:
            for enemigo in datos_partida_actual[region]["enemigos"]:
                cursor.execute(f"UPDATE enemies SET xpos = {datos_partida_actual[region]['enemigos'][enemigo]['x']}, ypos = {datos_partida_actual[region]['enemigos'][enemigo]['y']}, "
                               f"lifes_remaining = {datos_partida_actual[region]['enemigos'][enemigo]['vida']} WHERE game_id = {primary_key} AND region = '{region}' AND enemy_id = {enemigo};")
    db.commit()


def show_map():
    mapa_show_map = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
        [" ", " ", "H", "y", "r", "u", "l", "e", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "D", "e", "a", "t", "h", " ", "m", "o", "u", "n", "t", "a", "i", "n", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", "a", "s", "t", "l", "e", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "G", "e", "r", "u", "d", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "N", "e", "c", "l", "u", "d", "a", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    lugares = ["hyrule", "death mountain", "necluda", "gerudo"]
    for lugar in lugares:
        for santuario in datos_partida_actual[lugar]["santuarios"]:
            mapa_show_map[datos_partida_actual[lugar]["santuarios"][santuario]["x"]][datos_partida_actual[lugar]["santuarios"][santuario]["y"]] = "S"
            mapa_show_map[datos_partida_actual[lugar]["santuarios"][santuario]["x"]][datos_partida_actual[lugar]["santuarios"][santuario]["y"] + 1] = datos_partida_actual[lugar]["santuarios"][santuario]["nombre"][1]
            if not datos_partida_actual[lugar]["santuarios"][santuario]["descubierto"]:
                mapa_show_map[datos_partida_actual[lugar]["santuarios"][santuario]["x"]][datos_partida_actual[lugar]["santuarios"][santuario]["y"] + 2] = "?"
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


while not flag_general_juego:
    while flag_main_menu:
        # limpiar_pantalla()
        print_main_menu()
        prompt(lista_prompt)
        input_main_menu()
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
    #while flag_queries:
        # limpiar_pantalla()
    while flag_saved_games:
        print(lista_partidas)
        #limpiar_pantalla()
        print_saved_games()
        prompt(lista_prompt)
        input_saved_games()
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
            print("Commit del insert")
            key_primaria_partida = cursor.lastrowid
            print(f"Key primaria de partida creada = {key_primaria_partida}")
            crear_nueva_partida(key_primaria_partida)
            flag_plot = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")
    while flag_in_game:
        # SI (datos_jugador_actual["vida_actual"]) < 1
            # flag_in_game = False
            # flag_link_death
        # Si vida ganon == 0
        # limpiar_pantalla()
        print("Bienvenido al Juego Principal")
        save_game(key_primaria_partida) #PARA GUARDAR LA PARTIDA
        """ RESET DE DATOS DENTRO DE PARTIDA
        info_alimento_partida = importar_datos_comida_sin_modificaciones()
        info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
        datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
        datos_partida_actual = importar_datos_partida_sin_modificaciones()
        key_primaria_partida = ""
        partidas_guardadas = seleccionar_partidas_guardadas()
        lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
        opc = input("Press enter to continue")
        if opc.lower() == "guardar partida":
            save_game(key_primaria_partida)
            """
    """
    while flag_castillo_ganon:
    while flag_show_map:
        show_map()
        if opc.lower() == "back":
            flag_show_map = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")
    while flag_help_inventory:
        pm.print_help_inventory()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_inventory = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")
    while flag_link_death:
        pm.print_personaje_death(datos_jugador_actual["nombre"])
        prompt(lista_prompt)
        opc = input("What to do now? ")
        # hay que pillar la vida total que tiene y igualar la actual y hacer update en la BBDD
        if opc.lower() == "continue:
            # restart de los datos de partida
            info_alimento_partida = importar_datos_comida_sin_modificaciones()
            info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
            datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
            datos_partida_actual = importar_datos_partida_sin_modificaciones()
            key_primaria_partida = ""
            partidas_guardadas = seleccionar_partidas_guardadas()
            lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
            flag_link_death = False
            flag_main_menu = True
        else:
            lista_prompt.append("Invalid action")
    while flag_zelda_saved:
"""



# PARA HACER RESET DE DATOS
"""
info_alimento_partida = importar_datos_comida_sin_modificaciones()
info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
datos_partida_actual = importar_datos_partida_sin_modificaciones()
key_primaria_partida = ""
partidas_guardadas = seleccionar_partidas_guardadas()
lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
"""
