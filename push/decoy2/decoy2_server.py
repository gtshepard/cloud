import socket 
def get_resources():
    return bytes("1-12-6-4", 'utf-8')
        #return b'10.10.4.1'

def listener():
    HOST = ''        # Symbolic name meaning all available interfaces
    PORT = 3002             # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(get_resources())
def main():
    listener()

if __name__ == '__main__':
    main()

