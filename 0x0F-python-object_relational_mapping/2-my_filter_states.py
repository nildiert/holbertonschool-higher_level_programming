#!/usr/bin/python3
# Script that takes in an argument and displays all values
import MySQLdb
from sys import argv

if len(argv) is 5:
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT id, name\
        FROM states\
        WHERE name='{}';".format(argv[4])
    )
    for result in cursor:
        print("{}".format(result))
