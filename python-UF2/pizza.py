'''
Imagineu-vos que heu estat contractats per dissenyar el sistema de gestió d'una pizzeria. 
l'objectiu és desenvolupar un conjunt de funcions que permetin gestionar diferents tasques relacionades amb el funcionament de la pizzeria. Això inclou la presa de comandes, la preparació de pizzes, la gestió de l'estoc d'ingredients i el processament dels pagaments.
Recordeu fer servir disseny top down, i mantenir un baix acoblament i una alta cohesió.
'''

COMANDA = 1
PREPARACIO = 2
ESTOC = 3
PAGAMENT = 4
SALIR = 5

pizza = []
fin_programa= False

while not fin_programa:

    print("\nAccions disponibles:")
    print(str(COMANDA) + ". Ingredients")
    print(str(PREPARACIO) + ". Eliminar un ingrediente")
    print(str(ESTOC) + ". Llista de tots els ingredients en estoc")
    print(str(PAGAMENT) + ". efectiu o tarjeta")
    print(str(SALIR) + ". Sortir")
    Opcion = int(input("Escull una opció (1-5): "))
    
    def LACOMANDA():
    pizza = int(input(" Que pizza vols?: 1. Pizza 4 quesos, 2. pizza carbonara, 3. pizza vegetal"))     
    if pizza == 1:
        print("Els ingredients de " + pizza + " son:")

    print(LACOMANDA)