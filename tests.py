import unittest
from math import *
import rectangle
import circle
import square
import triangle

class RectangleTest(unittest.TestCase):
    
#---------------AREA-----------------#
    def testAREA_zero_args(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def testAREA_one_zero_arg(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def testAREA_positive_args(self):
        res = rectangle.area(4, 5)
        self.assertEqual(res, 20)

    def testAREA_negative_args(self):
        res = rectangle.area(-3, 4)
        self.assertEqual(res, -12)
        
    def testAREA_float_args(self):
        res = rectangle.area(2.5, 1.5)
        self.assertEqual(res, 3.75)
        
#---------------PERIMETER-----------------#
    def testPERIMETER_positive_args(self):
        res = rectangle.perimeter(4, 5)
        self.assertEqual(res, 18)
        
    def testPERIMETER_negative_args(self):
        res = rectangle.perimeter(4, -3)
        self.assertEqual(res, 2)

    def testPERIMETER_one_zero_arg(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def testPERIMETER_float_args(self):
        res = rectangle.perimeter(2.5, 1.5)
        self.assertEqual(res, 8)

class SquareTest(unittest.TestCase):

#---------------AREA-----------------#
    def testAREA_zero_args(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def testAREA_positive_args(self):
        res = square.area(3)
        self.assertEqual(res, 9)

    def testAREA_negative_args(self):
        res = square.area(-3)
        self.assertEqual(res, 9)

    def testAREA_float_args(self):
        res = square.area(0.5)
        self.assertEqual(res, 0.25)

#---------------PERIMETER-----------------#
    def testPERIMETER_positive_args(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)

    def testPERIMETER_negative_args(self):
        res = square.perimeter(-3)
        self.assertEqual(res, -12)

    def testPERIMETER_zero_args(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def testPERIMETER_float_args(self):
        res = square.perimeter(0.5)
        self.assertEqual(res, 2)

class CircleTest(unittest.TestCase):

#---------------AREA-----------------#
    def testAREA_zero_args(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def testAREA_positive_args(self):
        res = circle.area(3)
        self.assertAlmostEqual(res, 9 * pi)

    def testAREA_negative_args(self):
        res = circle.area(-2)
        self.assertAlmostEqual(res, 4 * pi)

    def testAREA_float_args(self):
        res = circle.area(0.5)
        self.assertAlmostEqual(res, pi / 4)

#---------------PERIMETER-----------------#
    def testPERIMETER_positive_args(self):
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 6 * pi)

    def testPERIMETER_negative_args(self):
        res = circle.perimeter(-2)
        self.assertAlmostEqual(res, -4 * pi)

    def testPERIMETER_zero_args(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def testPERIMETER_float_args(self):
        res = circle.perimeter(0.5)
        self.assertAlmostEqual(res, pi)

class TriangleTest(unittest.TestCase):

#---------------AREA-----------------#
    def testAREA_one_zero_arg(self):
        res = triangle.area(6, 0)
        self.assertEqual(res, 0)

    def testAREA_positive_args(self):
        res = triangle.area(6, 4)
        self.assertEqual(res, 12)

    def testAREA_negative_args(self):
        res = triangle.area(6, -2)
        self.assertEqual(res, -6)

    def testAREA_float_args(self):
        res = triangle.area(2.5, 6)
        self.assertEqual(res, 7.5)

#---------------PERIMETER-----------------#
    def testPERIMETER_positive_args(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def testPERIMETER_negative_args(self):
        res = triangle.perimeter(3, 4, -5)
        self.assertEqual(res, 2)

    def testPERIMETER_float_args(self):
        res = triangle.perimeter(1.5, 2, 2.5)
        self.assertEqual(res, 6)

    def testPERIMETER_equal_sides(self):
        res = triangle.perimeter(5, 5, 5)
        self.assertEqual(res, 15)
