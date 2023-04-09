import typing

from test import test

from models.monstruos.IchicOllko import IchicOllko

if typing.TYPE_CHECKING:
  from models.monstruos.Monstruo import Monstruo


def recibirDamangeTest(monstruoAtacante: "Monstruo"):
  ichicollko = IchicOllko()
  VidaInicial = ichicollko.VidaActual
  ichicollko.eventoObservable.subscribe(
    lambda evento: print(evento)
  )
  
  for _ in range(3):
    monstruoAtacante.atacar(ichicollko)

  assert ichicollko.vidaActual < VidaInicial
  assert ichicollko.vidaActual == 0
  tests.pelea_test()
  

def tests():
  recibirDamangeTest(IchicOllko())
