''' Define a function named list_xor. Your function should take three parameters: n, list1 and list2.

Your function must return whether n is exclusively in list1 or list2.

In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.

For example:

list_xor(1, [1, 2, 3], [4, 5, 6]) == True
list_xor(1, [0, 2, 3], [1, 5, 6]) == True
list_xor(1, [1, 2, 3], [1, 5, 6]) == False
list_xor(1, [0, 0, 0], [4, 5, 6]) == False '''

# Final solution
def list_xor(n, list1, list2):
    return (n in list1) != (n in list2)

# Naive solution: 
def list_xor(n,list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return False
            elif i==n or j==n:
                return True
            else:
                return False
                return True