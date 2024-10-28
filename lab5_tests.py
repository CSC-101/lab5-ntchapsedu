import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_Time_repr_1(self):
        time1 = data.Time(3, 10, 30)
        time2 = data.Time(2, 5, 15)
        result = lab5.time_add(time1,time2)
        expected = data.Time(5,15,45)
        self.assertEqual(result, expected)

    def test_Time_repr_2(self):
        time1 = data.Time(3, 50, 30)
        time2 = data.Time(2, 5, 35)
        result = lab5.time_add(time1, time2)
        expected = data.Time(5, 56, 5)
        self.assertEqual(result, expected)

    # Part 4
    def test_Time_is_descending_1(self):
        input = [5.3, 9.8, 1.0, 4.7, 4.6, 3.5, 11.78]
        result = lab5.is_descending(input)
        expected = [11.78, 9.8, 5.3, 4.7, 4.6, 3.5, 1.0]
        self.assertEqual(result, expected)

    def test_Time_is_descending_2(self):
        input = [36.1,15.2,40,51.98,42,0.01]
        result = lab5.is_descending(input)
        expected = [51.98, 42, 40, 36.1, 15.2, 0.01]
        self.assertEqual(result, expected)

    # Part 5
    def test_Time_largest_between_1(self):
        input = [1,5,2,8,9,3]
        up = 6
        low = 1
        result = lab5.largest_between(input, up, low)
        expected = 5
        self.assertEqual(expected,result)

    def test_Time_largest_between_2(self):
        input = [11, 22, 4, 16, 10, 24, 9]
        up = 9
        low = 10
        result = lab5.largest_between(input, up, low)
        expected = None
        self.assertEqual(expected, result)
    # Part 6
    def test_Time_furthest_from_origin_1(self):
        input = [data.Point(1,1),data.Point(2,3),data.Point(4,9),data.Point(5,3)]
        result = lab5.furthest_from_origin(input)
        expected = data.Point(4,9)
        self.assertEqual(expected, result)

    def test_Time_furthest_from_origin_2(self):
        input = [data.Point(9.11, 2.13), data.Point(0, 0), data.Point(32.9,43.9), data.Point(31.3, 39.8)]
        result = lab5.furthest_from_origin(input)
        expected = data.Point(32.9,43.9)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
