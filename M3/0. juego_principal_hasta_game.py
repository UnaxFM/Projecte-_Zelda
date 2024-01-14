import os
import platform
import random
import prints_menus as pm
import mysql.connector

# Conexión con la BBDD
db = mysql.connector.connect(
    host="172.187.200.252",  # IP
    user="root",  # root
    passwd="root",  # root
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

# se cargan datos de partida
info_alimento_partida = importar_datos_comida_sin_modificaciones()
info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
datos_partida_actual = importar_datos_partida_sin_modificaciones()


# CARGADO DE PARTIDAS
ver_todos = False  # RESET A TRUE CUANDO SE PASE DE PANTALLA
def seleccionar_partidas_guardadas():
    if ver_todos: # MODIFICAR AL CAMBIAR LA BBDD
        cursor.execute("SELECT GameID, DataLastSave, NomJugador, Region, HeartsRemaining, HeartsTotal "
                       "FROM v_inf_player ORDER BY DataLastSave DESC")
    else:
        cursor.execute("SELECT GameID, DataLastSave, NomJugador, Region, HeartsRemaining, HeartsTotal "
                       "FROM v_inf_player ORDER BY DataLastSave DESC LIMIT 8;")
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

def print_main_menu():  # Se pone aqui por error (se produce circular import)
    print("* " * 40)
    eleccion_personaje_ascii = random.randrange(3)
    for i in range(len(pm.decoracion_personaje_1)):
        if i == 4:
            print("* " + " Zelda breath of the Wild".ljust(56) + pm.decoracion_main_menu[eleccion_personaje_ascii][i] + " " * 5 + "*")
        else:
            print("* " + " " * 56 + pm.decoracion_main_menu[eleccion_personaje_ascii][i] + " " * 5 + "*")
    # PUEDE ESTAR PENDIENTE DE MODIFICAR AL HACER SELECT DE LAS PARTIDAS GUARDADAS
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
            key_primaria = partidas_guardadas[0]
            print("hay una sola partida")
            # Se hace el select
            # Se modifican datos importados del .py
            # Envia al game
            flag_main_menu = False
            flag_in_game = True
        else:
            global flag_saved_games
            flag_main_menu = False
            flag_saved_games = True
    else:
        lista_prompt.append("Invalid action")

def input_saved_games():
    global flag_saved_games
    global lista_partidas
    global ver_todos
    global partidas_guardadas
    opc = input("What to do now? ")
    if opc.lower() == "help":
        flag_saved_games = False
        global flag_help_saved_games
        flag_help_saved_games = True
    elif opc.lower() == "back":
        ver_todos = False
        flag_saved_games = False
        global flag_general
        flag_general = True
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
            indice_partida = int(opc[5:].replace(" ", "/"))
            assert 0 <= indice_partida < len(lista_partidas)
        except (ValueError, AssertionError):
            lista_prompt.append("Invalid Action")
    elif opc[0:5].lower() == "erase":
        try:
            if int(opc[6]) == 0 and len(opc[6:]) > 1:
                raise ValueError
            indice_partida = int(opc[6:].replace(" ", "/"))
            assert 0 <= indice_partida < len(lista_partidas)
            del partidas_guardadas[lista_partidas[indice_partida]]
            query_delete = f"DELETE FROM game WHERE game_id = {lista_partidas[indice_partida]};"
            cursor.execute(query_delete)
            db.commit()
            partidas_guardadas = seleccionar_partidas_guardadas()
            lista_partidas = metodo_burbuja_ordenar_partidas_recientes(list(partidas_guardadas.keys()))
        except (ValueError, AssertionError):
            lista_prompt.append("Invalid Action")
    else:
        lista_prompt.append("Invalid Action")


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
            # SE HACE INSERT DE LO NECESARIO EN LA NUEVA PARTIDA
            flag_plot = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")
    while flag_in_game:
        # limpiar_pantalla()
        print("Bienvenido al Juego Principal")
        print(datos_jugador_actual)
        print(info_alimento_partida)
        print(info_equipamiento_partida)
        print(datos_partida_actual)
        prompt(lista_prompt)
        input("Press enter to continue")
    """
    while flag_help_inventory:
        pm.print_help_inventory()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_inventory = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")
    """


