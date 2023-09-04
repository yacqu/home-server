from py_imessage import imessage
from time import sleep

phone = "4806486823"


guid = imessage.send(phone, "Hello World!")

# Let the recipient read the message
sleep(5)
resp = imessage.status(guid)

print(f'Message was read at {resp.get("date_read")}')