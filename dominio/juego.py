"""
Módulo que contiene la clase Juego.
Gestiona la lógica principal de la partida.
"""

class Juego:
    """
    Controla el estado y las reglas del juego Hundir la Flota.
    """

    def __init__(self, tablero, disparos_maximos, caracter_vacio, caracter_tocado, caracter_agua):
        """
        Inicializa una nueva partida.

        :param tablero: Objeto tablero.
        :type tablero: Tablero
        :param disparos_maximos: Número máximo de disparos permitidos.
        :type disparos_maximos: int
        :param caracter_vacio: Carácter para casillas vacías.
        :type caracter_vacio: str
        :param caracter_tocado: Carácter para disparos acertados.
        :type caracter_tocado: str
        :param caracter_agua: Carácter para disparos fallidos.
        :type caracter_agua: str
        """
        self.tablero = tablero
        self.disparos_maximos = disparos_maximos
        self.disparos_realizados = 0

        self.caracter_vacio = caracter_vacio
        self.caracter_tocado = caracter_tocado
        self.caracter_agua = caracter_agua
        array_caracteres = []

        for barco in self.tablero.barcos:
            array_caracteres.append(barco.caracter)

        # Tableros
        self.tablero_usuario = []
        self.tablero_barcos = []

        # Inicialización
        self.tablero.crear_tablero(self.tablero_usuario, self.caracter_vacio)
        self.tablero.crear_tablero(self.tablero_barcos, self.caracter_vacio)

        for i in range(3):
            self.tablero.generar_barcos(self.tablero_barcos, self.tablero.barcos[i], array_caracteres)


    def disparar(self, x, y, array_caracteres):
        """
        Realiza un disparo sobre el tablero.

        :param x: Coordenada X.
        :type x: int
        :param y: Coordenada Y.
        :type y: int
        :param array_caracteres: Lista de caracteres de barcos.
        :type array_caracteres: list
        :return: Resultado del disparo.
        :rtype: str
        """
        if self.tablero.disparo_repetido(
            self.tablero_usuario, x, y, self.caracter_tocado, self.caracter_agua
        ):
            return "REPETIDO"

        self.disparos_realizados += 1

        if self.tablero.comprobar_acierto(self.tablero_barcos, x, y, array_caracteres):
            self.tablero.marcar_disparo(
                self.tablero_usuario,
                self.tablero_barcos,
                x,
                y,
                self.caracter_tocado
            )
            return "TOCADO"
        else:
            self.tablero.marcar_disparo(
                self.tablero_usuario,
                self.tablero_barcos,
                x,
                y,
                self.caracter_agua
            )
            return "AGUA"


    def quedan_disparos(self):
        """
        Indica si aún quedan disparos disponibles.

        :return: True si quedan disparos, False en caso contrario.
        :rtype: bool
        """
        return self.disparos_realizados < self.disparos_maximos


    def hay_victoria(self, array_caracteres):
        """
        Comprueba si quedan barcos en el tablero interno.

        :param array_caracteres: Lista de caracteres de barcos.
        :type array_caracteres: list
        :return: True si no quedan barcos.
        :rtype: bool
        """
        return not self.tablero.quedan_barcos(self.tablero_barcos, array_caracteres)
