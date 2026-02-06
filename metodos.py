import random

###########
# MÉTODOS #
###########

# Genera un array bidimensional en función del ancho y alto introducidos
def crear_tablero(array, ancho, alto, caracter_vacio):
        for i in range(alto):
            fila = []
            for j in range(ancho):
                fila.append(caracter_vacio)
            array.append(fila)

# Genera un valor aleatorio para un rango dado
def valor_aleatorio(menor, mayor):
    return random.randint(menor, mayor)

# Establece si la posición es horizontal o vertical de forma aleatoria
def es_horizontal():
    if valor_aleatorio(0, 1) == 0:
        return True
    else:
        return False

# Introduce un barco dentro del array
def rellenar_tablero(array, horizontal, tamanyo, x, y, caracter_barco):
        if horizontal:
            for i in range(tamanyo):
                array[y][x] = caracter_barco
                x = x + 1
        else:
            for i in range(tamanyo):
                array[y][x] = caracter_barco
                y = y + 1

# Imprime por consola el tablero
def ver_tablero(array, alto):
    for i in range(alto):
        print(array[i])

# Comprueba si la opción introducida es un entero dentro del rango
def opcion_valida(valor, opcion_maxima):
    return valor.isdigit() and 0 <= int(valor) <= opcion_maxima

# Comprueba si el valor introducido es un número entero
def es_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Calcula el límite para los ejes x o y 
def calcular_maximos(tamanyo, alto_o_ancho):
    return alto_o_ancho - tamanyo

# Comprueba que la posicón dada no supere el límite
# El límite se obtiene en calcular_maximos()
def posicion_valida(posicion, maximo):
    if posicion <= maximo:
        return True
    else:
        return False

# Comprueba si hay un 1 (barco) en las posiciones del array copia
def ya_hay_barco_en_posicion(array, horizontal, tamanyo, x, y, caracter_barco):
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

# Comprobar si el disparo ha dado en un barco
def disparo_acertado(array_original, array_copia, x, y):
    if array_copia[y][x] == "1":
        return True
    else:
        array_original[y][x] = "O"
        return False
    
# Marcar con fallo o acierto los arrays
def marcar_disparo(array_original, array_copia, x, y, caracter):
    array_copia[y][x] = caracter
    array_original[y][x] = caracter
    
# Comprobar si el disparo ha dado en una casilla ya descubierta
def disparo_repetido(array, x, y, caracter_tocado, caracter_agua):
    return array[y][x] == caracter_tocado or array[y][x] == caracter_agua

# Comprobar si quedan barcos sin hundir
def quedan_barcos(array, ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            if array[i][j] == "1":
                return True
    return False

# Función para generar barcos
def bucle_generar_barcos(contador, repeticiones, bandera, minimo, tamanyo, ancho, alto, array, caracter_barco):
    while contador < repeticiones: # Se introducen x barcos, hasta que no se introduzcan se repite el bucle
        horizontal = es_horizontal()

        while not bandera: # Bucle anidado que se repite hasta que la bandera está en True
            posicion_x = valor_aleatorio(minimo, calcular_maximos(tamanyo, ancho))
            posicion_y = valor_aleatorio(minimo, calcular_maximos(tamanyo, alto))
            if not ya_hay_barco_en_posicion(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco): # Comprobar si hay barco en las posiciones dadas
                rellenar_tablero(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco) # Si no lo hay, introducir barco
                contador = contador + 1 # Contador del bucle principal
                if contador == repeticiones:
                    bandera = True # Fin del bucle

    bandera = False # Reiniciar bandera y contador para próximos usos
    contador = 0