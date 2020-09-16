# -*- coding: utf-8 -*-
"""
Updated Sep 16, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Pooja Patel
@author: Pooja Patel
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testTriangle(self):
        self.assertEqual(classifyTriangle(1, 6, 8), 'NotATriangle')

    def testValidInput1(self):
        """ To test for input less than 0"""
        self.assertEqual(classifyTriangle(-1, 1, 2), 'InvalidInput')

    def testValidInput2(self):
        """ To test for integers input"""
        self.assertEqual(classifyTriangle(1, "a", "b"), 'InvalidInput')

    def testValidInput3(self):
        """ To test for input above 200"""
        self.assertEqual(classifyTriangle(201, 1, 8), 'InvalidInput')

    def testRightTriangleA(self):
        """ To test right angle triangles"""
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        """ To test Right angle triangles"""
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testEquilateralTriangles(self):
        """ To test Equilateral triangles"""
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testIsoscelesTriangles(self):
        """ To test Isosceles triangles"""
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles')

    def testScaleneTriangles(self):
        """ To test Scalene triangles"""
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

