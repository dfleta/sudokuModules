import pytest
from src.checkFilas import checkFilas
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correcto, True),
                            (casosTest.numero_repetido_fila_columna, False),
                            (casosTest.numero_repetido_columna, True),
                            (casosTest.numero_no_presente, False),
                            (casosTest.numero_fuera_del_rango, True),
                            # (casosTest.caracteres, True),
                            # (casosTest.numeros_reales, True),
                            # (casosTest.irregular_fila, True),
                            # (casosTest.irregular_columna, True)
                            ])
def test_check_filas(sudoku, sano):
    assert checkFilas(sudoku) == sano