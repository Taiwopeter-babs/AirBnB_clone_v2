#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
import shlex


class Place(BaseModel, Base):
    """
    Place class mapped to places table on the database

    Args:
            city_id(str): cities.id
            user_id(str): users.id
            name(str): name of Airbnb residence
            description(str): description of Airbnb residence
            number_rooms(int): Number of rooms in Airbnb residence
            number_bathrooms(int): Number of bathrooms in Airbnb residence
            max_guest(int): Maximum guests residence can accomodate
            price_by_night(int): Price of residence per night
            latitude(float): latitudinal location of residence
            longitude(float) longitudinal location of residence
            amenity_ids(list): amenities.id
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship(
        "Review", cascade="all, delete, delete-orphan", backref="place"
    )

    @property
    def reviews(self) -> list:
        """Returns a list of Review instances"""
        from models import storage

        all_objs = storage.all()
        reviews_list = []
        for key, value in all_objs.key():
            review = key.replace(".", " ")
            review = shlex.split(review)
            if review[0] == "Review":
                if all_objs[key].__dict__["place_id"] == self.id:
                    reviews_list.append({key, value})
        return reviews_list
