import unittest

from main import check_if_coordinates_valid, get_move_translation, move, set_location


class TestPacman(unittest.TestCase):

    def test_valid_coordinates_min(self):
        self.assertEqual(check_if_coordinates_valid(0, 0), True, "Should be true")

    def test_valid_coordinates_max(self):
        self.assertEqual(check_if_coordinates_valid(4, 4), True, "Should be true")

    def test_invalid_coordinates_min(self):
        self.assertEqual(check_if_coordinates_valid(-1, -1), False, "Should be false")

    def test_invalid_coordinates_max(self):
        self.assertEqual(check_if_coordinates_valid(5, 5), False, "Should be false")

    def test_north_translation(self):
        value, axis = get_move_translation("NORTH")
        self.assertEqual(value == 1 and axis == 'y', True, "Should move by 1 step on y-axis")

    def test_south_translation(self):
        value, axis = get_move_translation("SOUTH")
        self.assertEqual(value == -1 and axis == 'y', True, "Should move by -1 step on y-axis")

    def test_west_translation(self):
        value, axis = get_move_translation("WEST")
        self.assertEqual(value == -1 and axis == 'x', True, "Should move by -1 step on x-axis")

    def test_east_translation(self):
        value, axis = get_move_translation("EAST")
        self.assertEqual(value == 1 and axis == 'x', True, "Should move by 1 step on x-axis")

    def test_moving_north_from_origin(self):
        curr_x_axis = 0
        curr_y_axis = 0
        self.assertEqual(move("NORTH", curr_x_axis, curr_y_axis), True, "Should be true")

    def test_moving_south_from_origin(self):
        curr_x_axis = 0
        curr_y_axis = 0
        self.assertEqual(move("SOUTH", curr_x_axis, curr_y_axis), False, "Should be False")

    def test_moving_west_from_north_west_max(self):
        curr_x_axis = 4
        curr_y_axis = 4
        self.assertEqual(move("WEST", curr_x_axis, curr_y_axis), True, "Should be True")

    def test_moving_east_from_north_east_max(self):
        curr_x_axis = 4
        curr_y_axis = 0
        self.assertEqual(move("EAST", curr_x_axis, curr_y_axis), False, "Should be False")

    def test_moving_north_from_north_west_max(self):
        curr_x_axis = 4
        curr_y_axis = 4
        self.assertEqual(move("NORTH", curr_x_axis, curr_y_axis), False, "Should be False")

    def test_set_location(self):
        self.assertEqual(set_location(2, 2), True, "Should be True")


if __name__ == '__main__':
    unittest.main()
