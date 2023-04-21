    
class Personaje:
    def __init__(self):
        self.supervivencia = 0  # Atributo de instancia para la supervivencia, inicializado en 0.

    def obtenerEstado(self):
        return 'Supervivencia: ' + str(self.supervivencia)  # Retorna una cadena de texto con el valor actual de la supervivencia.

        # Utiliza la sintaxis self.supervivencia para acceder al valor del atributo supervivencia de la instancia.
        # El valor del atributo supervivencia se convierte a una cadena de texto con str() antes de concatenarse con la cadena 'Supervivencia: '.


class Personaje:
    def __init__(self):
        self.supervivencia = 0
        # Atributo de instancia llamado "supervivencia" inicializado en 0.
        # Este atributo representa el nivel de supervivencia del personaje y se establece en 0 al crear una nueva instancia de la clase.

    def obtenerEstado(self):
        return 'Supervivencia: ' + str(self.supervivencia)
        # Método de instancia llamado "obtenerEstado" que devuelve una cadena de texto con el valor actual de la supervivencia.
        # Utiliza la sintaxis self.supervivencia para acceder al valor del atributo supervivencia de la instancia actual.
        # El valor del atributo supervivencia se convierte a una cadena de texto con str() antes de concatenarse con la cadena 'Supervivencia: '.
