import asyncio
import json
from random import randint
import sys
import websockets
import time
import constantes
import player
import tablero


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    #print(message)
    await websocket.send(message)


async def start(auth_token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(auth_token)
    while True:
        print('connection to {}'.format(uri))
        async with websockets.connect(uri) as websocket:
            await play(websocket)


async def play(websocket):
    while True:
        try:
            response = await websocket.recv()
            #print(f"< {response}")
            data = json.loads(response)
            if data['event'] == 'update_user_list':
                print("User List: ")
                print(data['data']['users_list'])
                pass
            if data['event'] == 'gameover':
                print(data['data']['white_username'] + " White score: " + data['data']['white_score'])
                print(data['data']['black_username'] + " Black score: " + data['data']['black_score'])
                pass
            if data['event'] == 'ask_challenge':
                print('Te ha desafiado: ' + data['data']['username'])
                if (data['data']['username'] == 'ivanmillan'):
                    await send(
                        websocket,
                        'accept_challenge',
                        {
                            'board_id': data['data']['board_id'],
                        },
                    )   

            if data['event'] == 'your_turn':
                print("********* Partida contra " + data['data']['opponent_username'] + " ****************")  
                print("Color = " + data['data']['actual_turn'])
                tablero.imprimirTablero(data['data']['board'])
                movimiento = player.realizarMovimiento(data['data']['board'], data['data']['actual_turn'])

                if(constantes.CANCELAR_PARTIDAS_ACTIVAS):
                    await send(
                        websocket,
                        'abort',
                        {
                            'board_id':data['data']['board_id']
                        },
                    )
                else:
                    await send(
                        websocket,
                        'move',
                        {
                            'board_id': data['data']['board_id'],
                            'turn_token': data['data']['turn_token'],
                            'from_row': movimiento[0][1],
                            'from_col': movimiento[0][0],
                            'to_row': movimiento[1][1],
                            'to_col': movimiento[1][0], 
                        },
                    )

        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start(constantes.AUTH_TOKEN))

