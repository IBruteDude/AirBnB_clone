#!/usr/bin/python3
''' Unit testing module for the User class '''
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    ''' A unittest class for testing the User class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.U1 = User()

    def test_email_attr(self):
        ''' Test the email attribute is set correctly '''
        self.assertTrue(hasattr(self.U1, 'email'))
        self.assertIsInstance(self.U1.email, str)

    def test_password_attr(self):
        ''' Test the password attribute is set correctly '''
        self.assertTrue(hasattr(self.U1, 'password'))
        self.assertIsInstance(self.U1.password, str)

    def test_first_name_attr(self):
        ''' Test the first_name attribute is set correctly '''
        self.assertTrue(hasattr(self.U1, 'first_name'))
        self.assertIsInstance(self.U1.first_name, str)

    def test_last_name_attr(self):
        ''' Test the last_name attribute is set correctly '''
        self.assertTrue(hasattr(self.U1, 'last_name'))
        self.assertIsInstance(self.U1.last_name, str)
