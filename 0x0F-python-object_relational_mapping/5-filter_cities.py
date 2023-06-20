#!/usr/bin/python3
"""
    Script that takes in the name of a state
    as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
        Accesses to the database and get the cities
        from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM cities INNER JOIN states
                        ON cities.state_id = states.id
                        ORDER BY cities.id""")
    rows = cursor.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
