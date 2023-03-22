#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """Test city class"""

    def __init__(self, *args, **kwargs):
        """Constructor for test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test that state_id is valid"""
        state = State(name="Lagos")
        new = self.value(name="Ikeja", state_id=state.id)
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test that city name is valid"""
        new = self.value(name="Lagos")
        self.assertIsNotNone(new.name)
        self.assertEqual(type(new.name), str)
