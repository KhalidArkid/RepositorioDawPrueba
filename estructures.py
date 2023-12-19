def calcular_media(notes):
    return 0.3 * notes[3] + 0.4 * notes[4] + 0.3 * notes[5]

sup_7 = []
sup_8 = []

num_estudiants = int(input("Quants estudiants vols introduir? "))

for i in range(num_estudiants):
    nombre = (input("Introduce tu nombre: "))
    apellido = (input("Introduce tu apellido: "))
    Edad = (input("Introduce tu edad: "))
    Nota1 = int(input("Introduce tu primera nota: "))
    Nota2 = int(input("Introduce tu segunda nota: "))
    Nota3 = int(input("Introduce tu tercera nota: "))
    
    alumno= (nombre, apellido, Edad, Nota1, Nota2, Nota3)
    media = calcular_media(alumno)

    if media > 7:
        sup_7.append(alumno)
    
    if Nota1 > 8 or Nota2 > 8 or Nota3 > 8:
        if alumno not in sup_8:
            sup_8.append(alumno)

print("-----------------------------------------")
print("La nota media es mayor a un 7:")
for alumnos in sup_7:
    print("\t", "Nom:", alumno[0],"\n" , "\t", "Apellido:", alumno[1], "\n","\t", "Edad:", alumno[2], "\n", "\t", "Nota1:", alumno[3], "\n", "\t", "Nota2:", alumno[4], "\n", "\t", "Nota3:", alumno[5], "\n",)
print("-----------------------------------------")
print("Saca un 8 o mas en cada nota:")
for alumnos in sup_8:
    print("\t", "Nom:", alumnos[0],"\n" , "\t", "Apellido:",alumnos[1], "\n","\t", "Edad:",alumnos[2], "\n", "\t", "Nota1:",alumnos[3], "\n", "\t", "Nota2:",alumnos[4], "\n", "\t", "Nota3:",alumnos[5], "\n",)