import json
import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('Connected to server')


@sio.event
def disconnect():
    print('Disconnected from server')


@sio.event
def onProcessNow(data: str):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    sio.connect('http://localhost:3000')
    sio.wait()