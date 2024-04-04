#!/usr/bin/python3
""" Script with python for connect with MySQL """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    lists all cities from the database hbtn_0e_4_usa
    """

    host = "localhost"
    port = 3306
    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        """
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
    """,
        {"state_name": argv[4]},
    )
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
