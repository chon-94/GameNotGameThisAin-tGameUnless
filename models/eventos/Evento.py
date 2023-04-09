import abc
import typing

if typing.TYPE_CHECKING:
  from controlador.juego import Juego
  
  

class Evento (metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def visitarJuego(self,juego:'juego'):
    pass