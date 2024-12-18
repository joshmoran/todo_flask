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
def index( ):
   conn = db_connection()

   new = [] 

   lists = conn.execute("SELECT * FROM lists").fetchall()
   tasks = conn.execute("select * from time_refer left join tasks on time_refer.task_id = tasks.id right join lists on time_refer.list_id = lists.list_id").fetchall()
   complete = conn.execute("select * from completed_tasks").fetchall()

   for task in tasks:
      new.append((task['name'], task['name'], task['description'], task['priority'], task['time'], task['date']))
   # for list in lists:
   #    id =  list['list_id']
   #    list_name = list['name']
   #    compiled_tasks = []
   # print( tasks, file=sys.stderr )
   # conn.close()
   # #  list_name = request.args.get('list', list)
   return render_template('index.html', tasks=new, lists=lists, complete=complete)
   #  return render_template('index.html', title="Home ")

# # A decorator used to tell the application
# # which URL is associated function
# @app.route('/addtask', methods =["POST"])
# # @app.ri
# def add_task():
#    if request.method == "POST":
#       errors = False
#       # getting input with name = fname in HTML form
#       description = request.form.get("description")
#       # getting input with name = lname in HTML form 
#       priority = request.form.get("priority") 
#       due_date = request.form.get("duefor")
#       due_time = request.form.get("duetime")
#    else:
#       return redirect( url_for('index'))

# @app.route('/<int:list>')
# def view_list(list):
#     list_id = request.args.get('list')

if __name__=='__main__':
   app.run(
      debug=True,
      host="192.168.0.220"
   )