#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Test base models"""

    def __init__(self, *args, **kwargs):
        """Constructor for tests"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def setUp(self):
        """setup method"""
        pass

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def tearDown(self):
        try:
            os.remove("file.json")
        except (OSError, FileNotFoundError):
            pass

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_default(self):
        """test that the type is correct"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_kwargs(self):
        """test for creation of new instance from kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_kwargs_int(self):
        """test correct type"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_str(self):
        """test __str__ method"""
        i = self.value()
        _id = i.id
        _dict = i.__dict__
        self.assertEqual(str(i), "[{}] ({}) {}".format(self.name, _id, _dict))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_todict(self):
        """test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_kwargs_none(self):
        """test kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_kwargs_one(self):
        """test kwargs"""
        n = {"Name": "test"}
        new = self.value(**n)
        self.assertIsNot(new, n)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_id(self):
        """test that id is of instance str"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_created_at(self):
        """test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_updated_at(self):
        """test updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
