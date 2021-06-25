import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(50), nullable=False)
    clave = Column(String(50), ForeignKey('claves.id'))

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre":self.name
        }

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre":self.name
        }

class Clave(Base):
    __tablename__ = 'claves'
    id = Column(Integer, primary_key=True)
    clave = Column(String(50), nullable=False)

    def to_dict(self):
        return {
            "clave": self.clave
        }

class Nave(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre":self.name
        }

class Pelicula(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre":self.name
        }

class Especie(Base):
    __tablename__ = 'especies'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre":self.name
        }

class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre":self.name
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')