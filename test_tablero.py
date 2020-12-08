import pytest 
from tablero import *


@pytest.mark.parametrize(
    "data , x, y, expected",
    [
        ('   ', 0, 0, True),
        ('p  ', 0, 0, False),
        (' p   ', 1, 0, False),
        ('                p', 0, 1, False),
        ('                p ', 1, 1, True),
    ] 
)
def test_posicionVacia(data, x, y, expected):
    assert posicionVacia(data, x, y) == expected

##############################################################################################

@pytest.mark.parametrize(
    "data , x, y, expected",
    [
        ('   ', 0, 0, ' '),
        ('p  ', 0, 0, 'p'),
        (' k   ', 1, 0, 'k'),
        ('                r', 0, 1, 'r'),
    ] 
)
def test_getPieza(data, x, y, expected):
    assert getPieza(data, x, y) == expected

##############################################################################################

@pytest.mark.parametrize(
    "pieza, expected",
    [
        ('p', 'black'),
        ('k', 'black'),
        ('q', 'black'),
        ('h', 'black'),
        ('b', 'black'),
        ('r', 'black'),
        ('R', 'white'),
        ('H', 'white'),
        ('B', 'white'),
        ('P', 'white'),
        ('K', 'white'),
        ('Q', 'white'),
    ] 
)
def test_getColor(pieza, expected):
    assert getColor(pieza) == expected

##############################################################################################

@pytest.mark.parametrize(
    " x, y, expected",
    [
        ( 0, 0, 0),
        ( 0, 1, 16),
        ( 1, 0, 1),
        ( 1, 1, 17),
    ] 
)
def test_getPiezaIndex( x, y, expected):
    assert getPiezaIndex( x, y) == expected

##############################################################################################

@pytest.mark.parametrize(
    "index, expected",
    [
        (0, [0,0]),
        (16, [0,1]),
        (32, [0,2]),
        (31, [15,1]),
        (255, [15,15]),
    ] 
)
def test_getPosicion(index, expected):
    assert getPosicion(index) == expected

##############################################################################################

@pytest.mark.parametrize(
    "x,y, expected",
    [
        (0,0, 0),
        (15,0, 15),
        (15,1, 31),
        (1,1, 17),
        (3,0, 48),
        (3,5, 53),
        (6,0, 96),
        (15,0, 240),
        (15,15, 255),

    ] 
)
def test_getPiezaIndex(x,y, expected):
    assert getPiezaIndex(x,y) == expected

##############################################################################################

@pytest.mark.parametrize(
    "pieza,y, expected",
    [
        ('p',9, True),
        ('q',4, False),
        ('P',4, True),
        ('R',0, True),
        ('B',2, True),
        ('H',1, True),
        ('h',14, True),
        ('h',1, False),
    ] 
)
def test_campoEnemigo(pieza,y, expected):
    assert campoEnemigo(pieza,y) == expected

##############################################################################################

TABLERO_TEST_ENTRADA = ('rrhhbbqqkkbbhhrr' +
                        'rrhhbbqqkkbbhhrr' +
                        'pppppppppppppppp' +
                        ' ppppppppppppppp' +
                        '                ' +
                        '                ' +
                        'p               ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        'PPPPPPPPPPPPPPPP' +
                        'PPPPPPPPPPPPPPPP' +
                        'RRHHBBQQKKBBHHRR' +
                        'RRHHBBQQKKBBHHRR' )

TABLERO_TEST_SALIDA =  ('rrhhbbqqkkbbhhrr' +
                        'rrhhbbqqkkbbhhrr' +
                        'pppppppppppppppp' +
                        ' ppppppppppppppp' +
                        '                ' +
                        '                ' +
                        '                ' +
                        'q               ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        'PPPPPPPPPPPPPPPP' +
                        'PPPPPPPPPPPPPPPP' +
                        'RRHHBBQQKKBBHHRR' +
                        'RRHHBBQQKKBBHHRR' )

@pytest.mark.parametrize(
    "board, movimiento, expected",
    [
        (TABLERO_TEST_ENTRADA,[[0,6],[0,7]], TABLERO_TEST_SALIDA),
    ] 
)
def test_getTableroLuegoDeMovimiento(board, movimiento, expected):
    assert getTableroLuegoDeMovimiento(board, movimiento) == expected