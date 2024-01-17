import random
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
    datos_jugador["items_equipados"] = ["wood sword","wood shield"]
    return datos_jugador

info_alimento_partida = importar_datos_comida_sin_modificaciones()
info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
datos_partida_actual = importar_datos_partida_sin_modificaciones()


def cargar_partida():
    # CARGAR PARTIDA
    # para datos jugador
    # cursor.execute(f"SELECT nombre_usuario, vida actual, blood_moon_countdown, "blood_moon_appearances", region WHERE primary_key = {key_primaria}")
    cursor = ("Pablo", 4, 17, 5, "hyrule")
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
    cursor = (("hyrule", 0, 3, 8, 5), ("death mountain", 0, 3, 50, 6), ("castle", 0, 3, 50, 0))
    for enemigo in cursor:
        if enemigo[0] == "castle":
            datos_partida_actual[enemigo[0]][0]["vida"] = enemigo[4]
        else:
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


#.................... lo he cambiado el print para el dinamico de abajo ...................
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

    global hierba, cocinar, talar, pescar, santuario, cofre, atacar_enemigo, equip, unequip, eat, atacar_general

    lista_acciones = ["exit", "attack", "equip", "eat", "cook", "fish", "open"]
    lista_acciones_disponibles = ["exit", "go"]

    if atacar_general:
        lista_acciones_disponibles.append(lista_acciones[1])
    if equip:
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


# ----- prompt -----

lista_prompt = []

def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)

#FUNCIONES --------------------

def verificar_alrededor(matriz, fila, columna):
    # guardar elementos
    alrededor = []

    #3x3 alrededor del jugador
    for i in range(fila - 2, fila + 2): #-1,0,1: range(-1,2)
        for j in range(columna - 2, columna + 2): #-1,0,1 rrange(-1,2)
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]) and (i != fila or j != columna):
                alrededor.append(matriz[i][j])

    return alrededor


def permitir_acciones_jugador(mapa_cargado, xpos, ypos):
    global hierba, cocinar, talar, pescar, santuario, cofre, atacar_enemigo,equip,unequip,eat

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

    return hierba,cocinar,talar,pescar,santuario,cofre,atacar_enemigo,equip,unequip,eat,atacar_general


def encontrar_celda_vacia_adyacente(x,y,mapa):
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
    for id_objeto,info_objeto in diccionario.items():
        id_objeto_adyacente = None

        #1)verificar arriba izquierda +1
        if info_objeto["x"] == xpos-1 and info_objeto["y"] == ypos-2:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #2)verificar arriba izquierda
        elif info_objeto["x"] == xpos-1 and info_objeto["y"] == ypos-1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #3)verificar arriba
        elif info_objeto["x"] == xpos-1 and info_objeto["y"] == ypos:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #4)verificar arriba derecha
        elif info_objeto["x"] == xpos-1 and info_objeto["y"] == ypos+1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #5)verificar izquierda +1
        elif info_objeto["x"] == xpos and info_objeto["y"] == ypos-2:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #7)derecha
        elif info_objeto["x"] == xpos and info_objeto["y"] == ypos+1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #8)abajo izquierda +1
        elif info_objeto["x"] == xpos+1 and info_objeto["y"] == ypos-2:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #9)abajo izquierda
        elif info_objeto["x"] == xpos+1 and info_objeto["y"] == ypos-1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #10)abajo
        elif info_objeto["x"] == xpos+1 and info_objeto["y"] == ypos:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente
        #11)abajo derecha
        elif info_objeto["x"] == xpos+1 and info_objeto["y"] == ypos+1:
            id_objeto_adyacente = id_objeto
            return id_objeto_adyacente


