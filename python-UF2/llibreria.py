AFEGIR = 1
MOSTRAR = 2
ELIMINAR = 3
SORTIR  = 4

llibreria = {}
fin_programa = False

while not fin_programa:
    print("\nAccions disponibles:")
    print(str(AFEGIR) + ". Afegir un llibre")
    print(str(MOSTRAR) + ". Mostrar llista dels llibres")
    print(str(ELIMINAR) + ". Eliminar un llibre")
    print(str(SORTIR) + ". Sortir")
    
    opcion = int(input("Escull una opció (1-4): "))

    if opcion == AFEGIR:
        nom = input("Introdueix el nom del llibre: ")
        llibreria.append(nom)
        print("Llibre " + nom + " afegit.")

    if opcion == MOSTRAR:
        if llibreria:
            for nom in llibreria.keys():
                print("Nom: " + nom)
        else:
            print("No hi ha llibres registrats.")

    if opcion == ELIMINAR:
        nom = input("Introdueix el nom del llibre que vols eliminar: ")
        if llibreria.count(nom) > 0:
            llibreria.remove(nom)
            print("Llibre " + nom + " eliminat.")
        else:
            print("El llibre " + nom + " no existeix a la llista.")
    
    if opcion == SORTIR:
        print("Programa tancat.")
        fin_programa = True