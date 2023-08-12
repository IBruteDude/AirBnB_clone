#!/usr/bin/python3
''' Unit testing module for the Review class '''
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    ''' A unittest class for testing the Review class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.R1 = Review()

    def test_place_id_attr(self):
        ''' Test the place_id attribute is set correctly '''
        self.assertTrue(hasattr(self.R1, 'place_id'))
        self.assertIsInstance(self.R1.place_id, str)

    def test_user_id_attr(self):
        ''' Test the user_id attribute is set correctly '''
        self.assertTrue(hasattr(self.R1, 'user_id'))
        self.assertIsInstance(self.R1.user_id, str)

    def test_text_attr(self):
        ''' Test the text attribute is set correctly '''
        self.assertTrue(hasattr(self.R1, 'text'))
        self.assertIsInstance(self.R1.text, str)
