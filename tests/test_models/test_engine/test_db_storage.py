#!/usr/bin/python3
""" Module for testing database storage """
from models import storage
import unittest
from models.base_model import BaseModel, Base
from models.state import State
from models.engine.db_storage import DBStorage
import pycodestyle
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Tests for DBStorage")
class DBStorage(unittest.TestCase):
    """ Test for DBStorage class """
    max_diff = None

    def test_documentation(self):
        """ Tests for documentation """
        self.assertTrue(len(DBStorage.__doc__) >= 20, "Short or no doc")
        self.assertTrue(len(DBStorage.all.__doc__) >= 20, "Short doc")
        self.assertTrue(len(DBStorage.new.__doc__) >= 20, "Short doc")
        self.assertTrue(len(DBStorage.save.__doc__) >= 20, "Short doc")
        self.assertTrue(len(DBStorage.delete.__doc__) >= 20, "Short doc")
        self.assertTrue(len(DBStorage.reload.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ Tests for pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        p = 'tests/test_models/test_engine/test_db_storage.py'
        result = pystyle.check_files(['models/engine/db_storage.py', p])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state(self):
        """ Tests for creating state """
        state = State(name="California")
        if state.id in storage.all():
            self,assertTrue(state.name, "California")
