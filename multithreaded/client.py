# echo client using TCP in Python

import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT=54321

# create socket
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP,PORT))
    print(f"client is connected")
except Exception as e:
    print("Error in socket creation: ",e)
    sys.exit()



# client operations
while True:
    try:
        input_message=input("Enter here: ")
        sock.send(input_message.encode("utf-8"))
        recv_msg=sock.recv(1024)
        if not recv_msg:
            print("No messafe received")
            break
        print("echo >>",recv_msg.decode("utf-8"))
    except Exception as e:
        print("Error in client operation: ",e)
        break
    except KeyboardInterrupt:
        print("Closing client connection ")
        break
sock.close()
sys.exit