import pytest
from piezas.alfil import getMovimientos
import tablero

BOARD_TEST_ALFIL =               (  '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' b              ' +
                                    '                ' +
                                    '                ' +
                                    '            B   ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_ALFIL, 1, 9, [[2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [0, 10], [0, 8]]),
        (BOARD_TEST_ALFIL, 12, 12, [[13, 11], [14, 10], [15, 9], [13, 13], [14, 14], [15, 15], [11, 13], [10, 14], [9, 15], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected