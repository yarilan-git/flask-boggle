from flask import Flask, session, render_template, jsonify, request, flash
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = '123456'



boggle_game = Boggle()
games_played = 0
high_score = 0

@app.route("/")
def setup_the_board():    
    session['board'] = boggle_game.make_board()
    
    return render_template('game_board.html', title='Boggle game board', games=games_played, high_score=high_score)

@app.route('/check_guess', methods=["POST", "GET"])
def validate_guess():
    print('on the server side')
    board=session['board']
    res=request.form["a_guess"]
    print("input word list was this:", request.form) 
    print("request form was:", res)
    return jsonify({"result" : boggle_game.check_valid_word(board, res)})

@app.route('/update_stats', methods=['POST', 'GET'])
def upadate_stats ():
    global games_played
    global high_score

    games_played += 1
    if request.form['score'] > high_score:
        high_score = request.form['score']    
    return jsonify({high_score : high_score, games : games_played})
    
    

