from format_number import *
import random

for i in range (10):
    x = random.uniform(20, 600)
    decimals = random.randrange(1,10)
    formatted_result = format_number(x, decimals)
    #TODO: #1  Fix the assertion - currently you can't convert the result of the above line back into a float 
    print(f"Original Number: {x}, Decimals: {decimals}, Formatted Result: {formatted_result}")