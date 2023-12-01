#!/usr/bin/python3
"""
print all City objects
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    query = session.query(City, State).join(State)

    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    session.commit()
    session.close()
