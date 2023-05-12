class Personaje:#Jugador

    def __init__(self): 
        self.nombre=input("\nIngresa tu nombre:\n")
        self.habilidad_escogida = ""        
        self.inteligencia = 0        
        self.carisma = 0
        self.fuerza = 0
        self.nivel=0
        self.vida=0
        self.calulos_personaje()

    def calulos_personaje(self):
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.vida = int ((self.fuerza*1.5 + self.inteligencia*1.5 + self.carisma*1.5)*(self.nivel*self.fuerza)+self.carisma+self.inteligencia)

    def puntos_cif(self):
        print("\nAsigna puntos a tus hlabilidades (tienes 5 puntos):")
        print("1. Fuerza")
        print("2. Inteligencia")
        print("3. Carisma")

        for i in range(6):# Aumentar puntos, niveles
            opcion = input("\nSelecciona una habilidad: ")
            
            if opcion.lower() == "1" or opcion.lower() == "fuerza":
                self.fuerza += 1
                print("Nivel de Fuerza", self.fuerza)                
                
            elif opcion.lower() == "2" or opcion.lower() == "inteligencia":
                self.inteligencia += 1
                print("Nivel de Inteligencia", self.inteligencia)

            elif opcion.lower() == "3" or opcion.lower() == "Carisma":
                self.carisma += 1
                print("Nivel de Carisma", self.carisma)

            else:
                print("Opción inválida. Intenta de nuevo.")

    def escoger_habilidad(self):
        print("\nEscoge un Item:")
        print("1. Espada Blademaster (multiplica la fuerza por 3)")
        print("2. Bastón de Paragons (multiplica la inteligencia por 3)")
        print("3. Lengua de plata de Jeremías Springfield (multiplica el carisma por 3)")

        opcion = input("\nSelecciona una habilidad: ")

        if opcion == "1" or opcion.lower() == "espada" or opcion.lower() == "espada blademaster":
            self.fuerza *= 3
            self.habilidad_escogida = "Espada Blademaster"
            print("¡Tu fuerza ha sido multiplicada por 3!")

        elif opcion == "2" or opcion.lower() == "bastón" or opcion.lower() == "bastón de paragons":
            self.inteligencia *= 3
            self.habilidad_escogida = "Bastón de Paragons"
            print("¡Tu inteligencia ha sido multiplicada por 3!")

        elif opcion == "3" or opcion.lower() == "lengua" or opcion.lower() == "lengua de plata de jeremías springfield":
            self.carisma *= 3
            self.habilidad_escogida = "Lengua de plata de Jeremías Springfield"
            print("¡Tu carisma ha sido multiplicado por 3!")

        else:
            print("Opción inválida. Intenta de nuevo.")

        
        self.calulos_personaje()

    def mostrar_habilidades(self):
        estilo = {
                    "negrita": "\033[1m",
                    "subrayado": "\033[4m",
                    "rojo": "\033[91m",
                    "verde": "\033[92m",
                    "amarillo": "\033[93m",
                    "azul": "\033[94m",
                    "reset": "\033[0m"
                 }

        print(f"\n  {estilo['verde']}      Nombre:{estilo['reset']} {self.nombre}")
        print(f"  {estilo['negrita']}      Fuerza:{estilo['reset']} {self.fuerza}")
        print(f"  {estilo['negrita']}     Carisma:{estilo['reset']} {self.carisma}")
        print(f"  {estilo['negrita']}Inteligencia:{estilo['reset']} {self.inteligencia}")
        print(f"  {estilo['rojo']}        Vida:{estilo['reset']} {self.vida}")
        print(f"  {estilo['amarillo']}       Nivel:{estilo['reset']} {self.nivel}")
        print(f"  {estilo['azul']}   Habilidad:{estilo['reset']} {self.habilidad_escogida}\n") 