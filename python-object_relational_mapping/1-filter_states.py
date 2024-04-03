#!/usr/bin/python3
""" Script with python for connect with MySQL """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
    """

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password, db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
    cur.close()
    db.close()
