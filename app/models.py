from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
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


class Works(Base):
    __tablename__ = 'works'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(250))
    url = Column(String(250))
    image = Column(String(250))
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(engine)
