"""
Punto de entrada del juego Hundir la Flota.
"""

from dominio.tablero import Tablero
from dominio.juego import Juego
from dominio.barco import Barco
from interfaz.interfaz_consola import InterfazConsola
from utils.utils import Util
from config.textos import TEXTOS


def main():
    """
    Ejecuta el juego Hundir la Flota.
    """
    validador = Util()
    interfaz = InterfazConsola(TEXTOS, validador)

    # Crear barcos
    portaaviones = Barco(4, 1, "P")
    destructores = Barco(3, 2, "D")
    submarinos = Barco(2, 3, "S")

    barcos = [portaaviones, destructores, submarinos]

    # Crear tablero y juego
    tablero = Tablero(10, 10, barcos)
    juego = Juego(tablero, disparos_maximos=50)

    while juego.quedan_disparos() and not juego.hay_victoria():
        x = interfaz.pedir_coordenada("x", tablero.ancho - 1)
        y = interfaz.pedir_coordenada("y", tablero.alto - 1)

        resultado = juego.disparar(x, y)
        interfaz.mostrar_resultado(resultado)
        interfaz.mostrar_balas(juego.disparos_maximos - juego.disparos_realizados)

        tablero.ver_tablero()

    interfaz.mostrar_mensaje_final(juego.hay_victoria())


if __name__ == "__main__":
    main()
