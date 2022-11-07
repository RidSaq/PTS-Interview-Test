from typing import List, Tuple
import math

"""
BONUS: I really enjoyed this question. As a bonus I have implemented some additional functionality to present my 
expertise with python. The extra functionality is as follows:   
1- Use of type annotations in variable / parameter declarations
2- Use of switch-case (python 3.10) instead of if-else
3- Use of try-except block where required
3- Implemented using OOP as follows:
    a. A robot class
    b. Initialisation (Constructor) cleans and validates the instructions list before assigning it to an instance variable.
    c. Constructor can also take user-defined start coordinates if provided. Otherwise, defaults to (0,0). 
    d. Use of private method and variables
4- Any instruction that is not LEFT, RIGHT, UP or DOWN is ignored and next instruction is processed. 
"""
class Robot:

    def __init__(self, instructions: List[str] = [], start_coordinates: Tuple[int] = (0, 0)) -> None:
        # Usually managed via logging:
        self.error = False  # Error flag
        self.error_message = ''

        # Validate instructions list before assigning to instance variable:
        try:
            # Check existence of a BEGIN and get its index from the instructions list:
            begin_index: int = instructions.index("BEGIN")
        except ValueError:
            # BEGIN not found
            self.error = True
            self.error_message = "'BEGIN' is missing from the list of instructions. Cannot Proceed."

        try:
            # Check existence of a STOP and get its index from the instructions list:
            stop_index: int = instructions.index("STOP")
        except ValueError:
            # STOP not found
            self.error = True
            self.error_message = "'STOP' is missing from the list of instructions. Cannot Proceed."

        # Check position of BEGIN and STOP so that index of BEGIN is before STOP:
        if stop_index < begin_index:
            self.error = True
            self.error_message = "'STOP' appears before 'BEGIN' in the list of instructions. Cannot Proceed."

        if self.error:
            # If error flags, initialise instruction to empty list so other methods don't process it
            # and print the error message
            self._instructions = []
            print(self.error_message)
        else:
            # Cleanup instructions and remove everything before first BEGIN and after first STOP.
            self._instructions = instructions[begin_index: stop_index + 1]  # slicing

        # Start coordinates. Private variables. default: (0, 0):
        self._coordinate_x1 = start_coordinates[0]
        self._coordinate_y1 = start_coordinates[1]

        # Coordinate to be updated after each instruction. Intialise the same as start coordinates:
        self.coordinate_x2 = start_coordinates[0]
        self.coordinate_y2 = start_coordinates[1]

    """
    To be called after initialising this class. 
    """
    def calculate_distance(self) -> float | None:
        if self.error:  # Check error flag in case there was an error during initialisation
            print('There was an error during Robot initialisation.', self.error_message)
            return

        # Note: instructions were already validated in the constructor so, no need to revalidate here
        for instruction in self._instructions:
            if instruction == 'BEGIN':
                pass  # Do nothing. Move on to next instruction. There can be multiple BEGINS which is fine.
            elif instruction == 'STOP':
                break  # break the for loop.
            else:
                # Split the instruction into direction and step and validate:
                spltd_instructions: List = instruction.split()
                if len(spltd_instructions) == 2:
                    direction = spltd_instructions[0]
                    step = int(spltd_instructions[1])
                    # Here we can validate that direction is among the accepted values: UP, DOWN, LEFT, RIGHT
                    # and step is an int value
                    if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT'] and isinstance(step, int):
                        self._move(direction, step)  # Only move if valid otherwise ignore and move to next step

        # All move instructions executed. Calculate distance:
        begin_coordinates = [self._coordinate_x1, self._coordinate_y1]
        stop_coordinates = [self.coordinate_x2, self.coordinate_y2]

        # Calculate Euclidean distance using formula: sqrt( (x2 - x1) ^ 2 + (y2 - y1) ^ 2 )
        # Manually:
        # distance = ((self.coordinate_x2-self._coordinate_x1) ** 2 + (self.coordinate_y2-self._coordinate_y1) ** 2) ** 0.5
        # OR using math.dist:
        distance = math.dist(begin_coordinates, stop_coordinates)

        print(f"The total distance between {begin_coordinates} and {stop_coordinates} is: {distance}\n")
        return distance

    """
    This is a private move method that updates the coordinates
    """
    def _move(self, direction: str = None, steps: int = 0) -> None:
        match direction:
            case "RIGHT":
                self.coordinate_x2 += steps
            case "LEFT":
                self.coordinate_x2 -= steps
            case "UP":
                self.coordinate_y2 += steps
            case "DOWN":
                self.coordinate_y2 -= steps
            case "BEGIN":
                pass  # This case block is optional. Do nothing
            case _:
                pass  # This is an unknown direction. Do nothing

        return  # 'return' here is optional. Good practice for readability
