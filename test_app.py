from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


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
       
        req=client.get('/check_word')
        # req=client.get('/check_word', data={'a_word': 'A'})
        print("in begining of test")
        print("req:", req)
        self.assertEqual(req, 'ok')
        # with app.test_client() as client:
           
            
            # req=client.post('/check_word', data={'a_word': 'A'})
        #     print("in begining of test")
        #     ret=req.get_data(as_text=True)
        #     self.assertIn("ok", ret)
        #     print("in the test")





# upadate_stats ()
