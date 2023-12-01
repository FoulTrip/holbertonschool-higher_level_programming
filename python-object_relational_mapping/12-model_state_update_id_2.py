#!/usr/bin/python3

"""
change the name of a State
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object on the database
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

    ari_state = session.query(State).filter(State.id == "2").first()
    ari_state.name = "New Mexico"
    session.commit()
    session.close()
