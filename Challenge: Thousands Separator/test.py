from format_number import *
import random

for i in range (10):
    x = random.uniform(20, 60)
    decimals = random.randrange(0,10)
    formatted_result = format_number(x, decimals)
    assert round(x,decimals) == float(formatted_result), f"Error: Original Number {x} not equal to Formatted Result {formatted_result}"
    print(f"Original Number: {x}, Decimals: {decimals}, Formatted Result: {formatted_result}")
