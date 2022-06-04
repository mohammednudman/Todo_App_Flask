from urllib import request
from flask import Flask , render_template
from models import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:Vruddhi@9@localhost:5432/todo_list'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db.init_app(app)

@app.route('/')
def home():
    # if request.method == 'GET':
        # todos=get_pending_todo()
        db.create_all()
        return render_template('index.html',todos=todos,cnt=len(todos))
    
    # title=request.form.get('title')
    # message=request.form.get('message')
    # todo=request.form.get(title=title, message=message)
    # db.session.add(todo)
    # db.session.commit()
    # return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
    