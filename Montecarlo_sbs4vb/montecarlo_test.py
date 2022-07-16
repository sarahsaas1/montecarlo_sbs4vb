import unittest
import pandas as pd
import numpy as np
import random

from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyser


class dieTestSuite(unittest.TestCase):
    """[unit tests to test if the methods receive the correct inputs and return valid outputs]

    Args:
        unittest ([type]): [description]
    """

    def test_change_die(self):
        """[checks to see if the weight of the die was changed]
        """
 
        
        test_die = Die([1,2,3,4,5,6])
        test_die.change_weight(2, .3)

        expected = .3

        self.assertEqual(test_die._dice_df.iloc[1,1], expected) 

    def test_roll_die(self):
        """[checks to see if the dicd were rolled. The length of the frame needs to be the same as the number of rolls]
        """

        test_die = Die([1,2,3,4,5,6])
        expected = 5

        self.assertTrue(len(test_die.roll_die(5))  == expected )

    def test_show_die(self):
        """[Test to see if show die shows the die. This is done by creating a tuple of the expected dimensions of the 
            dataframe and comparing that with the results]
        """
    
        test_die = Die([1,2,3,4,5,6])
        expected = (6,2)

        self.assertEqual(test_die._dice_df.shape, expected)

    def test_play(self):
        """[Tests to see if the play method returns the correct data frame. This is tested by creating a tuple of the expected
            dimensions of the dataframe and comparing that with the returned frame ]
        """

        test_game_die = Game([ Die([1,2,3,4,5,6]),  Die([1,2,3,4,5,6]), Die([1,2,3,4,5,6])])

        expected = (3,3)

        test_game_die.play(3)

        self.assertEqual(test_game_die._rolls_results.shape, expected)


    def test_show_recent(self):
        """[Tests to see if the show recent method returns the correct data frame. This is tested by creating a tuple of the expected
            dimensions of the dataframe and comparing that with the returned frame]
        """

        test_game_die = Game([ Die([1,2,3,4,5,6]),  Die([1,2,3,4,5,6]), Die([1,2,3,4,5,6])])

        expected = (3,3)

        test_game_die.play(3)
        test_game_die.show_recent()

        self.assertEqual(test_game_die._rolls_results.shape, expected)

    def test_jackpot(self):
        """[Tests to see if the jackpot method returns the number of times all dice were the same face. This is  tested by 
            running the game and comparing the jackpots. ]
        """

        game1 = Game([ Die([1,2,3,4,5,6]),  Die([1,2,3,4,5,6]), Die([1,2,3,4,5,6])])
        game1.play(3)

        test_analyser_die = Analyser(game1)

        jackpots = sum(test_analyser_die._result.eq(test_analyser_die._result.iloc[:, 0], axis=0).all(1))


        self.assertEqual(test_analyser_die.jackpot(), jackpots)

    def combo(self):
        """[Tests to see if the combo method returns the data frame with the combinations of rolls. This is tested by
            making sure the length is the same as the number of rolls]
        """

        game1 = Game([ Die([1,2,3,4,5,6]),  Die([1,2,3,4,5,6]), Die([1,2,3,4,5,6])])
        game1.play(3)

        test_analyser_die = Analyser(game1)

        combos = test_analyser_die.combo().combo_n.sum()

        self.assertEqual(combos, 3)


    def face_counts(self):
        """[Test to see if face_counts method generates the number of times a value comes up during rolls. This is tested
            by making sure the length is the same as the number of rolls]
        """

        game1 = Game([ Die([1,2,3,4,5,6]),  Die([1,2,3,4,5,6]), Die([1,2,3,4,5,6])])
        game1.play(3)

        test_analyser_die = Analyser(game1)

        counts = test_analyser_die.face_counts().sum()

        self.assertEqual(combos, 3)





if __name__ == '__main__':
        
    unittest.main(verbosity=3)  


    
        


    



