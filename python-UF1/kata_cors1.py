 # Primera tarea, LEER el enunciado

cartas = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd']

jugadores = [[], [], [], []]
for i in range(0, 13):
    for j in range(0,4):
        jugadores[j].append(cartas.pop())

index = 1
for jugador in jugadores:
    print("Jugador ", index, ": ", ", ".join(jugador)) 
    print("Cartas repartidas al jugador:", len(jugador))
    print()
    index = index + 1

mesa = []
for jugador in jugadores:
    mesa.append(jugador.pop(0))
for carta in mesa:
    print(carta) 

carta = mesa.pop(0)
carta_mas_alta = {"numero": carta[:-1], "palo": carta[-1]}
for carta in mesa:
    carta_a_comparar = {"numero": carta[:-1], "palo": carta[-1]} 
    if carta_mas_alta["palo"] == carta_a_comparar["palo"]:
        if carta_mas_alta["numero"] < carta_a_comparar["numero"]:
            carta_mas_alta = carta_a_comparar

print("La carta más alta en la mesa es:", carta_mas_alta["numero"] + carta_mas_alta["palo"])
# ... (el código que ya tienes)

# Determinar quién tiene la carta más alta en la mesa por palo
carta_mas_alta_por_palo = {"s": None, "h": None, "c": None, "d": None}

for palo in ["s", "h", "c", "d"]:
    cartas_en_palo = [carta for carta in mesa if carta[-1] == palo]
    if cartas_en_palo:
        carta_mas_alta_por_palo[palo] = max(cartas_en_palo, key=lambda x: int(x[:-1]))

# Encontrar el palo con la carta más alta
palo_ganador = None
carta_ganadora = None

for palo, carta in carta_mas_alta_por_palo.items():
    if carta and (carta_ganadora is None or int(carta[:-1]) > int(carta_ganadora[:-1])):
        palo_ganador = palo
        carta_ganadora = carta

print("La carta más alta en la mesa es:", carta_ganadora)

# Encontrar el jugador que tiene la carta ganadora y mostrarlo
ganador = None
for jugador in jugadores:
    if carta_ganadora in jugador:
        ganador = jugadores.index(jugador) + 1  # Sumamos 1 para mostrar el número del jugador
        break

if ganador is not None:
    print(f"El ganador de la mano es el Jugador {ganador}.")

# ... (cualquier otra acción que desees agregar al juego)