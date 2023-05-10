# Importamos clases desde su propio módulo
from personaje import Personaje
from menu import Menu

class Main:

    def __init__(self):        
        self.personaje = Personaje()# Instancia de clase Personaje le asignamos al atributo personaje
        self.menu = Menu()

    def iniciar_juego(self):

        # Escoger habilidades del personaje
        print("\n¡Comienza el juego!")
        self.personaje.puntos_cif()
        self.personaje.escoger_habilidad()

        # Mostrar habilidades del personaje
        print("\n¡ESTAS NOS LAS CARACTERISTICAS!")        
        self.personaje.mostrar_habilidades()

        # Muestra el menu
        self.menu.ejecutar_menu()
        
# Instancia de clase Main llamamos al método iniciar_juego() para comenzar el juego
if __name__ == "__main__":
    juego = Main()
    juego.iniciar_juego()