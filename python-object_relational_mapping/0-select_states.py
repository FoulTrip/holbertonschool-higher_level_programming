#!/usr/bin/python3

import pymysql
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_username> <mysql_password> <mysql_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect MySQL server
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        db=database_name,
    )

    # cursor object
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # close connection
    cursor.close()
    db.close()
