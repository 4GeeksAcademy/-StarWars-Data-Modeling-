import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    rotation_period = Column(Integer)
    terrain = Column(String(60))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    mass = Column(Integer)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    homeworld_relationship = relationship(Planets)


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    starship_clas = Column(String(100))
    pilots = Column(String(50), ForeignKey('character.id'))
    pilots_relationship = relationship(Character)


class Favorite_Planets(Base):
    __tablename__ = 'favplanets'
    id = Column(Integer, primary_key=True)
    planets = Column(String(60), ForeignKey('planets.id'))
    planets_relationship = relationship(Planets)


class Favorite_Character(Base):
    __tablename__ = 'favcharacter'
    id = Column(Integer, primary_key=True)
    character = Column(String(60), ForeignKey('character.id'))
    character_relationship = relationship(Character)


class Favorite_Starships(Base):
    __tablename__ = 'favstarships'
    id = Column(Integer, primary_key=True)
    Starships = Column(String(60), ForeignKey('starships.id'))
    Starships_relationship = relationship(Starships)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
