#by Rishab Budale team Nebula
import socket
import json


connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def con(ip,port):
    connection.connect((ip,port))

def send_data(data):
    jdata=json.dumps(data)
    connection.send(jdata.encode())

def recieve_data():
    data=b""
    while True:
        try:
            data=data+connection.recv(1024)
            return json.loads(data.decode())
        except ValueError:
            continue  

con('127.0.0.1',4444)

while True:
    data=input("Enter data ")
    send_data(data)
        
    ret_data=recieve_data()
    print(ret_data)

    
