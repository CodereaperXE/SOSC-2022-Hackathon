#by Rishab Budale team Nebula
import json
import re
import socket

#connection-----------------------------------
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(("127.0.0.1", 4444))
connection.listen(0)
conn,add=connection.accept()
 
def send_data(data):
    jdata=json.dumps(data)
    conn.send(jdata.encode())

def recieve_data():
    data=b""
    while True:
        try:
            data=data+conn.recv(1024)
            return json.loads(data.decode())
        except ValueError:
            continue 

def filter(f):
    data = json.load(f)
    string = '|'.join(data)
    regex = rf"({string})"
    result=re.findall(regex,text)
    return result



def rating(data_class,volume):
    if(data_class==3):
        score=100-(100/volume)
        print(100-(100/volume))
    elif(data_class==2):
        score=66-(66/volume)
        print(66-(66/volume))
    elif(data_class==1):
        score=33-(33/volume)
        print(33-(33/volume))

    return str(score)


while True:
    finaldata=""
   
    text=recieve_data()
   

    f1 = open('data_class_1.json')
    f2 = open('data_class_2.json')
    f3 = open('data_class_3.json')
    #--------------------------------------------------------------



    if (len(filter(f3))>0):
        f3 = open('data_class_3.json')
        state1=str(len(filter(f3)))
        rate=rating(3,int(state1))
        print(state1+" class 3 words detected")
        finaldata+=state1+" class 3 world detected "+rate+" "
        
    


    if (len(filter(f2))>0):
        f2 = open('data_class_2.json')
        state2=str(len(filter(f2)))
        rate=rating(2,int(state2))
        print(state2+" class 2 words detected")
        finaldata+=state2+" class 2 word detected "+rate+" "
        
   


    if (len(filter(f1)) >0):
        f1 = open('data_class_1.json')
        state3=str(len(filter(f1)))
        rate=rating(1,int(state3))
        print(state3+" class 1 words detected")
        finaldata+=state3+" class 1 words detected "+rate+" "
       
    
    if(finaldata==""):
        send_data("None")
        continue

    send_data(finaldata)
    finaldata=""
    
    
    
    
