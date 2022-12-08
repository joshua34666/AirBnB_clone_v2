#!/usr/bin/python3
""" City Module for HBNB project """
from models import HBNB_TYPE_STORAGE
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    if HBNB_TYPE_STORAGE == 'db':
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        name = Column(String(128),
                      nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)
