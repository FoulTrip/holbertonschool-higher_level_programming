#!/usr/bin/python3

"""
lists all State objects
that contain the letter `a`
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database
    """

    conn = "mysql+mysqldb"
    port = "localhost:3306"
    arg1 = argv[1]
    arg2 = argv[2]
    arg3 = argv[3]

    db_uri = f"{conn}://{arg1}:{arg2}@{port}/{arg3}"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).filter(State.name.contains("a")):
        print("{0}: {1}".format(instance.id, instance.name))
