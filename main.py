import sys

# global vars
curr_x_axis = 0
curr_y_axis = 0
curr_facing_position = ""
debug_flag = False


def check_if_coordinates_valid(x_axis_intended, y_axis_intended):
    # pacman can be on valid x-axis coordinates && valid y-axis coordinates
    if x_axis_intended < 5 and x_axis_intended >= 0 and y_axis_intended < 5 and y_axis_intended >= 0:
        return True
    else:
        if debug_flag:
            print(
                "illegal move ; move would exceed bounds x:",
                x_axis_intended,
                " y:",
                y_axis_intended
            )
        return False


def set_location(x_axis, y_axis):
    if (check_if_coordinates_valid(x_axis, y_axis)):
        global curr_x_axis
        curr_x_axis = x_axis
        global curr_y_axis
        curr_y_axis = y_axis
        if debug_flag:
            print ("location set", curr_x_axis, curr_y_axis)
        return True
    else:
        if debug_flag:
            print ("illegal location set", curr_x_axis, curr_y_axis)
        return False


def set_direction(direction_intended):
    if direction_intended == "NORTH" or direction_intended == "EAST" or direction_intended == "SOUTH" or direction_intended == "WEST":

        global curr_facing_position
        curr_facing_position = direction_intended
        if debug_flag:
            print ("direction set", curr_facing_position)
            return True
    else:
        if debug_flag:
            print ("bad direction given", direction_intended)
            sys.exit(-1)
        return False

    # do the actual movement
    move_step, axis = get_move_translation(facing)
    if axis == 'x':
        if check_if_coordinates_valid(x_axis+move_step, y_axis):
            global curr_x_axis
            curr_x_axis = x_axis+move_step
            return True
        else:
            if debug_flag:
                print("move would be illegal x-axis value would be ", x_axis+move_step)
            return False
    if axis == 'y':
        if check_if_coordinates_valid(x_axis, y_axis+move_step):
            global curr_y_axis
            curr_y_axis = y_axis+move_step
            return True
        else:
            if debug_flag:
                print("move would be illegal y-axis value would be ", y_axis+move_step)
            return False


if __name__ == '__main__':
    # file input

    if len(sys.argv) == 1:
        print ("You must supply the input file to process instructions ; Example: python main.py <input_file.txt>")
    else:
        input_file_arg = sys.argv[1]

        if len(sys.argv) > 1:
            if len(sys.argv) == 3:
                debug_flag_check = sys.argv[2]
                if debug_flag_check == "--debug" or debug_flag_check == "-d":
                    debug_flag = True
                print("debug flag is ", debug_flag)
        with open(input_file_arg, 'r') as f:
            lines = f.readlines()
            if debug_flag:
                print ("DEBUG: ", lines)
            for line in lines:
                line = line.rstrip('\n')
                if "PLACE" in line:
                    coordinates_with_direction = line.split(" ")[1]
                    coordinates = coordinates_with_direction.split(",")[0], coordinates_with_direction.split(",")[1]
                    direction = coordinates_with_direction.split(",")[2]
                    set_location(int(coordinates[0]), int(coordinates[1]))
                    set_direction(direction)
                if "MOVE" in line:
                    # do movement
                if "LEFT" in line:
                    print ("go left")
                if "RIGHT" in line:
                    print ("go right")
                if "REPORT" in line:
                    # report
                    print ("report")
