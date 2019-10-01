import unittest


def is_triangle(sides):
    """ To check if the sides formed triangle"""
    if min(sides) <= 0 or sum(sorted(sides)[:-1]) < sorted(sides)[-1]:
        return False
    else:
        return True


def equilateral(sides): 
    """ To check if the sides are equilater triangle """
    if is_triangle(sides):
        t1, t2, t3 = sides
        return t1 == t2 == t3
    else:
        return False

def isosceles(sides):
    """ To check if sides are isosceles triangle """
    if is_triangle(sides):
        t1, t2, t3 = sides
        return t1 == t2 or t2 == t3 or t3 == t1
    else:
        return False
            
    

def scalene(sides):
    if equilateral(sides) or isosceles(sides):
        return False
    else:
        return is_triangle(sides)





class TestEquilateralTriangle(unittest.TestCase):

    def test_equal_sides(self):
        self.assertIs(equilateral([5,5,5]), True)
    def test_unequal_sides(self):
        self.assertIs(isosceles([2,6,4]),False)
    def test_float_sides(self):
        self.assertTrue(equilateral([0.2, 0.2, 0.2]), True)


class TestIsoscelesTriangle(unittest.TestCase):

    def test_twoequal_sides(self):
        self.assertTrue(isosceles([8,5,5]), True)
    def test_equal_sides(self):
        self.assertIs(isosceles([4,4,4]),True)
    def test_float_sides(self):
        self.assertTrue(isosceles([0.2, 0.2, 0.4]), True)


                        

class TestScaleneTriangle(unittest.TestCase):

    def test_equal_sides(self):
        self.assertFalse(scalene([5,5,5]), False)
    def test_unequal_sides(self):
        self.assertTrue(scalene([2,6,4]), True)
    def test_float_sides(self):
        self.assertFalse(scalene([0.2, 0.2, 0.2]), False)


if __name__=='__main__':
    unittest.main(exit = False, verbosity=2)
