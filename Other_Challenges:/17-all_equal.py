"Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True."

def all_equal(list):
    for i in range(len(list)):
        if list[0] != list[i]:
            return False
            break
    return True

## It is possible to do this using the 'all' function, which checks a condition for every item in an iterable and returns an overall True or False.
def all_even(list):
    return all(x % 2 == 0 for x in list)

## Creating other functions using 'all'
def all_greater(list,n): # Checks all items greater than n for a list of numbers
    return all(x > n for x in list)

def all_longer(list,min_length): # Checks all items have a length longer than a minimum
    return all(len(str(x)) > min_length for x in list)

def all_even(list): # Checks all items are even.
    return all(x % 2 == 0 for x in list)
    