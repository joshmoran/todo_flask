



# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for
 
# Flask constructor
app = Flask(__name__)   

# A decorator used to tell the application
# which URL is associated function
@app.route('/addtask', methods =["POST"])
# @app.ri
def add_task():
    if request.method == "POST":
       errors = False
       # getting input with name = fname in HTML form
       description = request.form.get("description")
       # getting input with name = lname in HTML form 
       priority = request.form.get("priority") 
       due_date = request.form.get("duefor")
       due_time = request.form.get("duetime")

      #  Add task to the list 

      redirect(url_for('index'))
      
      return "Your name is " + str(due_time)
      
    return render_template("form.html")
 
if __name__=='__main__':
   app.run(
      debug=True,
      host="192.168.0.220"
   )