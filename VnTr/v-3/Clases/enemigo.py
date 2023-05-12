import random, string

class Enemigo:
    def __init__(self):
        self.nombre = self.generar_nombre()
        self.fuerza = 0
        self.inteligencia = 0
        self.carisma = 0
        self.nivel = 0
        self.vida = 0

    def generar_nombre(self):
        longitud = random.randint(3, 15)
        nombre = ""
        
        for i in range(longitud):
            if i % 2 == 0:
                # Generar una letra aleatoria
                letra = random.choice(string.ascii_lowercase)
                nombre += letra
            else:
                # Generar una vocal aleatoria
                vocal = random.choice("aeiou")
                nombre += vocal
        
        return nombre

    def calculos_enemigo(self):
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = int ((self.fuerza*1.5 + self.inteligencia*1.5 + self.carisma*1.5)*(self.nivel*self.fuerza)+self.carisma+self.inteligencia)
    
    def generar_combate_habilidad_aleatoria(self):
        self.nombre = self.generar_nombre()+' - El Aleatorio'
        self.fuerza = random.randint(3,8)
        self.inteligencia = random.randint(3,8)
        self.carisma = random.randint(3, 8)
        self.calculos_enemigo()
        self.mostrar_habilidades()
            
    def generar_combate_inteligencia_aleatoria(self):
        self.nombre = self.generar_nombre()+' - El Inteligente'
        self.fuerza = random.randint(2, 5)
        self.inteligencia = random.randint(3,8)
        self.carisma = random.randint(2, 5)
        self.calculos_enemigo()
        self.mostrar_habilidades()


    def generar_combate_carisma_aleatoria(self):
        self.nombre = self.generar_nombre()+' - El Carismatico'
        self.fuerza = random.randint(2,5)
        self.inteligencia = random.randint(2,5)
        self.carisma = random.randint(3,8)
        self.calculos_enemigo()
        self.mostrar_habilidades()

    
    def generar_combate_fuerza_aleatoria(self):
        self.nombre = self.generar_nombre()+' - El Forzudo'
        self.fuerza = random.randint(3,8)
        self.inteligencia = random.randint(2,5)
        self.carisma = random.randint(2,5)
        self.calculos_enemigo()
        self.mostrar_habilidades()

    def mostrar_habilidades(self):
        print("\nNombre:", self.nombre)
        print("Vida:", self.vida)
        print("Fuerza:", self.fuerza)
        print("Carisma:", self.carisma)
        print("Inteligencia:", self.inteligencia)
        print("Nivel:", self.nivel)

