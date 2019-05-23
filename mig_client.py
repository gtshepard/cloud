# Echo client program
import socket
import os

def request_dest():
    HOST = '10.10.3.2'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    return data.decode('utf-8')

def migrate():
    dest = request_dest()
    os.system("./migrate " + str(dest))

def main():
    request_dest()
    
if __name__ == '__main__':
    main()
