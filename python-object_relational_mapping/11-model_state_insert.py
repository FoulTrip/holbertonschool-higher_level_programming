#!/usr/bin/python3

"""
Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    nameState = State(name="Louisiana")
    session.add(nameState)
    session.commit()
    print("{}".format(nameState.id))
    session.close()
