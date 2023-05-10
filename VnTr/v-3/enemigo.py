import random
import string

class Enemigo:
    def __init__(self):
        self.nombre = self.generar_nombre()
        
        # Generamos las estadísticas aleatoriamente
        self.inteligencia = random.randint(1, 6)
        self.carisma = random.randint(1, 6)
        self.fuerza = random.randint(1, 6)
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = int((self.fuerza * 1.5 + self.inteligencia * 1.5 + self.carisma * 1.5) * (self.nivel * self.fuerza) + self.carisma + self.inteligencia)
    
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
        
        nombre += "-" + str(random.randint(0, 5))
        #nombre += "-" + random.choice(["0", "2", "3", "5", "6", "7", "9"])
        return nombre
    
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
        
        print(f"\n{estilo['negrita']}Nombre:{estilo['reset']} {self.nombre}")
        print(f"{estilo['negrita']}Fuerza:{estilo['reset']} {self.fuerza}")
        print(f"{estilo['negrita']}Carisma:{estilo['reset']} {self.carisma}")
        print(f"{estilo['negrita']}Inteligencia:{estilo['reset']} {self.inteligencia}")
        print(f"{estilo['negrita']}Vida:{estilo['reset']} {self.vida}")
        print(f"{estilo['negrita']}Nivel:{estilo['reset']} {self.nivel}")
