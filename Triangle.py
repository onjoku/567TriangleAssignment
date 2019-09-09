import unittest

""" Assignmenst description: Program to determine classify Triangle
     Author: Ogadinma Njoku
     Surmmary: A homework assignment on triangle classification to demonstrate the application of test cases
      Details: All function returns a string with the type of triangle from three integer 
    values corresponding to the lengths of the three sides of the Triangle.
    
         all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then 
    return 'Right'


"""
def classifyTriangle(a,b,c):
    # require that the input values be >= 0 and <= 200
    if a >= 200 or b >= 200 or c >= 200:
        raise ValueError ( 'InvalidInput sides >= 200')
    elif a <= 0 or b <= 0 or c <= 0:
        raise ValueError ('InvalidInput sides <= 0')
    else:
        if a >= 0 or b >= 0 or c >= 0:
            # verify that all 3 inputs are integers
            # Python's "isinstance(object,type) returns True if the object is of the specified type
            if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
                raise ValueError ('InvalidInput Error not an Integer number')
        # This information was not in the requirements spec but
            
        # is important for correctness
        # the sum of any two sides must be strictly less than the third side
        
        # of the specified shape is not a triangle
        if (a + b <= c) or ( a + c <= b) or (c + b <= a):
            return 'NotATriangle'
        # now we know that we have a valid triangle
        if a == b and b == c and c == a:
            return 'Equilateral'
        elif (((a ** 2) + (b ** 2)), 2) == ((c ** 2), 2):
            return 'Right'
        elif (a == b)or (b == c)or(a == c):
            return 'Isosceles'
        elif (a != b) and (b != c) and (c != a):
            
            return 'Scalene'
        else:
            return 'NotEqual'


