import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Alhamdulillah main uler"
    # return render_template("index.html", message="Hello Flask!");
    #return render_template("index.html", message="Hello Flask!", contacts = ['c1', 'c2', 'c3', 'c4', 'c5']);   

if __name__ == '__main__':
    app.run()
