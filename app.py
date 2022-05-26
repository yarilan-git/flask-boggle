from flask import Flask, session, render_template, jsonify, request, flash
from boggle import Boggle
# import pdb

app = Flask(__name__)
app.config["SECRET_KEY"] = '123456'



boggle_game = Boggle()
games_played = 0
high_score = 0

@app.route("/")
def setup_the_board():    
    """Instantiates a new game object and stores it in the session"""

    session['board'] = boggle_game.make_board()
    return render_template('game_board.html', title='Boggle game board', games=games_played, high_score=high_score)

@app.route('/check_word', methods=["POST"])
def validate_word():
    """Checks if a word provided by the user is valid, i.e. it exists in 
       the dictionary and exists in the current game board.
    """
    board=session['board']
    res=request.json["a_word"]
    return jsonify({"result" : boggle_game.check_valid_word(board, res)})

@app.route('/update_stats', methods=['POST'])
def upadate_stats ():
    """Keeps a tally of how many games have been played, and what the high score was.
    """
    global games_played
    global high_score

    games_played += 1
    if request.json['score'] > high_score:
        high_score = request.json['score']    
    return jsonify({"high_score" : high_score, "games" : games_played})
    
    

