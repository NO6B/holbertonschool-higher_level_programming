#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
