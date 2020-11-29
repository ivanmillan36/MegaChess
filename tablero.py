import constantes

def imprimirTablero(data):
    print(data[0:16])
    print(data[16:32])
    print(data[32:48])
    print(data[48:64])
    print(data[64:80])
    print(data[80:96])
    print(data[96:112])
    print(data[112:128])
    print(data[128:144])
    print(data[144:160])
    print(data[160:176])
    print(data[176:192])
    print(data[192:208])
    print(data[208:224])
    print(data[224:240])
    print(data[240:256])

def getPieza(board, x, y):
    if(x <= 15 and y <= 15 and x >= 0 and y >= 0):
        posicionEnString = (y*16) + x
        pieza = board[posicionEnString]   
        return pieza

def getPiezaIndex( x, y):
    if(x <= 15 and y <= 15 and x >= 0 and y >= 0):
        posicionEnString = (y*16) + x 
        return posicionEnString

def getColor(pieza):
    if(pieza == 'p' or pieza == 'q' or pieza == 'r' or pieza == 'h' or pieza == 'k' or pieza == 'b'):
        return 'black'
    if(pieza == 'P' or pieza == 'Q' or pieza == 'R' or pieza == 'H' or pieza == 'K' or pieza == 'B'):
        return 'white'

def posicionVacia(data, x, y):
    pieza = getPieza(data, x, y)
    if (pieza == ' '):
        return True
    else:
        return False

def getPosicion(index):
    if(index < 16):
        return [index,0]
    if(index >= 16 and index < 32):
        return [index - 16, 1]
    if(index >= 32 and index < 48):
        return [index -32, 2]
    if(index >= 48 and index < 64):
        return [index - 48, 3]
    if(index >= 64 and index < 80):
        return [index - 64, 4]
    if(index >= 80 and index < 96):
        return [index -80, 5]
    if(index >= 96 and index < 112):
        return [index - 96, 6]
    if(index >= 112 and index < 128):
        return [index - 112, 7]
    if(index >= 128 and index < 144):
        return [index - 128, 8]
    if(index >= 144 and index < 160):
        return [index - 144, 9]
    if(index >= 160 and index < 176):
        return [index - 160, 10]
    if(index >= 176 and index < 192):
        return [index -176, 11]
    if(index >= 192 and index < 208):
        return [index -192, 12]
    if(index >= 208 and index < 224):
        return [index - 208, 13]
    if(index >= 224 and index < 240):
        return [index - 224, 14]
    if(index >= 240 and index < 256):
        return [index - 240, 15]

def getTableroLuegoDeMovimiento(board, movimiento):
    pieza = getPieza(board, movimiento[0][0], movimiento[0][1])
    board[getPiezaIndex(movimiento[0][0],movimiento[0][1])] = ' '
    board[getPiezaIndex(movimiento[1][0],movimiento[1][1])] = pieza
    return board

def campoEnemigo(pieza, y):
    if (getColor(pieza) == 'black'):
        if(y >= 8):
            return True
        else:
            return False
    if (getColor(pieza) == 'white'):
        if(y <= 7):
            return True
        else:
            return False