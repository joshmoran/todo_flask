from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', title="Home ")

@app.route("/add/", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        task_name = request.form['name']
        task_priority = request.form.get['priority']
        task_deadline = request.form.get['deadline']

    return render_template('add.html', title='Add a Task')

if __name__ == "__main__":
    app.run(
        debug=True,
        host="192.168.0.220"
    )