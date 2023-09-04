from py_imessage import imessage
import datetime
import time
from time import sleep

phone = "4806486823"


guid = imessage.send(phone, "Hello World!")

# Let the recipient read the message
sleep(5)
resp = imessage.status(guid)

print(f'Message was read at {resp.get("date_read")}')


def textSender(number, message, timestamp):
    print(datetime.fromtimestamp(time.time()))

    if timestamp == datetime.datetime.now():
        print('now')

    guid = imessage.send(number, message)

    print(f'Message was read at {resp.get("date_read")}')


