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


    # id
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


    # width
    def test_rectangle_width(self):
        """test rectangle width"""
        self.assertEqual(self.r.width, 10)
    
    def test_rectangle_width_setter(self):
        """test rectangle width setter"""
        self.r.width = 20
        self.assertEqual(self.r.width, 20)


    #height
    def test_rectangle_height(self):
        """test rectangle height"""
        self.assertEqual(self.r.height, 2)
    
    def test_rectangle_height_setter(self):
        """test rectangle height setter"""
        self.r.height = 4
        self.assertEqual(self.r.height, 4)


    # x
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


    # y    
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
