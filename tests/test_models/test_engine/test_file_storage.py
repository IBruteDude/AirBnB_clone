#!/usr/bin/python3
''' Unit testing module for the FileStorage class '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    ''' A unittest class for testing the FileStorage class '''
    def setUp(self):
        ''' Set up all the class test units '''
        self.FS = FileStorage()
        self.BM = BaseModel()

    def test_file_storage_all_new(self):
        self.FS.new(self.BM)
        self.assertIn(f'BaseModel.{self.BM.id}', self.FS.all().keys())
        self.assertIn(str(self.BM),
                      [str(obj) for obj in self.FS.all().values()])

    def test_file_storage_save_reload(self):
        self.FS.new(self.BM)
        self.FS.save()
        self.FS.reload()
        self.assertIn(f'BaseModel.{self.BM.id}', self.FS.all().keys())
        self.assertIn(str(self.BM),
                      [str(obj) for obj in self.FS.all().values()])
