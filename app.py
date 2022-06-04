from flask import Flask , render_template,request,redirect
from models import db,Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:12345678@localhost:5432/todo_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        todos=Todo.get_pending_todo()
        db.create_all()
        return render_template('index.html',todos=todos,cnt=len(todos))
    
    title=request.form.get('title')
    message=request.form.get('message')
    todo=Todo(title=title, message=message)
    db.session.add(todo)
    db.session.commit()
    return redirect('/')

@app.route('/todos/complete/<int:todo_id>')
def complete_todo(todo_id):
    todo=Todo.get_todo(todo_id)
    if todo is None:
        return "<h1>Invalid todo id</h1>"
    todo.status="completed"
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/todos/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.get_todo(todo_id)
    if todo is None:
        return "<h1>Invalid todo id</h1>"
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
    