#!/usr/bin/python3
"""Tests for Rectangle module"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
# io and contextlib used to redirect the output
import io
from contextlib import redirect_stdout


class Test_Rectangle(unittest.TestCase):
    """Test_Rectangle class"""
    def setUp(self):
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 2, 0, 0, 12)

    def test_rectangle_init(self):
        """test that r1 intilized correctly,
            with two args passed width and height"""
        r1 = Rectangle(2, 10)
        self.assertIsInstance(r1, Rectangle)

    def test_rectangle_init1(self):
        """test no args passing"""
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    # ID
    def test_Rectangle_id_auto_increment(self):
        """test multiple ids auto increment"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 3)
        r3 = Rectangle(10, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_rectangle_id(self):
        """test that rectangle id set correctly"""
        self.assertEqual(self.r.id, 12)

    # Width
    def test_rectangle_width(self):
        """test rectangle width"""
        self.assertEqual(self.r.width, 10)

    def test_rectangle_width_setter(self):
        """test rectangle width setter"""
        self.r.width = 20
        self.assertEqual(self.r.width, 20)

    def test_rectangle_width_str(self):
        """test the validation of width value"""
        with self.assertRaises(TypeError):
            r = Rectangle("2", 2)

    def test_rectangle_width_negative(self):
        """test the validation of width value"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_rectangle_width_zero(self):
        """test the validation of width value"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    # Height
    def test_rectangle_height(self):
        """test rectangle height"""
        self.assertEqual(self.r.height, 2)

    def test_rectangle_height_setter(self):
        """test rectangle height setter"""
        self.r.height = 4
        self.assertEqual(self.r.height, 4)

    def test_rectangle_height_str(self):
        """test the validation of height value"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, "2")

    def test_rectangle_height_negative(self):
        """test the validation of height value"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_rectangle_height_zero(self):
        """test the validation of height value"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    # X
    def test_rectangle_x(self):
        """test rectangle x"""
        self.assertEqual(self.r.x, 0)

    def test_rectangle_x_setter(self):
        """test rectangle x setter"""
        self.r.x = 1
        self.assertEqual(self.r.x, 1)

    def test_rectangle_x_default(self):
        """test default values"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

    def test_rectangle_x_str(self):
        """test the validation of x value"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "2")

    def test_rectangle_x_negative(self):
        """test the validation of x value"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -1)

    # Y
    def test_rectangle_y(self):
        """test rectangle y """
        self.assertEqual(self.r.y, 0)

    def test_rectangle_y_setter(self):
        """test rectangle y setter"""
        self.r.y = 1
        self.assertEqual(self.r.y, 1)

    def test_rectangle_y_default(self):
        """test default values"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

    def test_rectangle_y_str(self):
        """test the validation of y value"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 2, "2")

    def test_rectangle_y_negative(self):
        """test the validation of y value"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 1, -2)

    # Area
    def test_rectangle_area(self):
        area = self.r.area()
        self.assertEqual(area, 20)

    def test_rectangle_area_multiple(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 5)
        r3 = Rectangle(7, 4)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 25)
        self.assertEqual(r3.area(), 28)

    def test_rectangle_area_large(self):
        r = Rectangle(1000, 2000)
        self.assertEqual(r.area(), 2000000)

    # display
    def test_rectangle_dispaly(self):
        """test rectangle display without x and y"""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            r.display()

        self.assertEqual(buffer.getvalue(), expected_output)

    def test_rectangle_dispaly_with_x_y(self):
        """test rectangle display with x and y"""
        r = Rectangle(3, 2, 2, 2)
        expected_output = "\n\n  ###\n  ###\n"
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            r.display()

        self.assertEqual(buffer.getvalue(), expected_output)

    # __str__
    def test_str(self):
        """test __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        excpected = "[Rectangle] (12) 2/1 - 4/6"

        self.assertEqual(r1.__str__(), excpected)

    # update
    def test_rectangle_update_1_args(self):
        """test update function. 1 argument"""
        self.r.update(89)
        self.assertEqual(self.r.id, 89)

    def test_rectangle_update_2_args(self):
        """test update function 2 arguments"""
        self.r.update(89, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)

    def test_rectangle_update_3_args(self):
        """test update function 3 arguments"""
        self.r.update(89, 2, 3)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)

    def test_rectangle_update_4_args(self):
        """test update function 4 arguments"""
        self.r.update(89, 2, 3, 4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 4)

    def test_rectangle_update_5_args(self):
        """test update function 5 arguments"""
        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 4)
        self.assertEqual(self.r.y, 5)

    def test_rectangle_update_1_kwargs(self):
        """test update using kwargs 1 kwarg"""
        self.r.update(id=1)
        self.assertEqual(self.r.id, 1)

    def test_rectangle_update_2_kwargs(self):
        """test update using kwargs 2 kwarg"""
        self.r.update(id=1, width=1)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 1)

    def test_rectangle_update_3_kwargs(self):
        """test update using kwargs 3 kwarg"""
        self.r.update(id=1, width=1, height=1)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 1)

    def test_rectangle_update_4_kwargs(self):
        """test update using kwargs 4 kwarg"""
        self.r.update(id=1, width=1, height=1, x=1)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 1)
        self.assertEqual(self.r.x, 1)

    def test_rectangle_update_5_kwargs(self):
        """test update using kwargs 5 kwarg"""
        self.r.update(id=1, width=1, height=1, x=1, y=1)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 1)

    def test_rectangle_update_kwargs_no_order(self):
        """test update using kwargs no need to be ordered"""
        self.r.update(height=1, id=1, width=1, x=1, y=1)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 1)

    # to_dict
    def test_rectangle_to_dict(self):
        excepted = {'id': 12, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        dictionary = self.r.to_dictionary()
        self.assertEqual(dictionary, excepted)


if __name__ == "__main__":
    unittest.main()
