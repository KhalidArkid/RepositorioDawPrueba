
#PRE: El usuario introduce un rango(número inicial i número final.)

inicio = int(input("Introduce el número inicial del rango: "))
final = int(input("Introduce el número final del rango: "))

def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_primos(inicio, final):
    lista_primos = []
    for num in range(max(2, inicio), final + 1):
        if es_primo(num):
            lista_primos.append (num)
    return lista_primos

if inicio > final:
    print("El número inicial debe ser menor o igual que el número final.")
else:
    primos = generar_primos(inicio, final)
    if primos:
        print("Números primos en el rango de {} a {}: {}".format(inicio, final, primos))
    else:
        print("No se encontraron números primos en el rango de {} a {}.".format(inicio, final))


