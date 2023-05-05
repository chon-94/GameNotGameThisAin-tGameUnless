import random

class Forzudos:
    
    def __init__(self):
        self.nombre = self.generar_nombre()
        self.inteligencia = 2
        self.carisma = 2
        self.fuerza = random.randint(3, 6)
        self.calculos_forzudo()

    def generar_nombre(self):
        consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vocales = ['a', 'e', 'i', 'o', 'u']
        nombre = ""
        while len(nombre) < 7:
            if len(nombre) % 2 == 0:
                nombre += random.choice(consonantes)
            else:
                nombre += random.choice(vocales)
        return nombre


    # Calcula el nivel, experiencia y vida  tdo esto basado en sus habilidades    
    def calculos_forzudo(self):
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.experiencia = (self.nivel*100)+100
        self.vida = int ((self.fuerza*3.5 + self.inteligencia*2.5 + self.carisma*1.5)*(self.nivel**self.fuerza)+self.carisma+self.inteligencia)

        
    def mostrar_habilidades(self):
        print("\nNombre:", self.nombre)
        print("Habilidades de los Forzudos:")
        print(f"inteligencia: {self.inteligencia}")
        print(f"Carisma: {self.carisma}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Experiencia: {self.experiencia}")