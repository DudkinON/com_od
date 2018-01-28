from models import Certificates, Works, Base, egg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# create session
engine = create_engine(egg)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# database actions
def get_certificates():
    return session.query(Certificates).filter_by(is_active=True).all()
