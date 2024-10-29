import pytest
from src.checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correcto, True),
                            (casosTest.numero_repetido_fila_columna, False),
                            (casosTest.numero_repetido_columna, False),
                            (casosTest.numero_no_presente, False),
                            pytest.param(casosTest.numero_fuera_del_rango,
                                         False,
                                         marks=pytest.mark.barricada),
                            (casosTest.caracteres, False),
                            (casosTest.numeros_reales, False),
                            (casosTest.irregular_fila, False),
                            (casosTest.irregular_columna, False)])
def test_check_sudoku(sudoku, sano):
    assert checkSudoku(sudoku) == sano
