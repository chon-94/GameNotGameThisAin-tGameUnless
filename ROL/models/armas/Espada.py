# Importación de la clase abstracta "Arma" desde el módulo "models.armas"
from models.armas.Arma import Arma

# Definición de la clase "Espada" que deriva de la clase abstracta "Arma"


class Espada(Arma):

    # Implementación del método abstracto "getAttackPoints" para la clase "Espada"
    def getAttackPoints(self) -> int:
        return 3

    # Implementación del método abstracto "__str__" para la clase "Espada"
    def __str__(self) -> str:
        return "Espada"
