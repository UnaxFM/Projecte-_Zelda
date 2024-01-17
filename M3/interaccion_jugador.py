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
print(datos_jugador_actual)

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


#FUNCIONES --------------------

def verificar_alrededor(matriz, fila, columna):
    # guardar elementos
    alrededor = []

    #3x3 alrededor del jugador
    for i in range(fila - 1, fila + 2): #-1,0,1: range(-1,2)
        for j in range(columna - 1, columna + 2): #-1,0,1 rrange(-1,2)
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
    #print(datos_partida_actual[datos_jugador_actual["region"]]["santuarios"])

    id_santuario_adyacente = obter_id_objeto_adyacente(datos_partida_actual[datos_jugador_actual["region"]]["santuarios"])

    print(f"Santuario {id_santuario_adyacente} es el de al lado")

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

        # save_game(key_primaria_partida) !!!!!!!!!!!


def open_chest():
    #localizar cofre y ponerlo a true
    id_cofre_adyacente = obter_id_objeto_adyacente(
        datos_partida_actual[datos_jugador_actual["region"]]["cofres"])

    print(f"Cofre {id_cofre_adyacente} es el de al lado")

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

    # save_game(key_primaria_partida) !!!!!!!!!!!

#VARIABLES -------------------
xpos = 4
ypos = 34

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

#------------------------------

lista_prompt = []

def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)

#------------------------------


while True:
    print(hierba, cocinar, talar, pescar, santuario, cofre,atacar_enemigo, equip, unequip, eat, atacar_general)
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

    elif to_do.lower() == "attack" and hierba and ("wood sword" in datos_jugador_actual["items_equipados"] or "sword" in datos_jugador_actual["items_equipados"]):
        attack_grass()

    # order: FISH

    elif to_do.lower() == "fish" and pescar and pescar_mapa:
        fish()

    # orden: OPEN

    elif to_do.lower() == "open sanctuary" and santuario:
        open_sacntuary()

    elif to_do.lower() == "open chest" and cofre:
        open_chest()

    # orden INCORRECTA

    else:
        lista_prompt.append("Incorrect Option")

    mapa_cargado = generar_mapa()
    (hierba,cocinar,talar,pescar,santuario,cofre,
     atacar_enemigo,equip,unequip,eat,atacar_general) = permitir_acciones_jugador(mapa_cargado, xpos,ypos)
    print_tablero(mapa_cargado)