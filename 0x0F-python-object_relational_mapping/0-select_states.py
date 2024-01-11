#!/usr/bin/python3

#!/usr/bin/python3
"""
A script should take 3 arguments:
mysql username, mysql password and database name
"""

from sys import argv
import MySQLdb
username = argv[1];
password = argv[2];
databaseName = argv[3];

if (__name__ == "__main__"):
    connection = MySQLdb.connect(user=username,
                                 passwd=password,
                                 db=databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states;")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()
