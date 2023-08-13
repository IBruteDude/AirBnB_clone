#!/usr/bin/python3
''' Unit testing module for the City class '''
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    ''' A unittest class for testing the City class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.C1 = City()

    def test_name_attr(self):
        ''' Test the name attribute is set correctly '''
        self.assertTrue(hasattr(self.C1, 'name'))
        self.assertIsInstance(self.C1.name, str)

    def test_state_id_attr(self):
        ''' Test the name attribute is set correctly '''
        self.assertTrue(hasattr(self.C1, 'state_id'))
        self.assertIsInstance(self.C1.state_id, str)
