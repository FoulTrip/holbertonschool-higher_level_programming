#!/usr/bin/python3

"""
prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(City, State).join(State)

    for _city, _state in instance.all():
        print("{}: ({:d}) {}".format(
            _state.name,
            _city.id,
            _city.name))
