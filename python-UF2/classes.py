# Coordenada inicial
class Coordenada:
    def __init__(self):
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

class Main:
    # Executar moviments
    def __init__(self):
        coordenada: Coordenada = Coordenada()
        coordenada.moure_dreta()
        print(f"Nova coordenada després de moure a la dreta: ({coordenada.x}, {coordenada.y})")

        coordenada.moure_amunt()
        print(f"Nova coordenada després de moure amunt: ({coordenada.x}, {coordenada.y})")

Main()