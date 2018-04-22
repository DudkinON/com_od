#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Education, Social
from models import Certificates, Works, User, SkillsCategory, Experience, Info
from models import session


# database actions
def get_certificates():
    """
    Return list of certificates order by id desc
    :return object:
    """
    return session.query(Certificates).filter_by(
        is_active=True).order_by(Certificates.id.desc()).all()


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
    return session.query(SkillsCategory).order_by('id').all()


def get_experience():
    """
    Return list of experience work places
    :return:
    """
    return session.query(Experience).all()


def get_info():
    """
    Return user info
    :return:
    """
    return session.query(Info).all()


def get_education():
    """
    Return education info
    :return:
    """
    return session.query(Education).all()


def get_social():
    """
    Return list of contacts and social networks
    :return:
    """
    return session.query(Social).all()
