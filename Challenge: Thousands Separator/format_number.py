### Create a function which takes a number and returns the number as a string and add commas as a thousands separator.
from remove_dots import *

def format_number(num, decimals=2):
    i = remove_dots(num) 
    k = round(float(num-int(i)),decimals) ## Give as many decimals as requested 
    j = len(i)
    thousands = (j-1)//3
    leading_digits = (j-1)%3
    A = ""
    A += i[:leading_digits+1]
    pos = leading_digits+1
    for x in range(thousands):
        A += ","+i[pos:pos+3]
        pos += 3
    A += str(k)[1:]
    return A

print(format_number(2333.223353,4))