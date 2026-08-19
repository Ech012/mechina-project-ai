import socket
import threading

# Now this Host is the IP address of the Server, over which it is running.
# I've user my localhost.
host = "127.0.0.1"
port = 5555  # Choose any random port which is not so common (like 80)
# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 55555        # Choose any unassigned port

# Start server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    """Sends a message to all connected clients."""
    for client in clients:
        try:
            client.send(message)
        except:
            # Handle broken connections gracefully
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)

def handle_client(client):
    """Handles communication with an individual client."""
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            if not message:
                raise Exception("Disconnected")
            broadcast(message)
        except:
            # Remove client if they disconnect
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} left the chat.".encode('utf-8'))
                nicknames.remove(nickname)
            break

def receive_connections():
    """Main loop to accept new incoming clients."""
    print(f"Server is running and listening on {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask the client for their nickname
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        # Start a thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()
