#!/usr/bin/python3
''' Unit testing module for the  class '''
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User


class TestHBNBCommand_help_quit(unittest.TestCase):
    '''Unittest to test the console'''

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_enter(self):
        message = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("help quit")
            self.assertEqual(message, f.getvalue().strip())

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

class TestHBNBCommand_create(unittest.TestCase):
    '''unittest for the creat command'''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_create_miss_class(self):
        errMessage = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_create_exist_class(self):
        errMessage = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create MyModal")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_create_unknown_methon(self):
        errMessage = "** unKnown method **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("BaseModel.create()")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_create_instance(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create BaseModel")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(f.getvalue().strip(),storage.all().keys()))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create Amenity")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(f.getvalue().strip(),storage.all().keys()))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create City")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(f.getvalue().strip(),storage.all().keys()))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create Place")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(f.getvalue().strip(),storage.all().keys()))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create Review")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(f.getvalue().strip(),storage.all().keys()))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create State")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(f.getvalue().strip(),storage.all().keys()))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("create User")
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(f.getvalue().strip(),storage.all().keys()))

class TestHBNBCommand_show(unittest.TestCase):
    '''Unit test for show command'''
    def test_missing_class(self):
        errMessage = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("show")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_exist_class(self):
        errMessage = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("show MyModal")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_missing_id(self):
        errMessage = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("show BaseModel")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_notFount_id(self):
        errMessage = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand.onecmd("show BaseModel 121212")
            self.assertEqual(errMessage, f.getvalue().strip())

    def test_show_instance(self):
        with patch("sys.stdout", new=StringIO()) as f:
            my_model = BaseModel()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show BaseModel {}".format(my_model.id))
            self.assertIn("BaseModel.{}".format(my_model.id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            my_model = Amenity()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show Amenity {}".format(my_model.id))
            self.assertIn("Amenity.{}".format(my_model.id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            my_model = City()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show City {}".format(my_model.id))
            self.assertIn("City.{}".format(my_model.id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            my_model = Place()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show Place {}".format(my_model.id))
            self.assertIn("Place.{}".format(my_model.id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            my_model = Review()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show Review {}".format(my_model.id))
            self.assertIn("Review.{}".format(my_model.id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            my_model = User()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show User {}".format(my_model.id))
            self.assertIn("User.{}".format(my_model.id), storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            my_model = State()
            my_model.save()
            storage.new(my_model)
            HBNBCommand.onecmd("show State {}".format(my_model.id))
            self.assertIn("State.{}".format(my_model.id), storage.all().keys())
