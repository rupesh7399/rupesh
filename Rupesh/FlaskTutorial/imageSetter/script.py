from flask import Flask, request, flash, url_for, redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///employees.sqlite3'  
app.config['SECRET_KEY']="secret key"

db = SQLAlchemy(app)



@app.route("/")  
def index():  
    return render_template("login.html");  

@app.route("/Image")
def imageUpload():
    return render_template("upload.html");

@app.route("/check")
def checkUser():
    return render_template("upload.html");

if __name__ == '__main__':  
   db.create_all()  
   app.run(debug = True)  