from models.eventos.Evento import Evento
# Importa clase Evento módulo models.eventos.Evento

import typing

if typing.TYPE_CHECKING:
    from controlador.juego import juego
    # Si cumple condición TYPE_CHECKING, importa clase juego módulo controlador.juego.


class jugadorMuere(Evento):
    # Define la clase jugadorMuere que hereda de la clase Evento.

    def visitarJuego(self, juego: 'juego'):
        # D efine método visitarJuego toma 1 instancia de clase juego como argumento.

        juego.perder()
