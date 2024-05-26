#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
database = os.getenv('HBNB_MYSQL_DB')

engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}')
Session = scoped_session(sessionmaker(bind=engine))

def storage():
    """Returns a scoped session"""
    return Session()

def close():
    """Closes the session"""
    Session.remove()