def bajar_uso_cantidad_espada():

    if "wood sword" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["wood sword"]["usos"] -= 1
        #print("wood sw usos", info_equipamiento_partida["wood sword"]["usos"])

        if info_equipamiento_partida["wood sword"]["usos"] % 5 == 0:
            info_equipamiento_partida["wood sword"]["cantidad"] -= 1
            #print("wood sword cantidad", info_equipamiento_partida["wood sword"]["cantidad"])

    elif "sword" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["sword"]["usos"] -= 1
        #print("sword usos", info_equipamiento_partida["sword"]["usos"])

        if info_equipamiento_partida["sword"]["usos"] % 9 == 0:
            info_equipamiento_partida["sword"]["cantidad"] -= 1
            #print("sword cantidad", info_equipamiento_partida["sword"]["cantidad"])


def bajar_uso_cantidad_escudos():
    if "wood shield" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["wood shield"]["usos"] -= 1
        #print("wood sh usos", info_equipamiento_partida["wood shield"]["usos"])

        if info_equipamiento_partida["wood shield"]["usos"] % 5 == 0:
            info_equipamiento_partida["wood shield"]["cantidad"] -= 1
            #print("wood shield cantidad", info_equipamiento_partida["wood shield"]["cantidad"])

    elif "shield" in datos_jugador_actual["items_equipados"]:
        info_equipamiento_partida["shield"]["usos"] -= 1
        #print("shield usos", info_equipamiento_partida["shield"]["usos"])

        if info_equipamiento_partida["shield"]["usos"] % 9 == 0:
            info_equipamiento_partida["shield"]["cantidad"] -= 1
            #print("shield cantidad", info_equipamiento_partida["shield"]["cantidad"])

    else:
        datos_jugador_actual["vida_actual"] -= 1
        lista_prompt.append(f"Be careful {datos_jugador_actual['nombre']}, you only have {datos_jugador_actual['vida_actual']} hearts")



# -- funciones acciones --

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

    #print(datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["x"],",",datos_partida_actual[datos_jugador_actual["region"]]["enemigos"][id_enemigo_adyacente]["y"])


def attack_fox():
    info_alimento_partida["meat"]["cantidad"] += 1
    bajar_uso_cantidad_espada()

    # save_game(key_primaria_partida) !!!!!!!!!!!
    lista_prompt.append("You got meat")

    #matar a la guineu
    datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"] = True


def attack_tree():
    # id del arbol adyacente
    id_arbol_adyacente = obter_id_objeto_adyacente(datos_partida_actual[datos_jugador_actual["region"]]["arboles"])

    print(f"Enemigo {id_arbol_adyacente} es el de al lado")

    # el arbol está spawneando
    if datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["turnos_restantes"] > 0:
        lista_prompt.append("The tree is not ready yet")


    # se ataca SIN arma
    elif not "wood sword" in datos_jugador_actual["items_equipados"] and not "sword" in datos_jugador_actual[
        "items_equipados"]:
        print("sin arma")

        # se gana una manzana
        if random.random() < 0.4:
            print(info_alimento_partida["vegetables"])
            info_alimento_partida["vegetables"]["cantidad"] += 1
            print(info_alimento_partida["vegetables"])

            # save_game(key_primaria_partida) !!!!!!!!!!!

            lista_prompt.append("You got an apple")

        # se gana un arma
        elif random.random() < 0.1:
            dado = random.randrange(0, 1)

            if dado == 1:
                print(info_equipamiento_partida["wood sword"])
                info_equipamiento_partida["wood sword"]["cantidad"] += 1
                info_equipamiento_partida["wood sword"]["usos"] += 5
                print(info_equipamiento_partida["wood sword"])

                # save_game(key_primaria_partida) !!!!!!!!!!!

                lista_prompt.append("You got a Wood sword")

            else:
                print(info_equipamiento_partida["wood shield"])
                info_equipamiento_partida["wood shield"]["cantidad"] += 1
                info_equipamiento_partida["wood shield"]["usos"] += 5
                print(info_equipamiento_partida["wood shield"])

                # save_game(key_primaria_partida) !!!!!!!!!!!

                lista_prompt.append("You got a wood shield")

        else:
            lista_prompt.append("The tree didn't give you anything")

    # se atca CON arma
    else:
        print("con arma")
        if random.random() < 0.4:
            print(info_alimento_partida["vegetables"]["cantidad"])
            info_alimento_partida["vegetables"]["cantidad"] += 1
            print("cantidad vegetables", info_alimento_partida["vegetables"]["cantidad"])

            # save_game(key_primaria_partida) !!!!!!!!!!!

            lista_prompt.append("You got an apple")

        elif random.random() < 0.2:
            print(info_equipamiento_partida["wood sword"]["cantidad"])
            info_equipamiento_partida["wood sword"]["cantidad"] += 1
            print("cantidad wood s", info_equipamiento_partida["wood sword"]["cantidad"])

            # save_game(key_primaria_partida) !!!!!!!!!!!

            lista_prompt.append("You got a Wood sword")


        elif random.random() < 0.2:
            print(info_equipamiento_partida["wood shield"]["cantidad"])
            info_equipamiento_partida["wood shield"]["cantidad"] += 1
            print("cantidad wood shield", info_equipamiento_partida["wood shield"]["cantidad"])

            # save_game(key_primaria_partida) !!!!!!!!!!!

            lista_prompt.append("You got a wood shield")

        else:
            lista_prompt.append("The tree didn't give you anything")

        # quitar vida a la espada
        bajar_uso_cantidad_espada()

        # quitar vida al arbol adyacente
        datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["vida"] -= 1
        print(datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["vida"])

        # añadir +9 turnos restantes si su vida es cero
        if datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["vida"] == 0:
            datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["turnos_restantes"] += 9
            print(datos_partida_actual[datos_jugador_actual["region"]]["arboles"][id_arbol_adyacente]["turnos_restantes"])

