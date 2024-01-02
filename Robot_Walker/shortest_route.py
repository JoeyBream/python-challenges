''' Interview question: You are given an input string that controls the movement of a robot.
- "F" means take a step forward.
- "L" means turn 90 degrees to the left.
- "R" means turn 90 degrees to the right.
Example: "FLF" moves the robot one step forward, then turns it left by 90 degrees, then it takes another step.

Write a function that returns the minimum number of commands to return the robot to its starting position. 
Ignore any characters that aren't 'F', 'L' or 'R'.

'''
import math
import numpy as np
def position(string):
    x = y = d = 0
    pos = [x,y,d]
    for i in string:
        if i == "L":
            d += 90
        if i == "R":
            d -= 90 
        if i == "F":
            x += math.cos(math.radians(d))
            y += math.sin(math.radians(d))
    pos = [round(x),round(y),round(d)]
    return pos

def shortest_route(string):
    pos = position(string)
    x,y,d = pos[0], pos[1], pos[2]
    min_steps = abs(x) + abs(y)  # Initialize with the current position
    xy_vec = (x,y)
    d_vec = (math.cos(math.radians(d)),math.sin(math.radians(d)))
    #print(np.shape(d_vec))
    vector = np.dot(xy_vec,d_vec) 
    print(vector)

print(shortest_route("RFFFLLLFFFFFLLFFFF"))
print(shortest_route("RF"))
print(shortest_route("LFRFRFR"))
print(shortest_route("FxLxLxFx")) 