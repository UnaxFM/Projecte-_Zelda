import random
frases_ganon = ("Ganon is powerful, are you sure you can defeat him?",
                "Ganon's strength is supernatural, Zelda fought with bravery.",
                "To Ganon, you are like a fly, find a weak spot and attack.",
                "Ganon will not surrender easily.",
                "Ganon has fought great battles, is an expert fighter.",
                "Link, transform your fears into strengths.",
                "Keep it up, Link, Ganon can't hold out much longer.",
                "Link, history repeats itself, Ganon can be defeated.",
                "Think of all the warriors who have tried before.",
                "You fight for the weaker ones, Link, persevere.")

print(frases_ganon[random.randrange(0, len(frases_ganon))])
print("* " * 30)
print("* " + "Castle  " + "*" * 25)
mapa_ganon = \
    [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", "\\", " ", "/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "G", "a", "n", "o", "n", " ", f"{'♥'* 8}".ljust(8), " ", " "],
    [" ", " ", " ", " ", " ", " ", "-", "-", " ", "o", " ", "-", "-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", "/", " ", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", ">", " ", " ", "V", " ", "V", "-", "V", "-", "V", " ", " ", " ", "|", ">", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ",", " ", " ", " ", ",", " ", " ", "/", "_", "\\", " ", " ", "|", " ", " ", " ", " ", " ", "|", " ", " ", "/", "_", "\\", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", "\\", "_", "/", "|", " ", " ", "|", " ", "|", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "|", " ", "|", "'", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "(", "q", " ", "p", ")", ",", "-", "|", " ", "|", " ", "|", "|", " ", " ", "_", " ", " ", "|", "|", " ", "|", " ", "|", " ", " ", "·", "_", " ", " ", "|", "\\", " ", " ", " ", " "],
    ["O", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\\", "_", "/", "_", "(", "/", "|", " ", "|", " ", " ", " ", " ", "|", "#", "|", " ", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", "'", "-", "/", "/", " ", " ", " ", " "],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O","O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O","O", "O", "O", "O", "O", "O", "O", "O", "O"]]

for lista in mapa_ganon:
    print("*", end="")
    for elemento in lista:
        print(elemento, end="")
    print("* ")
print("* " * 30)

#
""" FORMA DE GENERAR EL MAPA
mapa_a_cargar = []
for fila in localizaciones[informacion_jugador["region"]]:
    fila_mapa_a_cargar = []
    for elemento in fila:
        fila_mapa_a_cargar.append(elemento)
    mapa_a_cargar.append(fila_mapa_a_cargar)
"""