'''
Opcions:
    1.1 Mostra les opcions disponibles: RT,MJ,DF,FI.
    1.2 Seleccionar una acció a realitzar.

Fechas
    2.1 Introduir les feches per posar la temperatura començant desde 1 gener fins a l'últim dia de l’any
    2.2 Només els primers dies de cada setmana (dilluns)
	2.3 Dividir els dies en mesos i ens surt 52 setmanes

Temperatura:
    3.1 Introdueix la temperatura per a cada dia de la setmana.
    3.2 Es van enregistrant les temperatures mesurades.
    3.3 El programa calcula auto el dia i el mes actual. 

Mitjana de Temperatura:
    4.1 Calcular la temperatura mitjana per a la setmana actual.
    4.2 Mostra la data actual amb la mitjana.

Max i Min:
    5.1 Calcula la diferència entre la temperatura màxima i mínima per a la setmana actual.
    5.2 Mostra la data actual amb la diferència.

Errors:
    6.1 l'usuari consulta valors sense tenir cap data enregistrada.
    6.3 Maneja casos en què l'usuari intenta registrar temperatures amb tipus de dades incorrectes.
'''
print("Bienvenido al registro de temperaturas")
print("------------------------------------------")

def opcions():
    while True:
        print("\n1. Introducir fechas")
        print("2. Introducir temperaturas")
        print("3. Calcular temperatura media para la semana actual")
        print("4. Calcular diferencia entre temperatura máxima y mínima para la semana actual")
        print("5. Mostrar fecha actual")
        print("6. Salir")
        opcion = input("Introduce la opcion que quieres realizar (1-6)")


def fechas():
    ...

def temperatura():
    ...

def mitjana_temperatura():
    ...

def max_min():
    ...

