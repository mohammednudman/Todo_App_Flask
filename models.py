from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Todo(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20),nullable=False)
    message=db.Column(db.String(200),nullable=False)
    status=db.Column(db.String(10),nullable=False,default="pending")
    
    def get_todo(todo_id):
        return Todo.query.filter(Todo.id==todo_id).first()

    def get_pending_todo():
        return Todo.query.filter(Todo.status=='pending').all()

    def get_completed_todo():
        return Todo.query.filter(Todo.status=='completed').all()
    