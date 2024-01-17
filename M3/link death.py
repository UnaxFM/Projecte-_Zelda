import datos_juego as datos_importados
import prints_menus as pm

lista_prompt = []
def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)


import mysql.connector
# Conexión con la BBDD
db = mysql.connector.connect(
    host="51.105.57.176",  # IP
    user="root",  # root
    passwd="root",  # root
    database="zelda"  # la BBDD que sea
)

cursor = db.cursor()

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
key_primaria_partida = 1
datos_jugador_actual['vida_total'] = 7
cursor.execute(
    f"UPDATE game SET hearts_total = {datos_jugador_actual['vida_total']} WHERE game_id = {key_primaria_partida};")
db.commit()

main_menu = False
flag_in_game = True
flag_link_death = False
datos_jugador_actual["nombre"] = "Pablo"
key_primaria_partida = 1

def jugador_muerto():
    global flag_link_death
    global flag_in_game
    if datos_jugador_actual["vida_actual"] < 1:
        lista_prompt.append("Nice try, you died, game is over")
        datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]
        cursor.execute(f"UPDATE game SET hearts_remaining = {datos_jugador_actual['vida_actual']}, hearts_total = {datos_jugador_actual['vida_total']} WHERE game_id = {key_primaria_partida};")
        db.commit()
        flag_link_death = True
        flag_in_game = False

while True:
    while flag_in_game:
        print(datos_jugador_actual["vida_actual"], datos_jugador_actual["vida_total"])
        prompt(lista_prompt)
        datos_jugador_actual["vida_actual"] -= 1
        jugador_muerto()
        input("Enter")
    while flag_link_death:
            pm.print_personaje_death(datos_jugador_actual["nombre"])
            prompt(lista_prompt)
            opc = input("What to do now")
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

