#!/usr/bin/python3
# script that lists all states from the database
import MySQLdb
from sys import argv

if len(argv) is 4:
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id;")
    for id_query in cursor:
        print("{}".format(id_query))
