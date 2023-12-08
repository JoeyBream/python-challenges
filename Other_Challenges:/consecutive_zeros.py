'''Takes a string, returns the number of consecutive zeros'''
import time
def consecutive_zeros(string):
    full_max = []
    current_max = 0
    for letter in string:
        if letter == "0":
            current_max += 1
            full_max.append(current_max)
        else:
            current_max = 0 # Reset the maximum count found. Unecessary unless this is the first time 
    return max(full_max, default=0)
    

start = time.time_ns()

print(consecutive_zeros("asdaf"))
print(consecutive_zeros("10001"))
print(consecutive_zeros("101"))
print(consecutive_zeros("11"))
print(consecutive_zeros("0000"))
print(consecutive_zeros("000000-00-0-0"))
print(consecutive_zeros(""))

end = time.time_ns()
print(end - start)