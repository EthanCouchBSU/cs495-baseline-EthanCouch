

import random

# a function to replace each instance of a substring within an input string with a 
# randomly picked string from a predetermined array of strings.
def replace_SubString_Randomly(substring,input,replace_List):
    return input.replace(substring, random.choice(replace_List))
        