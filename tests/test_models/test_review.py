#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.place import Place
from models.user import User


class test_review(test_basemodel):
    """Test review class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        place = Place()
        new = self.value(place_id=place.id)
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test user_id"""
        user = User()
        new = self.value(user_id=user.id)
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test text"""
        new = self.value(text="Lovely place. 5 stars")
        self.assertIsNotNone(new.text)
        self.assertEqual(type(new.text), str)
