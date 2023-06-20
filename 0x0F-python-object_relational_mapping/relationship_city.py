#!/usr/bin/python3
"""
    Script that defines a city class
    to work with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
        City class
        Attributes:
            __tablename__ (str): The table name of the class
            id (int): The State id of the class
            name (str): The State name of the class
            cities (:obj:`City`): The Cities belongs to State
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
