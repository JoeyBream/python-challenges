''' Interview question: You are given an input string that controls the movement of a robot.
- "F" means take a step forward.
- "L" means turn 90 degrees to the left.
- "R" means turn 90 degrees to the right.
Example: "FLF" moves the robot one step forward, then turns it left by 90 degrees, then it takes another step.

Write a function that returns the minimum number of commands to return the robot to its starting position. 
Ignore any characters that aren't 'F', 'L' or 'R'.

'''
import math
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
    x = pos[0], y = pos[1], d = pos[2], s = 0
    s += abs(x) + abs(y)
    # Calculate the contribution from d #
        # Using vectors? Unsure..
    return s

print(position("RFFFLLLFFFFFLLFFFF"))

# assert shortest_route("RF")==3
# assert shortest_route("LFRFRFR") == 1
# assert shortest_route("FxLxLxFx")== 0 