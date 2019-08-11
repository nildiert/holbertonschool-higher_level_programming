#!/usr/bin/python3
# Script that takes in an argument and displays all values
import MySQLdb
from sys import argv

if __name__ == '__main__':

    try:
        db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

        cursor = db.cursor()
        query = "SELECT id, name \
        FROM states \
        WHERE name='{}';".format(argv[4])
        cursor.execute(query)
        for result in cursor:
            print(result)
    except Exception:
        pass
