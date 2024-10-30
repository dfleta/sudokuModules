import pytest
from src.checkNumerosValidos import checkNumerosValidos
import casosTest.casosTestSudoku as casosTest


@pytest.mark.numeros_validos
@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correcto, True),
                            (casosTest.numero_repetido_fila_columna, True),
                            (casosTest.numero_repetido_columna, True),
                            (casosTest.numero_no_presente, True),
                            (casosTest.numero_fuera_del_rango, False),
                            (casosTest.caracteres, False),
                            (casosTest.numeros_reales, False),
                            (casosTest.irregular_fila, False),
                            (casosTest.irregular_columna, True)])
def test_check_numeros_validos(sudoku, sano):
    assert checkNumerosValidos(sudoku) == sano
