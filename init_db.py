import sqlite3


conn = sqlite3.connect('schema.db')

with open ( 'schema.sql' ) as file:
  conn.executescript(f.read());