"""
Interfaz de consola del juego Hundir la Flota.
"""

class InterfazConsola:
    """
    Gestiona la interacción con el usuario por consola.
    """

    def __init__(self, textos, validador):
        """
        :param textos: Diccionario de textos del juego.
        :type textos: dict
        :param validador: Objeto validador.
        :type validador: Util
        """
        self.textos = textos
        self.validador = validador

    def pedir_coordenada(self, eje, limite):
        """
        Solicita una coordenada válida al usuario.

        :param eje: Eje ('x' o 'y').
        :type eje: str
        :param limite: Valor máximo permitido.
        :type limite: int
        :return: Coordenada válida.
        :rtype: int
        """
        while True:
            valor = input(self.textos[f"TEXTO_POSICION_{eje.upper()}"])

            if not self.validador.es_numero_entero(valor):
                print(self.textos["ERROR_NUMERO_ENTERO"])
                continue

            if not self.validador.opcion_valida(valor, limite):
                print(self.textos["ERROR_LIMITE_TABLERO"])
                continue

            return int(valor)


    def mostrar_resultado(self, resultado):
        """
        Muestra el resultado del disparo.

        :param resultado: Resultado del disparo.
        :type resultado: str
        """
        print(self.textos[f"TEXTO_{resultado}"])


    def mostrar_tablero(self, tablero, array):
        """
        Muestra el tablero visible al usuario.

        :param tablero: Objeto tablero.
        :type tablero: Tablero
        :param array: Tablero a mostrar.
        :type array: list
        """
        print("")
        tablero.ver_tablero(array)
        print("")


    def mostrar_balas(self, restantes):
        """
        Muestra las balas restantes.

        :param restantes: Número de disparos restantes.
        :type restantes: int
        """
        print(self.textos["TEXTO_BALAS_RESTANTES"], restantes)


    def mostrar_mensaje_final(self, victoria):
        """
        Muestra el mensaje final del juego.

        :param victoria: Indica si el jugador ha ganado.
        :type victoria: bool
        """
        if victoria:
            print(self.textos["TEXTO_VICTORIA"])
        else:
            print(self.textos["TEXTO_DERROTA"])
