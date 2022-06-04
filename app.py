

from flask import Flask , render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:12345678@localhost:5432/todo_list'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db=SQLAlchemy(app)
db.init_app(app)
class Todo(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20),nullable=False)
    message=db.Column(db.String(200),nullable=False)
    status=db.Column(db.String(10),nullable=False,default="pending")
    
# with app.app_context():
#     db.create_all()


@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        todos=get_pending_todo()
        db.create_all()
        return render_template('index.html')
    
    title=request.form.get('title')
    message=request.form.get('message')
    todo=request.form.get(title=title, message=message)
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    