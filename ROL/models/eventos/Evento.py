# Importación de los módulos "abc" y "typing"
import abc
import typing

# Chequeo de tipos estáticos usando el módulo "typing"
if typing.TYPE_CHECKING:
    # Importación de la clase "Juego" desde el módulo "controlador.juego"
    from controlador.juego import Juego

# Definición de la clase abstracta "Evento" que utiliza el metaclass "abc.ABCMeta"


class Evento(metaclass=abc.ABCMeta):

    # Definición del método abstracto "visitarJuego" que toma un argumento "juego" de tipo 'juego'
    @abc.abstractmethod
    def visitarJuego(self, juego: 'Juego'):
        pass
