#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """Getter attribute, returns a list"""
        from models import storage
        #my_list = []
        #extracted_cities = storage.all(City).values()
        #for city in extracted_cities:
        #    if self.id == city.state_id:
        #        my_list.append(city)
        #print("list of cities:", my_list)
        #return my_list

        all_objects = models.storage.all()
        filtered_cities = []

        for key, val in all_objects.items():
            if "City" in key:
                filtered_cities.append(key[val])
        print("got cities")
        return [city for city in filtered_cities if city.state_id == self.id]
