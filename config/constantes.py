DIFICULTAD = {
    
    # Fácil
    1: {
        "ancho": 8,
        "alto": 8,
        "disparos": 60,
        "barcos": [
            (5, 1, "P"),
            (4, 1, "A"),
            (3, 1, "D"),
            (2, 1, "L"),
        ]
    },

    # Media
    2: {
        "ancho": 10,
        "alto": 10,
        "disparos": 50,
        "barcos": [
            (5, 1, "P"),
            (4, 1, "A"),
            (3, 2, "D"),
            (2, 1, "L"),
        ]
    },

    # Difícil
    3: {
        "ancho": 10,
        "alto": 10,
        "disparos": 40,
        "barcos": [
            (5, 1, "P"),
            (4, 1, "A"),
            (3, 2, "D"),
            (2, 1, "L"),
        ]
    }
}

# Caracteres comunes
CARACTER_VACIO = "~"
CARACTER_TOCADO = "X"
CARACTER_AGUA = "O"


# Instrucciones
INSTRUCCIONES = """
OBJETIVO
--------
Descubrir y hundir todos los barcos enemigos antes de que
se agoten los disparos disponibles. El tamaño del tablero,
la cantidad de barcos y la cantidad de disparos dependen
de la dificultad.

------------------------------------------------------------

FÁCIL
-------
- Tablero 8x8.
- 60 disparos.
- 1 portaaviones de tamaño 5.
- 1 acorazado de tamaño 4
- 1 destructor de tamaño 3
- 1 lancha de tamaño 2

------------------------------------------------------------

MEDIA
------
- Tablero 10x10.
- 50 disparos.
- 1 portaaviones de tamaño 5.
- 1 acorazado de tamaño 4
- 2 destructores de tamaño 3
- 1 lancha de tamaño 2

------------------------------------------------------------

DIFÍCIL
--------
- Tablero 10x10.
- 40 disparos.
- 1 portaaviones de tamaño 5.
- 1 acorazado de tamaño 4
- 2 destructores de tamaño 3
- 1 lancha de tamaño 2

------------------------------------------------------------

Pulsa ENTER para volver al menú...
============================================================
"""
