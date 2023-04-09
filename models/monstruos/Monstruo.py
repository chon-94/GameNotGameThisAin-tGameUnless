import abc
# Importa módulo abc para trabajar con clases abstractas

import typing
# Importa módulo typing para utilizar la anotación de tipo TYPE_CHECKING

from rx.subject import Subject
# Importa clase Subject módulo rx.subject para trabajar con Observables

from models.eventos.MostruoMuere import MostruoMuere
# Importa clase MostruoMuere módulo models.eventos.MostruoMuere para utilizarla método morir()


if typing.TYPE_CHECKING:
    from models.armas.Arma import Arma
    from models.eventos.Evento import Evento
    # Anotación TYPE_CHECKING para importar clases Arma y Evento únicamente para comprobación de tipos

class Monstruo(metaclass=abc.ABCMeta):
# Define clase abstracta Monstruo utiliza metaclase ABCMeta

    def __init__(self, VidaMaxima: int, arma: "Arma", nombre: str):
    # Constructor clase Monstruo recibe 3 argumentos: VidaMaxima  int, arma class y nombre str

        self.vidaMaxima = VidaMaxima
        self.arma = arma
        self.nombre = nombre
        self.vidaActual = VidaMaxima
        # Inicializan los atributos de la clase Monstruo: vidaMaxima, arma, nombre y vidaActual

        self.eventoObservable: Subject["Evento"] = Subject()
        # Crea objeto Subject llamado eventoObservable para trabajar Observables se anota tipo"Evento"

    def getAttackPoints(self) -> int:
        # Método getAttackPoints no recibe argumentos devuelve 1 valo int

        return self.arma.getAttackPoints()
        # Método getAttackPoints() objeto arma de instancia de clase Monstruo se devuelve valor

    def recibirDanmange(self, monstruo: "Monstruo") -> None:
        # Método recibirDanmange recibe argumento monstruo tipo Monstruo no devuelve ningún valor

        self.vidaActual -= monstruo.getAttackPoints()
        # Resta cantidad puntos ataque del monstruo atacante valor vidaActual jugador receptor

        if self.vidaActual < 0:
        # Si valor de vidaActual menor a 0, vidaActual es 0
            
            self.vidaActual = 0
            # Garantiza que vidaActual jugador no sea negativa

        self.morir()
        # Invoca método morir() jugador receptor

    def atacar(self, monstruoReceptor: "Monstruo") -> None:
    # Método atacar recibe argumento monstruoReceptor tipo Monstruo no devuelve valor

        monstruoReceptor.recibirDanmange(self)
        # Invoca método recibirDanmange() jugador receptor, pasando como argumento
        # El jugador receptor recibirá daño del monstruo atacante

    def morir(self) -> None:
    # Método morir no recibe argumentos no devuelve valor

        self.eventoObservable.on_next(JugadorMuere())
        # El método on_next() del objeto eventoObservable 
        # Objeto JugadorMuere() como argumento
        # Esto indica que el jugador ha muerto notifica a los observadores registrados en el Observable

        self.eventoObservable.on_completed()
        # El método on_completed() del objeto eventoObservable
        # Indica que Observable completado emisión eventos
