
from src.checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTestSudoku

for attr in sorted(casosTestSudoku.__dict__):
    # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
    # Asi podemos añadir todos los casos que queramos
    # en la unidad casosTestSudoku sin modificar este codigo
    if attr.startswith('__'):
        pass
        # Skip atributo
    else:
        print(attr, " => ", checkSudoku(casosTestSudoku.__dict__[attr]))
        # mismo codigo que getattr(module, attr)
        # es necesario añadir el espacio de nombres del modulo:
        # casosTestSudoku.irregular
