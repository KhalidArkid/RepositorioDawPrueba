
min = int(input("Introduce inicio de rango: "))
max = int(input("Introduce fin de rango: "))
numeros_primers = []
numeros_encontrados = 0

for i in range(min, max + 1):
    
    i_es_primo = True
    j = 2
    while j < i and i_es_primo == True:
        if i % j == 0:
            i_es_primo = False
        j = j + 1

    # Si I es un numero primo lo introduciremos en una lista de numeros
    if i_es_primo == True:
        numeros_encontrados = numeros_encontrados + 1
        # Tenemos que introducir el numero en la lista, PERO la lista tiene un tamanyo menor del que necesitamos
        # La lista tiene que tener el tamanyo de numeros primos encontrados
        numeros_primers_auxiliar = [None] * numeros_encontrados
        for k in range(0, numeros_encontrados - 1): 
            numeros_primers_auxiliar[k] = numeros_primers[k]
        
        numeros_primers_auxiliar[numeros_encontrados - 1] = i

        numeros_primers = numeros_primers_auxiliar

print(numeros_primers)
