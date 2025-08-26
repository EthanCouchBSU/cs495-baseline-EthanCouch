from utils import *


test_List = ["apple","orange","pear"]

def test_NoMatches():
    assert replace_SubString_Randomly("[]", "Hello World", test_List) == "Hello World"