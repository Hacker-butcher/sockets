import socket
import sys
import threading

IP = socket.gethostbyname("192.168.167.187")
PORT = 55203

# List to store connected clients
connected_clients = []

# Function to broadcast a message to all clients
def broadcast_message(message, sender_sock):
    for client_sock in connected_clients:
        if client_sock != sender_sock:
            try:
                client_sock.send(message.encode("utf-8"))
            except Exception as e:
                print("Error broadcasting message to a client: ", e)

# Create socket
try:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((IP, PORT))
    server_sock.listen()
    print(f"Server is up and running at {IP}:{PORT}")
except Exception as e:
    print("Error in socket creation: ", e)
    sys.exit()

# Function to handle a new client
def client_handler(client_sock):
    try:
        while True:
            message = client_sock.recv(1024)
            if not message:
                print("Client disconnected")
                break
            message_str = message.decode("utf-8")
            print(f"Received: {message_str}")
            broadcast_message(f"Client: {message_str}", client_sock)
    except Exception as e:
        print("Error in client handling: ", e)
    finally:
        connected_clients.remove(client_sock)
        client_sock.close()

# Accept and handle client connections
while True:
    try:
        client_sock, client_addr = server_sock.accept()
        print(f"[+] {client_addr[0]}:{client_addr[1]} connected")
        connected_clients.append(client_sock)
        broadcast_message(f"Client {client_addr[0]}:{client_addr[1]} joined the chat", client_sock)
        client_thread = threading.Thread(target=client_handler, args=(client_sock,))
        client_thread.start()
    except Exception as e:
        print(f"Error accepting client connection: ", e)
        break
    except KeyboardInterrupt:
        break

# Close the server socket
server_sock.close()
sys.exit()
