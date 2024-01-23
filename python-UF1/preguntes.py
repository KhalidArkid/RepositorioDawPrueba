llista_preguntes = ["Cuanto es 77+33?" , "Como se llaman los animales que tienen un esqueleto articulado?" , "Como se llama un poligono de 6 lados?" , "Que pokemon dice pica pica?" , "En que año se descubrio America?"]
llista_respuestas = ["110" , "vertebrados" , "hexagono" , "pikachu" , "1492"]
parar = 0 
puntos = 0

seed = int(input("introdueix un numero mayor que 0: "))

while parar is 0:
    seed = (seed * 997) % 1000
    random = (seed * 503) % 1000 / 1000  #no 100 sino 1000
    numero_pregunta = int(random * (len(llista_preguntes)))
    respuesta = input(llista_preguntes[numero_pregunta])
    puntos += 1 if respuesta == llista_respuestas[numero_pregunta] else 0
    parar = int(input("Si no quieres seguir jugando? [0 para seguir, 1 para parar]"))

print("Tus puntos han sido:", puntos)
