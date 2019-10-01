
"""
Program to demonstrate the classify triangle
Author: Ogadinma Njoku
Details: function returns a string """
import unittest

def classifyTriangle(a, b, c):
    """ Triangle multiple sets of functions  """
    if a >= 200 or b >= 200 or c >= 200:
        raise ValueError('InvalidInput sides >= 200')
    elif a <= 0 or b <= 0 or c <= 0:
        raise ValueError('InvalidInput sides <= 0')
    else:
        if a >= 0 or b >= 0 or c >= 0:
            raise ValueError('InvalidInput Error not an Integer number')
        if (a + b <= c)or(a + c <= b)or(c + b <= a):
            return 'NotATriangle'
        if a == b and b == c and c == a:
            return 'Equilateral'
        if (((a ** 2) + (b ** 2)), 2) == ((c ** 2), 2):
            return 'Right'
        if (a == b)or (b == c)or(a == c):
            return 'Isosceles'
        if (a != b) and (b != c) and (c != a):
            return 'Scalene'
        return 'NotEqual'

class TestTriangles(unittest.TestCase):
    """ Testing Triangle """
    def testRightTriangleA(self):
        """ define multiple sets of tests as functions with names that begin """
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def testRightTriangleB(self):
        """ define multiple sets of tests as functions with names that begin """
        self.assertEqual(classifyTriangle(5, 3, 4), 'Scalene', '5,3,4 is a Right triangle')
    def testEquilateralTriangles(self):
        """ define multiple sets of tests as functions with names that begin """
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
if __name__ == '__main__':
    print('Running unit tests on Classify Triangle')
    unittest.main()
