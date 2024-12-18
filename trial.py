# importing Flask and other modules
import sqlite3
import sys
from flask import Flask, request, render_template, redirect, url_for

# Flask constructor
app = Flask(__name__)   
 
def db_connection():
    conn = sqlite3.connect('schema.db')
    conn.row_factory = sqlite3.Row
    return conn
   
@app.route('/')
@app.route('/<int:list>')
def index( list = -1 ):
  
   list_id = request.args.get('list')
   print( list_id, file=sys.stderr )
   if list_id == 'None':
      return "Yes a number {}".format(list_id)
   else:
      return "No a number {}".format(list_id)

if __name__=='__main__':
   app.run(
      debug=True,
      host="192.168.0.220"
   )