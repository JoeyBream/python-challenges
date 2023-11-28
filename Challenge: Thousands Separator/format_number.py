### Create a function which takes a number and returns the number as a string and add commas as a thousands separator.
def format_number(int):
    i = str(int) 
    j = len(i)
    thousands = (j-1)//3
    leading_digits = (j-1)%3
    A = ""
    
    print("j has ",j," digits - that is", thousands, "000s and",leading_digits,"leading digits")
    
    A += i[:leading_digits+1]
    for x in range(thousands):
        A += ","+i[leading_digits+1:leading_digits+4]
    return A

print(format_number(2333))