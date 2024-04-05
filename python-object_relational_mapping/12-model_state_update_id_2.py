#!/usr/bin/python3

"""
changes the name of a State object
from the database hbtn_0e_6_usa
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

    instance = session.query(State).filter(State.id == "2").first()
    instance.name = "New Mexico"
    session.commit()
    session.close()
