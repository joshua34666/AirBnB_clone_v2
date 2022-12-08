#!/usr/bin/python3
""" State Module for HBNB project """
from models import HBNB_TYPE_STORAGE
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    __tablename__ = 'Amenity'
    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)
