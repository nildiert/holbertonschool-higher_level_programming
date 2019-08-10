#!/usr/bin/python3
# Script that lists all states that starging with N

import MySQLdb
import sys

if __name__ == '__main__':

    try:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        cursor = db.cursor()

        cursor.execute("SELECT id, name\
        FROM states WHERE name LIKE 'N%'\
        ORDER BY states.id ASC;")
        for result in cursor:
            print("{}".format(result))
    except Exception:
        pass
