# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

# Si ejecutamos este modulo desde su directorio actual
# el contexto de ejecucion es src y no es necesario
# incluir el directorio en la ruta de los imports,
# pero si ejecutamos este modulo importandolo desde
# sudoku.py en el directorio raiz, el contexto de
# ejecucion es el directorio raiz y hay que incluir
# ./src en la busqueda de los otros modulos de los
# que depende checkSudoku para que los encuentre

import sys
sys.path.append('..')

from src.checkCuadrado import checkCuadrado
from src.checkNumerosValidos import checkNumerosValidos
from src.checkFilas import checkFilas
from src.checkColumnas import checkColumnas


def checkSudoku(sudoku):

    return checkCuadrado(sudoku) and checkNumerosValidos(sudoku) \
        and checkFilas(sudoku) and checkColumnas(sudoku)


if __name__ == '__main__':

    print("Esto es el main de checkSudoku")

    # Cuando ejecuto un programa python el directorio
    # desde el que se ejecuta la busqueda de modulos
    # es el directorio desde el que se invoca
    # en consola python3
    # python3 ./checkSudoku => ruta relativa a casos test
    # ../test/casosTestsudoku
    # python3 src/checkSudoku => ruta relativa a casos test
    # ../sudokuModules/casosTest/casosTestsudokus

    # Reimportar un modulo no recarga el modulo.
    # No es necesario si ya esta importado.
    # Lo dejo para hacer explicita la ruta relativa
    # a las dependencias del directorio casosTest
    import sys
    sys.path.append('..')

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        # en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith('__'):
            pass
            # Skip atributo
        else:
            print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular
