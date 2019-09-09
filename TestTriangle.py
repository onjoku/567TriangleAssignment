import unittest
from Triangle import *
""" Assignmenst description: Program to determine classify Triangle
     Author: Ogadinma Njoku
     Surmmary: A homework assignment on triangle classification to demonstrate the application of test cases
     Result: All the test cases passed
     Test results were determined based on series of test performed.

"""



class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Right triangle')
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
 
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

 
