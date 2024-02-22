"""
Feu un programa anomenat CalculTirada que calculi la probabilitat en tant per cent de treure per sota d’un valor concret tirant dos daus de sis cares. 

Per fer això, l’estratègia que s’ha considerat és desar dins d’un  el nombre de repeticions de cada tirada possible (sempre entre 2 i 12) i després treballar a partir d’aquests valors, sabent que:

    Probabilitat de treure 2: suma del nombre de tirades que valen 2 * 100 / 36.
    Probabilitat de treure 3 o menys: suma del nombre de tirades que valen 2 o 3 * 100 / 36.
    Probabilitat de treure 4 o menys: suma del nombre de tirades que valen 2 o 3 o 4 * 100 / 36.
    etc.

Es parteix de la descomposició del problema següent, que haureu de seguir per codificar-lo:

    Llegir el valor.
    Processar entrada pel teclat.
    Comprovar si està entre 2 i 12.

Generar tirades.Calcular probabilitat.
A mode de guia, la sortida hauria de ser més o menys com es mostra tot seguit:

Escriu el valor a calcular [2 - 12]. 
18 
El valor no és entre 2 i 12. 
5 
La probabilitat es 27.0%.
"""

'''
TOP DOWN:

1. Calcular_Tirada
2. 
'''
    
def Calcular_Tirada():
    valor = int(input("Escribe el valor a calcular [2 - 12]: "))
    
    if valor < 2 or valor > 12:
        print("El valor no és entre 2 y 12.")
        return
    
    num_tiradas = 0
    
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 <= valor:
                num_tiradas += 1
    
    probabilidad = num_tiradas * 100 / 36
    
    print("La probabilidad és", probabilidad, "%.")

Calcular_Tirada()
