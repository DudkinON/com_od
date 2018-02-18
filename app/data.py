#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Certificates, Works, User, Skills, Experience, session


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


def get_user_by_id(uid):
    """
    Return user by user id
    :param uid:
    :return return:
    """
    return session.query(User).filter_by(id=uid).one()


def get_skills():
    """
    Return list of skills
    :return:
    """
    return session.query(Skills).all()


def get_experience():
    """
    Return list of experience work places
    :return:
    """
    return session.query(Experience).all()
