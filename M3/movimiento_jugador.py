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
    datos_jugador["items_equipados"] = []
    return datos_jugador

info_alimento_partida = importar_datos_comida_sin_modificaciones()
info_equipamiento_partida = importar_datos_armas_sin_modificaciones()
datos_jugador_actual = importar_datos_jugador_sin_modificaciones()
datos_partida_actual = importar_datos_partida_sin_modificaciones()
#print(datos_partida_actual)

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


def print_tablero(mapa): # hace print del tablero
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



#FUNCIONES ------------

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


# -------

#VARIABLES -------------------
xpos = 4
ypos = 5

pescar_mapa = True

#------------------------------


# flags importados"
flag_in_game = False
flag_ganon_castle = False

#---------------

lista_prompt = []

def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)

#------------------------------

while True:
    #MAPA
    mapa_cargado = generar_mapa()
    print_tablero(mapa_cargado)
    #PROMPT
    prompt(lista_prompt)

    # INPUT

    to_do = input("What to do know?") #esto será un input

    if to_do.lower() == "exit":
        break

    # orden: GO BY THE [f,t,water,sX,eX,m,c]

    if to_do[0:9].lower() == "go by the":
        xpos,ypos = go_by_the_x(to_do,xpos,ypos)

    # ordern: GO TO [REGION]

    elif to_do[0:5].lower() == "go to":
        region_to_go = to_do[6:].lower()

        xpos,ypos,datos_jugador_actual["region"] = move_region(datos_jugador_actual["region"],region_to_go,xpos,ypos)

        # save_game(key_primaria_partida) !!!!!!!!!!!

        if xpos == 8 and ypos == 2:
            flag_in_game = False
            flag_ganon_castle = True

            print(flag_in_game,flag_ganon_castle)

    # orden: GO [DIRECCIÓN]

    elif to_do[0:2].lower() == "go":
        xpos,ypos = go_direction(to_do,xpos,ypos)

    else:
        lista_prompt.append("Invalid Option")


    actualizar_turnos_restantes_arboles(datos_jugador_actual["region"])


    mapa_cargado = generar_mapa()
    print_tablero(mapa_cargado)