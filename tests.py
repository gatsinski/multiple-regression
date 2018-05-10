import unittest
from utils import solve_system, get_variables, get_answers, multiply_lists


class GaussianEliminationTestCase(unittest.TestCase):

    def test_valid_input(self):
        variables = [
            [6, 4863, 8761, 654],
            [4863, 4521899, 8519938, 620707],
            [8761, 8519938, 21022091, 905925],
            [654, 620707, 905925, 137902]
        ]
        results = [714, 667832, 1265493, 100583]

        result = solve_system(variables, results)

        expected_result = [
            6.701336536389188,
            0.07836603673386534,
            0.015041331199344957,
            0.24605633258014775
        ]

        self.assertEqual(result, expected_result)


class GetVariablesTestCase(unittest.TestCase):

    def test_valid_input(self):
        z = [31.4, 14.6, 6.4, 28.3, 42.1, 15.3]
        w = [345, 168, 94, 187, 621, 255]
        x = [65, 18, 0, 185, 87, 0]
        y = [23, 18, 0, 98, 10, 0]

        result = get_variables(z, w, x, y)

        expected_result = [
            [6, 138.10000000000002, 1670, 355],
            [138.10000000000002,
             4047.4700000000003,
             49225.100000000006,
             11202.0],
            [1670, 49225.100000000006, 641720, 114071],
            [355, 11202.0, 114071, 46343]
        ]

        self.assertEqual(result, expected_result)


class GetAnswersTestCase(unittest.TestCase):

    def test_valid_input(self):
        z = [31.4, 14.6, 6.4, 28.3, 42.1, 15.3]
        w = [345, 168, 94, 187, 621, 255]
        x = [65, 18, 0, 185, 87, 0]
        y = [23, 18, 0, 98, 10, 0]

        result = get_answers(z, w, x, y)

        expected_result = [149, 4179.4, 35495, 20819]

        self.assertEqual(result, expected_result)


class MultiplyListTestCase(unittest.TestCase):

    def test_valid_input(self):
        list_a = [1, 2, 3]
        list_b = [4, 5, 6]

        result = multiply_lists(list_a, list_b)

        expected_result = 32

        self.assertEqual(result, expected_result)

    def test_mismatching_lists(self):
        list_a = [1, 2, 3]
        list_b = [4, 5, 6, 9]

        result = multiply_lists(list_a, list_b)
        swaped_params_result = multiply_lists(list_b, list_a)

        expected_result = 32

        self.assertEqual(result, expected_result)
        self.assertEqual(swaped_params_result, expected_result)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
