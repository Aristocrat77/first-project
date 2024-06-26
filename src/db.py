import sqlite3
def connect():
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()

