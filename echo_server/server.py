# echo server using TCP in Python

import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT=54321

# create socket
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP,PORT))
    sock.listen()
    print(f"Sever is up and running at {IP}:{PORT}")
except Exception as e:
    print("Error in socket creation: ",e)
    sys.exit()


# handle the client
while True:
    try:
        client,addr=sock.accept()
        print("Client connected from: ",addr[0],":",addr[1])
        while True:
            try:
                msg=client.recv(1024)
                if not msg:
                    print("no data received")
                    break
                print(addr[0],":",addr[1],">>",msg.decode("utf-8"))
                client.send(msg)
            except Exception as e:
                print("Error in send/recv:",e)
                break
            except KeyboardInterrupt:
                print("Closing client connection")
                client.close()
                break
    except Exception as e:
        print("Error in handling client: ",e)
        break
    except KeyboardInterrupt:
        print("Closing server ")
        break
sock.close()
sys.exit