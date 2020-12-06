import pytest
import movimientos

PLAYEER_TEST_MEJOR_MOVIMIENTO = (   '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '     Q pppp     ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '       P P      ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '    BB          ' +
                                    '                ' +
                                    '       Kq       ' )

@pytest.mark.parametrize(
    "board, color, expected",
    [
        (PLAYEER_TEST_MEJOR_MOVIMIENTO, 'white', [[7, 15], [8, 15]]),
    ] 
)
def test_getMejorMovimiento(board, color, expected):
    assert movimientos.getMejorMovimiento(board, color) == expected
