"""Q3. A robot moves around a flat surface from position (0,0). It accepts instructions, and moves accordingly. For
example:
“BEGIN”
LEFT 3
UP 5
RIGHT 4
DOWN 7
The first word indicates direction and the number shows steps. The robot will stop moving with
instruction “STOP”. Please write a function, which accepts instructions as a list. When first
“STOP” instruction is given, it calculates the distance of Robot from the original position (0,0) """

from typing import List
from Robot import Robot

instructions: List[str] = [
    "LEFT 3",
    "UP 5",
    "RIGHT 4",
    "DOWN 7",
    "BEGIN",    # <- Everything before this BEGIN will be ignored
    "sdsdf",    # <- This instruction is invalid and will be ignored
    "LEFT 3",
    "UP 5",
    "BEGIN",    # <- Another BEGIN. Will be ignored
    "RIGHT 4",
    "DOWN 7",
    "STOP",     # <- Everything after this STOP will be ignored
    "LEFT 3",
    "UP 5",
    "RIGHT 4",
    "DOWN 7",
    "dsafsdf",
    "STOP"
]

if __name__ == "__main__":
    robot: Robot = Robot(instructions)
    robot.calculate_distance()

    # We can also give the robot  our own start coordinates:
    robot_2: Robot = Robot(instructions, (1, 1))
    robot_2.calculate_distance()

# Note: Both distances above will be the same because the instructions are the same with respect to starting point
