import socket
import threading
import json
import os

nickname = input("Hello Teacher, what is your name: ")
region = input("region: ")
grades_input = input("Enter your grades you are teaching (comma separated, e.g. 1,2,3): ")

grades = [g.strip() for g in grades_input.split(",") if g.strip()]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

json_lock = threading.Lock()

DB_FILE = "data.json"


def save_message_to_db(message_text):
    with json_lock:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r", encoding="utf-8") as f:
                try:
                    db = json.load(f)
                except json.JSONDecodeError:
                    db = {}
        else:
            db = {}

        db.setdefault(region, {})

        for g in grades:
            db[region].setdefault(g, [])
            db[region][g].append(message_text)

        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=4, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
    print("Written to disk successfully in real-time!")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("Server closed connection.")
                client.close()
                break
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(f"Received: {message}")
        except Exception as e:
            print(f"An error occurred in receiver: {e}")
            client.close()
            break


def send_messages():
    while True:
        try:
            text = input("")
            if text.lower() == 'exit':
                client.close()
                break
            message = f"{nickname}: {text}"
            client.send(message.encode('utf-8'))
            save_message_to_db(message)
        except Exception as e:
            print(f"An error occurred in sender: {e}")
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=send_messages)
write_thread.start()