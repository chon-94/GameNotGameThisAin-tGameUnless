import random

class Enemigo:
    def __init__(self,):
        self.nombre= "TRABPUKCIP"
        self.fuerza = random.randint(4,15)
        self.inteligencia = random.randint(3,15)
        self.carisma = random.randint(3,15)
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = int ((self.fuerza*3.5 + self.inteligencia*2.5 + self.carisma*1.5)*\
                         (self.nivel**self.fuerza)+\
                          self.carisma+self.inteligencia)
        
    def mostrar_habilidades(self):
        print("\nNombre:", self.nombre)
        print("Vida:", self.vida)
        print("Fuerza:", self.fuerza)
        print("Carisma:", self.carisma)
        print("Inteligencia:", self.inteligencia)
        print("Nivel:", self.nivel,'\n')