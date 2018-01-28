from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
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

        return pwd_context.verify(password, self.hash)


# create engine
engine = create_engine(egg)
Base.metadata.create_all(engine)
