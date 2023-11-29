import sqlite3

def createConnection():
    connection = sqlite3.connect('database.sqlite',check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("create table if not exists students(id text unique, firstName text,lastName text, course text)")
    return connection