def attack_grass():
    if random.random() < 0.1:
        info_alimento_partida["meat"]["cantidad"] += 1

        # save_game(key_primaria_partida) !!!!!!!!!!!

        lista_prompt.append("You got a lizard")
    else:
        lista_prompt.append("It seems like there is nothing in the grass")

def fish():
    if random.random() < 0.2:
        info_alimento_partida["pescatarian"]["cantidad"] += 1
        pescar_mapa = False

        # save_game(key_primaria_partida) !!!!!!!!!!!

        lista_prompt.append("You got a fish")

    else:
        lista_prompt.append("You didn't get a fish")


def open_sacntuary():

    id_santuario_adyacente = obter_id_objeto_adyacente(datos_partida_actual[datos_jugador_actual["region"]]["santuarios"])

    #print(f"Santuario {id_santuario_adyacente} es el de al lado")

    #comprobar si ya está abierto
    if datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["descubierto"] == True:
        lista_prompt.append("You already opened this sanctuary")

    else:
        #actualizar santuario a true
        datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["descubierto"] = True

        #aumentar vida máxima
        datos_jugador_actual["vida_total"] += 1

        #restaurar vida al máximo
        datos_jugador_actual["vida_actual"] = datos_jugador_actual["vida_total"]

        #commit a la BBDD
        '''
        sql = "INSERT INTO santuaries_opened (sactuary_id,game_id,region,xpos,ypos) VALUES (%s, %s, %s, %s, %s)
        val = (id_santuario_adyacente,key_primaria_partida,datos_jugador_actual["region"],
              datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["x"],
              datos_partida_actual[datos_jugador_actual["region"]]["santuarios"][id_santuario_adyacente]["y"]
              )
        cursor.execute(sql,val)
        
        save_game(key_primaria_partida) !!!!!!!!!!!
        '''

        lista_prompt.append(f"Sanctuaire {id_santuario_adyacente} done")


