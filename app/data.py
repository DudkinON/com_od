#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Certificates, Works, Base, User, egg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# create session
engine = create_engine(egg)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# database actions
def get_certificates():
    """
    Return list of certificates
    :return object:
    """
    return session.query(Certificates).filter_by(is_active=True).all()


def get_works():
    """
    Return list of works
    :return object:
    """
    return session.query(Works).filter_by(is_active=True).all()


def add_certificate(certificate):
    """
    Add a new certificate in database
    :param certificate: (dict)
    :return object:
    """
    new_certificate = Certificates(
        title=certificate['title'],
        description=certificate['description'],
        url=certificate['url'],
        image=certificate['image']
    )
    session.add(new_certificate)
    session.commit()
    return new_certificate
