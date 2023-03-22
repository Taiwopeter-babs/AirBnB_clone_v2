#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User


class test_Place(test_basemodel):
    """Test for place class"""

    def __init__(self, *args, **kwargs):
        """Constructor for tests"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test that place has a valid city_id"""
        city = City(name="Lagos")
        new = self.value(name="Lovely_place", city_id=city.id)
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test user_id"""
        user = User()
        new = self.value(name="Lovely_place", user_id=user.id)
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test name attribute"""
        new = self.value(name="Lovely_place")
        self.assertIsNotNone(new.name)
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test description"""
        new = self.value()
        self.assertIs(new.description, None)

    def test_number_rooms(self):
        """test number of rooms"""
        new = self.value(number_rooms=3)
        self.assertEqual(type(new.number_rooms), int)
        self.assertEqual(new.number_rooms, 3)

    def test_number_bathrooms(self):
        """test bathrooms"""
        new = self.value(number_bathrooms=3)
        self.assertEqual(type(new.number_bathrooms), int)
        self.assertEqual(new.number_bathrooms, 3)

    def test_max_guest(self):
        """test number of guests"""
        new = self.value(max_guest=6)
        self.assertEqual(new.max_guest, 6)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test price"""
        new = self.value(price_by_night=190)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude"""
        new = self.value(latitude=33.453)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test longitude"""
        new = self.value(longitude=-122.431297)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """test amenity list"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
