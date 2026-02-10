class Interfaz:
    """
    Gestiona la interacción con el usuario por consola.
    """

    def __init__(self, textos):
        """
        :param textos: Diccionario de textos del juego
        :type textos: dict[str, str]
        """
        self.textos = textos


    def pedir_coordenada(self, eje):
        """
        Solicita una coordenada al usuario.

        :param eje: 'x' o 'y'
        :type eje: str
        :return: Coordenada introducida
        :rtype: int
        """
        while True:
            try:
                return int(input(self.textos[f"TEXTO_POSICION_{eje.upper()}"]))
            except ValueError:
                print(self.textos["ERROR_NUMERO_ENTERO"])


    def mostrar_resultado_disparo(self, resultado):
        """
        Muestra el resultado de un disparo.
        """
        if resultado == "TOCADO":
            print(self.textos["TEXTO_TOCADO"])
        elif resultado == "AGUA":
            print(self.textos["TEXTO_AGUA"])
        elif resultado == "REPETIDO":
            print(self.textos["TEXTO_REPETIDO"])


    def mostrar_balas(self, balas):
        """
        Muestra las balas restantes.
        """
        print(f"{self.textos['TEXTO_BALAS_RESTANTES']}{balas}")


    def mostrar_fin_partida(self, estado):
        """
        Muestra el mensaje final de la partida.
        """
        if estado == "VICTORIA":
            print(self.textos["TEXTO_VICTORIA"])
        elif estado == "DERROTA":
            print(self.textos["TEXTO_DERROTA"])
