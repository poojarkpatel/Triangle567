# -*- coding: utf-8 -*-
"""
Updated Sep 16, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Pooja Patel
@author: Pooja Patel
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangle(unittest.TestCase):
    """test triangle class"""
    # define multiple sets of tests as functions with names that begin
    def test_triangle(self):
        """test triangles"""
        self.assertEqual(classify_triangle(1, 6, 8), 'NotATriangle')

    def test_valid_input1(self):
        """ To test for input less than 0"""
        self.assertEqual(classify_triangle(-1, 4, 2), 'InvalidInput')

    def test_valid_input2(self):
        """ To test for integers input"""
        self.assertEqual(classify_triangle(1, "a", "b"), 'InvalidInput')

    def test_valid_input3(self):
        """ To test for input above 200"""
        self.assertEqual(classify_triangle(201, 1, 8), 'InvalidInput')

    def test_right_triangle_a(self):
        """ To test right angle triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def test_right_triangle_b(self):
        """ To test Right angle triangles"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right')

    def test_equilateral_triangles(self):
        """ To test Equilateral triangles"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test_isosceles_triangles(self):
        """ To test Isosceles triangles"""
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles')

    def test_scalene_triangles(self):
        """ To test Scalene triangles"""
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
