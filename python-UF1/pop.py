def calculate_average(Nota1, Nota2, Nota3):
    return (Nota1 * 0.3) + (Nota2 * 0.4) + (Nota3 * 0.3)

alumnos = [("Nom", "Cognom", 12, 4, 5, 6),
           ("Nom", "Cognom", 12, 8, 5, 6),
           ("Nom", "Cognom", 12, 4, 9, 6)]

nota_sup_7 = []
nota_sup_8 = []

for alumno in alumnos:
    Nom, Cognom, Edat, Nota1, Nota2, Nota3 = alumno

    NotaFinal = calculate_average(Nota1, Nota2, Nota3)

    # Check conditions
    if NotaFinal > 7:
        nota_sup_7.append(alumno)
        if NotaFinal > 8:
            nota_sup_8.append(alumno)

print("Estudiants amb mitjana ponderada superior a 7:")
for alumno in nota_sup_7:
    print("\t", alumno)

print("\nEstudiants amb nota superior a 8 en alguna de les proves:")
for alumno in nota_sup_8:
    print("\t", alumno)