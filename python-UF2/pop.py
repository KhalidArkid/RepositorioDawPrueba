import random

def generar_histograma():
    repeticions = [0] * 12
    for i in range(100):
        tirada = random.randint(2, 12)
        repeticions[tirada - 2] += 1
    mostrar_histograma(repeticions)

def mostrar_histograma(repeticions):
    print(" 2: ", "*" * repeticions[0], sep="")
    print(" 3: ", "*" * repeticions[1], sep="")
    print(" 4: ", "*" * repeticions[2], sep="")
    print(" 5: ", "*" * repeticions[3], sep="")
    print(" 6: ", "*" * repeticions[4], sep="")
    print(" 7: ", "*" * repeticions[5], sep="")
    print(" 8: ", "*" * repeticions[6], sep="")
    print(" 9: ", "*" * repeticions[7], sep="")
    print("10: ", "*" * repeticions[8], sep="")
    print("11: ", "*" * repeticions[9], sep="")
    print("12: ", "*" * repeticions[10], sep="")
    max_repetitions = max(repeticions)
    print("El màxim és", max_repetitions)

generar_histograma()