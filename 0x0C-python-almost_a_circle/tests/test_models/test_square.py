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
    # update
    def test_square_update_1_args(self):
        """test update function. 1 argument"""
        self.sq.update(89)
        self.assertEqual(self.sq.id, 89)

    def test_square_update_2_args(self):
        """test update function 2 arguments"""
        self.sq.update(89, 2)
        self.assertEqual(self.sq.id, 89)
        self.assertEqual(self.sq.size, 2)

    def test_square_update_3_args(self):
        """test update function 4 arguments"""
        self.sq.update(89, 2, 3)
        self.assertEqual(self.sq.id, 89)
        self.assertEqual(self.sq.size, 2)
        self.assertEqual(self.sq.x, 3)

    def test_square_update_4_args(self):
        """test update function 4 arguments"""
        self.sq.update(89, 2, 3, 4)
        self.assertEqual(self.sq.id, 89)
        self.assertEqual(self.sq.size, 2)
        self.assertEqual(self.sq.x, 3)
        self.assertEqual(self.sq.y, 4)

    def test_square_update_1_kwargs(self):
        """test update using kwargs 1 kwarg"""
        self.sq.update(id=1)
        self.assertEqual(self.sq.id, 1)

    def test_square_update_2_kwargs(self):
        """test update using kwargs 2 kwarg"""
        self.sq.update(id=1, size=1)
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq.size, 1)

    def test_square_update_3_kwargs(self):
        """test update using kwargs 3 kwarg"""
        self.sq.update(id=1, size=1, x=1)
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.x, 1)
        self.assertEqual(self.sq.y, 2)

    def test_square_update_4_kwargs(self):
        """test update using kwargs 4 kwarg"""
        self.sq.update(id=1, size=1, x=1, y=1)
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.x, 1)
        self.assertEqual(self.sq.y, 1)

    def test_square_update_kwargs_no_order(self):
        """test update using kwargs no need to be ordered"""
        self.sq.update(size=1, id=1, x=1, y=1)
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.x, 1)
        self.assertEqual(self.sq.y, 1)

    # to_dict
    def test_square_to_dict(self):
        excepted = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        dictionary = self.sq.to_dictionary()
        self.assertEqual(dictionary, excepted)
