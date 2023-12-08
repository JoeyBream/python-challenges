'''Summary: Using ChatGPT3.5 to implement the challenges found at https://pythonprinciples.com/challenges/.
ChatGPT scored 100% for challenges rated 3/10 and 4/10. 

Methodology: Providing as an input "Write a solution to this python challenge:", followed by the description of the challenge.

Printing here the solution provided by ChatGPT on the first attempt, with a Yes/No on whether it has achieved the test, using PythonPrinciples test cases.'''

# 10. Flatten_list
def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]
# Result: PASS

# 11. Min Maxing
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# 12. Divisible by 3
def div_3(number):
    return number % 3 == 0
# Result: PASS
# Comment: To be fair this was a simple one.

# 13. Tic Tac Toe input
def get_row_col(cell):
    row = int(cell[1]) - 1
    col = ord(cell[0]) - ord("A")
    return row, col
# Result: Pass
# Comment: Great solution

# 14. Palindrome
def palindrome(s):
    return s == s[::-1]
# Result: Pass
# Comment: Very concise. Nice.

# 15. Up and down
def up_down(number):
    return (number - 1, number + 1)
# Result: Pass

# 16. Consecutive zeros
def consecutive_zeros(binary_string):
    return max(map(len, binary_string.split('1')))
# Result: PASS
# Comment: It passed the test cases. But it fails outside of the test case, when using characters other than 0 or 1.
