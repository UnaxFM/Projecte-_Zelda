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
    print("* ")
print("* " + "Back" + "* " * 27)

informacion_jugador = {
    "nombre": "Link",
    "vida_actual": 3,
    "vida_total": 3,
    "blood_moon_countdown": 25,
    "blood_moon_appearances": 0,
    "items_equipados": [],
    "region": "death mountain"
}

weapons = {
    "wood sword": {"nombre": "wood sword", "equipado": False, "usos": 5, "cantidad": 0},
    "sword": {"nombre": "sword", "equipado": False, "usos": 9, "cantidad": 0},
    "wood shield": {"nombre": "wood shield", "equipado": False, "usos": 5, "cantidad": 0},
    "shield": {"nombre": "shield", "equipado": False, "usos": 9, "cantidad": 0}}

food = {
    "vegetables": {"nombre": "vegetables", "cantidad": 0},
    "fish": {"nombre": "fish", "cantidad": 0},
    "meat": {"nombre": "meat", "cantidad": 0},
    "salads": {"nombre": "salads", "cantidad": 0},
    "pescatarian": {"nombre": "pescatarian", "cantidad": 0},
    "roasted": {"nombre": "roasted", "cantidad": 0}
}

localizaciones = {
    "hyrule": [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "O", "O", "O"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "O", "O", "~", "O", "O", "O", "O", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", " ", " ", " ", "~", "~", "~", "~", "~", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", " ", " ", " ", " ", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]],
    "death mountain": [["0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["0", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", "0", "0", " ", " ", " ", " ", "0", "0", "0", "0", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]],
    "gerudo": [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "0", "0", "0", "0", "0", " ", " ", "0", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", "0", "0"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0",
     "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", " ", " ", " ", " ", " ", " ",
     " ", " ", "0", "0", "0", "0", "0", " ", " ", " ", " ", "0", "0", "0", "0", "0", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", "0", "0", "0", "0", "0", "0",
     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~"]],
    "necluda": [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~"],
    ["0", "0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["0", "0", "0", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~",
     "~", "~", "~", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", "~", "~", "~", "~", "~", "~"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
     " ", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "
        , " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "~", "~", "~", "~",
     "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]
}

datos = {
    "hyrule": {
        "spawn": {"x": 7, "y": 10},
        "enemigos": {
            0: {"vida": 9, "x": 4, "y": 35},
            1: {"vida": 1, "x": 8, "y": 20}
        },  # Viene de la BBDD
        "arboles": {
            0: {"vida": 4, "turnos_restantes": 9, "x": 3, "y": 5},
            1: {"vida": 4, "turnos_restantes": 9, "x": 7, "y": 48},
            2: {"vida": 4, "turnos_restantes": 9, "x": 8, "y": 45}
        },
        "cofres": {
            0: {"abierto": False, "x": 8, "y": 48}
        },  # Viene de la BBDD abiertos
        "fox": {
            0: {"intento": False,"visible": True, "muerto": False, "x": 8, "y": 53}
        },
        "santuarios": {
            0: {"nombre": "S0", "descubierto": False, "x": 5, "y": 43},
            1: {"nombre": "S1", "descubierto": False, "x": 8, "y": 30}
        }  # Viene de la BBDD abiertos
    },
    "death mountain": {
        "spawn": {"x": 8, "y":1},
        "enemigos": {
            0: {"vida": 2, "x": 2, "y": 52},
            1: {"vida": 2, "x": 3, "y": 12}
        },
        "arboles": {
            0: {"vida": 4, "turnos_restantes": 9, "x": 6, "y": 18},
            1: {"vida": 4, "turnos_restantes": 9, "x": 7, "y": 17},
            2: {"vida": 4, "turnos_restantes": 9, "x": 8, "y": 17}
        },
        "cofres": {
            0: {"abierto": False, "x": 7, "y": 36}
        },
        "fox": {
            0: {"intento": False, "visible": False, "muerto": False, "x": 1, "y": 29}
        },
        "santuarios": {
            2: {"nombre": "S2", "descubierto": False, "x": 2, "y": 5},
            3: {"nombre": "S3", "descubierto": False, "x": 8, "y": 50}
        }
    },
    "gerudo": {  # SPAWN 8/1
        "spawn": {"x": 8, "y":1},
        "enemigos": {
            0: {"vida": 1, "x": 3, "y": 2},
            1: {"vida": 2, "x": 5, "y": 37}
        },
        "arboles": {
            0: {"vida": 4, "turnos_restantes": 9, "x": 1, "y": 28},
            1: {"vida": 4, "turnos_restantes": 9, "x": 1, "y": 29},
            2: {"vida": 4, "turnos_restantes": 9, "x": 1, "y": 30},
            3: {"vida": 4, "turnos_restantes": 9, "x": 2, "y": 30},
            4: {"vida": 4, "turnos_restantes": 9, "x": 2, "y": 31},
            5: {"vida": 4, "turnos_restantes": 9, "x": 7, "y": 4}
        },
        "cofres": {
            0: {"abierto": False, "x": 0, "y": 53},
            1: {"abierto": False, "x": 8, "y": 7}
        },
        "fox": {
            0: {"intento": False,"visible": False, "muerto": False, "x": 7, "y": 49}
        },
        "santuarios": {
            4: {"nombre": "S4", "descubierto": False, "x": 2, "y": 47}
        }
    },
    "necluda": {  # SPAWN 1/1
        "spawn": {"x": 1, "y": 1},
        "enemigos": {
            0: {"vida": 1, "x": 1, "y": 9},
            1: {"vida": 2, "x": 5, "y": 37}
        },
        "arboles": {
            0: {"vida": 4, "turnos_restantes": 10, "x": 1, "y": 36},
            1: {"vida": 4, "turnos_restantes": 10, "x": 1, "y": 37},
            2: {"vida": 4, "turnos_restantes": 10, "x": 2, "y": 34},
            3: {"vida": 4, "turnos_restantes": 10, "x": 2, "y": 35},
            4: {"vida": 4, "turnos_restantes": 10, "x": 5, "y": 14},
            5: {"vida": 4, "turnos_restantes": 10, "x": 6, "y": 13},
            6: {"vida": 4, "turnos_restantes": 10, "x": 7, "y": 14}
        },
        "cofres": {
            0: {"abierto": False, "x": 0, "y": 21},
            1: {"abierto": False, "x": 1, "y": 50},
            2: {"abierto": False, "x": 8, "y": 22}
        },
        "fox": {
            0: {"intento": False,"visible": True, "muerto": False, "x": 6, "y": 5}
        },
        "santuarios": {
            5: {"nombre": "S5", "descubierto": False, "x": 5, "y": 50},
            6: {"nombre": "S6", "descubierto": False, "x": 8, "y": 32}
        }
    },
    "castle": {"ganon_vivo": True, "vida_ganon": 8}
}

# GENERAR COPIA MAPA -----> a partir de esta se hace el mapa sobre el que interactuar
"""
mapa_a_cargar = []
for fila in localizaciones[informacion_jugador["region"]]:
    fila_mapa_a_cargar = []
    for elemento in fila:
        fila_mapa_a_cargar.append(elemento)
    mapa_a_cargar.append(fila_mapa_a_cargar)

# CARGAR ENEMIGO EN EL MAPA
for enemigo in datos[informacion_jugador["region"]]["enemigos"]:
    if datos[informacion_jugador["region"]]["enemigos"][enemigo]["vida"] > 0:
        mapa_a_cargar[datos[informacion_jugador["region"]]["enemigos"][enemigo]["x"]][datos[informacion_jugador["region"]]["enemigos"][enemigo]["y"]] = "E"
        mapa_a_cargar[datos[informacion_jugador["region"]]["enemigos"][enemigo]["x"]][datos[informacion_jugador["region"]]["enemigos"][enemigo]["y"] + 1] = datos[informacion_jugador["region"]]["enemigos"][enemigo]["vida"]

# CARGAR SANTUARIO EN EL MAPA
for santuario in datos[informacion_jugador["region"]]["santuarios"]:
    mapa_a_cargar[datos[informacion_jugador["region"]]["santuarios"][santuario]["x"]][datos[informacion_jugador["region"]]["santuarios"][santuario]["y"]] = "S"
    mapa_a_cargar[datos[informacion_jugador["region"]]["santuarios"][santuario]["x"]][datos[informacion_jugador["region"]]["santuarios"][santuario]["y"] + 1] = datos[informacion_jugador["region"]]["santuarios"][santuario]["nombre"][1]
    if not datos[informacion_jugador["region"]]["santuarios"][santuario]["descubierto"]:
        mapa_a_cargar[datos[informacion_jugador["region"]]["santuarios"][santuario]["x"]][datos[informacion_jugador["region"]]["santuarios"][santuario]["y"] + 2] = "?"

# CARGAR COFRE EN EL MAPA
for cofre in datos[informacion_jugador["region"]]["cofres"]:
    if datos[informacion_jugador["region"]]["cofres"][cofre]["abierto"]:
        mapa_a_cargar[datos[informacion_jugador["region"]]["cofres"][cofre]["x"]][datos[informacion_jugador["region"]]["cofres"][cofre]["y"]] = "W"
    else:
        mapa_a_cargar[datos[informacion_jugador["region"]]["cofres"][cofre]["x"]][datos[informacion_jugador["region"]]["cofres"][cofre]["y"]] = "M"

# CARGAR ARBOL (conflicto si hay arboles juntos) EN EL MAPA
for arbol in datos[informacion_jugador["region"]]["arboles"]:
    mapa_a_cargar[datos[informacion_jugador["region"]]["arboles"][arbol]["x"]][datos[informacion_jugador["region"]]["arboles"][arbol]["y"]] = "T"
    if datos[informacion_jugador["region"]]["arboles"][arbol]["vida"] <= 0:
        mapa_a_cargar[datos[informacion_jugador["region"]]["arboles"][arbol]["x"]][datos[informacion_jugador["region"]]["arboles"][arbol]["y"] + 1] = datos[informacion_jugador["region"]]["arboles"][arbol]["turnos_restantes"]

# CARGAR FOX

if datos[informacion_jugador["region"]]["fox"][0]["visible"] and not datos[informacion_jugador["region"]]["fox"][0]["muerto"]:
    mapa_a_cargar[datos[informacion_jugador["region"]]["fox"][0]["x"]][datos[informacion_jugador["region"]]["fox"][0]["y"]] = "F"
"""
"""
def print_mapa():
    titulo = informacion_jugador["region"] + " "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    if len(titulo) % 2 != 0:
        print("* " + titulo.title() + " " + "* " * calculo)
    else:
        print("* " + titulo.title() + "* " * calculo)
    for lista in localizaciones[informacion_jugador["region"]]:
        print("*", end="")
        for elemento in lista:
            print(elemento, end="")
        print("* ")
    print("* " * 30)

print_mapa()
"""


"""
def print_tablero(mapa):  #BACKUP
    titulo = informacion_jugador["region"] + " "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    lista = ["Inventor", "Weapons", "Fosdod"]
    titulo_2 = lista[0]
    calculo_secundario = int(((20 - len(titulo_2)) / 2) - 1)
    if len(titulo) % 2 != 0:
        print("* " + titulo.title() + " " + "* " * calculo, end="")
    else:
        print("* " + titulo.title() + "* " * calculo, end="")
    if len(titulo_2) % 2 != 0:
        print("* " * calculo_secundario + " " + titulo_2.title() + " *")
    else:
        print("* " * calculo_secundario + titulo_2.title() + " *")
    for fila in mapa:
        print("*", end="")
        for elemento in fila:
            print(elemento, end="")
        print("* ")
    print("* " * 30)
"""

decoracion_personaje_1 = ("Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ",
                          "Link          3/9 ")
def print_tablero(mapa): # hace print del tablero
    titulo = informacion_jugador["region"] + " "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    lista = ["Inventory", "Weapons", "Fosdod"]
    titulo_2 = lista[1]
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
        print("* ", end="")
        for elemento in decoracion_personaje_1[i]:
            print(elemento, end="")
        print("* ")
    print("* " * 40)
def generar_mapa(): # genera el mapa
    # GENERAR COPIA MAPA -----> a partir de esta se hace el mapa sobre el que interactuar
    mapa_a_cargar = []
    for fila in localizaciones[informacion_jugador["region"]]: # para cambiar de localizacion, cambia la region en info personaje
        fila_mapa_a_cargar = []
        for elemento in fila:
            fila_mapa_a_cargar.append(elemento)
        mapa_a_cargar.append(fila_mapa_a_cargar)
    # CARGAR ENEMIGO EN EL MAPA
    for enemigo in datos[informacion_jugador["region"]]["enemigos"]:
        if datos[informacion_jugador["region"]]["enemigos"][enemigo]["vida"] > 0:  # Si vida > 0, hago print de E + vida
            mapa_a_cargar[datos[informacion_jugador["region"]]["enemigos"][enemigo]["x"]][
                datos[informacion_jugador["region"]]["enemigos"][enemigo]["y"]] = "E"
            mapa_a_cargar[datos[informacion_jugador["region"]]["enemigos"][enemigo]["x"]][
                datos[informacion_jugador["region"]]["enemigos"][enemigo]["y"] + 1] = \
            datos[informacion_jugador["region"]]["enemigos"][enemigo]["vida"]  # Esto es la vida
    # CARGAR SANTUARIO EN EL MAPA
    for santuario in datos[informacion_jugador["region"]]["santuarios"]: # El santuario se carga siempre
        mapa_a_cargar[datos[informacion_jugador["region"]]["santuarios"][santuario]["x"]][
            datos[informacion_jugador["region"]]["santuarios"][santuario]["y"]] = "S"
        mapa_a_cargar[datos[informacion_jugador["region"]]["santuarios"][santuario]["x"]][
            datos[informacion_jugador["region"]]["santuarios"][santuario]["y"] + 1] = \
        datos[informacion_jugador["region"]]["santuarios"][santuario]["nombre"][1]
        if not datos[informacion_jugador["region"]]["santuarios"][santuario]["descubierto"]: # Pero si no esta descubierto
            mapa_a_cargar[datos[informacion_jugador["region"]]["santuarios"][santuario]["x"]][
                datos[informacion_jugador["region"]]["santuarios"][santuario]["y"] + 2] = "?" # Se hace print de ?
    # CARGAR COFRE EN EL MAPA
    for cofre in datos[informacion_jugador["region"]]["cofres"]:
        if datos[informacion_jugador["region"]]["cofres"][cofre]["abierto"]:  # Si esta abierto, W
            mapa_a_cargar[datos[informacion_jugador["region"]]["cofres"][cofre]["x"]][
                datos[informacion_jugador["region"]]["cofres"][cofre]["y"]] = "W"
        else:  # Si esta cerrado, M
            mapa_a_cargar[datos[informacion_jugador["region"]]["cofres"][cofre]["x"]][
                datos[informacion_jugador["region"]]["cofres"][cofre]["y"]] = "M"
    # CARGAR ARBOL (conflicto si hay arboles juntos) EN EL MAPA
    for arbol in datos[informacion_jugador["region"]]["arboles"]:
        mapa_a_cargar[datos[informacion_jugador["region"]]["arboles"][arbol]["x"]][
            datos[informacion_jugador["region"]]["arboles"][arbol]["y"]] = "T"
        if datos[informacion_jugador["region"]]["arboles"][arbol]["vida"] <= 0:
            mapa_a_cargar[datos[informacion_jugador["region"]]["arboles"][arbol]["x"]][
                datos[informacion_jugador["region"]]["arboles"][arbol]["y"] + 1] = \
            datos[informacion_jugador["region"]]["arboles"][arbol]["turnos_restantes"]
    # CARGAR FOX
    if datos[informacion_jugador["region"]]["fox"][0]["visible"] and not datos[informacion_jugador["region"]]["fox"][0][
        "muerto"]:
        mapa_a_cargar[datos[informacion_jugador["region"]]["fox"][0]["x"]][
            datos[informacion_jugador["region"]]["fox"][0]["y"]] = "F"
    return mapa_a_cargar

mapa_cargado = generar_mapa()
print_tablero(mapa_cargado)

"""
# SHOW MAP
mapa_show_map = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
    [" ", " ", "H", "y", "r", "u", "l", "e", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "D", "e", "a", "t", "h", " ", "m", "o", "u", "n", "t", "a", "i", "n", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "G", "e", "r", "u", "d", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "N", "e", "c", "l", "u", "d", "a", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

def crear_show_map():
    mapa_show_map = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
        [" ", " ", "H", "y", "r", "u", "l", "e", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "D", "e", "a",
         "t", "h", " ", "m", "o", "u", "n", "t", "a", "i", "n", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "G", "e", "r", "u", "d", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", "N", "e", "c", "l", "u", "d", "a", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
         " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    lugares = ["hyrule", "death mountain", "necluda", "gerudo"]
    for lugar in lugares:
        for santuario in datos[lugar]["santuarios"]:
            mapa_show_map[datos[lugar]["santuarios"][santuario]["x"]][datos[lugar]["santuarios"][santuario]["y"]] = "S"
            mapa_show_map[datos[lugar]["santuarios"][santuario]["x"]][datos[lugar]["santuarios"][santuario]["y"] + 1] = datos[lugar]["santuarios"][santuario]["nombre"][1]
            if not datos[lugar]["santuarios"][santuario]["descubierto"]:
                mapa_show_map[datos[lugar]["santuarios"][santuario]["x"]][datos[lugar]["santuarios"][santuario]["y"] + 2] = "?"


"""

