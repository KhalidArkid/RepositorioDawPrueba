
#PRE: El usuario introdueix un nombre enter positiu N.

n = int(input("introdueix un numero primer: "))

a = 0
b = 1
print(a)
print(b)

for n in range(0, n-2):
    c = a + b
    print (c) 
    a = b
    b = c

#POST: Muestra la sèrie de Fibonacci generada.