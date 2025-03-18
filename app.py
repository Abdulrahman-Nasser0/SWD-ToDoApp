from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dwdwjijdwid jwidjwi jiwjd iwjdiwjd'

tasks_list = []



@app.route('/',methods=['POST','GET'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        completed = 'completed' in request.form 
        
        tasks_list.append({'task': task, 'completed': completed})
        return redirect(url_for('tasks'))
    return render_template('add_task.html', title='Add Task', tasks= tasks_list)

@app.route('/tasks',methods=['POST','GET'])
def tasks():
    return render_template('tasks.html', title='Tasks', tasks= tasks_list)


if __name__ == "__main__":
    app.run(debug=True, port=3000)