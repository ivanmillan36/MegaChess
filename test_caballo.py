import pytest
from piezas.caballo import getMovimientos
import tablero

BOARD_TEST_CABALLO =               ('                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' k              ' +
                                    '                ' +
                                    '                ' +
                                    '            K   ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_CABALLO, 1, 9, [[2, 7], [3, 8], [3, 10], [2, 11], [0, 11], [0, 7]]),
        (BOARD_TEST_CABALLO, 12, 12, [[13, 10], [14, 11], [14, 13], [13, 14], [11, 14], [10, 13], [10, 11], [11, 10]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected