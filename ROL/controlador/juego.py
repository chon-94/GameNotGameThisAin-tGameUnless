import typing

from rx.subject import Subject

from models.monstruos.IchicOllko import IchicOllko

if typing.TYPE_CHECKING:
    from models.monstruos.Jugador import Jugador
    from models.eventos.Evento import Evento
    from models.monstruos.Monstruo import Monstruo


class juego:

    def __init__(self, jugador: 'Jugador'):
        self.jugador = Jugador(nombre)
        # Asigna la instancia de la clase Jugador a la variable self.jugador

    def __init__(self, jugador: 'Jugador'):
        # Se asigna el objeto 'jugador' al atributo 'jugador' de la instancia.
        self.jugador = jugador
        # Se crea una instancia de la clase IchicOllko y se asigna a 'monstruoActual'.
        self.monstruoActual = IchicOllko()
        # Se crea una lista con dos instancias de IchicOllko y se asigna a 'monstruoLista'.
        self.monstruoLista = [IchicOllko(), IchicOllko()]

        self.jugadorDisposable =\
            self.jugador.eventoObservable.subscribe(self.aceptarEvento)
        # Se crea una suscripción al eventoObservable del 'jugador' y se llama al método 'aceptarEvento' cuando se recibe un evento.

        self.monstruoActualDisposable =\
            self.monstruoActual.eventoObservable.subscribe(self.aceptarEvento)
        # Se crea una suscripción al eventoObservable del 'monstruoActual' y se llama al método 'aceptarEvento' cuando se recibe un evento.

        self.resultado: Subject[bool] = Subject()
        # Se crea un Subject llamado 'resultado' que emite eventos de tipo bool.

        self.nombreSiguienteMonstruo: Subject[str] = Subject()
        # Se crea un Subject llamado 'nombreSiguienteMonstruo' que emite eventos de tipo str (cadena de texto).

    def liberar(self) -> None:

        self.jugadorDiposable.dispose()
        # Método dispose()

        self.monstruoActualDisposable.dispose()
        # Método dispose()

    def ganar(self) -> None:

        self.liberar()
        # Llama al método liberar()

        self.resultado.on_next(True)
        # Emite el valor True en Subject resultado usando método on_next()

        self.resultado.on_completed()
        # Emite la señal de completado en    Subject resultado usando método on_completed()

    def perder(self) -> None:

        self.liberar()
        # Llama al método liberar()
        self.resultado.on_next(False)
        self.resultado.on_completed()

    def aceptarEvento(self, evento: 'Evento') -> None:
        evento.visitarJuego(self)

    def pasarAsiguienteMonstruo(self) -> None:
        self.monstruoActualDisposable.dispose()
        if len(self.monstruoLista) == 0:
            self.ganar()
        else:
            self.monstruoActual = self.monstruoLista.pop()
            self.monstruoActualDisposable =\
                self.monstruoActual.eventoObservable.subscribe(
                    self.aceptarEvento)
            self.nombreSiguienteMonstruo.on_nexL(self.monstruoActual.__str__())

    def interaccion(self, monstruoAtacante: 'Monstruo',
                    monstruoAtacado: 'Monstruo') -> str:
        monstruoAtacante.atacar(monstruoAtacado)
        return "{}recibido daño".format(monstruoAtacado.__str())

    def jugadorAtaca(self) -> str:
        return self.interaccion(self.jugador, self.monstruoAtacado)

    def monstruoAtaca(self) -> str:
        return self.interaccion(self.monstruoActual, self.jugador)

    def comenzar(self) -> None:
        self.nombreSiguienteMonstruo.on_next(self.monstruoActual.__str__())
