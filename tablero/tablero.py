class Tablero():
    def __init__(self, ancho, alto):
        """
        Inicializa un tablero bidimensional.
        
        :param ancho: número de columnas.
        :type tamanyo: int
        :param alto: número de filas.
        :type tamanyo: int
        :param alto: Description
        """
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self, array, caracter_vacio):
        """
        Genera un tablero bidimensional (lista de listas) con las dimensiones indicadas.

        Cada posición del tablero se inicializa con el carácter especificado como vacío.

        :param array: Lista que contendrá el tablero generado.
        :type array: list
        :param caracter_vacio: Carácter utilizado para inicializar cada celda.
        :type caracter_vacio: str
        :return: None
        """
        for i in range(self.alto):
            fila = []
            for j in range(self.ancho):
                fila.append(caracter_vacio)
            array.append(fila)


    def rellenar_tablero(self, array, barco, x, y):
        """
        Introduce un barco en el tablero según la orientación indicada.

        El barco se coloca a partir de la posición (x, y) y ocupa tantas
        posiciones como indique su tamaño.

        :param array: Tablero donde se colocará el barco.
        :type array: list
        :param x: Coordenada inicial en el eje X.
        :type x: int
        :param y: Coordenada inicial en el eje Y.
        :type y: int
        :return: None
        """
        if barco.horizontal:
            for i in range(barco.tamanyo):
                array[y][x] = barco.caracter
                x = x + 1
        else:
            for i in range(barco.tamanyo):
                array[y][x] = barco.caracter
                y = y + 1


    def ver_tablero(self, array):
        """
        Muestra por consola el tablero de juego con índices de filas y columnas.

        El tablero se imprime en formato matricial:
        - La primera línea muestra los índices de las columnas.
        - Cada fila se muestra precedida por su índice correspondiente.

        :param array: Tablero bidimensional a mostrar.
        :type array: list[list[str]]
        :return: None
        """
        encabezado = "   " + " ".join(str(i) for i in range(len(array[0])))
        print(encabezado)

        for i in range(self.alto):
            fila_str = f"{i:<2} " + " ".join(array[i])
            print(fila_str)


    def comprobar_caracter(self, array, array_caracteres):
        for i in range(self.alto):
            for j in range(self.ancho):
                for caracter in array_caracteres:
                    if array[i][j] == caracter:
                        return True
        return False

    def ya_hay_barco_en_posicion(self, array, barco, x, y, array_caracteres):
        """
        Comprueba si ya existe un barco en las posiciones donde se pretende colocar otro.

        :param array: Tablero donde se realiza la comprobación.
        :type array: list
        :param x: Coordenada inicial en el eje X.
        :type x: int
        :param y: Coordenada inicial en el eje Y.
        :type y: int
        :param array_caracteres: Lista de caracteres de barco (portaaviones, destructor, submarino).
        :type array_caracteres: list
        :return: True si hay un barco en alguna posición, False en caso contrario.
        :rtype: bool
        """
        if barco.horizontal:
            for i in range(barco.tamanyo):
                for caracter in array_caracteres:
                    if array[y][x] == caracter:
                        return True
                x = x + 1
        else:
            for i in range(barco.tamanyo):
                for caracter in array_caracteres:
                    if array[y][x] == caracter:
                        return True
                y = y + 1

        return False


    def quedan_barcos(self, array, array_caracteres):
        """
        Comprueba si quedan barcos sin hundir en el tablero.

        :param array: Tablero donde se realiza la comprobación.
        :type array: list
        :param array_caracteres: Lista de caracteres de barco (portaaviones, destructor, submarino).
        :type array_caracteres: list
        :return: True si quedan barcos, False si no.
        :rtype: bool
        """
        for i in range(self.alto):
            for j in range(self.ancho):
                for caracter in array_caracteres:
                    if array[i][j] == caracter:
                        return True
        return False


    def generar_barcos(self, contador, repeticiones, bandera, minimo, array, barco, util, array_caracteres):
        """
        Genera y coloca barcos aleatoriamente en el tablero.

        El proceso se repite hasta introducir el número de barcos indicado,
        comprobando que no se solapen entre sí.

        :param contador: Contador interno del número de barcos colocados.
        :type contador: int
        :param repeticiones: Número total de barcos a introducir en el tablero.
        :type repeticiones: int
        :param bandera: Bandera de control del bucle.
        :type bandera: bool
        :param minimo: Valor mínimo para las posiciones aleatorias.
        :type minimo: int
        :param array: Tablero donde se colocan los barcos.
        :type array: list
        :param array_caracteres: Lista de caracteres de barco (portaaviones, destructor, submarino).
        :type array_caracteres: list
        :return: None
        """
        while contador < repeticiones:
            barco.horizontal = barco.es_horizontal()

            while not bandera:
                posicion_x = util.valor_aleatorio(minimo, barco.calcular_maximo(barco.tamanyo, self.ancho))
                posicion_y = util.valor_aleatorio(minimo, barco.calcular_maximo(barco.tamanyo, self.alto))
                if not self.ya_hay_barco_en_posicion(array, barco, posicion_x, posicion_y, array_caracteres):
                    self.rellenar_tablero(array, barco, posicion_x, posicion_y)
                    contador = contador + 1
                    if contador == repeticiones:
                        bandera = True

        bandera = False
        contador = 0