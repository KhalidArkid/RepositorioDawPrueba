
AFEGIR = "1"
ELIMINAR = "2"
LLISTAR = "3"
SORTIR = "4"

diccionari = {}
fin_programa = False

#El signe '+' entre les variables s'utilitza per concatenar les cadenes que representen (nom) i (ip) del dispositiu.

while not fin_programa:
    print("\nAccions disponibles:")
    print(AFEGIR + ". Afegir un dispositiu")
    print(ELIMINAR + ". Eliminar un dispositiu")
    print(LLISTAR + ". Llistar tots els dispositius")
    print(SORTIR + ". Sortir")

    opcion = input("Escull una opció (1-4): ")

    if opcion == AFEGIR:
        nom = input("Introdueix el nom del dispositiu: ")
        ip = input("Introdueix l'adreça IP del dispositiu: ")
        diccionari[nom] = ip
        print("Dispositiu " + nom + " amb adreça IP " + ip + " afegit.")
    
    if opcion == ELIMINAR:
        nom = input("Introdueix el nom del dispositiu que vols eliminar: ")
        if nom in diccionari:
            del diccionari[nom]
            print("Dispositiu " + nom + " eliminat.")
        else:
            print("El dispositiu " + nom + " no existeix al registre.")
    
    if opcion == LLISTAR:
        print("Dispositius registrats:")
        if diccionari:
            for nom, ip in diccionari.items():
                print("Nom: " + nom + ", IP: " +ip)
        else:
            print("No hi ha dispositius registrats.")
    
    if opcion == SORTIR:
        print("Programa tancat.")
        fin_programa = True
        






