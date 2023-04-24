class Jugador:
    exp_por_nivel = 100  # Cantidad de experiencia necesaria para subir de nivel
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")
        self.fuerza = 0
        self.inteligencia = 0
        self.carisma = 0
        self.experiencia = 0
        self.nivel = 1  # Empezar en el nivel 1

    def asignar_puntos(self):
        print("Asigna puntos a tus habilidades (tienes 5 puntos):")
        print("1. Fuerza")
        print("2. Inteligencia")
        print("3. Carisma")
        print("\n\n")
        for i in range(5):
            opcion = input("Selecciona una habilidad: ")
            if opcion.lower() == "1" or opcion.lower() == "fuerza":    
                self.experiencia += Jugador.exp_por_nivel
                print("Obtuviste", Jugador.exp_por_nivel, "puntos de experiencia.\n")

            elif opcion.lower() == "2" or opcion.lower() == "inteligencia":
                self.experiencia += 2 * Jugador.exp_por_nivel
                print("Obtuviste", 2 * Jugador.exp_por_nivel, "puntos de experiencia.\n")

            elif opcion.lower() == "3" or opcion.lower() == "carisma":
                self.experiencia += 3 * Jugador.exp_por_nivel
                print("Obtuviste", 3 * Jugador.exp_por_nivel, "puntos de experiencia.\n")

            else:
                print("Opción inválida. Intenta de nuevo.")

        self.verificar_nivel()

    def verificar_nivel(self):
        # Verificar si el jugador alcanzó la cantidad de experiencia necesaria para subir de nivel
        if self.experiencia >= Jugador.exp_por_nivel * self.nivel:
            print("¡Has subido de nivel!")
            self.nivel += 1
            Jugador.exp_por_nivel *= 2  # Aumentar la cantidad de experiencia necesaria para subir de nivel
            self.asignar_puntos()  # Asignar los puntos adicionales al subir de nivel

    def mostrar_habilidades(self):
        print("Nombre:", self.nombre)
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Carisma:", self.carisma)
        print("Experiencia:", self.experiencia)
        print("Nivel:", self.nivel)
