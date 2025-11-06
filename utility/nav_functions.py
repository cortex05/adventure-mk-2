from typing import List


def navigation_options(target: int, actual_options: list, moving_coords: list):
    choice = target - 1
    print(f'Modded :{choice}')

    if choice in actual_options:
        if target == 1:
            # West
            moving_coords[1] = moving_coords[1] - 1
        elif target == 2:
            # North
            moving_coords[0] = moving_coords[0] - 1
        elif target == 3:
            # South
            moving_coords[0] = moving_coords[0] + 1
        elif target == 4:
            # East
            moving_coords[1] = moving_coords[1] + 1
        return target
    else:
        input("Please pick a valid option. Press enter to continue")


def reverse_step(last_command, moving_coords):
    if last_command == 1:
        # Came  west, move east
        moving_coords[1] = moving_coords[1] + 1

    elif last_command == 2:
        # Came north, move south
        moving_coords[0] = moving_coords[0] + 1
    elif last_command == 3:
        # was Came south, head north
        moving_coords[0] = moving_coords[0] - 1
    elif last_command == 4:
        # Came east, move west
        moving_coords[1] = moving_coords[1] - 1

def compass_display(options: List[int]):
    one = '1' if 0 in options else ' '
    two = '2' if 1 in options else ' '
    three = '3' if 2 in options else ' '
    four = '4' if 3 in options else ' '
    holder = f'      {two}    \n' + f'      |     \n' + f' {one} ──   ── {four} \n' + f'      {'|'}     \n' + f'      {three}    \n'

    return holder


    
