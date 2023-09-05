from py_imessage import imessage, db_conn
import datetime
import time
from time import sleep



class iMessageSender:
    
    def __init__(self):
        
        pass
    
    def textSender(self, phoneNumber, message, timestamp):

        scheduledAtTimestamp = datetime.datetime.now()
        guid = imessage.send(phoneNumber, message)
        return print('Text saying', message, 'was sent to', phoneNumber, "@", scheduledAtTimestamp)
    
    def gptTextSender(self, phoneNumber, message):
        guid = imessage.send(phoneNumber, message)
        print('Text saying', message, 'was sent to', phoneNumber)
        return guid
    


#phoneNumber = "4806486823"
#message = "this is a test message to test the class"
#timestamp = "2023-09-04 12:01:40.347519"

#sender = iMessageSender()
#sender.textSender(phoneNumber, message, timestamp)