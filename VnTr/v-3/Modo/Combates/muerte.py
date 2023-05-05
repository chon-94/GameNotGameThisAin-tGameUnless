import random

class Muerte:

    # Inicializa las variables del enemigo
    def __init__(self):
        self.nombre = self.generar_nombre()
        self.fuerza = random.randint(2,3)
        self.inteligencia = random.randint(2,3)
        self.carisma = random.randint(2,3)
        self.calculos_enemigo()

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

    def calculos_enemigo(self):
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = int((self.fuerza*3.5 + self.inteligencia*2.5 + self.carisma*1.5)*(self.nivel**self.fuerza) + self.carisma + self.inteligencia)

    def mostrar_habilidades(self):
        print("\nNombre:", self.nombre)
        print("Vida:", self.vida)
        print("Fuerza:", self.fuerza)
        print("Carisma:", self.carisma)
        print("Inteligencia:", self.inteligencia)
        print("Nivel:", self.nivel, '\n')
