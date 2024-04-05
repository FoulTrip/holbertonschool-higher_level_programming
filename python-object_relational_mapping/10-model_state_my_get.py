#!/usr/bin/python3

"""
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance == None:
        print("Not found")
    else:
        print("{}".format(instance.id))
