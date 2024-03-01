from flask import Flask
from flask import request
import string


app = Flask(__name__)
current = 0
fld = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

@app.route('/start_game')
def start_game():
    global current
    global fld
    fld = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    current = 0
    return 'Game started...'

@app.route('/make_move', methods=['POST'])
def move():
    global current
    global fld
    pl = int(request.form['player'])
    pos = int(request.form['position'])-1
    print(pl, pos)
    if(pl == current and pos < 9):
        fld[pos // 3][pos % 3] = pl
        current = 1 - current
        return 'ok'
    else:
        return 'not ok =('
    

@app.route('/board', methods=['GET'])
def board():
    global current
    global fld
    s = ''
    for i in range(3):
        for j in range(3):
            if(fld[i][j] == -1):
               s+='.'
            if(fld[i][j] == 0):
               s+='o'
            if(fld[i][j] == 1):
               s+='x'
        s+='\n'
    return s

@app.route('/status', methods=['GET'])
def status():
    global current
    global fld
    draw = 1
    for i in range(3):
        for j in range(3):
            if(fld[i][j] == -1):
               draw = 0
               
    for i in range(3):
        if(fld[0][i] == fld[1][i] == fld[2][i] and fld[0][i] != -1):
            return 'PLAYER ' + str(fld[0][i]) + ' WON!'
        if(fld[i][0] == fld[i][1] == fld[i][2] and fld[i][0] != -1):
            return 'PLAYER ' + str(fld[i][0]) + ' WON!'
        
    if(fld[0][0] == fld[1][1] == fld[2][2] and fld[1][1] != -1):
        return 'PLAYER ' + str(fld[1][1]) + ' WON!'
    if(fld[0][2] == fld[1][1] == fld[2][2] and fld[1][1] != -1):
        return 'PLAYER ' + str(fld[1][1]) + ' WON!'
    if(draw == 1):
        return 'DRAW'
    if(draw == 0):
        return 'IN PROGRESS; CURRENT PLAYER: ' + str(current)

if __name__ == '__main__':
    app.run(port=5001)
