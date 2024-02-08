'''
CORRECCIÓN
'''
#Registro de temperaturas
temperaturas = []
mes = 1
dia = 1

# Problema general
def inici():
    ...

# Primer nivel de descomposicion
def mostrar_menu():
    ...

def tractar_opcion():
    ...

# Segundo nivel de descomposicion
def registro_temperaturas_semanales():
    ...

def mostrar_media():
    ...

def mostrar_diferencia():
    ...

def finalizar_ejecucion():
    ...

# Tercer nivel de descomposicion
def leer_temperaturas_teclado():
    lector = input("Escribe las temperaturas de esta semana: ")
    for temperatura in lector.split():
        temperaturas.append(float(temperatura.replace(',','.')))

def calcular_media():
    suma = 0
    for temperatura in temperaturas:
        suma += temperatura
    return suma/len(temperaturas)

def calcular_diferencia():
    #temperatura minima
    #temperatura maxima
    #recorrer todas las temperaturas e ir modificando

def mostrar_fecha():
    print(dia, "de", end=' ')
    if mes == 1:
        print("Enero")
    elif mes == 2:
        print("Febrero")
    elif mes == 3:
        print("Marzo")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Mayo")
    elif mes == 6:
        print("Junio")
    elif mes == 7:
        print("Julio")
    elif mes == 8:
        print("Agosto")
    elif mes == 9:
        print("Septiembre")
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Noviembre")
    elif mes == 12:
        print("Diciembre")

def incrementar_fecha():
    dias_mes_actual = 0
    if mes == 2:
        dias_mes_actual = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes_actual = 30
    else:
        dias_mes_actual = 31
    dia += 7
    if dia > dias_mes_actual:
        dia -= dias_mes_actual
        mes += 1
        if mes > 12:
            mes = 1

mostrar_fecha()