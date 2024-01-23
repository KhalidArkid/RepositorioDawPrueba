
#PRE: El usuario introduce un número binario(una cadena de 0s y 1s).


num = str(input("introduce un número binario para pasarlo a decimal: "))

result = 0

for i in range(len(num)):
    result += int(num[i]) * 2 ** (len(num) - i - 1)

print(result) 

#POST: Devolver resultado de el equivalente decimal del binario introducido.