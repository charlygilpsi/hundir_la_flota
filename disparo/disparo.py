class Disparo:
    def __init__(self, x, y):
        """
        Representa un disparo dentro del juego.
        
        :param x: coordenada x del disparo.
        :type x: int
        :param y: coordenada y del disparo.
        :type y: int
        """
        self.x = x
        self.y = y
        self.acertado = None  # None = no resuelto, True/False tras comprobar


    def comprobar_acierto(self, array_copia, array_caracteres):
        """
        Determina si el disparo impacta en un barco.

        :param array_copia: Tablero interno con los barcos.
        :type array_copia: list
        :param array_caracteres: Lista de caracteres de barco (portaaviones, destructor, submarino).
        :type array_caracteres: list
        :return: True si el disparo ha sido acertado, False en caso contrario.
        :rtype: bool
        """
        self.acertado = array_copia[int(self.y)][int(self.x)] in array_caracteres
        return self.acertado 