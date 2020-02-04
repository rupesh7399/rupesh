from flask import Flask, request, flash, url_for, redirect, render_template
from flask import *  
from flask_sqlalchemy import SQLAlchemy  
import os
from flask import flash
from Xlib.display import Display
import sys  


  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)  
class Employees(db.Model): 

    
    id = db.Column('img_id', db.Integer, primary_key = True)  
    pw1 = db.Column(db.Integer)
    ph1 = db.Column(db.Integer)
    im1 = db.Column(db.String(200))
    iw1 = db.Column(db.Integer)
    ih1 = db.Column(db.Integer)
    ph2 = db.Column(db.Integer)
    im2 = db.Column(db.String(200))
    iw2 = db.Column(db.Integer)
    ih2 = db.Column(db.Integer)
    ph3 = db.Column(db.Integer)
    im3 = db.Column(db.String(200))
    iw3 = db.Column(db.Integer)
    ih3 = db.Column(db.Integer)
    fw = db.Column(db.Integer)
    fh = db.Column(db.Integer)
       
    def __init__(self,pw1, ph1, im1, iw1, ih1, ph2, im2, iw2, ih2, ph3, im3, iw3, ih3, fw, fh ):
        self.pw1 = pw1
        self.ph1 = ph1
        self.im1 = im1
        self.iw1 = iw1
        self.ih1 = ih1
        self.ph2 = ph2
        self.im2 = im2
        self.iw2 = iw2
        self.ih2 = ih2
        self.ph3 = ph3
        self.im3 = im3
        self.iw3 = iw3
        self.ih3 = ih3
        self.fw = fw
        self.fh = fh
    

@app.route("/login")  
def index():
    return render_template('login.html')

@app.route("/success",methods=['GET', 'POST'])
def success():
     
    if request.method == 'POST':
        email = request.form['email']
        pasw = request.form['pwd']
         
        if email == 'rupesh@gmail.com' and pasw == 'asdfgf':
            session['email']='rupesh@gmail.com'                   
            return home()
        else:
            flash("Email and Password are wrong!!",'error') 
            return index()
   

@app.route("/") 
def home():
         
    return render_template("home.html",i = Employees.query.first());

@app.route("/Image")
def imageUpload():
    return render_template("upload.html");

@app.route("/check")
def checkUser():
    return render_template("upload.html");

@app.route("/logout")
def logout():
    session.pop('email',None)  
    flash("Logout successfully!!" ,"success")
    return index()


    
    
    
    

@app.route("/add",methods=['GET', 'POST'])
def add():
    #try:
    
    if request.method == 'POST':
       screen = Display(':0').screen()
       pcwidth = screen.width_in_pixels
       width = pcwidth * 0.8
       width = round(width)
       pcheight = screen.height_in_pixels
       UPLOAD_FOLDER = './static/Images/'
       f = request.files['img1']  
       f.save(UPLOAD_FOLDER + f.filename)
       f1 = request.files['img2']
       f1.save(UPLOAD_FOLDER + f1.filename)
       f2 = request.files['img3']
       f2.save(UPLOAD_FOLDER + f2.filename)
       image1 = UPLOAD_FOLDER + f.filename
       image2 = UPLOAD_FOLDER + f1.filename
       image3 = UPLOAD_FOLDER + f2.filename
       pw1 = request.form['pw1']
       ph1 = request.form['ph1']
       im1 = image1
       iw1 = request.form['iw1']
       ih1 = request.form['ih1']
       ph2 = request.form['ph2']
       im2 = image2
       iw2 = request.form['iw2']
       ih2 = request.form['ih2']
       ph3 = request.form['ph3']
       im3 = image3
       iw3 = request.form['iw3']
       ih3 = request.form['ih3']
       width = width / int(pw1)
       height = int(ph1) + int(ph2) + int(ph3)
       height = pcheight / height 
       height = round(height)
       
       fw = width
       fh = height
       employee = Employees(pw1  , ph1, im1, iw1, ih1, ph2, im2, iw2, ih2, ph3, im3, iw3, ih3,fw,fh)
       db.session.add(employee)
       db.session.commit()
       flash('Record was successfully added','success') 
       return render_template('home.html')
    else:
        flash('Record was Faild !!','error') 
        return render_template('upload.html')
    # except :
    #     flash('Record was Faild !!','error') 
    #     return render_template('upload.html')

@app.route("/update",methods=['GET', 'POST'])
def update():
    
    return render_template('update.html', i = Employees.query.first()) 
############################################################################################
@app.route("/edits",methods=['GET', 'POST'])
def edits():
    screen = Display(':0').screen()
    pcwidth = screen.width_in_pixels
    pcheight = screen.height_in_pixels

    if request.method == 'POST':
       
       UPLOAD_FOLDER = './static/Images/'

       pw1 = request.form['pw1']
       # 80%
       width = pcwidth * 0.8
       width = round(width)
       width = width / int(pw1)
       
       ph1 = request.form['ph1']


       if request.files['img1'].filename == '':
           im1 = request.form['image1']
       else:
           f = request.files['img1']  
           f.save(UPLOAD_FOLDER + f.filename)
           im = UPLOAD_FOLDER + f.filename
           im1 = im
           #os.remove(request.form['image1'])
       iw1 = request.form['iw1']
       ih1 = request.form['ih1']
       ph2 = request.form['ph2']
       if request.files['img2'].filename == '':
           im2 = request.form['image2']
       else:
           f1 = request.files['img2']
           f1.save(UPLOAD_FOLDER + f1.filename)
           im = UPLOAD_FOLDER + f1.filename
           im2 = im
           #os.remove(request.form['image3'])
       iw2 = request.form['iw2']
       ih2 = request.form['ih2']
       ph3 = request.form['ph3']
       if request.files['img3'] .filename == '':
           im3 = request.form['image3']
       else:
           f2 = request.files['img3']
           f2.save(UPLOAD_FOLDER + f2.filename)
           im = UPLOAD_FOLDER + f2.filename
           im3 = im
           #os.remove(request.form['image3'])
       iw3 = request.form['iw3']
       ih3 = request.form['ih3']
       
       height = int(ph1) + int(ph2) + int(ph3)
       height = pcheight / height 
       pw1 = round(width * int(pw1))
       height = round(height)# 1 fit
       ph1 = round(int(ph1) * height)
       ph2 = round(int(ph2) * height)
       ph3 = round(int(ph3) * height)
       
       iw1 = round(width * int(iw1))
       ih1 = round(height * int(ih1))
       iw2 = round(width * int(iw2))
       ih2 = round(height * int(ih2))
       iw3 = round(width * int(iw3))
       ih3 = round(height * int(ih3))
       fw = width
       fh = height
       c = Employees.query.filter_by(id = 1).update(dict(pw1 = pw1, ph1=ph1, im1=im1, iw1=iw1, ih1=ih1, ph2=ph2, im2=im2, iw2=iw2, ih2=ih2, ph3=ph3, im3=im3, iw3=iw3, ih3=ih3, fw=fw, fh=fh))
       db.session.commit()
       flash('Record was successfully Updated','success') 
       return home()
    else:
        flash('Record was Faild !!','error') 
        return render_template('update.html')
    

if __name__ == '__main__':  
   db.create_all()  
   app.run(debug = True)  