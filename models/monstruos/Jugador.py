from models.armasEspada import Espada
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
    self.eventoObservable.on_completed()