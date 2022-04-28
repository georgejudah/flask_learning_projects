from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import functools
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# db.create_all()

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return secure_function

@app.get("/")
@login_required
def home():
    todo_list = db.session.query(Todo).all()
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template('base.html', todo_list=todo_list, name = session['username'])

@app.post("/add")
@login_required
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>", methods=["GET", "PUT"])
@login_required
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>", methods=["GET","DELETE"])
@login_required
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))



#users handling
# users = {"jose": ("jose", "1234")}
app.secret_key = "jose"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # if(db.session.query(User).filter(User.username == username)).first():
        if(User.query.filter(User.username == username)).first():
            if(User.query.filter(User.password == password)).first():
                print("Passwords match and user found")
                session["username"] = username
                return redirect(url_for("home"))
        
        password_match = False
        print("No password match")       
        return render_template("login.html", password_match=password_match)

        # if username in users and users[username][1] == password:
        #     session["username"] = username
            # return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if(User.query.filter(User.username != username)).first():
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
        else:
            user_already_registered = True
            return render_template("register.html", user_already_registered=user_already_registered)



        # if username not in users:
        #     users[username] = (username, password)
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')