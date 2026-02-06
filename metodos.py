import random

###########
# MÉTODOS #
###########

def crear_tablero(array, ancho, alto, caracter_vacio):
    """
    Genera un tablero bidimensional (lista de listas) con las dimensiones indicadas.

    Cada posición del tablero se inicializa con el carácter especificado como vacío.

    :param array: Lista que contendrá el tablero generado.
    :type array: list
    :param ancho: Número de columnas del tablero.
    :type ancho: int
    :param alto: Número de filas del tablero.
    :type alto: int
    :param caracter_vacio: Carácter utilizado para inicializar cada celda.
    :type caracter_vacio: str
    :return: None
    """
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(caracter_vacio)
        array.append(fila)


def valor_aleatorio(menor, mayor):
    """
    Genera un número entero aleatorio dentro de un rango dado.

    :param menor: Valor mínimo del rango.
    :type menor: int
    :param mayor: Valor máximo del rango.
    :type mayor: int
    :return: Número entero aleatorio entre menor y mayor (ambos incluidos).
    :rtype: int
    """
    return random.randint(menor, mayor)


def es_horizontal():
    """
    Determina aleatoriamente si la orientación es horizontal o vertical.

    :return: True si es horizontal, False si es vertical.
    :rtype: bool
    """
    if valor_aleatorio(0, 1) == 0:
        return True
    else:
        return False


def rellenar_tablero(array, horizontal, tamanyo, x, y, caracter_barco):
    """
    Introduce un barco en el tablero según la orientación indicada.

    El barco se coloca a partir de la posición (x, y) y ocupa tantas
    posiciones como indique su tamaño.

    :param array: Tablero donde se colocará el barco.
    :type array: list
    :param horizontal: Indica si el barco se coloca horizontalmente.
    :type horizontal: bool
    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param x: Coordenada inicial en el eje X.
    :type x: int
    :param y: Coordenada inicial en el eje Y.
    :type y: int
    :param caracter_barco: Carácter que representa al barco.
    :type caracter_barco: str
    :return: None
    """
    if horizontal:
        for i in range(tamanyo):
            array[y][x] = caracter_barco
            x = x + 1
    else:
        for i in range(tamanyo):
            array[y][x] = caracter_barco
            y = y + 1


def ver_tablero(array, alto):
    """
    Muestra por consola el tablero de juego con índices de filas y columnas.

    El tablero se imprime en formato matricial:
    - La primera línea muestra los índices de las columnas.
    - Cada fila se muestra precedida por su índice correspondiente.

    :param array: Tablero bidimensional a mostrar.
    :type array: list[list[str]]
    :param alto: Número de filas del tablero.
    :type alto: int
    :return: None
    """
    encabezado = "   " + " ".join(str(i) for i in range(len(array[0])))
    print(encabezado)

    for i in range(alto):
        fila_str = f"{i:<2} " + " ".join(array[i])
        print(fila_str)


def opcion_valida(valor, opcion_maxima):
    """
    Comprueba si un valor introducido es un número entero dentro de un rango válido.

    :param valor: Valor introducido por el usuario.
    :type valor: str
    :param opcion_maxima: Valor máximo permitido.
    :type opcion_maxima: int
    :return: True si el valor es válido, False en caso contrario.
    :rtype: bool
    """
    return valor.isdigit() and 0 <= int(valor) <= opcion_maxima


def es_numero_entero(valor):
    """
    Comprueba si un valor puede convertirse a número entero.

    :param valor: Valor a comprobar.
    :type valor: str
    :return: True si el valor es un entero válido, False en caso contrario.
    :rtype: bool
    """
    try:
        int(valor)
        return True
    except ValueError:
        return False


def calcular_maximos(tamanyo, alto_o_ancho):
    """
    Calcula el límite máximo para colocar un barco en un eje determinado.

    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param alto_o_ancho: Dimensión total del eje.
    :type alto_o_ancho: int
    :return: Posición máxima permitida.
    :rtype: int
    """
    return alto_o_ancho - tamanyo


def posicion_valida(posicion, maximo):
    """
    Comprueba si una posición se encuentra dentro del límite permitido.

    :param posicion: Posición a comprobar.
    :type posicion: int
    :param maximo: Valor máximo permitido.
    :type maximo: int
    :return: True si la posición es válida, False en caso contrario.
    :rtype: bool
    """
    if posicion <= maximo:
        return True
    else:
        return False


