from flask import Flask, render_template, request, url_for, flash, redirect,  jsonify
import datetime
import time
from time import sleep
import os
import sys
import openai
from toolbox.api import Prompter
from toolbox.imessageSender import iMessageSender

#db = sqlite3.connect(db_path, uri=True) sqlite3.DatabaseError: authorization denied

app = Flask(__name__)

OPENAI_API_KEY_import=os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY="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"



@app.route('/', methods=['GET', 'POST'])
def textScheduler():
    if request.method == 'POST':

        phoneNumber = request.form['phoneNumber']
        message = request.form['message']
        textSendTime = request.form['textSendTime']

        timestamp = datetime.datetime.now() # prints 2023-09-04 12:01:40.347519
        textString = phoneNumber + "--" + message + "--" + textSendTime
        textList = [phoneNumber, message, textSendTime]
        print(textString)

        with open('db/messageRequest.txt', 'a') as writer:
            writer.write('\n')
            writer.write('\n'.join(textList))
        
        sender = iMessageSender()
        sender.textSender(phoneNumber, message, timestamp)
        
    return render_template('text.html')

@app.route('/gpt', methods=['GET', 'POST'])
def gptResponder():
    if request.method == 'POST':

        recivedMessageSender = "4806486823"
        recivedMessage = "heyyy"
        recivedMessageResponseDelayTime = 30

        sleep(recivedMessageResponseDelayTime)
        gptBot = Prompter(OPENAI_API_KEY)
        gptResponse = gptBot.generateResponse(recivedMessage)
        print(gptResponse)
        
        sender = iMessageSender()
        sender.gptTextSender(recivedMessageSender, gptResponse)
        
    return render_template('text.html')


@app.route('/sendTextFromMac', methods=['GET', 'POST'])
def sendTextFromMac():
    if request.method == 'POST':
        print(request.form['message'])
    return render_template('text.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8003, debug=True)