#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity"""

    def __init__(self, *args, **kwargs):
        """Constrctor for test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test that name is valid"""
        new = self.value(name="wifi")
        self.assertIsNotNone(new.name)
        self.assertEqual(type(new.name), str)
