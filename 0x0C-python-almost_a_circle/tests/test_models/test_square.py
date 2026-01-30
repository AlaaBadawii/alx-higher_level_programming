#!/usr/bin/python3
"""Test Square class module"""
from models.square import Square
import unittest
# test print of square
import io
from contextlib import redirect_stdout


class Test_Square(unittest.TestCase):
    """Test_Square class"""
    def setUp(self):
        self.sq = Square(5, 1, 2, 10)

    def test_square_init(self):
        """test square intilization"""
        self.assertIsInstance(self.sq, Square)

    def test_square_str(self):
        """test __str__ method of square"""
        self.assertEqual(str(self.sq), "[Square] (10) 1/2 - 5")

    def test_square_display(self):
        """test square display method"""
        s = Square(3, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###\n"
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            s.display()

        self.assertEqual(buffer.getvalue(), expected_output)

    def test_square_update(self):
        """test square update method"""
        sq = Square(4, 2, 6, 5)
        sq.update()
        self.assertEqual(str(sq), "[Square] (5) 2/6 - 4")

    def test_square_area(self):
        """test square area method"""
        self.assertEqual(self.sq.area(), 25)

    def test_square_size_property(self):
        """test square size property"""
        self.assertEqual(self.sq.width, 5)
        self.assertEqual(self.sq.height, 5)
