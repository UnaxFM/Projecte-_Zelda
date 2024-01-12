import os
import platform
import random
import prints_menus as pm
import mysql.connector

# Conexión con la BBDD
db = mysql.connector.connect(
    host="localhost",  # IP
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


# CARGADO DE PARTIDAS
ver_todos = False
def seleccionar_partidas_guardadas():
    if ver_todos:
        cursor.execute("SELECT GameID, DataLastSave, NomJugador, Region, HeartsRemaining, HeartsTotal "
                       "FROM v_inf_player ORDER BY DataLastSave DESC")
    else:
        cursor.execute("SELECT GameID, DataLastSave, NomJugador, Region, HeartsRemaining, HeartsTotal "
                       "FROM v_inf_player ORDER BY DataLastSave DESC LIMIT 8;")
    diccionario_partidas_guardadas = {}
    for partida_cargada_bbdd in cursor:
        print(partida_cargada_bbdd)
        partida = {"nombre_jugador": partida_cargada_bbdd[2],
                   "fecha_modificacion": partida_cargada_bbdd[1].strftime("%d/%m/%Y %H:%M:%S"),
                   "region": partida_cargada_bbdd[3],
                   "corazones_actuales": partida_cargada_bbdd[4],
                   "corazones_totales": partida_cargada_bbdd[5]}
        diccionario_partidas_guardadas[partida_cargada_bbdd[0]] = partida
    print(diccionario_partidas_guardadas)
    return diccionario_partidas_guardadas

def metodo_burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if partidas_guardadas[lista[j]]["fecha_modificacion"] < partidas_guardadas[lista[j + 1]]["fecha_modificacion"]:  # Aqui se comprueba el parámetro
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Pero lo que se ordena es la lista de keys
    return lista

partidas_guardadas = seleccionar_partidas_guardadas()
lista_partidas = metodo_burbuja(list(partidas_guardadas.keys()))

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
            print("hay una sola partida")
            # Se hace el select y se cargan datos solo hay una key que se usa con WHERE 
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
        lista_partidas = metodo_burbuja(list(partidas_guardadas.keys()))
    elif ver_todos is True and opc.lower() == "show recent":
        ver_todos = False
        partidas_guardadas = seleccionar_partidas_guardadas()
        lista_partidas = metodo_burbuja(list(partidas_guardadas.keys()))
    elif opc[0:4].lower() == "play":
        try:
            if int(opc[5]) == 0 and len(opc[5:]) > 1:
                raise ValueError
            indice_partida = int(opc[5:].replace(" ", "/")) # lista_partidas[indice_partida] == primary key == key del diccionario
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
            lista_partidas = metodo_burbuja(list(partidas_guardadas.keys()))
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
            flag_plot = False
            flag_in_game = True
        else:
            lista_prompt.append("Invalid action")
    while flag_in_game:
        # limpiar_pantalla()
        print("Bienvenido al Juego Principal")
        prompt(lista_prompt)
        input("Press enter to continue")


