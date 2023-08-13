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


class TestHBNBCommand_help_quit(unittest.TestCase):
    '''Unittest to test the console'''

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_enter(self):
        message = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand.onecmd("help quit"))
            self.assertEqual(message, output.getvalue().strip())

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
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
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(errMessage, output.getvalue().strip())

    def test_create_exist_class(self):
        errMessage = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand.onecmd("create MyModal"))
            self.assertEqual(errMessage, output.getvalue().strip())

    def test_create_unknown_methon(self):
        errMessage = "** unKnown method **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand.onecmd("BaseModel.create()"))
            self.assertEqual(errMessage, output.getvalue().strip())

    def test_create_instance(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertEqual(HBNBCommand.onecmd("create BaseModel"))
            self.assertIsInstance(output.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(output.getvalue().strip(),storage.all().keys()))
