#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """
    lists all states from the database hbtn_0e_0_usa
    """

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password, db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
