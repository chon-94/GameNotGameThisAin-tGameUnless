class Enemigo:

    def __init__(self, fuerza, inteligencia, carisma):
        self.fuerza = 3
        self.inteligencia = 3
        self.carisma = 3
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = vida_jugador * 2
        
    def mostrar_habilidades(self):
        print("Vida:", self.vida)
        print("Fuerza:", self.fuerza)
        print("Carisma:", self.carisma)
        print("Inteligencia:", self.inteligencia)
        print("Nivel:", self.nivel)
