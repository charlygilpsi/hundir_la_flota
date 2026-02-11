"""
Gestiona el flujo principal de la aplicación Hundir la Flota.
Se encarga de coordinar el menú, la creación de partidas y
la ejecución del juego.
"""

from dominio.tablero import Tablero
from dominio.juego import Juego
from dominio.barco import Barco
from interfaz.interfaz_consola import InterfazConsola
from interfaz.menu import Menu
from utils.utils import Util
from utils.excepciones import SalirDelPrograma, VolverAlMenu
from config.textos import TEXTOS


class App:
    """
    Clase principal de la aplicación.

    Orquesta el funcionamiento general del programa:
    - Muestra el menú principal.
    - Crea nuevas partidas.
    - Ejecuta el bucle del juego.
    - Gestiona las excepciones de navegación.
    """

    def __init__(self):
        """
        Inicializa la aplicación.
        """
        validador = Util()
        self.interfaz = InterfazConsola(TEXTOS, validador)
        self.menu = Menu(self.interfaz)

    def ejecutar(self):
        """
        Inicia la ejecución de la aplicación.
        """
        try:
            while True:
                self.menu.ejecutar()
                juego = self._crear_juego()
                self._ejecutar_partida(juego)
        except SalirDelPrograma:
            self.interfaz.fin_programa()

    def _crear_juego(self):
        """
        Crea e inicializa una nueva partida del juego.

        :return: Objeto Juego inicializado.
        :rtype: Juego
        """
        CARACTER_VACIO = "~"
        CARACTER_TOCADO = "X"
        CARACTER_AGUA = "O"
        DISPAROS_MAXIMOS = 50

        portaaviones = Barco(4, 1, "P")
        destructores = Barco(3, 2, "D")
        submarinos = Barco(2, 3, "S")

        barcos = [portaaviones, destructores, submarinos]

        tablero_usuario = Tablero(10, 10, barcos, CARACTER_VACIO)
        tablero_interno = Tablero(10, 10, barcos, CARACTER_VACIO)

        return Juego(
            tablero_usuario,
            tablero_interno,
            DISPAROS_MAXIMOS,
            CARACTER_VACIO,
            CARACTER_TOCADO,
            CARACTER_AGUA
        )

    def _ejecutar_partida(self, juego):
        """
        Ejecuta el bucle principal de una partida.

        :param juego: Instancia del juego en curso.
        :type juego: Juego
        """
        try:
            while juego.quedan_disparos() and not juego.hay_victoria():

                self.interfaz.opcion_volver_menu()

                x, y = self.interfaz.pedir_disparo(
                    juego.tablero_barco.ancho,
                    juego.tablero_barco.alto
                )

                resultado = juego.disparar(x, y)

                self.interfaz.borrar_consola()
                self.interfaz.mostrar_resultado(resultado)
                self.interfaz.mostrar_tablero(juego.tablero_usuario)
                self.interfaz.mostrar_balas(juego.disparos_restantes())

            self.interfaz.mostrar_mensaje_final(juego.hay_victoria())

        except VolverAlMenu:
            self.interfaz.borrar_consola()
