### A supplementary function to help with handling decimals
def remove_dots(string):
    A = ""
    string = str(string)
    for i in range(len(string)):
        if string[i] != ".":
            A += string[i]
        else:
            break   
    return A