def open_chest():
    #localizar cofre y ponerlo a true
    id_cofre_adyacente = obter_id_objeto_adyacente(
        datos_partida_actual[datos_jugador_actual["region"]]["cofres"])

    datos_partida_actual[datos_jugador_actual["region"]]["cofres"][id_cofre_adyacente]["abierto"] = True


    #hyrule y gerudo
    if datos_jugador_actual["region"] == "hyrule" or datos_jugador_actual["region"] == "gerudo":
        print(info_equipamiento_partida["sword"])

        info_equipamiento_partida["sword"]["cantidad"] += 1
        info_equipamiento_partida["sword"]["usos"] += 9

        print(info_equipamiento_partida["sword"])

        lista_prompt.append("You got a sword")

    #death mountain y necluda
    else:
        print(info_equipamiento_partida["shield"])

        info_equipamiento_partida["shield"]["cantidad"] += 1
        info_equipamiento_partida["shield"]["usos"] += 9

        print(info_equipamiento_partida["shield"])

        lista_prompt.append("You got a shield")

    #commit a la BBDD
    '''
    sql = "INSERT INTO chest_opened (chest_id,game_id,region,xpos,ypos) VALUES (%s, %s, %s, %s, %s)"
    val = (id_cofre_adyacente,key_primaria_partida,datos_jugador_actual["region"],
           datos_partida_actual[datos_jugador_actual["region"]]["cofres"]["x"]
           datos_partida_actual[datos_jugador_actual["region"]]["cofres"]["y"]
          )
    
    cursor.executemany(sql,val)
    
    save_game(key_primaria_partida) !!!!!!!!!!!
    '''

# -- funciones movimiento --


def actualizar_turnos_restantes_arboles (region_actual):
    for arbol_id, arbol_info in datos_partida_actual[region_actual]["arboles"].items():
        #para los árboles con algún turno para reaparecer
        if arbol_info["turnos_restantes"] >0:
            datos_partida_actual[region_actual]["arboles"][arbol_id]["turnos_restantes"] -=1
            #poner vida de cuatro para el respawn
            if arbol_info["turnos_restantes"] == 0:
                datos_partida_actual[region_actual]["arboles"][arbol_id]["vida"] = 4


def mover_a_objeto(objeto, numero, mapa, xpos, ypos):

    #verificar si la posción en la que va a colocarse está vació o no
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
        #print("busca")
        for i, fila in enumerate(mapa):
            for j, elemento in enumerate(fila):
                #fox
                if objeto == "f" and elemento == "F":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    #print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                #tree
                elif objeto == "t" and elemento == "T":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    #print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                #water
                elif objeto == "water" and elemento == "~":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    #print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                #chest
                elif objeto == "m" and elemento == "M":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    #print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos

                #fire
                elif objeto == "c" and elemento == "C":
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    #print(f"objeto {objeto.upper()} en la posición {xpos},{ypos}")
                    return xpos, ypos


    # LO QUE BUSCA ES UN SANTUARIO
    elif numero.isdigit():
        #print("busca un santuario")
        for i, fila in enumerate(mapa):
            for j, elemento in enumerate(fila):

                #sanctuary
                if objeto == "s" and j+1 < len(fila) and fila[j] == "S" and fila[j+1] == str(numero):
                    xpos, ypos = encontrar_celda_vacia_adyacente(i, j)
                    #print(f"objeto {objeto.upper()}{numero} en la posición {xpos},{ypos}")
                    return xpos, ypos

                #enemy
                elif objeto == "e" and j+1 < len(fila) and fila[j] == "E" and fila[j+1] == int(numero):
                    xpos,ypos = encontrar_celda_vacia_adyacente(i,j)
                    #print(f"objeto {objeto.upper()}{numero} en la posición {xpos},{ypos}")
                    return xpos,ypos

    # NO HA ENCONTRADO NADA
    #print(f"No se encontró el objeto {objeto.upper()}{numero}")
    lista_prompt.append("Invalid option")
    return xpos, ypos


