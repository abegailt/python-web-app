from flask import render_template, session, url_for, request, g, jsonify,redirect
from app import app
from datetime import datetime
from app import app, db
#from .forms import LoginForm, EditForm
from .models import Task


@app.route('/')
def tasks_list():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


#after click add button and storing data to sqlserver
@app.route('/json')
def background_process():
    task2 = request.args.get('tasK')
    task=Task(task2)
    db.session.add(task)
    db.session.commit()
    return redirect('/')

#after clicking delete button
@app.route('/delete/<task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')

#after clicking edit button
@app.route('/edit/<int:task_id>')
def edit_task_id(task_id):
    details = Task.query.get(task_id)
    tasks   = Task.query.all()
    return render_template('edit.html',details=details ,tasks=tasks)

#for updating data after editing
@app.route('/json2')
def background_process2():
    content         = request.args.get('data')
    id              = request.args.get('data2')
    details         = Task.query.get(id)
    details.content = content
    db.session.add(details)
    db.session.commit()
    return "Success"

