#!/usr/bin/python3
# Script that lists all states that starging with N

import MySQLdb
from sys import argv

if len(argv) is 4:
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;")
    for result in cursor:
        print("{}".format(result))
