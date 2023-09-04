from py_imessage import imessage
import sleep

phone = "1234567890"

if not imessage.check_compatibility(phone):
    print("Not an iPhone")

guid = imessage.send(phone, "Hello World!")

# Let the recipient read the message
sleep(5)
resp = imessage.status(guid)

print(f'Message was read at {resp.get("date_read")}')