from controlador.juego import Juego
from models.monstruos.Jugador import Jugador

class Main:
    
    def __init__(self):
        self.jugador = self.crearJugador()
        self.juego = Juego(self.jugador)
        
    def crearJugador(self) -> 'jugador':
        nombre = input("Como te llamas? ")
        return Jugador(nombre)