

binario = list(input("Escribe un numero binario para pasarlo a decimal: "))
i = 0
size = 1
result = 0
es_final_de_binario = False

while es_final_de_binario == False:
    auxiliar_binario = [None] * size

    for j in range(0, size):
        auxiliar_binario[j] = binario[j]
    
    if auxiliar_binario == binario:
        es_final_de_binario = True

    result = (result * 2) + int(binario[i])
    i = i + 1
    size = size + 1

print(result)