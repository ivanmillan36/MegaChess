import constantes
import tablero
from movimientos import getMejorMovimiento

def realizarMovimiento(board, color):
    movimiento = getMejorMovimiento(board, color)
    return movimiento



