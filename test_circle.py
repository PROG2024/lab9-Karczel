"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def set_up(self):
        self.circle = Circle(1)
        self.c1 = Circle(3)
        self.c2 = Circle(4)
        self.c0 = Circle(0)

    # to test:
    #1. Typical case: Test `add_area` with two circles having positive radii.
# 2. Edge case: Test `add_area` when one of the circles has radius 0,
#    the other has non-zero radius. (Result should have same radius.)
#    Does `add_area` work the same regardless of which circle has radius 0?

    # Typical case

    def test_add_area(self):
        self.set_up()
        c = self.c1.get_area()
        self.c1.add_area(self.c2)
        self.assertEqual(5,self.c1.get_radius())
        self.assertGreater(self.c1, c)

    # Edge case

    def test_add_area_zero_back(self):
        self.set_up()
        c = self.c1.get_area()
        self.c1.add_area(self.c0)
        self.assertEqual(self.c1.get_area(), c)

    def test_add_area_zero_front(self):
        self.set_up()
        c = self.c1.get_area()
        self.c0.add_area(self.c1)
        self.assertEqual(c, self.c0.get_area())