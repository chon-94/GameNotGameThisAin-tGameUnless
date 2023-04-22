class Escenario:
    def __init__(self, descripcion, opciones):
        self.descripcion = descripcion
        self.opciones = opciones
        self.cambioSupervivencia = 0
        # Constructor de la clase "Escenario" que toma dos argumentos: "descripcion" y "opciones".
        # "descripcion" es un atributo de instancia que representa la descripción del escenario.
        # "opciones" es un atributo de instancia que representa las opciones disponibles en este escenario.
        # "cambioSupervivencia" es un atributo de instancia que representa el cambio en la supervivencia del personaje después de tomar una decisión en este escenario.

    def presentar(self, personaje):
        print('\n')
        print(personaje.obtenerEstado())
        print(self.descripcion)
        # El método "presentar" muestra la descripción del escenario y el estado actual del personaje en la consola.

        personaje.supervivencia += self.cambioSupervivencia
        # Actualiza el atributo de instancia "supervivencia" del objeto "personaje" sumándole el valor del atributo "cambioSupervivencia" de este escenario.

        if personaje.supervivencia <= 0:
            print("Has tomado una mala decisión y has muerto. Puedes intentarlo de nuevo.")
            personaje.supervivencia = 0
            return 'INICIO'
        # Si la supervivencia del personaje es menor o igual a cero, muestra un mensaje de que el personaje ha muerto y establece la supervivencia del personaje a cero. Luego, retorna el valor 'INICIO'.

        for i in range(len(self.opciones)):
            print("[" + str(i) + "] " + self.opciones[i].descripcion)
        # Muestra las opciones disponibles en este escenario en la consola, enumerándolas con números.

        error = True

        while error:
            eleccion = input()
            # Pide al usuario que ingrese la elección de opción deseada.

            if eleccion.isnumeric():
                eleccion = int(eleccion)

                if eleccion < len(self.opciones):
                    error = False
            # Verifica si la elección del usuario es un número entero válido y si está dentro del rango de opciones disponibles.

            if error:
                print("¡Escribe el número de alguna de las opciones!")
            # Si hay un error en la elección del usuario, muestra un mensaje de error.

            if not error:
                return self.opciones[eleccion].siguienteFragmento
            # Si no hay errores, retorna el siguiente fragmento o paso correspondiente a la opción elegida, accediendo al atributo "siguienteFragmento" del objeto de opción seleccionado.