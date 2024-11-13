import socket
import sys
import time
import _thread

counter = 1
arguments=sys.argv
server_ip="127.0.0.1"
server_port=5009
client_msg="Hello"
if(len(arguments)>=2):
	server_ip=str(arguments[1])

if(len(arguments)>=3):
	server_port=int(arguments[2])

def send_message_to_server(client_socket):
    global counter
    global client_msg
    print("Initialize thread on Client to send Message to Server")
    while(1):
        message = "Message from Client -> "+client_msg+str(counter)
        client_socket.send(message.encode())
        counter+=1
        time.sleep(10)

def receive_message_from_server(client_socket):
    print("Initialize thread on client to receive Message from Server")
    while(1):
        data = client_socket.recv(2048)
        print("RECEIVED FROM SERVER:",data.decode())
        time.sleep(0.1)

# Define the server's address and port
server_address = (server_ip, server_port)  # Replace with the server's IP address if necessary

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

print("conected to server")

try:
    # Send data to the server
    _thread.start_new_thread(send_message_to_server,(client_socket,))

    _thread.start_new_thread(receive_message_from_server,(client_socket,))

    while(1):
        time.sleep(1)
    # Receive data from the server
except Exception as e:
    print("Error!", e)
# Close the socket
finally:
    client_socket.close()
