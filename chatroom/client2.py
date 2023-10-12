import socket
import sys
import threading

IP = socket.gethostbyname("192.168.167.241")
PORT = 55203

# Create socket
try:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((IP, PORT))
    print(f"Connected to the server")
except Exception as e:
    print("Error in socket creation: ", e)
    sys.exit()

# Ask the user to input their name
client_name = input("Enter your name: ")

# Function to receive and display messages
def receive_messages():
    try:
        while True:
            message = client_sock.recv(1024)
            if not message:
                print("Server disconnected")
                break
            message_str = message.decode("utf-8")
            print(message_str)
    except Exception as e:
        print("Error receiving messages: ", e)
    finally:
        client_sock.close()

# Start a thread to receive and display messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Function to send messages to the server
def send_messages():
    try:
        while True:
            message = input()
            if message:
                message_with_name = f"{client_name}: {message}"
                client_sock.send(message_with_name.encode("utf-8"))
    except Exception as e:
        print("Error sending messages: ", e)
    finally:
        client_sock.close()

# Start a thread to send messages to the server
send_thread = threading.Thread(target=send_messages)
send_thread.start()

# Wait for both threads to finish
receive_thread.join()
send_thread.join()
