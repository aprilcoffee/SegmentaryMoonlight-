import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc
import socket 
import mu
sc.init()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host = '172.20.10.13'
port = 1688
s.bind((host,port))
s.listen(5)
sc.reset(10,0)
while True:
    conn,addr = s.accept()   
    if data:
        recvdata = str(data.decode('utf-8'))
        if recvdata == "end":
            mu.showLeftToRight()
            stringing = "B"
            conn.send(stringing.encode('utf-8'))
        else:
            mu.rhythem()

    else:
        conn,addr = s.accept()

conn.close()
