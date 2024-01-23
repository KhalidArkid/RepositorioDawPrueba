

AFEGIR = 1
ELIMINAR = 2
LLISTAR = 3
SALIR = 4

lista = []
nombre = ""
fin_programa = False

while fin_programa == False:
    opcion = int(input("Que quieres hacer 1- Afegir, 2- Eliminar, 3- Llistar: "))
    
    if opcion == AFEGIR:
        nombre = input("Introduce el nombre del usuario: ")
        lista.append(nombre)    
    else:
        if opcion == ELIMINAR:
            nombre = input("Introduce el nombre del usuario a eliminar: ")
        if lista.count(nombre) > 0:
            lista.remove(nombre)
        else:
            if opcion == LLISTAR:
                print("Opcion A")
                for i in range (0, len(lista)):
                    print (i)
                print("Opcion B")
                
                for i in lista:
                    print(i)
            else:
                if opcion == SALIR:
                    fin_programa = True

