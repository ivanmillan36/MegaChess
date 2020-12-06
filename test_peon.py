import pytest
from piezas.peon import getMovimientos
import tablero

BOARD_TEST_PEON =               (   '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' p              ' +
                                    '  Q             ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_PEON, 1, 9, [[1, 10], [2, 10]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected