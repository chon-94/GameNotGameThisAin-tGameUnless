import abc
import typing

from rx.subject import Subject

from models.eventos.MostruoMuere import MostruoMuere

if typing.TYPE_CHECKING:
  from models.armas.Arma import Arma
  from models.eventos.Evento import Evento

class Monstruo(metaclass=abc.ABCMeta):

  def __init__(self,VidaMaxima: int, arma:"Arma", nombre: str):
    
    self.vidaMaxima=VidaMaxima
    self.arma=arma
    self.nombre=nombre
    self.VidaActual=VidaMaxima
    self.eventoObservable: Subject ["Evento"]= Subject()    

  def getAttackPoints(self) -> int:
    return self.arma.getAttackPoints()

  def recibirdamange(self, monstruo: "Monstruo") -> None:
    self.vidaActual -= monstruo.getAttackPoints()
    if self.vidaActual < 0:
      self.vidaActual = 0
      self.morir()
      
  def atacar(self, monstruoReceptor: "Monstruo") -> None:
    monstruoReceptor.recibirDamange(self)

  def morir(self) -> None:
    self.eventoObservable.on_next(MostruoMuere())
    self.eventoObservable.on_completed()