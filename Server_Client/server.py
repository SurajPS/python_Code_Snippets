
import socket
import sys
import time
import _thread

counter = 1
arguments=sys.argv
server_ip="127.0.0.1"
server_port=5019
server_message="watsup"
enable_send=False

if(len(arguments)>=2):
	server_ip=str(arguments[1])

if(len(arguments)>=3):
	server_port=int(arguments[2])


def receive_message_from_client(conn):
    global enable_send
    print("Thread starting to receive Message from Client")
    while(1):
        data_path = conn.recv(4096).decode()
        if(len(data_path)>2):
            enable_send=not(enable_send)
            print("Data from Client -> " + str(data_path))
        time.sleep(0.5)

def send_message_to_client(conn):
    global server_message
    global counter
    global enable_send
    print("Thread starting to send Message to Client")
    while(1):
        if(enable_send):
            msg_s="Server ->"+server_message+str(counter)
            conn.send(msg_s.encode())
            counter+=1
            time.sleep(1)


port = server_port  # initiate port no above 1024
host = server_ip
print("Server -> Initiating Server.....")
server_socket = socket.socket()  # get instance
server_socket.bind((host, port))  # bind host address and port together
#while True:
    # configure how many client the server can listen simultaneously
server_socket.listen(2)
conn, address = server_socket.accept()  # accept new connection
print("Server :-> Connected from: " + str(address))
_thread.start_new_thread(receive_message_from_client,(conn,))
_thread.start_new_thread(send_message_to_client,(conn,))
while(1):
    time.sleep(1)
conn.close()  # close the connection