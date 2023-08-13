#!/usr/bin/python3
''' Unit testing module for the State class '''
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    ''' A unittest class for testing the State class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.S1 = State()

    def test_name_attr(self):
        ''' Test the name attribute is set correctly '''
        self.assertTrue(hasattr(self.S1, 'name'))
        self.assertIsInstance(self.S1.name, str)
