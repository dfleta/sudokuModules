import pytest
from src.checkNumerosValidos import checkNumerosValidos
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize("sudoku, sano",
                         [  (casosTest.correct, True),
                            (casosTest.incorrect, True),
                            (casosTest.incorrect1, True),
                            (casosTest.incorrect2, True),
                            (casosTest.incorrect3, False),
                            (casosTest.incorrect4, False),
                            (casosTest.incorrect5, False),
                            (casosTest.irregular, False),
                            (casosTest.irregular2, True)])
def test_sudoku_valido(sudoku, sano):
    assert checkNumerosValidos(sudoku) == sano
