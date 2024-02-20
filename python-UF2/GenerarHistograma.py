"""
Feu un programa anomenat GenerarHistograma que mostri l’histograma de totes les tirades possibles amb dos daus de sis cares. 

Per fer això, l’estratègia que s’ha considerat és desar dins d’un  el nombre de repeticions de cada tirada possible (sempre entre 2 i 12) i després treballar a partir d’aquests valors. 

A continuació, ha de dir quin valor de tirada és el que té més repeticions. 

A mode de guia, la sortida hauria de ser semblant a la que es mostra tot seguit:

 2: * 
 3: ** 
 4: *** 
 5: **** 
 6: ***** 
 7: ****** 
 8: ***** 
 9: **** 
10: *** 
11: ** 
12: * 
El màxim és 7.

"""

"""
TOP DOWN

1. 
"""

fi = False
repeticions = [0] * 13
combinacions = []

def inicio():
    while not fi:
        mostrar_menu()
        tratar_opcion()

def mostrar_menu():
    print("Benvingut a HISTOGRAMA")
    print("-------------------------------------")
    print("[IF] HISTOGRAMA.")
    print("[FI] Sortir")

def tratar_opcion():
    frase = input("Opciones: ")
    if frase.casefold() == "IF".casefold():
        numero_de_repes()
    elif frase.casefold() == "FI".casefold():
        finalizar_ejecucion()
    else:
        print("\nOpcion incorrecta.\n")

def contar_combinaciones():
    global repeticions
    repeticions = [0] * 13
    for tirada in combinacions:
        suma = tirada[0] + tirada[1]
        repeticions[suma - 2] += 1

def finalizar_ejecucion():
    global fi
    fi = True

inicio()