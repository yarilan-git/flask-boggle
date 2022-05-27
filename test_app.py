from unittest import TestCase
from app import app
from flask import Flask, session, render_template, jsonify, request
from boggle import Boggle
import pdb


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!


# setup_the_board()

    def test_setup(self):
        with app.test_client() as client:
            res=client.get('/')
            html=res.get_data(as_text=True)
            self.assertIn('board', session)
            self.assertIn('Boggle game board', html)
            self.assertIn('Games played: 0', html)
            self.assertIn('High score: 0', html)

    
    def test_validate_word(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"], 
                                    ["C", "A", "T", "T", "T"]]
       
        req=client.get('/check_word?a_word=a')
        res=req.get_data(as_text=True)
        self.assertIn('ok', res)

        req=client.get('/check_word?a_word=door')
        res=req.get_data(as_text=True)
        self.assertIn('not-on-board', res)

        req=client.get('/check_word?a_word=rdfv')
        res=req.get_data(as_text=True)
        self.assertEqual (req.json['result'], 'not-word')

    def test_update_stats(self):
        with app.test_client() as client:
            client.post('/update_stats', data={'score':'5'})
           
            # self.assertEqual(res.json['high_score'], '5')
            # self.assertEqual(res.json['games'], '1')



            # {"high_score" : high_score, "games" : games_played})



        
