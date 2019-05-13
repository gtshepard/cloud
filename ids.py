import os
import time
import mig_client

def get_est_conn():
    path = "/users/garrison/est-att-conn.txt"
    conn_line = len(open(path,'r').readlines())
    print(conn_line)
    return conn_line

def listen():
    while True:
        os.system("sudo netstat -anp | grep :80 | grep 192.122.236.119 | grep ESTABLISHED > est-att-conn.txt")

        if get_est_conn() > 10:
            print("UNDER ATTACK")
            defend_attack()
            exit(0)

        time.sleep(5)

def defend_attack():
    mig_client.migrate() 

def main():
    listen()

if __name__ == '__main__':
    main()
