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

llista_tirades:list[int] = [0] * (CARES_DAU * 2 - 1)

def generar_histograma() -> None:
    generar_tirades()
    mostrar_histograma()
    mostrar_maximo()

def generar_tirades() -> None:
    i:int = 1

    while i <= CARES_DAU:
        j:int = 1
        while j <= CARES_DAU:
            '''
            El nombre minim es 2, aixi que aquest sera el primer index que trobariem
            Com que les llistes comencen en el 0, aquesta diferencia sera la que
            ens marcara quin es el numero que busquem index 0 es el valor 2
            index 1 es el valor 3
            ...
            index 10 es el valor 12
            '''
            llista_tirades[i + j - 2] += 1
            j += 1
        i += 1

def mostrar_histograma() -> None:
    for i in range(len(llista_tirades)):
        valor_tirada = calcular_valor_tirada(i) 
        print(f"{valor_tirada}:", "*" * llista_tirades[i])

def calcular_valor_tirada(i:int) -> str:
    valor = i + 2 # Explicat en generar_tirades
    if valor < 10:
        valor_tirada = f" {valor}"
    else:
        valor_tirada = f"{valor}"
    return valor_tirada

def mostrar_maximo() -> None:
    valor_tirada = calcular_valor_tirada_mes_repeticions()
    print(f"El maxim es {valor_tirada}.")

def calcular_valor_tirada_mes_repeticions() -> int:
    maxim = 0
    index_maxim_tirades = 0

    for i in range(len(llista_tirades)):
        if llista_tirades[i] > maxim:
            maxim = llista_tirades[i]
            index_maxim_tirades = i
    
    return index_maxim_tirades + 2 # Explicat en generar_tirades


generar_histograma()