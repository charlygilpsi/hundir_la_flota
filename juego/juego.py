class Juego:
    """
    Representa una partida de Hundir la Flota.
    Gestiona el estado del juego y las reglas.
    """

    def __init__(self, tablero, barcos, balas):
        """
        :param tablero: Tablero del juego
        :type tablero: Tablero
        :param barcos: Lista de barcos activos
        :type barcos: list[Barco]
        :param balas: Número de disparos disponibles
        :type balas: int
        """
        self.tablero = tablero
        self.barcos = barcos
        self.balas = balas
        self.disparos_realizados = set()
        self.barcos_restantes = len(barcos)

    def disparar(self, x, y):
        """
        Realiza un disparo en la posición indicada.

        :param x: Coordenada X
        :type x: int
        :param y: Coordenada Y
        :type y: int
        :return: Resultado del disparo
        :rtype: str
        """
        if self.balas <= 0:
            return "SIN_BALAS"

        if (x, y) in self.disparos_realizados:
            return "REPETIDO"

        self.disparos_realizados.add((x, y))
        self.balas -= 1

        impacto = self.tablero.comprobar_disparo(x, y)

        if impacto == "TOCADO":
            if self.tablero.barco_hundido(x, y):
                self.barcos_restantes -= 1
            return "TOCADO"

        return "AGUA"

    def ha_ganado(self):
        """
        Comprueba si el jugador ha ganado.
        """
        return self.barcos_restantes == 0

    def ha_perdido(self):
        """
        Comprueba si el jugador ha perdido.
        """
        return self.balas <= 0 and not self.ha_ganado()

    def estado_partida(self):
        """
        Devuelve el estado actual de la partida.
        """
        if self.ha_ganado():
            return "VICTORIA"
        if self.ha_perdido():
            return "DERROTA"
        return "EN_CURSO"
