import requests
while(1):
    
    k = input()
    cmd = (k.split())[0]
    r = 1
    if(cmd == 'move'):
        pl = (k.split())[1]
        pos = (k.split())[2]
        r = requests.post('http://127.0.0.1:5001/make_move', data={'player': pl, 'position' : pos})
    if(cmd == 'status'):
        r = requests.get('http://127.0.0.1:5001/status')
    if(cmd == 'reset'):
        r = requests.get('http://127.0.0.1:5001/start_game')
    if(cmd == 'board'):
        r = requests.get('http://127.0.0.1:5001/board')
    print(r.text)
