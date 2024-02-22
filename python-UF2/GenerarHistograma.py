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
CARES_DAU:int = 6

llista_tirades:list[int] = 0 * (CARES_DAU * 2 - 1)

def generar_histograma() -> None:
    generar_tirades()
    mostrar_histograma()
    mostrar_maximo()

def generar_tirades() -> None:
    i:int = 1

    while i <= CARES_DAU:
        j:int = 1
        while j <= CARES_DAU:
            llista_tirades[i + j - 2] += 1
            j += 1
        i += 1

def mostrar_histograma() -> None:
    for i in range(len(llista_tirades)):
        valor_tirada = calcular_valor_tirada(i)
        print(f"{valor_tirada}:", "*" * llista_tirades[i])

def calcular_valor_tirada(i:int) -> str:
    valor = i + 2
    if valor < 10:
        valor_tirada = f" {valor}"
    else:
        valor_tirada = f"{valor}"
    return valor_tirada

