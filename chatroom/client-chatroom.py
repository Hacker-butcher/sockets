import socket
import threading
import sys

# Server configuration
SERVER_IP = socket.gethostbyname("192.168.167.187")  # Replace with the actual server IP address
SERVER_PORT = 55203

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to the chat server")
except Exception as e:
    print(f"Error connecting to the server: {e}")
    sys.exit()

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except Exception as e:
            print(f"Error receiving messages: {e}")
            break

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Function to send messages to the server
def send_messages():
    while True:
        try:
            message = input()
            if message.lower() == "exit":
                break
            client_socket.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error sending messages: {e}")
            break

# Start a thread to send messages to the server
send_thread = threading.Thread(target=send_messages)
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()

# Close the client socket
client_socket.close()