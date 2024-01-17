lista_prompt = []


def prompt(lista):
    lista = lista[-8:]
    for elemento in lista:
        print(elemento)


lista_prompt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 91, 2, 6, 7, 8, 9]

prompt(lista_prompt)
lista_prompt.append("polla")
prompt(lista_prompt)