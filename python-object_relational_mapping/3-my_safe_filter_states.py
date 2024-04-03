#!/usr/bin/python3
""" Script with python for connect with MySQL """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name
    matches the argument.
    """

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password, db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        if state[1] == state_name_searched:
            print("({}, \'{}\')".format(state[0], state[1]))
    cur.close()
    db.close()
