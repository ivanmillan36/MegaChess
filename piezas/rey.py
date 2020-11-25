import tablero

def getMovimientos(board, x, y):
    posicionInicial = [x,y]
    pieza = tablero.getPieza(board, x, y)
    color = tablero.getColor(pieza)
    movimientosPosibles = []

    if(color == 'black'):
        #eje y-
        X = x
        Y = y

        Y -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
        #eje y-x+
        X = x
        Y = y

        Y -= 1
        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
        #eje x+
        X = x
        Y = y

        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
        #eje y+x+
        X = x
        Y = y

        Y += 1
        X += 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
        #eje y+
        X = x
        Y = y

        Y += 1
        
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])

        #eje y+x-
        X = x
        Y = y

        Y += 1
        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
        #eje x-
        X = x
        Y = y

        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
        #eje y-x-
        X = x
        Y = y

        Y -= 1
        X -= 1
        if (tablero.posicionVacia(board, X, Y)):
            movimientosPosibles.append([X, Y])
        if (tablero.getColor(tablero.getPieza(board, X, Y)) == 'white'):
            movimientosPosibles.append([X , Y])
        
    
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