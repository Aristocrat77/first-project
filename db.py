import sqlite3 as sq
def db_start():

    db = sq.connect('database.db')
    cursor