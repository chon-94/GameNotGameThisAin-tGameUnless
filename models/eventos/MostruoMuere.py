from models.eventos.Evento import Evento
# Importa clase Evento módulo models.eventos.Evento

import typing

if typing.TYPE_CHECKING:
    from controlador.juego import juego

class MonstruoMuere(Evento):  
# Define clase MonstruoMuere hereda de la clase Evento.

    def visitarJuego(self, juego: 'juego'):  
    # Define método visitarJuego toma instancia de clase juego como argumento.
        
        juego.pasarAsiguienteMonstruo()  
        # Llama método pasarAsiguienteMonstruo() en instancia juego pasada como argumento.
