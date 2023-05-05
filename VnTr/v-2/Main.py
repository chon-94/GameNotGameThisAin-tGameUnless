from enemigo import Enemigo
from jugador import Jugador
from pelea import Pelea
#from cargar import Tiempo
#import time

class Main:

    def __init__(self):
        self.jugador = Jugador()
        self.enemigo = Enemigo()
        self.pelea   = Pelea(self.jugador,self.enemigo)
        
    def iniciar_juego(self):

        print("\n¡Comienza el juego!")
        
        self.jugador.asignar_puntos()
        self.jugador.mostrar_habilidades()
        self.enemigo.mostrar_habilidades()
        self.pelea.iniciar_pelea()
        

juego = Main()
juego.iniciar_juego()
