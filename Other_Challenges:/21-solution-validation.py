'''Challenge
Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

- the code must contain the def keyword
- - otherwise return "missing def"
- the code must contain the : symbol
- - otherwise return "missing :"
- the code must contain ( and ) for the parameter list
- - otherwise return "missing paren"
- the code must not contain ()
- - otherwise return "missing param"
- the code must contain four spaces for indentation
- - otherwise return "missing indent"
- the code must contain validate
- - otherwise return "wrong name"
- the code must contain a return statement
- - otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.'''

# Problem seems to be about mapping single inputs to single outputs, all using the same function.
# Seems like dictionaries or map would be useful.
# Creating the mapping

dict_include = {
    "def" : "missing def",
    ":" : "missing :",
    "(" : "missing paren",
    ")" : "missing paren",
    "    " : "missing indent",
    "validate" : "wrong name",
    "return" : "missing return",
    }

dict_exclude = {
    "()" : "missing param"
    }

def validate(input):
    # Testing for missing values
    for item in dict_include.keys():
        if (input.find(item) < 0):
            print(dict_include.get(item))
    
    # Testing for things included that should have been excluded.
    for item in dict_exclude.keys():
        if input.find(item) >= 0:
            print(dict_exclude.get(item))
    return

validate("Hi! This is Joey: Just writing a quick () ( ) param thingy you get me")
# validate("")
# TODO: Return 'True' if no errors raised.