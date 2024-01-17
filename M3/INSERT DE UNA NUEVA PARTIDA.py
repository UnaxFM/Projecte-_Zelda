
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

    sql = "INSERT INTO enemies (game_id, enemy_id, region, xpos, ypos, lifes_remaining) VALUES (%s, %s, %s, %s, %s, %s)"
    val = []
    lista_lugares = ["hyrule", "death mountain", "gerudo", "necluda"]
    for region_cargada in lista_lugares:
        for enemigo in datos_partida_actual[region_cargada]["enemigos"]:
            temp = (primary_key, enemigo, region_cargada, datos_partida_actual[region_cargada]["enemigos"][enemigo]["vida"], datos_partida_actual[region_cargada]["enemigos"][enemigo]["x"], datos_partida_actual[region_cargada]["enemigos"][enemigo]["y"])
            val.append(temp)
    print(val)
    val.append(primary_key, 0, "castle", datos_partida_actual['castle'][0]['vida'],
               datos_partida_actual['castle'][0]['x'], datos_partida_actual['castle'][0]['y'])
    print(val)
    cursor.executemany(sql, val)
    db.commit()

crear_nueva_partida(1)