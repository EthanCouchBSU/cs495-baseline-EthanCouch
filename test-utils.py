from unittest.mock import patch
from utils import *
import unittest


class TestStringReplacementMethod(unittest.TestCase):

    @patch('utils.random.choice')
    def test_NoMatches(self,unrandom_Value):
        unrandom_Value.return_value = "apple"
        result = replace_SubString_Randomly("[]", "Hello World", ["apple","orange","pear"])
        self.assertEqual(result, "Hello World")

    def test_Empty_Input(self):
        with self.assertRaises(ValueError):
            replace_SubString_Randomly("[]", None, ["apple","orange","pear"])
        


    @patch('utils.random.choice')
    def test_One_Replace(self,unrandom_Value):
        unrandom_Value.return_value = "apple"
        result = replace_SubString_Randomly("[]", "[] Hello World", ["apple","orange","pear"])
        self.assertEqual(result, "apple Hello World")

    @patch('utils.random.choice')
    def test_Multiple_Replace(self,unrandom_Value):
        unrandom_Value.return_value = "apple"
        result = replace_SubString_Randomly("[]", "[] [] [] Hello World", ["apple","orange","pear"])
        self.assertEqual(result, "apple apple apple Hello World")

if __name__ == 'main':
    unittest.main()
