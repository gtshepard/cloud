# Save as server.py
# Message Receiver
import psutil
import os
from socket import *
import time
import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line
    
    
def get_network_usage():
    network_bandwidth = 0
    diff_bandwidth = []
    time_limit = 10
    time_alloted = 0
    while True:
        if(time_limit == time_alloted):
            return diff_bandwidth
        new_bandwidth = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        val = network_bandwidth
        if network_bandwidth:
           val = network_bandwidth - new_bandwidth
        diff_bandwidth.append(val)
        network_bandwidth = new_bandwidth
        time.sleep(.1)
        time_alloted += 1

def convert_to_gbit(value):
    return value/1024./1024./1024.*8

def send_stat(value):
    print ("%0.3f" % convert_to_gbit(value))

random.seed(20411)
host = ""
port = 3000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
#f= open("decoy.txt","r")
#fileLine = random.choice(f.readLines()) #random_line(f)
#contents = f.read()
with open("decoy.txt","r") as f:
    lines = f.readlines()
    while True:
        #print(choice)
        #print(lines)
        fileData = lines[0].split()
        (data, addr) = UDPSock.recvfrom(buf)
        #print("Got something..")
        data = data.decode('utf-8')
        data = data.split(":")
        print("Received message: " , data)
        nexthost = str(data[0])
        nextport = int(data[1])
        print(nexthost, nextport)
        nextaddr = (nexthost, nextport)
        UDPSockSend = socket(AF_INET, SOCK_DGRAM)
        cpuUsage = fileData[0].split(":")[1] #psutil.cpu_percent()
        ramUsage = fileData[1].split(":")[1] #psutil.virtual_memory()
        networkUsage = fileData[2].split(":")[1] #get_network_usage()
        print("CPU:",cpuUsage, "\nRam:", ramUsage, "\nNetwork:", networkUsage)
        allData = "CPU:" + cpuUsage + " RAM:" + ramUsage + " NETWORK:" + networkUsage
        packetData = str.encode(allData)
        UDPSockSend.sendto(packetData, nextaddr)
        print("Send message!", packetData, nextaddr)
UDPSock.close()
os._exit(0)