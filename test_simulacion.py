import pytest
import simulacion
import constantes
from piezas import peon, rey, reina, torre, alfil, caballo


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

TEST_GET_MOVIMIENTOS =           (  'p               ' +
                                    ' k              ' +
                                    '  q             ' +
                                    '   b h r        ' +
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
    "board, pieza, x, y, expected",
    [
        (TEST_GET_MOVIMIENTOS, 'p', 0,0, peon.getMovimientos(TEST_GET_MOVIMIENTOS, 0, 0)),
        (TEST_GET_MOVIMIENTOS, 'k', 1,1, rey.getMovimientos(TEST_GET_MOVIMIENTOS, 1, 1)),
        (TEST_GET_MOVIMIENTOS, 'q', 2,2, reina.getMovimientos(TEST_GET_MOVIMIENTOS, 2, 2)),
        (TEST_GET_MOVIMIENTOS, 'b', 3,3, alfil.getMovimientos(TEST_GET_MOVIMIENTOS, 3, 3)),
        (TEST_GET_MOVIMIENTOS, 'h', 5,3, caballo.getMovimientos(TEST_GET_MOVIMIENTOS, 5, 3)),
        (TEST_GET_MOVIMIENTOS, 'r', 7,3, torre.getMovimientos(TEST_GET_MOVIMIENTOS, 7, 3)),
    ] 
)
def test_getMovimientos(board, pieza, x, y, expected):
    assert simulacion.getMovimientos(board, pieza, x, y) == expected

##############################################################################################

TEST_GET_PUNTOS_POR_MOVIMIENTO =  ( '       q        ' +
                                    '       K        ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '              R ' +
                                    'H              P' )

@pytest.mark.parametrize(
    "board, pieza, movimiento, expected",
    [
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'q', [7,1],  constantes.SCORE_REY*1200),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'K', [7,0],  constantes.SCORE_REINA*1200),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'P', [15,14],  constantes.SCORE_PEON+15-14),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'P', [16,16],  None),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'R', [15,14],  constantes.SCORE_TORRE),
        (TEST_GET_PUNTOS_POR_MOVIMIENTO, 'H', [0,14],  constantes.SCORE_CABALLO),     
    ] 
)
def test_getPuntosPorMovimiento(board, pieza, movimiento, expected):
    assert simulacion.getPuntosPorMovimiento(board, pieza, movimiento) == expected