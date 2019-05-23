# Echo client program
import socket
import os

def send(data):
    HOST = '10.10.3.2'    # The remote host
    PORT = 9000              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'192.122.236.119')
    data = s.recv(1024)
    return data.decode('utf-8')

def main():
    send()

if __name__ == '__main__':
    main()

