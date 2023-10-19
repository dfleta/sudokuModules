
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
