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
        "SELECT cities.name\
        FROM cities LEFT JOIN states ON cities.state_id = states.id\
        WHERE states.name = '%s' ORDER BY cities.id;" % argv[4]
    )
#    print('Total Row(s):', cursor.rowcount)
    rows = cursor.fetchall()
    new_list = []
    for row in rows:
        new_list.append(row[0])
#        new_list.append(row)
    print(", ".join(new_list))
