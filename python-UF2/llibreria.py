AFEGIR = 1
MOSTRAR = 2
ELIMINAR = 3
PRESTAMO = 4
MOSTRAR_PRESTAMOS = 5
DEVOLVER_PRESTAMO = 6
SORTIR = 7

llibreria = []
prestamos = []
fin_programa = False

while not fin_programa:
    print("\nAccions disponibles:")
    print(str(AFEGIR) + ". Afegir un llibre")
    print(str(MOSTRAR) + ". Mostrar llista dels llibres")
    print(str(ELIMINAR) + ". Eliminar un llibre")
    print(str(PRESTAMO) + ". Prestar un llibre") 
    print(str(MOSTRAR_PRESTAMOS) + ". Mostrar llibres prestats")
    print(str(DEVOLVER_PRESTAMO) + ". Retornar un llibre"
    print(str(SORTIR) + ". Sortir")
    
    opcion = int(input("Escull una opció (1-7): "))

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

    if opcion == PRESTAMO:
        nom = input("Introdueix el nom del llibre que vols prestar: ")
        if nom in llibreria and nom not in prestamos:
            prestamos[nom] = "Persona que presta" 
            print("Llibre " + nom + " prestat.")
        if nom in prestamos:
            print("El llibre " + nom + " ja està prestat.")
        else:
            print("No es pot prestar el llibre " + nom + " ja que no existeix a la llista.")

    lif opcion == MOSTRAR_PRESTAMOS:
        if prestamos:
            for nom, persona in prestamos.items():
                print("Nom: {}, Prestat a: {}".format(nom, persona))
        else:
            print("No hi ha llibres prestats.")

    elif opcion == DEVOLVER_PRESTAMO:
        nom = input("Introdueix el nom del llibre que vols retornar: ")
        if nom in prestamos:
            del prestamos[nom]
            print("Llibre " + nom + " retornat.")
        else:
            print("El llibre " + nom + " no està actualment prestat.")
    
    if opcion == SORTIR:
        print("Programa tancat.")
        fin_programa = True