import disparo.disparo as disparo
import tablero.tablero as tablero
import barco.barco as barco
import utils.utils as util
import os

#Objetos
portaaviones = barco.Barco(4, "P")
destructor = barco.Barco(2, "D")
submarino = barco.Barco(1, "S")
tablero_objeto = tablero.Tablero(10, 10)
validator = util.Util()

#Variables
tablero_usuario = [] # Array que se muestra al usuario con los disparos
tablero_barcos = [] # Array copia donde guardar las posiciones de los barcos
victoria = False # Banderas para saber cuándo finalizar los bucles
coordenadas_validas = False # Banderas para saber cuándo finalizar los bucles
contador = 0 # Contador para bucles
posicion_x = 0 # Coordenada X
posicion_y = 0 # Coordenada Y

# Constantes
ARRAY_CARACTERES = [portaaviones.caracter, destructor.caracter, submarino.caracter]
CARACTER_TOCADO = "X"
CARACTER_AGUA = "O"
CARACTER_VACIO = "~"
CANTIDAD_DISPAROS = 50
MINIMO_RANDOM = 0 # Mínimo para el rango de valores aleatorios
# Textos para los inputs
TEXTO_POSICION_X = "Introduzca la coordenada x: "
TEXTO_POSICION_Y = "Introduzca la coordenada y: "
# Textos para disparos
TEXTO_TOCADO = "TOCADO"
TEXTO_AGUA = "AGUA"
TEXTO_REPETIDO = "YA HABÍAS DISPARADO EN ESTE HUECO. NO PIERDES LA BALA."
TEXTO_BALAS_RESTANTES = "BALAS RESTANTES: "
# Textos victoria/derrota
TEXTO_VICTORIA = "TE HAS CARGADO TODOS LOS BARCOS, ENHORABUENA."
TEXTO_DERROTA = "LÁSTIMA, TE HAS QUEDADO SIN BALAS. AFINA TU PUNTERÍA Y VUELVE A INTENTARLO."
# Textos de error 
ERROR_LIMITE_TABLERO = "La posición del disparo excede los límites del tablero"
ERROR_NUMERO_ENTERO =  "Introduce números enteros, por favor"

# Generar dos tableros, uno para mostrar al usuario (original) 
# y otro para guardar los barcos (copia) y comparar con los disparos
tablero_objeto.crear_tablero(tablero_usuario, CARACTER_VACIO)
tablero_objeto.crear_tablero(tablero_barcos, CARACTER_VACIO)

# Introducir Portaaviones
tablero_objeto.generar_barcos(1, MINIMO_RANDOM, tablero_barcos, portaaviones, ARRAY_CARACTERES)
# Introducir Submarinos
tablero_objeto.generar_barcos(2, MINIMO_RANDOM, tablero_barcos, destructor, ARRAY_CARACTERES)
# Introducir Destructores
tablero_objeto.generar_barcos(3, MINIMO_RANDOM, tablero_barcos, submarino, ARRAY_CARACTERES)

# Bucle que se repite mientras queden disparos y barcos
while contador < CANTIDAD_DISPAROS and not victoria:
    # Mientras los valores no sean válidos, repetir bucle anidado
    while not coordenadas_validas: 
        print("")
        posicion_x = input(TEXTO_POSICION_X) # Pedir coordenada x

        if not validator.es_numero_entero(posicion_x): # Comprobar si es número entero
            print("")
            print("ERROR:", ERROR_NUMERO_ENTERO)
            continue
        else:
            if not validator.opcion_valida(posicion_x, tablero_objeto.ancho  - 1): # Comprobar si el valor está dentro del límte del tablero
                print("")
                print("ERROR:", ERROR_LIMITE_TABLERO) 
                continue
        
        print("")
        posicion_y = input(TEXTO_POSICION_Y)  # Pedir coordenada y

        if not validator.es_numero_entero(posicion_y): # Comprobar si es número entero
            print("")
            print("ERROR:", ERROR_NUMERO_ENTERO)
            continue
        else:
            if not validator.opcion_valida(posicion_y, tablero_objeto.alto - 1 ): # Comprobar si el valor está dentro del límte del tablero
                print("")
                print("ERROR:", ERROR_LIMITE_TABLERO)
                continue
        

        coordenadas_validas = True # Si llega hasta aquí, es que los valores son válidos, y termina el bucle anidado
        disparo_valido = disparo.Disparo(int(posicion_x), int(posicion_y))

    os.system('cls') # Borrar consola

    if tablero_objeto.disparo_repetido(tablero_usuario, disparo_valido, CARACTER_TOCADO, CARACTER_AGUA): # Comprobar si ya se había disparado en esta casilla
        print("")
        print(TEXTO_REPETIDO)
        print("")
        print(TEXTO_BALAS_RESTANTES, CANTIDAD_DISPAROS - contador) # Mostrar mensaje con las balas restantes
        print("")
        coordenadas_validas = False
        tablero_objeto.ver_tablero(tablero_usuario)
        print("")
        continue

    if disparo_valido.comprobar_acierto(tablero_barcos, ARRAY_CARACTERES): # Comprobar si se ha acertado en un barco
        tablero_objeto.marcar_disparo(tablero_usuario, tablero_barcos, disparo_valido, CARACTER_TOCADO)
        print("")
        print(TEXTO_TOCADO)
        if not tablero_objeto.quedan_barcos(tablero_barcos, ARRAY_CARACTERES): # Comprobar si quedan barcos
            victoria = True
    else:
        tablero_objeto.marcar_disparo(tablero_usuario, tablero_barcos, disparo_valido, CARACTER_AGUA)
        print(TEXTO_AGUA)

    if contador < CANTIDAD_DISPAROS:
        coordenadas_validas = False # Reinciar bandera si quedan disparos para volver a pedir coordenadas

    contador = contador + 1

    # Descomentar la siguiente sección para ver el array con los barcos
    # print("")
    # print("BARCOS")
    # print("")
    # tablero_objeto.ver_tablero(tablero_barcos)

    print("")
    tablero_objeto.ver_tablero(tablero_usuario) # Mostrar tablero con los disparos efectuados
    print("")
    print(TEXTO_BALAS_RESTANTES, CANTIDAD_DISPAROS - contador) # Mostrar mensaje con las balas restantes

os.system('cls') # Borrar consola

if victoria:
    print("")
    print(TEXTO_VICTORIA)
    print("")
    tablero_objeto.ver_tablero(tablero_usuario)
    print("")
else:
    print("")
    print(TEXTO_DERROTA)
    print("")
    tablero_objeto.ver_tablero(tablero_barcos)
    print("")