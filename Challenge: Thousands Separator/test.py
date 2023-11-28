from format_number import *
import random

for i in range (10):
    x = random.uniform(20, 600)
    decimals = random.randrange(1,10)
    formatted_result = format_number(x, decimals)
    # Fix the assertion - currently you can't convert the result back into a float 
    assert round(x,decimals) == float(formatted_result), f"Error: Original Number {x} not equal to Formatted Result {formatted_result}. This resulted from using {decimals} decimals."
    print(f"Original Number: {x}, Decimals: {decimals}, Formatted Result: {formatted_result}")