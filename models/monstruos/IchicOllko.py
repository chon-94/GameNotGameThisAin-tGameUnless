from models.armasEspada import Espada
from models.monstruos.Monstruo import Monstruo

class Goblin(Monstruo):
  def __init__(self):
    super().__init__(5,Espada(),"Goblin")