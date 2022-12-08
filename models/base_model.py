#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from datetime import datetime
from models import HBNB_TYPE_STORAGE


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60),
                unique=True,
                nullable=False,
                primary_key=True)
    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            if kwargs.get('created_at') and type(self.created_at) is str:
                setattr(self, 'created_at',
                        datetime.fromisoformat(self.created_at))
            else:
                setattr(self, 'created_at', datetime.now())

            if kwargs.get('updated_at') and type(self.updated_at) is str:
                setattr(self, 'updated_at',
                        datetime.fromisoformat(self.updated_at))
            else:
                setattr(self, 'updated_at', datetime.now())

            if 'id' not in kwargs.keys():
                setattr(self, 'id', str(uuid.uuid4()))


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if (dictionary.get('_sa_instance_state')): # delete '_sa_instance_state' key
            del self.__dict__['_sa_instance_state']   # if it exists
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage (models.storage)
        when called
        """
        from models import storage
        key = type(self).__name__ + '.' + str(self.id)
        storage.__objects.pop(key)
        storage.save()
