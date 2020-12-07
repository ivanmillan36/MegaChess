import pytest
import simulacion
import constantes


TEST_GET_PIEZAS_POR_COLOR =     (   'p               ' +
                                    ' k              ' +
                                    '  q             ' +
                                    '   b            ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '   KQ  PPPP     ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

@pytest.mark.parametrize(
    "board, color, expected",
    [
        (TEST_GET_PIEZAS_POR_COLOR, 'black', [['p',0,0], ['k',1,1] , ['q',2,2] , ['b',3,3]]),
    ] 
)
def test_getPiezasPorColor(board, color, expected):
    assert simulacion.getPiezasPorColor(TEST_GET_PIEZAS_POR_COLOR, 'black') == expected

##############################################################################################