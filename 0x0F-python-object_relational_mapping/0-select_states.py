#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
