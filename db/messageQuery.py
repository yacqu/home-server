import sqlite3
import datetime
import subprocess
import os
import json


def get_chat_mapping(db_location):
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    cursor.execute("SELECT room_name, display_name FROM chat")
    result_set = cursor.fetchall()

    mapping = {room_name: display_name for room_name, display_name in result_set}

    conn.close()

    return mapping
# Function to read messages from a sqlite database
def read_messages(db_location, n, self_number='Me', human_readable_date=True):
    # Connect to the database and execute a query to join message and handle tables
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()
    query = """
    SELECT message.ROWID, message.date, message.text, message.attributedBody, handle.id, message.is_from_me, message.cache_roomnames
    FROM message
    LEFT JOIN handle ON message.handle_id = handle.ROWID
    """
    if n is not None:
        query += f" ORDER BY message.date DESC LIMIT {n}"
    results = cursor.execute(query).fetchall()
    
    # Initialize an empty list for messages
    messages = []
    messagesNew = []

    # Loop through each result row and unpack variables
    for result in results:
        rowid, date, text, attributed_body, handle_id, is_from_me, cache_roomname = result

        # Use self_number or handle_id as phone_number depending on whether it's a self-message or not
        phone_number = self_number if handle_id is None else handle_id

        # Use text or attributed_body as body depending on whether it's a plain text or rich media message
        if text is not None:
            body = text
        
        elif attributed_body is None: 
            continue
        
        else: 
            # Decode and extract relevant information from attributed_body using string methods 
            attributed_body = attributed_body.decode('utf-8', errors='replace')
            if "NSNumber" in str(attributed_body):
                attributed_body = str(attributed_body).split("NSNumber")[0]
                if "NSString" in attributed_body:
                    attributed_body = str(attributed_body).split("NSString")[1]
                    if "NSDictionary" in attributed_body:
                        attributed_body = str(attributed_body).split("NSDictionary")[0]
                        attributed_body = attributed_body[6:-12]
                        body = attributed_body

        # Convert date from Apple epoch time to standard format using datetime module if human_readable_date is True  
        if human_readable_date:
            date_string = '2001-01-01'
            mod_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            unix_timestamp = int(mod_date.timestamp())*1000000000
            new_date = int((date+unix_timestamp)/1000000000)
            date = datetime.datetime.fromtimestamp(new_date).strftime("%Y-%m-%d %H:%M:%S")

        mapping = get_chat_mapping(db_location)  # Get chat mapping from database location

        try:
            mapped_name = mapping[cache_roomname]
        except:
            mapped_name = None

        messages.append(
            {"rowid": rowid, "date": date, "body": body, "phone_number": phone_number, "is_from_me": is_from_me,
             "cache_roomname": cache_roomname, 'group_chat_name' : mapped_name})
        
        messagesNew.append({"phone_number": phone_number, "body": body,})

    conn.close()
    return messages, messagesNew


def print_messages(messages):
    print(json.dumps(messages))


# ask the user for the location of the database
db_location = "/Users/yacqubabdirahman/Library/Messages/chat.db"
# ask the user for the number of messages to read
n = "10"

# Remove the 2 lines below after testing -- they are for testing only
[messages, messagesNew] = read_messages(db_location, n)
print_messages(messagesNew)
# Remove the 2 lines above after testing -- they are for testing only