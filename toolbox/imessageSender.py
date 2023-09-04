from py_imessage import imessage
import datetime
import time
from time import sleep



class iMessageSender:
    
    def __init__(self):
        pass
    
    def textSender(self, phoneNumber, message, timestamp):

        scheduledAtTimestamp = datetime.datetime.now()
        print(phoneNumber)
        print(message)
        print(scheduledAtTimestamp)

        guid = imessage.send(phoneNumber, message)

        return print('Text saying', message, 'was sent to', phoneNumber, "@", scheduledAtTimestamp)

phoneNumber = "4806486823"
message = "this is a test message to test the class"
timestamp = "2023-09-04 12:01:40.347519"

sender = iMessageSender()
sender.textSender(phoneNumber, message, timestamp)