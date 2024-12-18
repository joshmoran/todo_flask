#!/bin/usr/python
# importing Flask and other modules
import sqlite3
import sys
from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for

# Flask constructor
app = Flask(__name__)
 
def db_connection():
    conn = sqlite3.connect('schema.db')
    conn.row_factory = sqlite3.Row
    return conn
  
@app.route('/')
@app.route('/<verbose>')
def index( verbose = '' ):
  conn = db_connection()
  errors = []
  if verbose == '':
    errors = None
  elif verbose == 'updatetask':
    errors.append( ['updatetask', ''] )
  elif verbose == 'addedtask':
    errors.append( ['addtask', ''] )
  elif verbose == 'deletetask':
    errors.append( ['deletetask', ''] )
  elif verbose != 'update' or verbose != 'delete' or verbose != 'submitchange':
    errors = [] 
    removeQuestion = verbose[1:-1]
    initialSplit = removeQuestion.split('&')
    if len(initialSplit) > 0:
      for item in initialSplit:
        item = item.split('=')
        try:
          errors.append( [ item[0], item[1]])
        except IndexError:
          print("Out of range")
    else:
      errors = None

  tasks = conn.execute("select * from pending_tasks").fetchall()
  complete = conn.execute("select * from completed_tasks").fetchall()

  return render_template('index.html', tasks=tasks, complete=complete, errors=errors)

@app.route('/delete', methods=["POST"])
def delete( ):
  conn = db_connection()

  delete_id = request.form.get('task_id')
  complete = request.form.get('complete')

  # return complete
  sql = "delete from "

  if complete == 'True':
    sql += "completed_tasks"
  else:
    sql += "pending_tasks"
  sql += " where id = " + delete_id

  try: 
    conn.execute(str(sql))
    conn.commit()
  except Exception: 
    return "There has been an error"
  finally:
    conn.close()
   
    return redirect(url_for('index', verbose='deletetask'))
  
@app.route('/update')
def update( ):
  task_id = request.args.get('task_id')
  
  complete = request.args.get('complete')

  conn = db_connection()

  task = conn.execute("select * from pending_tasks where id =?", (task_id,)).fetchall()
  conn.close()

  return render_template('update.html', task=task, complete=complete)


@app.route('/submitchange', methods=['POST'])
def make_change():
  complete = request.form.get('complete')
  task_id = request.form.get('task_id')

  description = request.form.get('name')
  priority = request.form.get('priority')
  due_time = request.form.get('duetime')
  due_date = request.form.get('duefor')

  conn = db_connection()

  for_index = '?'

  errors = False

  if description == '':
    if checkAnd(for_index):
      for_index += '&'
    for_index += "description=empty"
    errors = True

  if due_date == '':
    if checkAnd(for_index):
      for_index += '&'
    for_index += "due_date=empty"
    errors = True
  else:
    splitDate = due_date.split('-')
    dueDate = datetime( int(splitDate[0]), int(splitDate[1]), int(splitDate[2]) )

    earliest = datetime(2023, 1, 1)
    latest = datetime(2100, 12, 30)

    if due_date != '' and dueDate < earliest or dueDate > latest: 
      if checkAnd(for_index):
        for_index += '&'
      for_index += "due_date=incorrect"
  if due_time == '':
    if checkAnd(for_index):
      for_index += '&'
    for_index += "due_time=empty"
    errors = True

  if errors:
    return redirect( url_for('index', verbose=for_index) )
  else:
    sql = "UPDATE "

    if complete == 'False':
      sql += "pending_tasks"
    else:
      sql += "completed_tasks"
    sql += " SET name = '" + description + "', priority = '" + priority + "', due_time = '" + due_time + "', due_date = '" + due_date+ "' where id = " + task_id

    conn.execute(sql)
    conn.commit()
    conn.close()
    return redirect(url_for('index', verbose='updatetask'))

@app.route('/complete', methods=['POST'])
def complete( ):
  error = False

  task_id = request.form.get('task_id')
  complete = request.form.get('complete')
  
  task_sql = "insert into "
  current_sql = "select name, priority, due_time, due_date from "

  conn = db_connection()
  
  if complete == 'True':
    current_sql += "completed_tasks"
    task_sql += "pending_tasks"
  elif complete == 'False':
    current_sql += "pending_tasks"
    task_sql += "completed_tasks"
  current_sql += " where id = " + task_id
  task_sql += " ( name, priority, due_time, due_date ) values ( "

  task_row = conn.execute(current_sql).fetchone()

  for row in task_row:
    task_sql += "'" + str(row) + "',"
  task_sql = task_sql[:-1]
  task_sql += ")"

  conn.execute( str(task_sql) )
  if complete == 'True':
    conn.execute(f"DELETE FROM completed_tasks WHERE id = {int(task_id)}")
    
  conn.execute(f"DELETE FROM pending_tasks WHERE id = {int(task_id)}")
  conn.commit()
  conn.close()
  return redirect( url_for('index'))


@app.route('/add', methods =["POST"])
# # @app.ri
def add():
  conn = db_connection()
  errors = False
  # getting input with name = fname in HTML form
  description = request.form.get("description")
  # getting input with name = lname in HTML form 
  priority = request.form.get("priority") 
  due_date = request.form.get("duefor")
  due_time = request.form.get("duetime")

  for_index = '?'

  errors = False

  if description == '':
    if checkAnd(for_index):
      for_index += '&'
    for_index += "description=empty"
    errors = True
  if due_date == '':
    if checkAnd(for_index):
      for_index += '&'
    for_index += "due_date=empty"
    errors = True
  else:
    splitDate = due_date.split('-')
    dueDate = datetime( int(splitDate[0]), int(splitDate[1]), int(splitDate[2]) )

    earliest = datetime(2023, 1, 1)
    latest = datetime(2100, 12, 30)

    if due_date != '' and dueDate < earliest or dueDate > latest: 
      if checkAnd(for_index):
        for_index += '&'
      for_index += "due_date=incorrect"
  if due_time == '':
    if checkAnd(for_index):
      for_index += '&'
    for_index += "due_time=empty"
    errors = True
  

  if errors:
    return redirect( url_for('index', verbose=for_index) )
  else: 
    sql = "INSERT INTO pending_tasks ( name, priority, due_time, due_date ) values ( '" + description + "', '" + priority + "', '" + due_time + "', '" + due_date + "')"
    conn.execute(sql)
    conn.commit()
    conn.close()
    return redirect( url_for('index', verbose='addedtask') )

def checkStart ( string ):
  if string[0] != '?':
    return True

def checkAnd( string ):
  if string == '?':
    return False
  elif string[-1] != '&':
    return True
# @app.route('/<int:list>')
# def view_list(list):
#     list_id = request.args.get('list')

if __name__=='__main__':
   app.run(
     debug=True,
     port=5000,
     host='192.168.0.220'  # Allows connections from outside the container.
   )
