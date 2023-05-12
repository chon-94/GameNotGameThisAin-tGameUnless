import random
import string
#import Clase
class Enemigo:
    def __init__(self, tipo):

        self.tipo = tipo
        
        self.nombre = self.generar_nombre()
        self.fuerza = 0
        self.carisma = 0
        self.inteligencia = 0
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = int((self.fuerza * 1.5 + self.inteligencia * 1.5 + self.carisma * 1.5) * (self.nivel * self.fuerza) + self.carisma + self.inteligencia)
        
        if tipo == 1:
            self.generar_combate_habilidad_aleatoria()
        elif tipo == 2:
            self.generar_combate_inteligencia_aleatoria()
        elif tipo == 3:
            self.generar_combate_carisma_aleatoria()
        elif tipo == 4:
            self.generar_combate_fuerza_aleatoria()
        else:
            pass
        
    
    def generar_nombre(self):
        nombre = ""
        longitud = random.randint(5, 10)
        
        for i in range(longitud):
            if i % 2 == 0:
                # Generamos una letra aleatoria
                letra = random.choice(string.ascii_lowercase)
                nombre += letra
            else:
                # Generamos una vocal aleatoria
                vocal = random.choice("aeiou")
                nombre += vocal
        
        nombre += "-" + str(random.randint(0, 9999))
        return nombre
    
    def generar_combate_habilidad_aleatoria(self):
        self.inteligencia = random.randint(1, 6)
        self.carisma = random.randint(1, 6)
        self.fuerza = random.randint(1, 6)
        self.mostrar_estadisticas()

    def generar_combate_inteligencia_aleatoria(self):
        self.inteligencia = random.randint(3, 6)
        self.carisma = random.randint(1, 2)
        self.fuerza = random.randint(1, 2)
        self.mostrar_estadisticas()


    def generar_combate_carisma_aleatoria(self):
        self.inteligencia = random.randint(1, 2)
        self.carisma = random.randint(3, 6)
        self.fuerza = random.randint(1, 2)
        self.mostrar_estadisticas()

    def generar_combate_fuerza_aleatoria(self):
        self.inteligencia = random.randint(1, 2)
        self.carisma = random.randint(1, 2)
        self.fuerza = random.randint(3, 6)
        self.mostrar_estadisticas()

    def mostrar_estadisticas(self):
        estilo = {
            "negrita": "\033[1m",
            "subrayado": "\033[4m",
            "rojo": "\033[91m",
            "verde": "\033[92m",
            "amarillo": "\033[93m",
            "azul": "\033[94m",
            "reset": "\033[0m"
        }
        
        print(f"\n{estilo['negrita']}Tipo:{estilo['reset']} {self.tipo}")
        print(f"{estilo['negrita']}Nombre:{estilo['reset']} {self.nombre}")
        print(f"{estilo['negrita']}Fuerza:{estilo['reset']} {self.fuerza}")
        print(f"{estilo['negrita']}inteligencia:{estilo['reset']} {self.fuerza}")
        print(f"{estilo['negrita']}carisma:{estilo['reset']} {self.fuerza}")
