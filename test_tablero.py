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

@pytest.mark.parametrize(
    "x,y, expected",
    [
        (0,0, 0),
        (15,0, 15),
        (15,1, 31),
        (1,1, 17),
    ] 
)
def test_getPiezaIndex(x,y, expected):
    assert getPiezaIndex(x,y) == expected

@pytest.mark.parametrize(
    "pieza,y, expected",
    [
        ('p',9, True),
        ('q',4, False),
        ('P',4, True),
        ('R',0, True),
    ] 
)
def test_campoEnemigo(pieza,y, expected):
    assert campoEnemigo(pieza,y) == expected