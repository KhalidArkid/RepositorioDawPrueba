lista1 = [__import__('random').randrange(50) for i in range(10)]
lista2 = [__import__('random').randrange(50) for i in range(7)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)

lista_fusion = lista1 + lista2

lista_unica = []
for num in lista_fusion:
    if num not in lista_unica:
        lista_unica.append(num)
print("Lista única:", lista_unica)

suma_nombres_unicos = sum(lista_unica)
print("Suma de los números únicos:", suma_nombres_unicos)
