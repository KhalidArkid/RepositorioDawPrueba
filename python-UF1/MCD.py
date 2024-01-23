#PRE: El usuario introdueix os numeros enters positius.


n1 = int(input("introduce el primer numero enteros positivos: "))
n2 = int(input("introduce el segundo numero enteros positivos: "))

menor = n1
mayor = n2

if n1 > n2:
    menor = n2
    mayor = n1

MCD = 1

for i in range(2,menor+1):
    while n1 % i == 0 and n2 % i == 0:
        MCD = MCD * i
        n1 = n1 / i
        n2 = n2 / i

print("El Maximo Comun Divisor de",mayor,"y",menor,"es",MCD)

#POST: Devolvemos el resultado del calculo del MCD.