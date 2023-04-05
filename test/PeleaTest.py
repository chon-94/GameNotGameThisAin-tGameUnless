from models.monstruos.IchicOllko import IchicOllko

import typing

if typing.TYPE_CHECKING:
  from models.monstruos.Monstruo import Monstruo


def recibirDamangeTest(monstruoAtacante: "Monstruo"):
  ichicollko = IchicOllko()
  VidaInicial = ichicollko.VidaActual

  for _ in range(3):
    monstruoAtacante.atacar(ichicollko)

  assert ichicollko.vidaActual < VidaInicial


def tests():
  recibirDamangeTest(IchicOllko())
