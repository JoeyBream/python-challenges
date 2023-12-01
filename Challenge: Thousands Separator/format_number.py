### Create a function which takes a number and returns the number as a string and add commas as a thousands separator.
from remove_dots import *

def format_number(num, decimals=2):
    i = str(int(num)) # Remove decimal, convert to string
    k = round(float(num-int(num)),decimals) ## Give as many decimals as requested 
    # Adding the case where decimal is greater than 0.9 and needs to be rounded
    if k == 1:
        num += 1
        i = str(int(num))
        print("k = 1") 
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