# Define a function which takes a list of numbers between -100 and 100 and returns the 
# difference between the largest and smallest items.

def largest_difference(list):
    return sorted(list)[-1]-sorted(list)[0]