from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/students'
db=SQLAlchemy(app)

app.app_context().push()

class Student (db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40))
    dept=db.Column(db.String(40))
    year=db.Column(db.String(40))

    def __init__(self,name,dept,year):
       self.name=name
       self.dept=dept
       self.year=year


@app.route('/')
def home():
    return "<h2>Welcome to Home Page</h2>"

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        dept=request.form['dept']
        year=request.form['year']
        
        student = Student(name,dept,year)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("score"))
        
    return render_template("index.html")

@app.route('/score')
def score():
    return render_template("score.html")



if __name__ == '__main__':
    app.run(debug = True)