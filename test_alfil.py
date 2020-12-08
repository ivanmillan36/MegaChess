import pytest
from piezas.alfil import getMovimientos
import tablero

BOARD_TEST_ALFIL =               (  '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '       P        ' +
                                    '                ' +
                                    ' P              ' +
                                    '                ' +
                                    '   b            ' +
                                    '                ' +
                                    'P         p   p ' +
                                    '      P         ' +
                                    '            B   ' +
                                    '                ' +
                                    '          p   p ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, x, y, expected",
    [
        (BOARD_TEST_ALFIL, 3, 8, [[4, 7], [5, 6], [6, 5], [7, 4], [4, 9], [5, 10], [6, 11], [2, 9], [1, 10], [0, 11], [2, 7], [1, 6]]),
        (BOARD_TEST_ALFIL, 12, 12, [[13, 11], [14, 10], [13, 13], [14, 14], [11, 13], [10, 14], [11, 11], [10, 10]]),
    ] 
)
def test_getMovimientos(board, x, y, expected):
    assert getMovimientos(board, x,y) == expected