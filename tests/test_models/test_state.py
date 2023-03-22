#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test state class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test state name"""
        new = self.value(name="Ondo")
        self.assertIsNotNone(new.name)
        self.assertIsNotNone(new.id)
        self.assertEqual(type(new.name), str)
        self.assertEqual(type(new.id), str)
