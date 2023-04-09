from models.armas.Espada import Espada
from models.monstruos.Monstruo import Monstruo

from models.eventos.JugadorMuere import JugadorMuere

class Jugador(Monstruo):
  def __init__(self, nombre: str):
    super().__init__(15,Espada(), nombre)

  def recuperarse(self) -> None:
    self.vidaActual += 3
    if self.vidaActual > self.vidaMaxima:
      self.vidaActual = self.vidaMaxima

  def morir(self) -> None:
    self.eventoObservable.on_next(JugadorMuere())
    self.eventoObservable.on_completed()from models.armas.Espada import Espada
from models.monstruos.Monstruo import Monstruo
from models.eventos.JugadorMuere import JugadorMuere
    
class Jugador(Monstruo):
    # Se define una clase llamada Jugador que hereda de la clase Monstruo

    def __init__(self, nombre: str):
        # Constructor de la clase Jugador que recibe un argumento de nombre de tipo str

        super().__init__(15, Espada(), nombre)
        # Se llama al constructor de la clase Monstruo utilizando la función super(), pasando los argumentos 15, Espada() y nombre

    def recuperarse(self) -> None:
        # Método recuperarse no recibe argumentos y no devuelve valor
        self.vidaActual += 3
        # Incrementa valor vidaActual jugador  3

        if self.vidaActual > self.vidaMaxima:
            self.vidaActual = self.vidaMaxima
            # vidaActual jugador no excede vidaMaxima

    def morir(self) -> None:

        self.eventoObservable.on_next(JugadorMuere())     
        
        # Invoca método on_next() del objeto eventoObservable
        # Objeto JugadorMuere() como argumento
        # Indica muerte jugador y notifica a los observadores registrados en el Observable

        self.eventoObservable.on_completed()
        
        # Se invoca el método on_completed() del objeto eventoObservable
        # Esto indica que el Observable ha completado su emisión de eventos
    