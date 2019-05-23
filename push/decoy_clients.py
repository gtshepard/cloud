# Echo client program
import socket

def req_decoy_1():	
  HOST = '10.10.1.1'    # The remote host
  PORT = 3001             # The same port as used by the server
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  s.sendall(b'Hello, world')
  data = s.recv(1024)
  print('Received', data.decode('utf-8'))
  with open("decoyInfo.txt","a+") as f:
      f.write(data.decode('utf-8') + "\n")
  return data.decode('utf-8')

def req_decoy_2():
  HOST = '10.10.2.1'    # The remote host
  PORT = 3002             # The same port as used by the server
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  s.sendall(b'Hello, world')
  data = s.recv(1024)
  print('Received', data.decode('utf-8'))
  with open("decoyInfo.txt","a+") as f:
      f.write(data.decode('utf-8') + "\n")
  return data.decode('utf-8')

def req_decoy_3():
  HOST = '10.10.4.1'    # The remote host
  PORT = 3003            # The same port as used by the server
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  s.sendall(b'Hello, world')
  data = s.recv(1024)
  print('Received', data.decode('utf-8') + "\n")
  with open("decoyInfo.txt","a+") as f:
      f.write(data.decode('utf-8') + "\n")
  return data.decode('utf-8')

def main():
	req_decoy_1()
	req_decoy_2()
	req_decoy_3()

if __name__ == '__main__':
	main()
	
