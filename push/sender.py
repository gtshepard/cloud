'''
Created on May 06, 2019

@author: muhammadusman
'''
import os
from socket import *

host = ""
port = 3000
addr = (host, port)

Sock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = bytes(input("Enter message to send:"), "utf-8")
    Sock.sendto(data,addr)
    if data == "exit":
        break
Sock.close()
os.exit(0)




