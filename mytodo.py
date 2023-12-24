from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bs


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_todo'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer ,primary_key = True)
    todoi_tem = db.Column(db.String(80),  nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    if (request.method =='POST'):
        todo = request.form.get('todo')
        a = Todo(todoi_tem = todo)
        db.session.add(a)
        db.session.commit()
    ls_col = bs.ls_cls
    todols = Todo.query.all()
    return render_template('todohome.html', col = ls_col, todols = todols)


@app.route("/addpost", methods = ['GET', 'POST'])
def addpost():
    pass

@app.route("/delete/<int:todo_id>", methods = ['GET', 'POST'])
def delete(todo_id):
    todo1 = Todo.query.get_or_404(todo_id)
    db.session.delete(todo1)
    db.session.commit()
    return redirect('/home')
    
    

# for todo in todols:
#     print(todo.todoi_tem)
app.run(debug=True)