import tablero

def getMovimientos(board, x, y):
    posicionInicial = [x,y]
    pieza = tablero.getPieza(board, x, y)
    color = tablero.getColor(pieza)
    movimientosPosibles = []

    if(color == 'black'):
        if (tablero.posicionVacia(board, x, y + 1)):
            movimientosPosibles.append([x,y+1])
        if (y == 3 and tablero.posicionVacia(board,x, y + 2)):
            movimientosPosibles.append([x, y + 2])
        if (tablero.getColor(tablero.getPieza(board, x + 1, y + 1)) == 'white'):
            movimientosPosibles.append([x + 1 , y + 1])
        if (tablero.getColor(tablero.getPieza(board, x - 1, y + 1)) == 'white'):
            movimientosPosibles.append([x - 1 , y + 1])
    
    if(color == 'white'):
        if (tablero.posicionVacia(board, x, y-1)):
            movimientosPosibles.append([x,y-1])
        if (y == 12 and tablero.posicionVacia(board,x, y - 2)):
            movimientosPosibles.append([x, y - 2])
        if (tablero.getColor(tablero.getPieza(board, x + 1, y - 1)) == 'black'):
            movimientosPosibles.append([x + 1 , y - 1])
        if (tablero.getColor(tablero.getPieza(board, x - 1, y - 1)) == 'black'):
            movimientosPosibles.append([x - 1 , y - 1])
    
    return movimientosPosibles