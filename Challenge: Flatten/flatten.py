'''A function which takes a list of of mulptiple sublists, e.g. [[1, 2], [3, 4]]'''
'''flatten([[1, 2], [3, 4]]) should return [1, 2, 3, 4]'''
def flatten(A):
    B = []
    for i in A:
        for j in i:
            B.append(j)
    return B

### Test ###
flatten([1, 2, 3, 4])
flatten([[1, 2],[3,4]])