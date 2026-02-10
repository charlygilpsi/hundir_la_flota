"""
Módulo que contiene la clase Juego.
Gestiona la lógica principal de la partida.
"""

#Tablero.disparar(x, y) devuelve "TOCADO" o "AGUA"
#Tablero.quedan_barcos() ya existe (o puedes adaptarlo)

class Juego:
    """
    Controla el estado y las reglas del juego Hundir la Flota.
    """

    def __init__(self, tablero, disparos_maximos):
        """
        Inicializa una nueva partida.

        :param tablero: Tablero interno con los barcos.
        :type tablero: Tablero
        :param disparos_maximos: Número máximo de disparos permitidos.
        :type disparos_maximos: int
        """
        self.tablero = tablero
        self.disparos_maximos = disparos_maximos
        self.disparos_realizados = 0
        self.disparos = set()

    def disparar(self, x, y):
        """
        Realiza un disparo sobre el tablero.

        :param x: Coordenada X.
        :type x: int
        :param y: Coordenada Y.
        :type y: int
        :return: Resultado del disparo.
        :rtype: str
        """
        if (x, y) in self.disparos:
            return "REPETIDO"

        self.disparos.add((x, y))
        self.disparos_realizados += 1

        return self.tablero.disparar(x, y)

    def quedan_disparos(self):
        """
        Indica si aún quedan disparos disponibles.

        :return: True si quedan disparos, False en caso contrario.
        :rtype: bool
        """
        return self.disparos_realizados < self.disparos_maximos

    def hay_victoria(self):
        """
        Comprueba si todos los barcos han sido hundidos.

        :return: True si no quedan barcos, False en caso contrario.
        :rtype: bool
        """
        return not self.tablero.quedan_barcos()
