import typing

if typing.TYPE_CHECKING:
    from models.monstruos.Jugador import Jugador
    from models.eventos.Evento import Evento
    
class juego:
    def __init__(self, jugador:'Jugador'):
        self.jugador = Jugador(nombre) 
        # Asigna la instancia de la clase Jugador a la variable self.jugador

    
    
    def __inint__(self,jugador:'Jugador'):
        self.jugador = jugador
        self.monstruoActual= IchicOllko()
        self.monstruoLista = [IchicOllko(),IchicOllko()]
        
        self.jugadorDisposable = \
            self.jugador.eventoObservable.subscribe(self.aceptarEvento)
        
        self.monstruoActualDisposable= \
            self.monstruoActual.eventoObservable.subscribe(self.aceptarEvento)
            
        self.resultado: Subject[bool] = Subject()
        self.nombreSiguienteMonstruo: Subject[str()] = subject()


    def __inint__(self,jugador:'Jugador'):
        
        self.jugador = jugador 
        # Asigna la instancia de clase Jugador pasada como argumento a la variable self.jugador
        
        self.monstruoActual= IchicOllko() 
        # Crea instancia de clase IchicOllko y asigna la variable self.monstruoActual
        
        self.monstruoLista = [IchicOllko(),IchicOllko()] 
        # Crea lista con instancias de la clase IchicOllko y la asigna a la variable self.monstruoLista

        self.jugadorDisposable.eventoObservable.subscribe() 
        # Suscribe eventoObservable jugador a disposable 
        
        self.monstruoActualDisposable= \
            self.monstruoActual.eventoObservable.subscribe() 
            # Suscribe eventoObservable monstruo actual a disposable

        self.resultado: Subject[bool] = Subject() 
        # Crea instancia de clase Subject tipo dato bool y asigna variable self.resultado
        
        self.nombreSiguienteMonstruo: Subject[str()] = subject() 
        # Crea instancia clase Subject tipo dato str  asigna  variable self.nombreSiguienteMonstruo

        
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
        
        self.jugadorDiposable.dispose(False ) 
        # Llama al método dispose()
        self.monstruoActualDisposable.dispose() 
        # Llama al método dispose()
        
    def aceptarEvento(self,evento:'Evento') -> None:
        evento.visitarJuego(self)
        
    def pasarAsiguienteMonstruo(self) -> None:
        self.monstruoActualDisposable.dispose()
        if len(self.monstruoLista)==0:
            self.ganar()
        else:
            self.monstruoActual = self.monstruoLista.pop()
            self.monstruoActualDisposable=\
                self.monstruoActual.eventoObservable.subscribe(self.aceptarEvento)
            self.nombreSiguienteMonstruo.on_nexL(self.monstruoActual.__str__())
    
    def interaccion(self,
                    monstruoAtacante:'Monstruo',
                    monstruoAtacado:'Monstruo') -> str :
        monstruoAtacante.atacar(monstruoAtacado)
        return"{}recibido daño".format(monstruoAtacado.__str())
        
    def jugadorAtaca(self) -> str:
        return self.interaccion(self.jugador, self.monstruoAtacado)
    
    def monstruoAtaca(self) -> str:
        return self.interaccion(self.monstruoActual,self.jugador)
    
    def comenzar(self) -> None:
        self.nombreSiguienteMonstruo.on_next(self.monstruoActual.__str__(x`x`))
    
    