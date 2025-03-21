from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def add_task():
    if request.method == 'POST':
        task_content = request.form.get('task')
        completed = 'completed' in request.form
        
        current = Task(task=task_content, completed=completed)
        db.session.add(current)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('add_task.html', title='Add Task')

@app.route('/tasks', methods=['POST', 'GET'])
def tasks():
    tasks_list = Task.query.all()
    return render_template('tasks.html', title='Tasks', tasks_list=tasks_list)

if __name__ == "__main__":
    app.run(debug=True, port=3000)