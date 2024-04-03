#!/usr/bin/python3
""" Script with python for connect with MySQL """
import MySQLdb
import sys

if __name__ == "__main__":
    """
    lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
