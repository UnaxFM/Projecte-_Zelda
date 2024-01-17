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

equipped_sword = None
equipped_shield = None



flag_help_inventory = """
Comandes disponibles:
- show inventory main: Mostra l'inventari principal.
- show inventory weapons: Mostra l'inventari d'armes.
- show inventory food: Mostra l'inventari d'aliments.
- eat <food_type>: Menja un tipus d'aliment.
- cook <dish_type>: Cuina un tipus de plat.
- open sanctuary: Obre un santuari per augmentar la capacitat màxima de cors.
- show inventory help: Mostra aquesta ajuda.
"""

def menu_inventario(matriz_mapa, matriz_inventario,tipo_inventario):
    titulo = datos_jugador_actual["region"] + " "
    calculo = int(((60 - len(titulo)) / 2) - 1)
    titulo_2 = ["Inventory", "Weapons", "Food"]
    if tipo_inventario == "show inventory main":
        titulo_2 = titulo_2[0]
    elif tipo_inventario == "show inventory weapons":
        titulo_2 = titulo_2[1]
    elif tipo_inventario == "show inventory food":
        titulo_2 = titulo_2[2]
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        return
    if len(titulo) % 2 != 0:
        print("* " + titulo + " " + "* " * calculo, end="")
    else:
        print("* " + titulo + "* " * calculo, end="")
    calculo_2 = int((17 - len(titulo_2)) // 2)
    if len(titulo_2) % 2 != 0:
        print("* " * calculo_2 + titulo_2 + " * ")
    else:
        print("* " * calculo_2 + " " + titulo_2 + " * ")

    for i in range(len(matriz_mapa)):
        print("*", end="")
        for elemento in matriz_mapa[i]:
            print(elemento, end="")
        print("", end="")
        for elemento2 in matriz_inventario[i]:
            print(elemento2, end="")
        print("*")

    print("* " * 40)


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
    #mapa[xpos][ypos]
    mapa_a_cargar[4][5] = "X"
    return mapa_a_cargar

mapa_cargado = generar_mapa()

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
"""

lista_prompt = []
def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)

def generar_inventory(info_alimento_partida,datos_jugador_actual,info_equipamiento_partida):
    suma_comida = 0
    for alimento in info_alimento_partida:
        suma_comida += info_alimento_partida[alimento]["cantidad"]
    suma_equip = 0
    for armamento in info_equipamiento_partida:
        suma_equip += info_equipamiento_partida[armamento]["cantidad"]

    return [
        [f"* {datos_jugador_actual['nombre']:<10} ❤ {datos_jugador_actual['vida_actual']}/{datos_jugador_actual['vida_total']} "],
        [f"* Blood moon in {datos_jugador_actual['blood_moon_appearances']:>3} "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["* Equipment:" + " " * 8],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [f"* Food {suma_comida:>12} "],
        [f"* Weapons {suma_equip:>9} "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
    ]

# Example usage
inventory = generar_inventory(info_alimento_partida,datos_jugador_actual,info_equipamiento_partida)

def generar_weapons(info_equipamiento_partida):

    return [
    ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
    ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
    [f"* Wood sword {info_equipamiento_partida['wood sword']['usos']:>4}/{info_equipamiento_partida['wood sword']['cantidad']:<2}"],
    [f"* {'Equipado' if info_equipamiento_partida['wood sword']['equipado'] else '        '}          " ],
    [f"* Sword {info_equipamiento_partida['sword']['usos']:>9}/{info_equipamiento_partida['sword']['cantidad']:<2}"],
    [f"* {'Equipado' if info_equipamiento_partida['sword']['equipado'] else '        '}          " ],
    [f"* Wood shield {info_equipamiento_partida['wood shield']['usos']:>3}/{info_equipamiento_partida['wood shield']['cantidad']:<2}"],
    [f"* {'Equipado' if info_equipamiento_partida['wood shield']['equipado'] else '        '}          " ],
    [f"* Shield {info_equipamiento_partida['shield']['usos']:>8}/{info_equipamiento_partida['shield']['cantidad']:<2}"],
    [f"* {'Equipado' if info_equipamiento_partida['shield']['equipado'] else '        '}          " ],
]

# Example usage
weapons_inventory = generar_weapons(info_equipamiento_partida)

# equip sword
# show inventory weapons

def equip_weapon(weapon_name):
    global equipped_sword, equipped_shield

    if weapon_name in info_equipamiento_partida and not info_equipamiento_partida[weapon_name]["equipado"]:
        if "sword" in weapon_name and equipped_sword is not None:
            lista_prompt.append(f"You already have {equipped_sword} equipped.")
        elif "shield" in weapon_name and equipped_shield is not None:
            lista_prompt.append(f"You already have {equipped_shield} equipped.")
        else:
            info_equipamiento_partida[weapon_name]["equipado"] = True
            lista_prompt.append(f"{weapon_name} equipped.")
            if "sword" in weapon_name:
                equipped_sword = weapon_name
            elif "shield" in weapon_name:
                equipped_shield = weapon_name
    else:
        lista_prompt.append(f"You don't have {weapon_name}.")

def unequip_weapon(weapon_name):
    global equipped_sword, equipped_shield

    if weapon_name in info_equipamiento_partida and info_equipamiento_partida[weapon_name]["equipado"]:
        info_equipamiento_partida[weapon_name]["equipado"] = False
        lista_prompt.append(f"{weapon_name} unequipped.")
        if "sword" in weapon_name:
            equipped_sword = None
        elif "shield" in weapon_name:
            equipped_shield = None
    else:
        lista_prompt.append(f"You don't have {weapon_name} equipped.")

def generar_food_inventory(info_alimento_partida):
    return [
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
        [f"* Vegetables {info_alimento_partida['vegetables']['cantidad']:>6} "],
        [f"* Fish {info_alimento_partida['fish']['cantidad']:>12} "],
        [f"* Meat {info_alimento_partida['meat']['cantidad']:>12} "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [f"* Salads {info_alimento_partida['salads']['cantidad']:>10} "],
        [f"* Pescatarian {info_alimento_partida['pescatarian']['cantidad']:>5} "],
        [f"* Roasted {info_alimento_partida['roasted']['cantidad']:>9} "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]
    ]
food_inventory = generar_food_inventory(info_alimento_partida)

def comer(opcion, informacion_jugador, info_alimento_partida, inventory):
    if opcion == "vegetables":
        if info_alimento_partida["vegetables"]["cantidad"] > 0:
            # Aumenta la vida actual
            informacion_jugador["vida_actual"] += 1
            # Disminuye la cantidad de comida
            info_alimento_partida["vegetables"]["cantidad"] -= 1
            # Asegúrate de que la vida actual no exceda la vida total
            if informacion_jugador["vida_actual"] > informacion_jugador["vida_total"]:
                informacion_jugador["vida_actual"] = informacion_jugador["vida_total"]
            lista_prompt.append("Has comido vegetales.")
        elif info_alimento_partida["vegetables"]["cantidad"] <= 0:
            lista_prompt.append("Not enough 1 vegetable")
    elif opcion == "salads":
        if info_alimento_partida["salads"]["cantidad"] > 0:
            # Aumenta la vida actual
            informacion_jugador["vida_actual"] += 2
            # Disminuye la cantidad de comida
            info_alimento_partida["salads"]["cantidad"] -= 1
            # Asegúrate de que la vida actual no exceda la vida total
            if informacion_jugador["vida_actual"] > informacion_jugador["vida_total"]:
                informacion_jugador["vida_actual"] = informacion_jugador["vida_total"]
            lista_prompt.append("Has comido salads.")
        elif info_alimento_partida["salads"]["cantidad"] <= 0:
            lista_prompt.append("Not enough 1 salads")
    elif opcion == "pescatarian":
        if info_alimento_partida["pescatarian"]["cantidad"] > 0:
            # Aumenta la vida actual
            informacion_jugador["vida_actual"] += 3
            # Disminuye la cantidad de comida
            info_alimento_partida["pescatarian"]["cantidad"] -= 1
            # Asegúrate de que la vida actual no exceda la vida total
            if informacion_jugador["vida_actual"] > informacion_jugador["vida_total"]:
                informacion_jugador["vida_actual"] = informacion_jugador["vida_total"]
            lista_prompt.append("Has comido pescatarian.")
        elif info_alimento_partida["pescatarian"]["cantidad"] <= 0:
            lista_prompt.append("Not enough 1 pescatarian")
    elif opcion == "roasted":
        if info_alimento_partida["roasted"]["cantidad"] > 0:
            # Aumenta la vida actual
            informacion_jugador["vida_actual"] += 4
            # Disminuye la cantidad de comida
            info_alimento_partida["roasted"]["cantidad"] -= 1
            # Asegúrate de que la vida actual no exceda la vida total
            if informacion_jugador["vida_actual"] > informacion_jugador["vida_total"]:
                informacion_jugador["vida_actual"] = informacion_jugador["vida_total"]
            lista_prompt.append("Has comido alimentos roasted.")
        elif info_alimento_partida["roasted"]["cantidad"] <= 0:
            lista_prompt.append("Not enough 1 roasted")
    else:
        lista_prompt.append("Invalid opcion ")

    # Actualiza la información del jugador en el inventario principal
    inventory[0][0] = f"* {informacion_jugador['nombre']:<10} ❤ {informacion_jugador['vida_actual']}/{informacion_jugador['vida_total']} "

    return inventory

def cocinar(opcion, informacion_jugador, info_alimento_partida, inventory):
    if opcion == "salad":
        if info_alimento_partida["vegetables"]["cantidad"] >= 2:
            # Disminuye un vegetal
            info_alimento_partida["vegetables"]["cantidad"] -= 1
            # Aumenta una ensalada
            info_alimento_partida["salads"]["cantidad"] += 1
            lista_prompt.append("Has cocinado una ensalada.")
        elif info_alimento_partida["vegetables"]["cantidad"] == 0:
            lista_prompt.append("Not enough 2 vegetables")
        elif info_alimento_partida["vegetables"]["cantidad"] == 1:
            lista_prompt.append("Not enough 1 vegetable")
    elif opcion == "pescatarian":
        if info_alimento_partida["vegetables"]["cantidad"] > 0 and info_alimento_partida["fish"]["cantidad"] > 0:
            # Disminuye un vegetal y un pez
            info_alimento_partida["vegetables"]["cantidad"] -= 1
            info_alimento_partida["fish"]["cantidad"] -= 1
            # Aumenta un pescatarian
            info_alimento_partida["pescatarian"]["cantidad"] += 1
            lista_prompt.append("Has cocinado un plato pescatariano.")
        elif info_alimento_partida["vegetables"]["cantidad"] < 1 and info_alimento_partida["fish"]["cantidad"] < 1:
            lista_prompt.append("Not enough 1 vegetable and 1 fish  ")
        elif info_alimento_partida["vegetables"]["cantidad"] < 1 and info_alimento_partida["fish"]["cantidad"] >= 1:
            lista_prompt.append("Not enough 1 vegetable ")
        elif info_alimento_partida["vegetables"]["cantidad"] >= 1 and info_alimento_partida["fish"]["cantidad"] < 1:
            lista_prompt.append("Not enough 1 fish ")
    elif opcion == "roasted":
        if info_alimento_partida["vegetables"]["cantidad"] > 0 and info_alimento_partida["meat"]["cantidad"] > 0:
            # Disminuye un vegetal y una carne
            info_alimento_partida["vegetables"]["cantidad"] -= 1
            info_alimento_partida["meat"]["cantidad"] -= 1
            # Aumenta un plato asado
            info_alimento_partida["roasted"]["cantidad"] += 1
            lista_prompt.append("Has cocinado un plato asado. ")
        elif info_alimento_partida["vegetables"]["cantidad"] < 1 and info_alimento_partida["meat"]["cantidad"] < 1:
            lista_prompt.append("Not enough 1 vegetable and 1 meat  ")
        elif info_alimento_partida["vegetables"]["cantidad"] < 1 and info_alimento_partida["meat"]["cantidad"] >= 1:
            lista_prompt.append("Not enough 1 vegetable ")
        elif info_alimento_partida["vegetables"]["cantidad"] >= 1 and info_alimento_partida["meat"]["cantidad"] < 1:
            lista_prompt.append("Not enough 1 meat ")
    else:
        lista_prompt.append("Invalid opcion ")

    # Actualiza la información del jugador en el inventario principal
    inventory[0][0] = f"* {informacion_jugador['nombre']:<10} ❤ {informacion_jugador['vida_actual']}/{informacion_jugador['vida_total']} "

    return inventory


def aplicar_truco(cheat, datos_jugador, info_alimento_partida, inventory, food_inventory, datos_partida_actual):
    cheat_parts = cheat.split()
    cheat_name = cheat_parts[1].lower() if len(cheat_parts) > 1 else None

    if cheat_name == "rename":
        if len(cheat_parts) == 5 and cheat_parts[3].lower() == "to":
            nuevo_nombre = cheat_parts[4].strip('"')
            if 3 <= len(nuevo_nombre) <= 10 and nuevo_nombre.isalnum() or " " in nuevo_nombre:
                datos_jugador["nombre"] = nuevo_nombre
                lista_prompt.append(f"Cheating: rename player to '{nuevo_nombre}'.")
                # Actualiza el nombre del jugador en el inventario principal
                inventory[0][0] = f"* {nuevo_nombre:<10} ❤ {datos_jugador['vida_actual']}/{datos_jugador['vida_total']} "
            else:
                print("Invalid new name. Must be between 3 and 10 characters and contain only letters, numbers, or spaces.")
        else:
            lista_prompt.append("Invalid command.")

    elif cheat_name == "add":
        if len(cheat_parts) == 3:
            item_name = cheat_parts[2].lower()
            if item_name == "vegetables":
                info_alimento_partida[item_name]["cantidad"] += 1
                lista_prompt.append("Cheating: vegetables:")
            elif item_name == "fish":
                info_alimento_partida[item_name]["cantidad"] += 1
                lista_prompt.append("Cheating: fisht:")
            elif item_name == "meat":
                info_alimento_partida[item_name]["cantidad"] += 1
                lista_prompt.append("Cheating: meat:")
            else:
                print(f"Invalid item '{item_name}'.")
        else:
            lista_prompt.append("Invalid command.")

    elif cheat_name == "cook":
        if len(cheat_parts) == 3:
            dish_name = cheat_parts[2].lower()
            if dish_name in ["salad", "pescatarian", "roasted"]:
                if dish_name == "salad" and info_alimento_partida["vegetables"]["cantidad"] >= 2:
                    info_alimento_partida["vegetables"]["cantidad"] -= 2
                    info_alimento_partida["salads"]["cantidad"] += 1
                    lista_prompt.append("Cheating: cook salad:")
                elif dish_name == "pescatarian" and info_alimento_partida["vegetables"]["cantidad"] >= 1 and \
                        info_alimento_partida["fish"]["cantidad"] >= 1:
                    info_alimento_partida["vegetables"]["cantidad"] -= 1
                    info_alimento_partida["fish"]["cantidad"] -= 1
                    info_alimento_partida["pescatarian"]["cantidad"] += 1
                    lista_prompt.append("Cheating: cook pescatarian")
                elif dish_name == "roasted" and info_alimento_partida["vegetables"]["cantidad"] >= 1 and \
                        info_alimento_partida["meat"]["cantidad"] >= 1:
                    info_alimento_partida["vegetables"]["cantidad"] -= 1
                    info_alimento_partida["meat"]["cantidad"] -= 1
                    info_alimento_partida["roasted"]["cantidad"] += 1
                    lista_prompt.append("Cheating: cook roasted")
                else:
                    print(f"Not enough ingredients to cook {dish_name}.")
            else:
                print(f"Invalid dish '{dish_name}'.")
        else:
            lista_prompt.append("Invalid command.")

    elif cheat_name == "open" and cheat_parts[2].lower() == "sanctuaries":
        # Aumenta el límite de corazones a 9 si no supera ese valor
        if datos_jugador["vida_total"] < 10:
            datos_jugador["vida_total"] = 10
            lista_prompt.append("Cheating: open sanctuaries")
            # Actualiza la información del jugador en el inventario principal
            inventory[0][0] = f"* {datos_jugador['nombre']:<10} ❤ {datos_jugador['vida_actual']}/{datos_jugador['vida_total']} "
            # Abre todos los santuarios
            lugares = ["hyrule", "death mountain", "necluda", "gerudo"]
            for lugar in lugares:
                for santuario in datos_partida_actual[lugar]["santuarios"]:
                    datos_partida_actual[lugar]["santuarios"][santuario]["descubierto"] = True
        else:
            print("You have already opened sanctuaries. Your maximum heart capacity is already 10.")
    elif cheat_name == "game" and cheat_parts[2].lower() == "over":
        datos_jugador["vida_actual"] = 0
        lista_prompt.append("Cheating: game over")
    elif cheat_name == "win" and cheat_parts[2].lower() == "game":
        datos_partida_actual["castle"][0]["vida"]=0
        # save_game(key_primaria_partida)
        lista_prompt.append("Cheating: win game")

    else:
        lista_prompt.append("Invalid command.")

    return datos_jugador, info_alimento_partida, inventory, food_inventory

def mostrar_inventario(opcion, informacion_jugador, inventory, food_inventory):
    opcion = opcion.lower()

    # Decrementar el contador de blood_moon_countdown por cada acción
    informacion_jugador["blood_moon_countdown"] -= 1

    # Lógica para el blood moon
    if informacion_jugador["blood_moon_countdown"] == 0:
        informacion_jugador["blood_moon_countdown"] = 25
        informacion_jugador["blood_moon_appearances"] += 1
        lista_prompt.append("The Blood moon rises once again. Please be careful, Link")

    # Actualizar el valor en el inventario principal
    inventory[1][0] = f"* Blood moon in {informacion_jugador['blood_moon_countdown']:>3} "

    if opcion == "show inventory main":
        imprimir_todo(mapa_cargado, inventory)
    elif opcion == "show inventory weapons":
        imprimir_todo(mapa_cargado, weapons_inventory)
    elif opcion == "show inventory food":
        imprimir_todo(mapa_cargado, food_inventory)
    elif opcion == "chea add wood sword":
        info_equipamiento_partida['wood sword']['cantidad']+= 1
    elif opcion == "chea add sword":
        info_equipamiento_partida['sword']['cantidad']+= 1
    elif opcion == "chea add wood shield":
        info_equipamiento_partida['wood shield']['cantidad']+= 1
    elif opcion == "chea add shield":
        info_equipamiento_partida['shield']['cantidad']+= 1
    elif opcion.startswith("eat "):
        comida_opcion = opcion[4:]
        if comida_opcion in info_alimento_partida:
            # Actualiza el inventario principal después de comer
            inventory = comer(comida_opcion, informacion_jugador, info_alimento_partida, inventory)
            food_inventory = generar_food_inventory(info_alimento_partida)
        else:
            lista_prompt.append("Invalid command.")
    elif opcion.startswith("cook "):
    # elif opcion.startswith("cook ") and cocinar == True: usar esta para que funcione con lo de Marta
        cocina_opcion = opcion[5:]
        if cocina_opcion in ["salad", "pescatarian", "roasted"]:
            # Actualiza el inventario principal después de cocinar
            inventory = cocinar(cocina_opcion, informacion_jugador, info_alimento_partida, inventory)
            food_inventory = generar_food_inventory(info_alimento_partida)
        else:
            lista_prompt.append("Invalid command.")
    elif opcion.lower() == 'show inventory help':
        print(flag_help_inventory)
    elif to_do.startswith('equip'):
        weapon_to_equip = to_do.split(' ', 1)[1]
        equip_weapon(weapon_to_equip)
    elif to_do.startswith('unequip'):
        weapon_to_unequip = to_do.split(' ', 1)[1]
        unequip_weapon(weapon_to_unequip)

    else:
        lista_prompt.append("Invalid command.")

    return inventory, food_inventory


def imprimir_todo(region,tipo_inventario):
    menu_inventario(region,tipo_inventario,to_do)


while True:
    to_do = input("What to do now? ")

    if to_do.lower() == 'exit':
        break
    elif to_do.startswith('cheat'):
        datos_jugador_actual, info_alimento_partida, inventory, food_inventory = aplicar_truco(to_do, datos_jugador_actual, info_alimento_partida, inventory, food_inventory, datos_partida_actual)
        prompt(lista_prompt)
    else:
        inventory, food_inventory = mostrar_inventario(to_do, datos_jugador_actual, inventory, food_inventory)
        print(info_equipamiento_partida, lista_prompt)



# eat pescatarian

# show inventory main
