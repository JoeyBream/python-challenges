"Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True."

def all_equal(list):
    for i in range(len(list)):
        if list[0] != list[i]:
            return False
            break
    return True