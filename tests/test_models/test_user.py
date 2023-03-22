#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test user class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test first name"""
        new = self.value(first_name="Taiwo")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last name"""
        new = self.value(last_name="Babs")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email"""
        new = self.value(email="babs@gmail.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password"""
        new = self.value(password="mypassword")
        self.assertEqual(type(new.password), str)
