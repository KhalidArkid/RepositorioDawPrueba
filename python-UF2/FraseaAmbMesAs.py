"""
Feu un programa anomenat FraseAmbMesAs que vagi llegint frases pel teclat i, en acabar cada entrada d’una frase, mostri quina és la frase que s’ha escrit fins al moment amb més lletres ‘a’ (minúscula o majúscula) i quantes en tenia. 

El programa ha d’anar-se executant fins a llegir la frase “fi”. 

A mode de guia de sortida hauria de ser semblant a la que es mostra tot seguit.
"""

"""
Escriu una frase:> Hola que tal
La frase amb més 'a' és: "Hola què tal"
Té 2 'a'.
Escriu una frase:
> Aquesta té més 'a'
La frase amb més 'a' és: "Aquesta té més a"
Té 3 'a'.
Escriu una frase:
> Menys 'a'
La frase amb més 'a' és: "Aquesta té més a"
Té 3 'a'.
Escriu una frase:
> fi
La frase amb més 'a' és: "Aquesta té més a"
Té 3 'a'.
(El programa acaba)
"""


#TOP DOWN

"""
Me fumé el Top Down, lo tenia ya en la cabeza, lo adjunto ahora:

0. Creacion de un menu
    0.1 Menu con opciones para mas comodidad
1. Gestion de texto
    1.1 Recibir lo que introduce el usuario
2. Calculo de los As
    2.1 Formular una equacion que pueda identificar las 'a'
3. Ejecutador de salida
"""

max_de_AS = 0
frase_max = ""
fi = False

# Problema general
def inicio():
    while not fi:
        mostrar_menu()
        tratar_opcion()

# Primer nivel de descomposicion
def mostrar_menu():
    print("Benvingut a FraseAmbMesAs")
    print("-------------------------------------")
    print("[IF] Introduir frase.")
    print("[FI] Sortir")

def tratar_opcion():
    frase = input("Opciones: ")
    if frase.casefold() == "IF".casefold():
        poner_la_frase()
    elif frase.casefold() == "FI".casefold():
        finalizar_ejecucion()
    else:
        print("\nOpcion incorrecta.\n")

def poner_la_frase():
    poner = input("\nEscribe una frase: ").lower()
    calcular_AS(poner)

def calcular_AS(frase, max_de_AS=0):
    AS = frase.count('a')
    if AS > max_de_AS:
        max_de_AS = AS
        frase_max = frase
    print(f"\nLa frase {frase_max}: ")
    print(f"Té {max_de_AS} 'a'.\n")
    return max_de_AS

def finalizar_ejecucion():
    global fi
    fi = True

inicio()

# (FALTA CORRECION POR NO ENTENDER BIEN LO QUE ME PEDIA LA TASCA, HE PUESTO UN CONTADOR DE "AS" PERO NO UN COMPARADOR DE QUIEN TIENE MÁS "AS")