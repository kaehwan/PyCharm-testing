#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""
The python db api is a consolidated interface for a number of database systems
Every db engine has its own interface, requirements, and paradigms, so no
single interface will ever serve them equally
"""

import sqlite3

def main():
    print('connect')
    # first step: connect to the database and return a database handle
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()
