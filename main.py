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


def move(facing, x_axis, y_axis):
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


def move_north():
    # move up on y axis ; positive addition to y axis
    return 1, "y"


def move_south():
    # move down on y axis ; negative addition to y axis
    return -1, "y"


def move_east():
    # move left on x axis ; positive addition to x axis
    return 1, "x"


def move_west():
    # move right on x axis ; negative addition to x axis
    return -1, "x"


def get_move_translation(facing):
    # get_move_translation ; facing - can be NORTH, SOUTH, EAST, WEST ; returns move_step, axis
    switcher = {
        "NORTH": move_north(),
        "SOUTH": move_south(),
        "EAST": move_east(),
        "WEST": move_west(),
    }

    # get facing axis translation (positive or negative) and axis
    return switcher.get(facing, "Invalid Facing Position")


def get_move_translation(facing):
    # get_move_translation ; facing - can be NORTH, SOUTH, EAST, WEST ; returns move_step, axis
    switcher = {
        "NORTH": move_north(),
        "SOUTH": move_south(),
        "EAST": move_east(),
        "WEST": move_west(),
    }

    # get facing axis translation (positive or negative) and axis
    return switcher.get(facing, "Invalid Facing Position")
    if debug_flag:
        print("move step: ", move_step)
        print("move axis: ", axis)


def move(facing, x_axis, y_axis):

    # do the actual movement
    move_step, axis = get_move_translation(facing)
    if axis == 'x':
        if check_if_coordinates_valid(x_axis+move_step, y_axis):
            global curr_x_axis
            curr_x_axis = x_axis+move_step
            if debug_flag:
                print("moving on x axis, x is now :", curr_x_axis)
            return True
        else:
            if debug_flag:
                print("move would be illegal x-axis value would be ", x_axis+move_step)
            return False
    if axis == 'y':
        if check_if_coordinates_valid(x_axis, y_axis+move_step):
            global curr_y_axis
            curr_y_axis = y_axis+move_step
            if debug_flag:
                print("moving on y axis, y is now :", curr_y_axis)
            return True
        else:
            if debug_flag:
                print("move would be illegal y-axis value would be ", y_axis+move_step)
            return False


def rotate_left():
    # rotate 90deg to the left
    global curr_facing_position
    if curr_facing_position == 'NORTH':
        set_direction("WEST")

    elif curr_facing_position == 'WEST':
        set_direction("SOUTH")

    elif curr_facing_position == 'SOUTH':
        set_direction("EAST")

    elif curr_facing_position == 'EAST':
        set_direction("NORTH")

    if debug_flag:
        print("rotating left")
    return curr_facing_position


def rotate_right():

    # rotate 90deg to the right
    global curr_facing_position
    if curr_facing_position == 'NORTH':
        set_direction("EAST")
    elif curr_facing_position == 'EAST':
        set_direction("SOUTH")
    elif curr_facing_position == 'SOUTH':
        set_direction("WEST")
    elif curr_facing_position == 'WEST':
        set_direction("NORTH")

    if debug_flag:
        print("rotating right")
    return curr_facing_position


def rotate(direction):
    switcher = {
        "LEFT": rotate_left,
        "RIGHT": rotate_right
    }
    return switcher.get(direction, "Invalid Direction")()


def report():
    return curr_x_axis, curr_y_axis, curr_facing_position


def report_str():
    reporting_output = report()
    print "Output: " + str(reporting_output[0])+","+str(reporting_output[1])+","+reporting_output[2]


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print ("You must supply the input file to process instructions ; Example: python main.py <input_file.txt>")
    else:
        # file input
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
                    move(curr_facing_position, curr_x_axis, curr_y_axis)
                if "LEFT" in line:
                    rotate("LEFT")
                if "RIGHT" in line:
                    rotate("RIGHT")
                if "REPORT" in line:
                    report_str()
