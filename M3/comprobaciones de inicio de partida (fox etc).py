import datos_juego as datos_importados
import random
import prints_menus as pm

# FUNCIONALIDADES AL FINAL DEL DOCUMENTO

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
            dato_por_mapa = {"spawn": spawn, "enemigos": enemigos, "arboles": arboles, "cofres": cofres, "fox": fox,
                             "santuarios": santuarios}
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


def generar_mapa():  # genera el mapa
    # GENERAR COPIA MAPA -----> a partir de esta se hace el mapa sobre el que interactuar
    mapa_a_cargar = []
    for fila in datos_importados.localizaciones[
        datos_jugador_actual["region"]]:  # para cambiar de localizacion, cambia la region en info personaje
        fila_mapa_a_cargar = []
        for elemento in fila:
            fila_mapa_a_cargar.append(elemento)
        mapa_a_cargar.append(fila_mapa_a_cargar)
    # CARGAR ENEMIGO EN EL MAPA
    for enemigo in datos_partida_actual[datos_jugador_actual["region"]]["enemigos"]:
        if datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo][
            "vida"] > 0:  # Si vida > 0, hago print de E + vida
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["y"]] = "E"
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["y"] + 1] = \
                datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][enemigo]["vida"]  # Esto es la vida
    # CARGAR SANTUARIO EN EL MAPA
    for santuario in datos_partida_actual[datos_jugador_actual["region"]][
        "santuarios"]:  # El santuario se carga siempre
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["y"]] = "S"
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["y"] + 1] = \
            datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["nombre"][1]
        if not datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario][
            "descubierto"]:  # Pero si no esta descubierto
            mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario]["x"]][
                datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][santuario][
                    "y"] + 2] = "?"  # Se hace print de ?
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
    if datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] and not \
    datos_partida_actual[datos_jugador_actual["region"]]["fox"][0][
        "muerto"]:
        mapa_a_cargar[datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["x"]][
            datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["y"]] = "F"
    return mapa_a_cargar


def print_tablero(mapa):  # hace print del tablero
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
    print("* " * 40)


mapa_cargado = generar_mapa()
print_tablero(mapa_cargado)


def cargar_partida():
    # CARGAR PARTIDA
    # para datos jugador
    # cursor.execute(f"SELECT nombre_usuario, vida actual, blood_moon_countdown, "blood_moon_appearances", region WHERE primary_key = {key_primaria}")
    cursor = ("Pablo", 4, 17, 5, "death mountain")
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
    cursor = (("hyrule", 0, 3, 8, 0), ("death mountain", 0, 5, 50, 0))
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


cargar_partida()
mapa_cargado = generar_mapa()
print_tablero(mapa_cargado)

lista_prompt = []
def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)

""" FOX YA INTEGRADO
def mostrar_fox():
    if not datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["intento"]:  # PERMITE QUE SOLO HAYA HABIDO UN INTENTO. SE DEBE REINICIAR AL SALIR DEL MAPA
        datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["intento"] = True
        visible = random.choice([True, False])  # 50% CHANCE
        if visible:
            lista_prompt.append("You see a Fox")
            datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] = True
        else:
            lista_prompt.append("You don't see a Fox")

while True:
    mostrar_fox()
    mapa_cargado = generar_mapa()
    print_tablero(mapa_cargado)
    prompt(lista_prompt)
    # ESTO ES EL INPUT, LO QUE TE INTERESA
    opc = input("Que hacer: ")
    if opc == "matar fox":
        if datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] and not datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"]:
            datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"] = True
        else:
            # lista_prompt.append("Invalid Action")
            lista_prompt.append("Invalid Action")

# SI CAMBIA DE MAPA, ANTES DE CAMBIAR LOS DATOS DE REGION ACTUAL SE DEBE REESTABLECER TODO A FALSE
    #datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["intento"] = False
    #datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["visible"] = False
    #datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"] = False
"""

