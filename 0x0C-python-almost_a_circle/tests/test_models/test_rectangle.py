#!/usr/bin/python3
"""Tests for Rectangle module"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


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


if __name__ == "__main__":
    unittest.main()
