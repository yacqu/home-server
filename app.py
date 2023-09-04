from flask import Flask, render_template, request, url_for, flash, redirect,  jsonify
from time import sleep
import os



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        print(request.form['message'])
    return render_template('text.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)