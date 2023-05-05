class Personaje:

    # Inicializa las variables del personaje
    def __init__(self): 
        self.nombre=input("\nIngresa tu nombre:\n")
        self.fuerza = 0
        self.inteligencia = 0
        self.carisma = 0
        self.experiencia = 0
        self.calulos_personaje()

    # Calcula el nivel, experiencia y vida  tdo esto basado en sus habilidades    
    def calulos_personaje(self):
        self.nivel = self.fuerza + self.inteligencia + self.carisma
        self.experiencia = (self.nivel*100)+100
        self.vida = int ((self.fuerza*3.5 + self.inteligencia*2.5 + self.carisma*1.5)*(self.nivel**self.fuerza)+self.carisma+self.inteligencia)

    # Permite asignar puntos a las habilidades
    def puntos_cif(self):
        print("\nAsigna puntos a tus hlabilidades (tienes 5 puntos):")
        print("1. Fuerza")
        print("2. Inteligencia")
        print("3. Carisma")

        for i in range(5):
            opcion = input("\nSelecciona una habilidad: ")
            if opcion.lower() == "1" or opcion.lower() == "fuerza":    
                self.fuerza += 1
                print("Nivel de Fuerza", self.fuerza)

            elif opcion.lower() == "2" or opcion.lower() == "inteligencia":
                self.inteligencia += 1
                print("Nivel de Inteligencia", self.inteligencia)

            elif opcion.lower() == "3" or opcion.lower() == "intelgencia":
                self.carisma += 1
                print("Nivel de Carisma", self.carisma)

            else:
                print("Opción inválida. Intenta de nuevo.")

        self.calulos_personaje()# Vuelva a hacer el calculo

    # Muestra Los detalles del personaje
    def mostrar_habilidades(self):
        print("\nNombre:", self.nombre)
        print("Vida:", self.vida)
        print("Fuerza:", self.fuerza)
        print("Carisma:", self.carisma)
        print("Inteligencia:", self.inteligencia)
        print("Experiencia:", self.experiencia)
        print("Nivel:", self.nivel,'\n')