#!/usr/bin/python3
"""Test file for Base class"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Tests for Base class
    Note: Base allows id to be any data type
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up created files"""
        for file in ("Rectangle.json", "Square.json"):
            if os.path.exists(file):
                os.remove(file)

    # id
    def test_without_id(self):
        """test automatic id assignment"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        """test id with int"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_with_float(self):
        """test id with float"""
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_with_str(self):
        """test id with string"""
        b = Base("abc")
        self.assertEqual(b.id, "abc")

    def test_with_list(self):
        """test id with list"""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_with_dict(self):
        """test id with dict"""
        b = Base({"a": 1})
        self.assertEqual(b.id, {"a": 1})

    def test_with_negative(self):
        """test id with negative number"""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_with_tuple(self):
        """test id with tuple"""
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))

    # json
    def test_to_json_dict(self):
        """test converting to json dictinary"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        excepted = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'

        self.assertEqual(json_dictionary, excepted)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)

        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["width"], 10)
        self.assertEqual(data[0]["height"], 7)
        self.assertEqual(data[1]["id"], 2)

    def test_save_to_file_square(self):
        s1 = Square(5, 1, 2, 9)
        Square.save_to_file([s1])

        with open("Square.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data[0]["size"], 5)
        self.assertEqual(data[0]["x"], 1)
        self.assertEqual(data[0]["y"], 2)

    def test_create_rectangle(self):
        r = Rectangle.create(id=10, width=4, height=5, x=1, y=2)

        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
    
    def test_create_rectangle(self):
        r = Rectangle.create(id=10, width=4, height=5, x=1, y=2)

        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_load_from_file_no_file(self):
        filename = "Rectangle.json"

        if os.path.exists(filename):
            os.remove(filename)

        objs = Rectangle.load_from_file()
        self.assertEqual(objs, [])
    
    def test_load_from_file_rectangle(self):
        r1 = Rectangle(3, 4, 1, 2, 99)
        r2 = Rectangle(5, 6, 0, 0, 100)

        Rectangle.save_to_file([r1, r2])

        objs = Rectangle.load_from_file()

        self.assertEqual(len(objs), 2)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertIsInstance(objs[1], Rectangle)

        self.assertEqual(objs[0].id, 99)
        self.assertEqual(objs[1].width, 5)
