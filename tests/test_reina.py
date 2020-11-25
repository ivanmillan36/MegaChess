import pytest
from piezas.reina import getMovimientos
import tablero
import constantes

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (constantes.BOARD_TEST_REINA, 1, 9, [[1, 8], [2, 9], [1, 10], [0, 9]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected