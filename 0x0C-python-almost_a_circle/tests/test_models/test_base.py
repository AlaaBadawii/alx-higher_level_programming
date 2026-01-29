#!/usr/bin/python3
"""Test file for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Tests for Base class
    Note: Base allows id to be any data type
    """

    def setUp(self):
        Base._Base__nb_objects = 0

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
