''' Create a function which will add dots between each item in a string. '''
 # I had created a naive version of this. But then I found the method .join()

def add_dots(string):
    return ".".join(string)

# Naive version:
def remove_dots(string):
    A = ""
    for i in range(len(string)):
        if string[i] != ".":
            A += string[i]    
    return A