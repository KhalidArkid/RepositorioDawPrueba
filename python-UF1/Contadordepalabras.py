#PRE: Recibimos un conjunto de palabras separadas por un unico espacio entre ellas
frase = []
aux = []
final_texto = False
espacios_blancos = 0
numero_palabras = 0
size_variable = 1
i = 0

frase = list(input("Escribe un conjunto de palabras separadas por unico espacio entre ellas: "))

while not final_texto:
    aux = [None] * (size_variable) # Aqui inicializamos un array con un tamanyo, es lo mismo que un char aux[size_variable] de pseudocodigo

    # Introducimos los valores en aux para tener una lista de size_variable + 1
    for j in range(size_variable):
        aux[j] = frase[j]

    # Si el indice en el que estamos en la iteracion es un espacio en blanco incrementamos la variable
    if frase[i] == " ":
        espacios_blancos += 1

    # Nos aseguramos de salir de bucle en algun momento
    final_texto = aux == frase
    # Incrementamos el tamanyo con el que crearemos en la siguiente iteracion la lista auxiliar
    size_variable += 1
    # Incrementamos el indice al que accederemos para comprobar el contenido
    i += 1

# Siempre hay una palabra mas que espacios en blanco, contar el espacio que hay entre los dedos para comprobarlo
numero_palabras = espacios_blancos + 1

print(numero_palabras)
#POST: Devolvemos el numero de palabras que contiene la frase

