
AFEGIR = 1
ELIMINAR = 2
MOSTRAR = 3
SALIR = 4

servidores = []
fin_programa = False

while fin_programa == False:
    opcion = int(input("Escoge entre las siguientes opciones: 1- Afegir servidor, 2- Eliminar servidor, 3- Mostrar servidores: "))
    if opcion == AFEGIR:
        nombre = input("Introduce el nombre del servidor: ")
        ip = input("Introduce la IP del servidor: ")
        estado = input("Introduce el estado del servidor [activo/inactivo]: ")
        tupla = (nombre, ip, estado)
        servidores.append(tupla)
    else:
        if opcion == ELIMINAR:
            nombre = input("Introduce el nombre del servidor: ")
        else:
            if opcion == MOSTRAR:
                for servidor in servidores:
                    print("Nombre del servidor: ", servidor[0])
                    print("IP del servidor: ", servidor[1])
                    print("Estado del servidor: ", servidor[2])
            else:
                if opcion == SALIR:
                    fin_programa = True
