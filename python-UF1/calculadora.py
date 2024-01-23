#PRE: Recibiremos 2 numeros enteros y un numero que indique la operacion
# Const
TXT_INTRODUCIR_NUMEROS = "introduce un numero: "
TXT_INTRODUCIR_OPERACION = "introduce que operacion hacer 1 para suma, 2 para resta, 3 para multiplicacion, 4 para division: "
SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
# EndConst


# Var
a = None
b = None
operado = None
# EndVar


a = int(input(TXT_INTRODUCIR_NUMEROS))
operado = int(input(TXT_INTRODUCIR_OPERACION))
b = int(input(TXT_INTRODUCIR_NUMEROS))


if operado == SUMA:
   result = a + b
else:
   if operado == RESTA:
       result = a - b
   else:
       if operado == MULTIPLICACION:
           result = a * b
       else:
           if operado == DIVISION and b !=0:
               result = a // b 
           else:
               result = "Syntax Error"


print(result)
#POST: Devolveremos el resultado de la operacion seleccionada si esta existe
