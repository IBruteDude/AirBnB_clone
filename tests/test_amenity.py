#!/usr/bin/python3
''' Unit testing module for the Amenity class '''
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    ''' A unittest class for testing the Amenity class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.A1 = Amenity()

    def test_name_attr(self):
        self.assertTrue(hasattr(self.A1, 'name'))
        self.assertIsInstance(self.A1.name, str)
