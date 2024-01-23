AFEGIR = 1
MOSTRAR = 2
ELIMINAR = 3
PRESTAR = 4
MOSTRAR_PRESTAMOS = 5
DEVOLVER = 6
SORTIR = 7

llibreria = {}
prestamos = {} 
fin_programa = False

while not fin_programa:
    print("\nAccions disponibles:")
    print(str(AFEGIR) + ". Afegir un llibre")
    print(str(MOSTRAR) + ". Mostrar llista dels llibres")
    print(str(ELIMINAR) + ". Eliminar un llibre")
    print(str(PRESTAR) + ". Prestar un llibre")
    print(str(MOSTRAR_PRESTAMOS) + ". Mostrar llibres prestats")
    print(str(DEVOLVER) + ". Retornar un llibre")
    print(str(SORTIR) + ". Sortir")

    opcion = int(input("Escull una opció (1-7): "))

    if opcion == AFEGIR:
        nom = input("Introdueix el nom del llibre: ")
        llibreria[nom] = "llibre interesant"
        print("Nom: " + str(nom) + " registrat")

    if opcion == MOSTRAR:
        if llibreria:
            for nom, detall in llibreria.items():
                print("Nom: {}, Detall: {}".format(nom, detall))
        else:
            print("No hi ha llibres registrats.")

    if opcion == ELIMINAR:
        nom = input("Introdueix el nom del llibre que vols eliminar: ")
        if nom in llibreria:
            del llibreria[nom]
            print("Nom: " + str(nom) + " eliminat")
        else:
            print("El llibre " + str(nom) + " no existeix a la llista.")

    if opcion == PRESTAR:
        nom = input("Introdueix el nom del llibre que vols prestar: ")
        if nom in llibreria and nom not in prestamos:
            prestamos[nom] = "Prestat"
            print("Llibre " + str(nom) + " prestat.")
        elif nom in prestamos:
            print("El llibre " + str(nom) + " ja està prestat.")
        else:
            print("No es pot prestar el llibre " + str(nom) + " ja que no existeix a la llista.")

    if opcion == MOSTRAR_PRESTAMOS:
        if prestamos:
            for nom, persona in prestamos.items():
                print("Nom: {}, Prestat a: {}".format(nom, persona))
        else:
            print("No hi ha llibres actualment prestats.")

    if opcion == DEVOLVER:
        nom = input("Introdueix el nom del llibre que vols retornar: ")
        if nom in prestamos:
            prestamos[nom] = None 
            print("Llibre " + str(nom) + " retornat.")
        else:
            print("El llibre " + str(nom) + " no està actualment prestat o ja ha estat retornat.")

    if opcion == SORTIR:
        print("Programa tancat.")
        fin_programa = True
