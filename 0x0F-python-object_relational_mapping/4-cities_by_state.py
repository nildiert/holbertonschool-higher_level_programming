#!/usr/bin/python3
# Script that takes in an argument and displays all values
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

    cursor.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities LEFT JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id;"
    )
#    print('Total Row(s):', cursor.rowcount)
    rows = cursor.fetchall()
    for row in rows:
        print("{}".format(row))