"""SI LINK MUERE datos_jugador_actual["vida_actual"] < 1:

flag_principal = True
ingame = True
flag_link_death = False
while flag_principal:
    while ingame:
        if datos_jugador_actual["vida_actual"] < 1:
            datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]
            # Lista_prompt.append("Nice try, you died, game is over")
            # Se guarda partida
            ingame = False
            flag_link_death = True
        else:
            datos_jugador_actual["vida_actual"] -= 1
        mapa_cargado = generar_mapa()
        print_tablero(mapa_cargado)
    while flag_link_death:
        pm.print_personaje_death(datos_jugador_actual["nombre"])
        opc = input("What to do now?")
        if opc.lower() == "continue":
            flag_link_death = False
            flag_main_menu = True
            print("Se acabo")
        else:
            #lista_prompt.append("Invalid Action")
            print("Invalid Action")
            
# VERSION 2 MEJORADA
SI LINK MUERE datos_jugador_actual["vida_actual"] < 1:

def jugador_muerto():
     global flag_in_game
     global flag_link_death
     if datos_jugador_actual["vida_actual"] < 1:
            datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]
            # lista_prompt.append("Nice try, you died, game is over")
            # Se guarda partida
            flag_in_game = False
            flag_link_death = True

flag_principal = True
flag_in_game = True
flag_link_death = False
while flag_principal:
    while flag_in_game:
        print(datos_jugador_actual["vida_actual"])

        if datos_jugador_actual["vida_actual"] >= 1:
            datos_jugador_actual["vida_actual"] -= 1
        mapa_cargado = generar_mapa()
        print_tablero(mapa_cargado)
        jugador_muerto()
    while flag_link_death:
        pm.print_personaje_death(datos_jugador_actual["nombre"])
        opc = input("What to do now?")
        if opc.lower() == "continue":
            flag_link_death = False
            flag_main_menu = True
            print("Se acabo")
        else:
            #lista_prompt.append("Invalid Action")
            print("Invalid Action")            
"""

# BLOODMOON

""" lógica para importar enemigos
print(datos_partida_actual["hyrule"]["enemigos"][0])
print(datos_partida_actual["death mountain"]["enemigos"][0])

lista_lugares = ["hyrule", "death mountain", "gerudo", "necluda"]
for region_cargada in lista_lugares:
    for enemigo_cargado in datos_importados.datos[region_cargada]["enemigos"]:
        datos_partida_actual[region_cargada]["enemigos"][enemigo_cargado]["x"] = datos_importados.datos[region_cargada]["enemigos"][enemigo_cargado]["x"]
        datos_partida_actual[region_cargada]["enemigos"][enemigo_cargado]["y"] = datos_importados.datos[region_cargada]["enemigos"][enemigo_cargado]["y"]
        datos_partida_actual[region_cargada]["enemigos"][enemigo_cargado]["vida"] = datos_importados.datos[region_cargada]["enemigos"][enemigo_cargado]["vida"]

print(datos_partida_actual["hyrule"]["enemigos"][0])
print(datos_partida_actual["death mountain"]["enemigos"][0])
"""

# ESTA ES LA PARTE GUAPA DE LA BLOODMOON
print(datos_jugador_actual["blood_moon_countdown"])
# a integrar
def blood_moon():  # Si resetean la posición, descomentar x, y
    if datos_jugador_actual["blood_moon_countdown"] < 1:
        print(datos_partida_actual["hyrule"]["enemigos"][0])
        print(datos_partida_actual["death mountain"]["enemigos"][0])
        datos_jugador_actual["blood_moon_countdown"] = 25
        datos_jugador_actual["blood_moon_appearances"] += 1
        print(f"The bloodmoon rises once again. Please, be careful {datos_jugador_actual['nombre']}")
        #lista_prompt.append(f"The bloodmoon rises once again. Please, be careful {datos_jugador_actual["nombre"]}")
        lista_lugares = ["hyrule", "death mountain", "gerudo", "necluda"]
        lista_lugares = ["hyrule", "death mountain", "gerudo", "necluda"]
        for region_cargada in lista_lugares:
            for enemigo_cargado in datos_importados.datos[region_cargada]["enemigos"]:
                #datos_partida_actual[region_cargada]["enemigos"][enemigo_cargado]["x"] = \
                #datos_importados.datos[region_cargada]["enemigos"][enemigo_cargado]["x"]
                #datos_partida_actual[region_cargada]["enemigos"][enemigo_cargado]["y"] = \
                #datos_importados.datos[region_cargada]["enemigos"][enemigo_cargado]["y"]
                datos_partida_actual[region_cargada]["enemigos"][enemigo_cargado]["vida"] = \
                datos_importados.datos[region_cargada]["enemigos"][enemigo_cargado]["vida"]
        print(datos_partida_actual["hyrule"]["enemigos"][0])
        print(datos_partida_actual["death mountain"]["enemigos"][0])

while True:
    print("Blood moon antes de resta", datos_jugador_actual["blood_moon_countdown"])
    datos_jugador_actual["blood_moon_countdown"] -= 1
    print("Blood moon despues de resta", datos_jugador_actual["blood_moon_countdown"])
    mapa_cargado = generar_mapa()
    print_tablero(mapa_cargado)
    blood_moon()
    input("Enter to continue")

