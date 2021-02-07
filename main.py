if __name__ == '__main__':
    with open('test.1.txt', 'r') as f:
        lines = f.readlines()
        # print (lines)
        for line in lines:
            line = line.rstrip('\n')
            if "PLACE" in line:
                coordinates_with_direction = line.split(" ")[1]
                coordinates = coordinates_with_direction.split(",")[0], coordinates_with_direction.split(",")[1]
                direction = coordinates_with_direction.split(",")[2]
                # print (direction)
                # set location
            if "MOVE" in line:
                # do movement
                print ("do movement")
            if "LEFT" in line:
                print ("go left")
            if "RIGHT" in line:
                print ("go right")
            if "REPORT" in line:
                # report
                print ("report")
