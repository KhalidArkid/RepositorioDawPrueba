'''
CORRECCIÓN
'''
#Registro de temperaturas
temperaturas = []
mes = 1
dia = 1
fi = False

# Problema general
def inici():
    while not fi:
        mostrar_menu()
        tractar_opcion()

# Primer nivel de descomposicion
def mostrar_menu():
    print("Benvingut al registre de temperatures")
    print("-------------------------------------")
    print("[RT] Registrar temperatures setmanas.")
    print("[MJ] Consultar temperatura mitjana.")
    print("[DF] Consultar diferencia maxima.")
    print("[FI] Sortir")

def tractar_opcion():
    opcio = input("Opcio: ")
    if opcio.casefold() == "RT".casefold():
        registro_temperaturas_semanales()
    elif opcio.casefold() == "MJ".casefold():
        mostrar_media()
    elif opcio.casefold() == "DF".casefold():
        mostrar_diferencia()
    elif opcio.casefold() == "FI".casefold():
        finalizar_ejecucion()
    else:
        print("Opcio incorrecta.")

# Segundo nivel de descomposicion
def registro_temperaturas_semanales():
    if (len(temperaturas) + 7) > (52*7):
        print("Ja tenim totes les setmanes introduides no podem introduir mes.")
    else:
        leer_temperaturas_teclado()
        incrementar_fecha()

def mostrar_media():
    if len(temperaturas) > 0:
        media = calcular_media()
        print("Fins avui", end = " ")
        mostrar_fecha()
        print("la mitjana a estat de", media, "graus.")
    else:
        print("No hi ha temperatures registrades")

def mostrar_diferencia():
    if len(temperaturas) > 0:
        diferencia = calcular_diferencia()
        print("Fins avui", end = " ")
        mostrar_fecha()
        print("la diferencia maxima ha estat de", diferencia, "graus.")

def finalizar_ejecucion():
    global fi
    fi = True

# Tercer nivel de descomposicion
def leer_temperaturas_teclado():
    lector = input("Escriu les temperatures d'aquesta setmana:\n ")
    for temperatura in lector.split():
        temperaturas.append(float(temperatura.replace(',','.')))

def calcular_media():
    suma = 0
    for temperatura in temperaturas:
        suma += temperatura

    return suma/len(temperaturas)

def calcular_diferencia():
    minima = temperaturas[0]
    maxima = temperaturas[0]
    for temperatura in temperaturas:
        if minima > temperatura:
            minima = temperatura
        if  maxima < temperatura:
            maxima = temperatura
    diferancia = maxima - minima
    return diferancia

def mostrar_fecha():
    print(dia, "de", end= ' ')
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
    global mes, dia
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

inici()