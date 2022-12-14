#!/usr/bin/python3
"""unittest"""

import unittest
import pycodestyle
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        b = BaseModel()
        self.assertEqual(type("string"), type(b.id))

    def test_name(self):
        b = BaseModel()
        b.name = "My_First_model"
        self.assertEqual(b.name, "My_First_model")

    def test_number(self):
        b = BaseModel()
        b.my_number = 89
        self.assertEqual(b.my_number, 89)


if __name__ == '__main__':
    unittest.main()
