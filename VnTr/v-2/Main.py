# Importamos la clase Jugador desde el archivo jugador.py
from jugador import Jugador


def main():
    # Creamos una instancia de la clase Jugador
    jugador = Jugador()

    # Creamos una instancia de la clase Enemigo, pasando la vida del jugador como argumento
    enemigo = Enemigo(jugador.vida * 2)

    # Llamamos al método asignar_puntos para que el jugador pueda asignar puntos a sus habilidades
    jugador.asignar_puntos()

    # Llamamos al método mostrar_habilidades para mostrar las habilidades del jugador
    jugador.mostrar_habilidades()

    # Mostramos la vida del enemigo
    enemigo.mostrar_vida()
