'''Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise. '''

def triple_and(para1,para2,para3):
    return all(x == True for x in [para1,para2,para3])