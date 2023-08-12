#!/usr/bin/python3
''' Unit testing module for the Place class '''
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    ''' A unittest class for testing the Place class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.P1 = Place()

    def test_name_attr(self):
        ''' Test the name attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'name'))
        self.assertIsInstance(self.P1.name, str)

    def test_city_id_attr(self):
        ''' Test the city_id attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'city_id'))
        self.assertIsInstance(self.P1.city_id, str)

    def test_user_id_attr(self):
        ''' Test the user_id attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'user_id'))
        self.assertIsInstance(self.P1.user_id, str)

    def test_description_attr(self):
        ''' Test the description attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'description'))
        self.assertIsInstance(self.P1.description, str)

    def test_number_rooms_attr(self):
        ''' Test the number_rooms attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'number_rooms'))
        self.assertIsInstance(self.P1.number_rooms, int)

    def test_number_bathrooms_attr(self):
        ''' Test the number_bathrooms attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'number_bathrooms'))
        self.assertIsInstance(self.P1.number_bathrooms, int)

    def test_max_guest_attr(self):
        ''' Test the max_guest attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'max_guest'))
        self.assertIsInstance(self.P1.max_guest, int)

    def test_price_by_night_attr(self):
        ''' Test the price_by_night attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'price_by_night'))
        self.assertIsInstance(self.P1.price_by_night, int)

    def test_latitude_attr(self):
        ''' Test the latitude attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'latitude'))
        self.assertIsInstance(self.P1.latitude, float)

    def test_longitude_attr(self):
        ''' Test the longitude attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'longitude'))
        self.assertIsInstance(self.P1.longitude, float)

    def test_amenity_ids_attr(self):
        ''' Test the amenity_ids attribute is set correctly '''
        self.assertTrue(hasattr(self.P1, 'amenity_ids'))
        self.assertIsInstance(self.P1.amenity_ids, list)
