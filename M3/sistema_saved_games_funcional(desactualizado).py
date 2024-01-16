import mysql.connector
import datetime

db = mysql.connector.connect(
    host="51.105.57.176",  # IP
    user="root",  # root
    passwd="root",  # root
    database="zelda"  # la BBDD que sea
)

cursor = db.cursor()

lista_prompt = []
def prompt(lista):
    if len(lista) > 8:
        lista_prompt.pop(0)
    for elemento in lista:
        print(elemento)

flag_general = False
flag_saved_games = True
flag_help_saved_games = False
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
        partida = {"nombre_jugador": partida_cargada_bbdd[2],
                   "fecha_modificacion": partida_cargada_bbdd[1].strftime("%d/%m/%Y %H:%M:%S"),
                   "region": partida_cargada_bbdd[3],
                   "corazones_actuales": partida_cargada_bbdd[4],
                   "corazones_totales": partida_cargada_bbdd[5]}
        diccionario_partidas_guardadas[partida_cargada_bbdd[0]] = partida
    return diccionario_partidas_guardadas

def metodo_burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if partidas_guardadas[lista[j]]["fecha_modificacion"] < partidas_guardadas[lista[j + 1]]["fecha_modificacion"]:  # Aqui se comprueba el parámetro
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Pero lo que se ordena es la lista de keys
    return lista

partidas_guardadas = seleccionar_partidas_guardadas()
lista_partidas = metodo_burbuja(list(partidas_guardadas.keys()))
print(lista_partidas)

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
            lista_partidas = metodo_burbuja(list(partidas_guardadas.keys()))
        except (ValueError, AssertionError):
            lista_prompt.append("Invalid Action")
    else:
        lista_prompt.append("Invalid Action")

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
def print_help_saved_game():
    print("* " + "Help, saved games " + "* " * 30 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'play X' to continue playing the game 'X'".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'erase X' to erase the game 'X'".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to the main menu".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to the 'Saved games'".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Back  " + "* " * 36)


while not flag_general:
    while flag_saved_games:
        print_saved_games()
        prompt(lista_prompt)
        input_saved_games()
    while flag_help_saved_games:
        print_help_saved_game()
        prompt(lista_prompt)
        opc = input("What to do now? ")
        if opc.lower() == "back":
            flag_help_saved_games = False
            flag_saved_games = True
        else:
            lista_prompt.append("Invalid action")