def ya_hay_barco_en_posicion(array, horizontal, tamanyo, x, y, caracter_barco):
    """
    Comprueba si ya existe un barco en las posiciones donde se pretende colocar otro.

    :param array: Tablero donde se realiza la comprobación.
    :type array: list
    :param horizontal: Orientación del barco.
    :type horizontal: bool
    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param x: Coordenada inicial en el eje X.
    :type x: int
    :param y: Coordenada inicial en el eje Y.
    :type y: int
    :param caracter_barco: Carácter que representa al barco.
    :type caracter_barco: str
    :return: True si hay un barco en alguna posición, False en caso contrario.
    :rtype: bool
    """
    if horizontal:
        for i in range(tamanyo):
            if array[y][x] == caracter_barco:
                return True
            x = x + 1
    else:
        for i in range(tamanyo):
            if array[y][x] == caracter_barco:
                return True
            y = y + 1

    return False


def disparo_acertado(array_original, array_copia, x, y):
    """
    Comprueba si un disparo ha impactado en un barco.

    :param array_original: Tablero visible para el jugador.
    :type array_original: list
    :param array_copia: Tablero interno con los barcos.
    :type array_copia: list
    :param x: Coordenada X del disparo.
    :type x: int
    :param y: Coordenada Y del disparo.
    :type y: int
    :return: True si el disparo ha sido acertado, False en caso contrario.
    :rtype: bool
    """
    if array_copia[y][x] == "1":
        return True
    else:
        array_original[y][x] = "O"
        return False


def marcar_disparo(array_original, array_copia, x, y, caracter):
    """
    Marca un disparo en ambos tableros.

    :param array_original: Tablero visible para el jugador.
    :type array_original: list
    :param array_copia: Tablero interno.
    :type array_copia: list
    :param x: Coordenada X del disparo.
    :type x: int
    :param y: Coordenada Y del disparo.
    :type y: int
    :param caracter: Carácter que representa el resultado del disparo.
    :type caracter: str
    :return: None
    """
    array_copia[y][x] = caracter
    array_original[y][x] = caracter


def disparo_repetido(array, x, y, caracter_tocado, caracter_agua):
    """
    Comprueba si el disparo se ha realizado sobre una casilla ya descubierta.

    :param array: Tablero visible para el jugador.
    :type array: list
    :param x: Coordenada X del disparo.
    :type x: int
    :param y: Coordenada Y del disparo.
    :type y: int
    :param caracter_tocado: Carácter que representa un disparo acertado.
    :type caracter_tocado: str
    :param caracter_agua: Carácter que representa un disparo fallido.
    :type caracter_agua: str
    :return: True si el disparo es repetido, False en caso contrario.
    :rtype: bool
    """
    return array[y][x] == caracter_tocado or array[y][x] == caracter_agua


def quedan_barcos(array, ancho, alto):
    """
    Comprueba si quedan barcos sin hundir en el tablero.

    :param array: Tablero donde se realiza la comprobación.
    :type array: list
    :param ancho: Número de columnas del tablero.
    :type ancho: int
    :param alto: Número de filas del tablero.
    :type alto: int
    :return: True si quedan barcos, False si no.
    :rtype: bool
    """
    for i in range(alto):
        for j in range(ancho):
            if array[i][j] == "1":
                return True
    return False


def bucle_generar_barcos(contador, repeticiones, bandera, minimo, tamanyo, ancho, alto, array, caracter_barco):
    """
    Genera y coloca barcos aleatoriamente en el tablero.

    El proceso se repite hasta introducir el número de barcos indicado,
    comprobando que no se solapen entre sí.

    :param contador: Contador interno del número de barcos colocados.
    :type contador: int
    :param repeticiones: Número total de barcos a generar.
    :type repeticiones: int
    :param bandera: Bandera de control del bucle.
    :type bandera: bool
    :param minimo: Valor mínimo para las posiciones aleatorias.
    :type minimo: int
    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param ancho: Ancho del tablero.
    :type ancho: int
    :param alto: Alto del tablero.
    :type alto: int
    :param array: Tablero donde se colocan los barcos.
    :type array: list
    :param caracter_barco: Carácter que representa al barco.
    :type caracter_barco: str
    :return: None
    """
    while contador < repeticiones:
        horizontal = es_horizontal()

        while not bandera:
            posicion_x = valor_aleatorio(minimo, calcular_maximos(tamanyo, ancho))
            posicion_y = valor_aleatorio(minimo, calcular_maximos(tamanyo, alto))
            if not ya_hay_barco_en_posicion(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco):
                rellenar_tablero(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco)
                contador = contador + 1
                if contador == repeticiones:
                    bandera = True

    bandera = False
    contador = 0
