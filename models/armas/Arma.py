import abc
   
class Arma(metaclass=abc.ABCMeta):

  # Este metodo sirve para definir cuanto va atacar
  @abc.abstractmethod
  def getAttackPoints(self) -> int:
    pass

  # Este metodo sirve para hacer string
  @abc.abstractmethod
  def __str__(self) -> str:
    pass
  
  