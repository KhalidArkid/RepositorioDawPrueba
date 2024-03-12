class coordenada:
    def __init__(self):
    # Coordenada inicial
    self.x: int = 0
    self.y: int = 0

    # Programa principal
    def moure_dreta(self):
        self.x += 1

    def moure_esquerra(self):
        self.x -= 1

    def moure_amunt(self):
        self.y += 1

    def moure_avall(self):
        self.y -= 1

class graella:
    # Executar moviments
    coordenada = moure_dreta(coordenada)
    print(f"Nova coordenada després de moure a la dreta: {coordenada}")

    coordenada = moure_amunt(coordenada)
    print(f"Nova coordenada després de moure amunt: {coordenada}")