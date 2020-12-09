###################################### CONFIG ###############################################

SCORE_PEON = 10
SCORE_CABALLO = 30
SCORE_ALFIL = 40
SCORE_TORRE = 60
SCORE_REINA = 20
SCORE_REY = 1000
AUTH_TOKEN = 'ce9b7d4f-3395-4a8b-8c27-8b3beff9b601'
CANT_ITERACIONES = 1

PRETTY_PIECES = {
    'p': '♟',
    'P': '♙',
    'r': '♜',
    'R': '♖',
    'k': '♚',
    'K': '♔',
    'h': '♞',
    'H': '♘',
    'b': '♝',
    'B': '♗',
    'q': '♛',
    'Q': '♕',
    ' ': ' ',
}

CANCELAR_PARTIDAS_ACTIVAS = False


####################################### TESTS ###############################################

TABLERO_INICIAL =  ('rrhhbbqqkkbbhhrr' +
                    'rrhhbbqqkkbbhhrr' +
                    'pppppppppppppppp' +
                    'pppppppppppppppp' +
                    '                ' +
                    '                ' +
                    '                ' +
                    '                ' +
                    '                ' +
                    '                ' +
                    '                ' +
                    '                ' +
                    'PPPPPPPPPPPPPPPP' +
                    'PPPPPPPPPPPPPPPP' +
                    'RRHHBBQQKKBBHHRR' +
                    'RRHHBBQQKKBBHHRR' )

TABLERO_TEST_ALFIL = (  'rrhhbbqqkkbbhhrr' +
                        'rrhhbbqqkkbbhhrr' +
                        'pppppppppppppppp' +
                        'pppppppppppppppp' +
                        '                ' +
                        'B               ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        '                ' +
                        'b               ' +
                        '                ' +
                        'PPPPPPPPPPPPPPPP' +
                        'PPPPPPPPPPPPPPPP' +
                        'RRHHBBQQKKBBHHRR' +
                        'RRHHBBQQKKBBHHRR' )

PLAYEER_TEST_MEJOR_MOVIMIENTO = (   '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    '                ' +
                                    ' q              ' +
                                    '                ' +
                                    '                ' +
                                    ' P              ' +
                                    '                ' +
                                    '                ' +
                                    '                ' )

BOARD_TEST_REINA =              (   'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'p pppppppppppppp' +
                                    ' q ppppppppppppp' +
                                    'p pppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' +
                                    'pppppppppppppppp' )

