from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Task(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done    = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done    = False

    def __repr__(self):
        return '<Content %s>' % self.content


db.create_all()


@app.route('/')
def tasks_list():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


#storing jsonjquery
@app.route('/json')
def background_process():
    task2 = request.args.get('tasK')
    task=Task(task2)
    db.session.add(task)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:task_id>')
def edit_task_id(task_id):
    details = Task.query.get(task_id)
    tasks   = Task.query.all()
    return render_template('edit.html',details=details ,tasks=tasks)

@app.route('/json2')
def background_process2():
    id              = request.args.get('id')
    content         = request.args.get('tasK')
    details         = Task.query.get(id)
    details.content = content
    db.session.add(details)
    db.session.commit()
    return render_template('index.html',tasks=tasks)


if __name__ == '__main__':
    app.run()
