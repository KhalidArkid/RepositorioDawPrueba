'''
Imagineu-vos que heu estat contractats per dissenyar el sistema de gestió d'una pizzeria. 
L'objectiu és desenvolupar un conjunt de funcions que permetin gestionar diferents tasques relacionades amb el funcionament de la pizzeria. Això inclou la presa de comandes, la preparació de pizzes, la gestió de l'estoc d'ingredients i el processament dels pagaments.
Recordeu fer servir disseny top down, i mantenir un baix acoblament i una alta cohesió.
'''

COMANDA = 1
ELIMINAR = 2
LLISTAR = 3
SALIR = 4

Pizza = []
nombre = ""
fin_programa = False

while fin_programa == False:

    def Comanda():
        print("\nAccions disponibles:")
        print(COMANDA + ". Ingredients")
        print(ELIMINAR + ". Eliminar un ingrediente")
        print(LLISTAR + ". Llista de tots els ingredients")
        print(SALIR + ". Sortir")
adas