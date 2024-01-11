#!/usr/bin/python3
"""
A script should take 3 arguments:
mysql username, mysql password and database name
format keyword is used to create the SQL query
with the user input as the 4th argument passed
"""

from sys import argv
import MySQLdb
username = argv[1];
password = argv[2];
databaseName = argv[3];
userInput = argv[4];

if (__name__ == "__main__"):
    connection = MySQLdb.connect(user=username,
                                 passwd=password,
                                 db=databaseName)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states\
            WHERE BINARY name = '{}';".
            format(userInput))

    for row in cursor.fetchall():
        print(row)

