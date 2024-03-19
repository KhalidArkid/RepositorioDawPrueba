class Coordenada:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0

    def moure_dreta(self):
        self.x += 1

    def moure_esquerra(self):
        self.y -= 1

