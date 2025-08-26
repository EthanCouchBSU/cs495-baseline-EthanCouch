# a function to replace each instance of a substring within an input string with a 
# randomly picked string from a predetermined array of strings.

import random


fruits_List = ["Orange","Apple","Pear","Pineapple"]
test = "[] are really good"

def replace_SubStringBrackets_Randomly(substring,input,replace_List):
    bracket_Count = input.count("[]")
    return input.replace(substring, random.choice(replace_List))
        
        

print(replace_SubStringBrackets_Randomly("[]",test,fruits_List))