import random

# HACER SISTEMA QUE DETECTE SI HAY PARTIDAS GUARDADAS


decoracion_personaje_1 = ("         ##    ",
                          "         ##    ",
                          "      ##OOO    ",
                          "     ###OOOO   ",
                          "     ###OOO \  ",
                          "       |@@@| \\ ",
                          "       |   |  \\",
                          "       =   ==  ",
                          "   %%%%%%%%%%%%",
                          "%%%%%%%%%%%%%%%")
decoracion_personaje_2 = ("         &&    ",
                          "        OO &   ",
                          "$       -- &## ",
                          "$$     <<OO####",
                          " $$  //OOO#### ",
                          "  $$// OO##### ",
                          "   ++   OOO### ",
                          "    &   @@@@\  ",
                          "        Q  Q   ",
                          "        Q  Q   ")
decoracion_personaje_3 = ('       &&      ',
                          '      ####     ',
                          '     " || "    ',
                          '  @@@@@@@@@@@@ ',
                          ' @     ||@@@   ',
                          '       |@@@    ',
                          '      @@@      ',
                          '    @@@||     @',
                          ' @@@@@@@@@@@@@ ',
                          '       ||      ')
decoracion_main_menu = (decoracion_personaje_1, decoracion_personaje_2, decoracion_personaje_3)

def print_help_main_menu():
    print("* " + "Help, main menu " + "* " * 31 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'continue' to continue to a saved game".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'new game' to start a new game".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'about' to see information about the game".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'queries' to see the queries".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'exit' to exit the game".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to the 'Main menu'".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Back  " + "* " * 36)


def print_about():
    print("* " + "About " + "* " * 36 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tGame developed by `Team 2, Queremos Calefacción´ :".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tUnax Fernandez".ljust(72) + "* " + "\n" +
          "* " + "\t\tMarta Arévalo".ljust(72) + "* " + "\n" +
          "* " + "\t\tWilliam Sargisson".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to the 'Main menu'".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Back  " + "* " * 36)


def print_new_game():
    print("* " + "New game  " + "* " * 34 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tSet your name ?".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to the 'Main menu'".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Back, Help  " + "* " * 33)

def print_help_new_game():
    print("* " + "Help, new game" + "* " * 32 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tWhen asked, type your name and press enter".ljust(72) + "* " + "\n" +
          "* " + "\t\tif 'Link' is fine for you, just press enter".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tName must be between 3 and 10 characters long and only".ljust(72) + "* " + "\n" +
          "* " + "\t\tletters, numbers and spaces are allowed".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to 'Set your name'".ljust(72) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Back  " + "* " * 36)

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

def print_legend():
    print("* " + "Legend  " + "* " * 35 + "\n" +
          "* " + "\t 10,000 years ago, hyrule was a land of prosperoty thanks to the Sheikah".ljust(75) + "* " + "\n" +
          "* " + "\t tribe. The Sheikah were a tribe of warriors who protected the Triforce,".ljust(75) + "* " + "\n" +
          "* " + "\t a sacred relic that granted wishes.".ljust(75) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t But one day, Ganondorf, an evil sorcerer, stole the Triforce and began ".ljust(75) + "* " + "\n" +
          "* " + "\t to rule Hyrule with an iron fist.".ljust(75) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "\t The princess, with the help of a heroic young man, managed to defeat".ljust(75) + "* " + "\n" +
          "* " + "\t Ganondorf and recover the Triforce.".ljust(75) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Continue  " + "* " * 34)

def print_plot(nombre):
    print("* " + "Plot  " + "* " * 36 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "*" + "  Now history is repeating itself, and Princess Zelda has been captured by".ljust(
        77) + "* " + "\n" +
          "*" + "  Ganon, He has taken over the Guardians and filled Hyrule with monsters.".ljust(
        77) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "*" + f"  But a young man named {nombre} has just awakened and".ljust(77) + "* " + "\n" +
          "*" + "  must reclaim the Guardians to defeat Ganon and save Hyrule".ljust(77) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Continue  " + "* " * 34)


def print_help_inventory():
    print("* " + "Help, inventory " + "* " * 31 + "\n" +
          "* " + "\t\tType 'show inventory main' to show the main inventory".ljust(72) + "* " + "\n" +
          "* " + "\t\t\t (main, weapons, Food)".ljust(69) + "* " + "\n" +
          "* " + "\t\tType 'eat X' to eat X, where X is a food item".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'cook X' to cook X, where X is a food item".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'equip X' to equip X, where X is a weapon".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'unequip X' to unequip X, where X is a weapon".ljust(72) + "* " + "\n" +
          "* " + "\t\tType 'back' now to go back to the 'Game'".ljust(72) + "* " + "\n" +
          "* " + "Back  " + "* " * 36)


def print_personaje_death(nombre):
    titulo = f"* {nombre} death "
    calculo = int(((80 - len(titulo)) / 2))
    if len(titulo) % 2 != 0:
        print(titulo + " " + "* " * calculo)
    else:
        print(titulo + "* " * calculo)
    print("* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "*" + "\tGame Over.".ljust(75) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Continue  " + "* " * 34)


def print_zelda_saved(nombre):
    print("* " + "Zelda saved " + "* " * 33 + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "*" + f"\t Congratulations, {nombre} has saved Princess Zelda".ljust(75) + "* " + "\n" +
          "*" + "\t Thanks for playing!".ljust(75) + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + " " * 76 + "* " + "\n" +
          "* " + "Continue  " + "* " * 34)
