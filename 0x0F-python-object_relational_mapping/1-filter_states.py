#!/usr/bin/python3
''' Script that lists all states that starging with N '''

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
        query = "SELECT id, name FROM states \
        WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for result in rows:
            print(result)
        cursor.close()
    except Exception:
        pass
