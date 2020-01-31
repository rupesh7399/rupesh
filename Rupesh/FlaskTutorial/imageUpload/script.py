from flask import Flask, request, flash, url_for, redirect, render_template  
from flask_sqlalchemy import SQLAlchemy  
import os
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)  
  
class Employees(db.Model):  
   id = db.Column('employee_id', db.Integer, primary_key = True)  
   name = db.Column(db.String(100))  
   phone = db.Column(db.String(50))  
   age = db.Column(db.String(200))   
   #pin = db.Column(db.String(10))  
  
   def __init__(self, name, phone, age):  
      self.name = name  
      self.phone = phone  
      self.age = age  
       
 
@app.route('/')  
def list_employees():  
   return render_template('list_employees.html', Employees = Employees.query.all() )  
 
@app.route('/add', methods = ['GET', 'POST'])  
def addEmployee():  
   if request.method == 'POST':  
      if not request.form['name'] or not request.form['phone'] or not request.form['age']:  
         flash('Please enter all the fields', 'error')  
      else:  
         employee = Employees(request.form['name'], request.form['phone'],  
            request.form['age'])  
           
         db.session.add(employee)  
         db.session.commit()  
         flash('Record was successfully added')  
         return redirect(url_for('list_employees'))  
   return render_template('add.html')  

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/success', methods = ['POST'])  
def success():  
    UPLOAD_FOLDER = './images/'
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(UPLOAD_FOLDER + f.filename)  
        return render_template("success.html", name = str(f.filename)       )  

if __name__ == '__main__':  
   db.create_all()  
   app.run(debug = True)  