from flask import Flask

app = Flask(__name__)

#@app.route('/home/<name>')

def about():
    return "hello, this is our first flask website,";

app.add_url_rule("/about","about",about)  

if __name__ == '__main__':
    app.run(debug=True) 