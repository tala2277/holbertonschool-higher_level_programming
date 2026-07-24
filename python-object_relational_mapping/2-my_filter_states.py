#!/usr/bin/python3
"""Display all states matching the given name."""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(
        sys.argv[4]
    )
    cur.execute(sql)

    for state in cur.fetchall():
        print(state)

    cur.close()
    conn.close()