def move_region(region,region_to_go,xpos,ypos):
    global pescar_mapa

    pos_spawn= { #revisar los puntos de spawn
        "hyrule" : (datos_partida_actual["hyrule"]["spawn"]["x"],datos_partida_actual["hyrule"]["spawn"]["y"]),
        "death mountain" : (datos_partida_actual["death mountain"]["spawn"]["x"],datos_partida_actual["death mountain"]["spawn"]["y"]),
        "gerudo" : (datos_partida_actual["gerudo"]["spawn"]["x"],datos_partida_actual["gerudo"]["spawn"]["y"]),
        "necluda" : (datos_partida_actual["necluda"]["spawn"]["x"],datos_partida_actual["necluda"]["spawn"]["y"]),
        "castle" : (datos_partida_actual["castle"]["spawn"]["x"],datos_partida_actual["castle"]["spawn"]["y"])
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
        print(f"You are now in {region_to_go}")
        return nuevas_pos[0], nuevas_pos[1],region


    #puedes cambiar de región
    elif region_to_go in restricciones_tp[region]:
        nuevas_pos = pos_spawn[region_to_go]
        pescar_mapa = True
        datos_partida_actual[datos_jugador_actual["region"]]["fox"][0]["muerto"] = False
        lista_prompt.append(f"You are now in {region_to_go}")

        return nuevas_pos[0], nuevas_pos[1],region_to_go

    elif region_to_go not in pos_spawn:
        lista_prompt.append("Invalid Option")
        return xpos,ypos,region

    #no puedes
    else:
        lista_prompt.append(f"You can't go to {region_to_go} from here")
        return xpos,ypos, region


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
                lista_prompt.append("You can't go there, is not a valid position")
                #print(f"obstáculo en el camino {fila_personaje},{columna_personaje}")
                return fila_anterior, columna_anterior

        # te sales del mapa - la nueva pos está fuera del mapa
        else:
            lista_prompt.append("You can't go there, is not a valid position")
            return fila_anterior, columna_anterior

    # actualizar los puntos restantes de espera de los arboles
    actualizar_turnos_restantes_arboles(datos_jugador_actual["region"])

    # el movimiento es correcto y se puede
    return fila_personaje, columna_personaje


def go_by_the_x(to_do,xpos,ypos):
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
        return xpos,ypos


def go_direction(to_do,xpos,ypos):

    to_do = to_do[3:].lower()

    # la dirección que quiere tomar: left/...
    direction = to_do[:-2]

    # el número de pasos que quiere dar: 2
    steps= to_do[-1]

    #print(direction,"-",steps)

    if not direction.isalpha() or not steps.isdigit():
        lista_prompt.append("Invalid Option")
        return xpos,ypos

    # la orden es correcta
    else:
        steps = int(steps)

        #print(f"steps: {steps}, dirección: {direction}")

        # Mover el jugador
        xpos, ypos = mover_a_direccion(mapa_cargado, xpos, ypos, direction, steps)

        return xpos,ypos



#VARIABLES -------------------
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


# flags importados"
flag_in_game = False
flag_ganon_castle = False


#------------------------------


while True:
    #print(hierba, cocinar, talar, pescar, santuario, cofre,atacar_enemigo, equip, unequip, eat, atacar_general)
    #MAPA
    mapa_cargado = generar_mapa()
    (hierba, cocinar, talar, pescar, santuario, cofre,
     atacar_enemigo, equip, unequip, eat, atacar_general) = permitir_acciones_jugador(mapa_cargado, xpos, ypos)
    print_tablero(mapa_cargado)
    #PROMPT
    prompt(lista_prompt)
    #INPUT
    to_do = input("What to do now?")

    if to_do.lower() == "exit":
        break

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

        # save_game(key_primaria_partida) !!!!!!!!!!!

        if xpos == 8 and ypos == 2:
            flag_in_game = False
            flag_ganon_castle = True

            print(flag_in_game, flag_ganon_castle)

    # orden: GO [DIRECCIÓN]

    elif to_do[0:2].lower() == "go":
        xpos, ypos = go_direction(to_do, xpos, ypos)

    # orden INCORRECTA

    else:
        lista_prompt.append("Incorrect Option")


    actualizar_turnos_restantes_arboles(datos_jugador_actual["region"])

    mapa_cargado = generar_mapa()
    (hierba,cocinar,talar,pescar,santuario,cofre,
     atacar_enemigo,equip,unequip,eat,atacar_general) = permitir_acciones_jugador(mapa_cargado, xpos,ypos)
    print_tablero(mapa_cargado)