# Se incluyen unos prints estilo devil guide to debugging
# para hacer explícita la ejecución del código de un módulo
# cuando lo importamos y entender el comportamiento
# de los Mixed Usage Modes __name__ y  __main__.

print("Esto es la pre-funcion checkCuadrado")


def checkCuadrado(sudoku):
    # Precondicion
    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    sudokuSano = True
    numeroFilas = len(sudoku)

    for fila in sudoku:
        # longitud de una lista vacia es 0
        if len(fila) != numeroFilas:
            sudokuSano = False
            break

    # Postcondicion
    assert isinstance(sudokuSano, bool), "la interfaz exige devolver un valor lógico"

    return sudokuSano


print("Esto es la post-funcion de checkCuadrado")

### CASOS TEST ###

if __name__ == "__main__":
    print("Esto es el main de checkCuadrado")

    import sys

    sys.path.append("..")

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        # en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith("__"):
            pass
            # Skip atributo
        else:
            print(attr, " => ", checkCuadrado(casosTest.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular
