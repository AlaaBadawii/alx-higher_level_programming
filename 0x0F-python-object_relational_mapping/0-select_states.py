#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access the DB"""
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        user=user_name,
        port=3306,
        passwd=password,
        database=db_name
    )

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id')
    table = cursor.fetchall()

    for row in table:
        print(row)
