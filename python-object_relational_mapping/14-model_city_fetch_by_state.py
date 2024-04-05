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

    for __city__, __state__ in instance.all():
        print("{}: ({:d}) {}".format(__state__.name, __city__.id, __city__.name))
