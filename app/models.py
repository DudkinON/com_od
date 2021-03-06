#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from passlib.apps import custom_app_context as pwd_context
from resource import get_unique_str
from settings import db

Base = declarative_base()
secret_key = get_unique_str(32)

# prepare engine
egg = 'postgresql://%s:%s@%s/%s' % (db['user'],
                                    db['password'],
                                    db['host'],
                                    db['database'])


# create session
engine = create_engine(egg)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Certificates(Base):

    __tablename__ = 'certificates'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(250))
    url = Column(String(250))
    image = Column(String(250))
    is_active = Column(Boolean, default=True)

    @property
    def serialize(self):
        """
        Return certificates serialize data

        :return dict:
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'images': self.image,
            'url': self.url,
            'is_active': self.is_active
        }


class Works(Base):

    __tablename__ = 'works'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(250))
    url = Column(String(250))
    image = Column(String(250))
    is_active = Column(Boolean, default=True)

    @property
    def serialize(self):
        """
        Return certificates serialize data

        :return dict:
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'images': self.image,
            'url': self.url,
            'is_active': self.is_active
        }


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(60))
    last_name = Column(String(60))
    email = Column(String(45))
    hash = Column(String(250))
    status = Column(Boolean, default=True)
    role = Column(String(10), default='user')

    def hash_password(self, password):
        """
        Get string and hashing it
        :param password: (str)
        :return void:
        """
        self.hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        """
        Password verification
        :param password:
        :return bool:
        """
        return pwd_context.verify(password, self.hash)

    def generate_auth_token(self, expiration=3600):
        """
        Generate authentication token
        :param expiration:
        :return string: (token)
        """
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'uid': self.id})

    @staticmethod
    def verify_auth_token(token):
        """
        Try to load token, success return user id false return None
        :param token:
        :return mix:
        """
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            # Valid Token, but expired
            return None
        except BadSignature:
            # Invalid Token
            return None
        uid = data['uid']
        return uid

    @property
    def serialize(self):
        """
        Return user info
        :return dict:
        """
        return {
            'uid': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'status': self.status,
            'role': self.role
        }


class SkillsCategory(Base):

    __tablename__ = 'skills_category'
    id = Column(Integer, primary_key=True)
    title = Column(String(60))

    def get_skills(self):
        """
        Return serialize skill
        :return:
        """
        return [item.serialize for item in session.query(Skills).filter_by(
            category=self.id).order_by(Skills.percent.desc()).all()]

    @property
    def serialize(self):
        """
        Return skills categories serialize data

        :return dict:
        """
        return {
            'id': self.id,
            'title': self.title,
            'skills': self.get_skills()
        }


class Skills(Base):

    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    percent = Column(Integer)
    category = Column(Integer, ForeignKey("skills_category.id"))

    @property
    def serialize(self):
        """
        Return skills serialize data

        :return dict:
        """
        return {
            'id': self.id,
            'title': self.title,
            'percent': self.percent
        }


class Experience(Base):

    __tablename__ = 'experience'
    id = Column(Integer, primary_key=True)
    title = Column(String(60))
    description = Column(String(250))
    start = Column(Integer)
    end = Column(Integer)

    @property
    def serialize(self):
        """
        Return experience serialize data

        :return dict:
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start': self.start,
            'end': self.end
        }


class Info(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    slogan = Column(String(250))
    title = Column(String(250))
    description = Column(String(250))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'slogan': self.slogan,
            'title': self.title,
            'description': self.description
        }


class Education(Base):

    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    name = Column(String(250))
    description = Column(String(250))
    specialisation = Column(String(250))
    url = Column(String(250))
    start = Column(String(250))
    end = Column(String(250))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'title': self.title,
            'description': self.description,
            'specialisation': self.specialisation,
            'url': self.url,
            'start': self.start,
            'end': self.end
        }


class Social(Base):

    __tablename__ = 'social'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    url = Column(String(250))
    style = Column(String(50))
    is_active = Column(Boolean)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'style': self.style
        }


# create engine
engine = create_engine(egg)
Base.metadata.create_all(engine)
