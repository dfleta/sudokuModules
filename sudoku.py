## ENUNCIADO ##

# Sudoku [https://es.wikipedia.org/wiki/Sudoku]
# es un juego de puzle logico donde un partida
# esta definida por un cuadrado de digitos 
# 9 x 9 parcialmente cubierto  
# donde cada cuadrado contiene uno de los digitos 
# 1,2,3,4,5,6,7,8,9.
# Para este ejercicio generalizaremos
# y simplificaremos el juego.

# Define una funcion -check_sudoku-
# que toma como entrada una lista de listas
# que representa una solucion n x n al sudoku
# y devuelve el booleano True si la entrada
# es un sudoku y False sino.

# Un sudoku valido satisface estas dos propiedades:

#   1. Cada columna del cuadrado contiene
#      cada uno de los numeros de 1 a n exactamente una vez.

#   2. Cada fila del cuadrado contiene
#      cada uno de los numeros de 1 a n exactamente una vez.


from src.checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTest

for attr in sorted(casosTest.__dict__):

    # Un modulo es un espacio de nombres

    # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
    # Asi podemos añadir todos los casos que queramos
    # en la unidad casosTestSudoku sin modificar este codigo
    if attr.startswith('__'):
        pass
        # Skip atributo
    else:
        print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))
        # mismo codigo que getattr(module, attr)
        # es necesario añadir el espacio de nombres del modulo:
        # casosTestSudoku.irregular
