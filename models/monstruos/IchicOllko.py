from models.armas.Espada import Espada
from models.monstruos.Monstruo import Monstruo

class IchicOllko(Monstruo):
  def __init__(self):
    super().__init__(5,Espada(),"IchicOllko")