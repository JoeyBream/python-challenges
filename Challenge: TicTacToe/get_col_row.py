### A function which takes an input such as 'B1' and returns the index of the row and column which correspond. ###
### This test was written rather strangely, since B1 is defined as column B, row 1.###
### This means that getting 'row_col' would give 1B instead of B1, unless you reverse the insides of your algorithm ###
### I have extended this from a 3x3 to a 10x10 board

def get_row_col(string):
    letters = "ABCDEFGHIJ"
    numbers = [0,1,2,3,4,5,6,7,8,9]
    i = int(string[1:]) # Since string[1] will be a written number
    row = numbers[i-1]
    col = letters.find(string[0])
    return (col, row)

print(get_row_col("A1"))
print(get_row_col("J10"))
