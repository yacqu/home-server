from py_imessage import imessage
import datetime
import time
from time import sleep



class iMessageSender:
    
    def __init__(self):
        pass
    
    def textSender(self, number, message, timestamp):

        scheduledAtTimestamp = datetime.fromtimestamp(time.time())
        print(number)
        print(message)
        print(scheduledAtTimestamp)

        guid = imessage.send(number, message)

        return print('Text saying', message, 'was sent to', number, "@", scheduledAtTimestamp)

phone = "4806486823"
message = "this is a test message to test the class"

sender = iMessageSender()
sender.textSender(phone, message)