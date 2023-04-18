from models.eventos.Evento import Evento


class IchicOllkoMuere(Evento):
    def visitarJuego(self, juego: 'juego'):
        juego.pasarASiguienteMonstruo()
