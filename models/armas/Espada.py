from models.armas.Arma import Arma

class Espada(Arma):

  def getAttackPoints(self) -> int:
    return 3
    
  def __str__(self) -> str:
    return "Espada"