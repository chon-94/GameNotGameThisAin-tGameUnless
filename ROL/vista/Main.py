from controlador.juego import Juego
from models.monstruos.Jugador import Jugador


class Main:

    def __init__(self):
        # Crear instancia de la clase Jugador y asignarla a la variable self.jugador
        self.jugador = self.crearJugador()
        # Crear instancia de la clase Juego con self.jugador como argumento y asignarla a la variable self.juego
        self.juego = Juego(self.jugador)
        
    def start(self):
        self.initCombatView()
        self.initWinOrLoseView()
        self.game.start()


if __name__ == '__main__':
    # Imprime un mensaje de bienvenida en la consola
    print("Bienvenidos al juego pes mamey:\n\n")
    Main()