from datetime import datetime, timezone
import time
import socket
import json
import csv
import _thread

# Define the GPS data to emulate

current_time = datetime.now(timezone.utc)
gps_data = {
    "class": "TPV",
    "device": "/dev/ttyUSB0",
    "magtrack": 3.3423,
    "time": current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    "ept": 0.05,
    "lat": 37.7749,
    "lon": -122.4194,
    "alt": 412.0,
    "epx": 2.0,
    "epy": 2.0,
    "epv": 6.0,
    "track": 45.0,
    "speed": 10.0,
    "climb": 0.8,
    "eps": 0.5,
    "epc": 4500,
    "mode": 3
}

number_of_clients = 0


file_name="FN_TLC.csv"
gps_points=[[47.65670607,9.484443284]]

with open(file_name) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(row[8]=='Left'):
            gps_points.append([float(row[0]),float(row[1])])

# Create a socket server to emulate GPSD
HOST = '127.0.0.1'
PORT = 2947
print(len(gps_points))
current_gps=gps_points[0]

def handle_client(server_socket):
    global number_of_clients
    global current_gps
    number_of_clients+=1
    try:
        connection, addr = server_socket.accept()
        print(f"----->Connected from {addr}")
        dev="tcp://"+str(addr[0])+":"+str(addr[1])
        print(connection.recv)
        while(1):
            gps_data["time"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            gps_data["lat"] = current_gps[0]
            gps_data["lon"] = current_gps[1]
            response = {"class": "TPV", "device": dev, **gps_data}
            response_str = json.dumps(response) + "\n"
            connection.sendall(response_str.encode())
            time.sleep(1)  # Emulate GPS data update every 1 second
    except Exception as e:
        print("Error: ", str(e))
    except KeyboardInterrupt:
        print("Stopping the GPSD Emulator")
    number_of_clients -= 1
    print(f"Current Client Count: {number_of_clients}")


try:
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"GPSD emulator listening on {HOST}:{PORT}")
    while(number_of_clients<10):
        _thread.start_new_thread(handle_client, (server_socket,))
        time.sleep(3)
    while (1):
        for data in gps_points:
            current_gps = data
            time.sleep(0.1)  # Emulate GPS data update every 1 second
except KeyboardInterrupt:
    print("GPSD emulator stopped.")
except Exception as e:
    print(f"An error occurred: {e}")

