from flask import Flask, render_template, request, url_for, flash, redirect,  jsonify
import datetime
import time
from time import sleep
import os

import sys
sys.path.append("toolbox/gpt")
from api import Prompter


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':

        phoneNumber = request.form['phoneNumber']
        message = request.form['message']
        textSendTime = request.form['textSendTime']
        textString = phoneNumber + "--" + message + "--" + textSendTime
        textList = [phoneNumber, message, textSendTime]
        print(textString)
        print(datetime.datetime.now()) # prints 2023-09-04 12:01:40.347519

        with open('db/messageRequest.txt', 'a') as writer:
            writer.write('\n')
            writer.write('\n'.join(textList))
        


    return render_template('text.html')

@app.route('/sendTextFromMac', methods=['GET', 'POST'])
def sendTextFromMac():
    if request.method == 'POST':
        print(request.form['message'])
    return render_template('text.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)