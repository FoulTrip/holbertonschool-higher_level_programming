#!/usr/bin/python3


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access a database
    """
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    rows = c.fetchall()

    for row in rows:
        print(row)
