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
    print(pos)
    return pos

def shortest_route(string):
    pos = position(string)
    x,y,d = pos[0], pos[1], pos[2]
    min_steps = abs(x) + abs(y)  # Initialize with the current position

    for i in range(4):  # Try all possible rotations (0, 90, 180, 270 degrees)
        # Simulate movement based on the current rotation
        rotated_string = string
        if i > 0:
            rotated_string += "R" * i

        # Calculate new position
        new_pos = position(rotated_string)

        # Calculate steps and update min_steps if needed
        steps = abs(new_pos[0]) + abs(new_pos[1])
        min_steps = min(min_steps, steps)

print(position("RFFFLLLFFFFFLLFFFF"))

print(shortest_route("RF"))
print(shortest_route("LFRFRFR"))
print(shortest_route("FxLxLxFx")) 