import os
import time
import mig_client
import ids_client
import time
#import datetime
from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder='templates')
from flask import request
#import queue
import signal
import subprocess
import psutil





current_time = 0
@app.route("/")
def index():
        return render_template('index.html')
        
@app.route("/home", methods=['GET', 'POST'])
def home():
        global current_time
        print(request.remote_addr)
        t_end = time.time() + 2
        print(t_end, " anddd " , time.time())
        while time.time() < t_end:
            listen()
        try:
            if request.method == 'POST':
                try:
                    print("What", request.form)
                    if request.form.get('getTime'):
                        print("getTime test")
                    print("Post test")
                except:
                    print("form failed")
                data = {}
                try:
                    data['time'] = request.json['time']
                except:
                    print("Failed to request data")
        except:
            print("rip")
        return render_template('main_page.html', timestamp = current_time)# app.send_static_file("/templates/main_page.html")
        
#@app.route("/video")
#def video():
    #return redirect('/templates/Video1.mp4')

def get_est_conn():
    path = "/users/garrison/est-att-conn.txt"
    data_f = []
    dataVar = None
    with open(path,'r') as f:
        curr_data = f.readline().split()
        for var in curr_data:
            data_f.append(var)
    try:
        dataVar = data_f[4]
    except:
         print("Checking")
    conn_line = len(open(path,'r').readlines())
    dataFinal = []
    dataFinal.append(conn_line)
    dataFinal.append(str(dataVar))
    #print(conn_line)
    return dataFinal

def listen(timestamp = 0):
    if os.stat("./est-att-conn.txt").st_size == 0:
        os.system("sudo netstat -anp | grep :5000 | grep 192.122.236.119 | grep ESTABLISHED > est-att-conn.txt")
    get_conn = get_est_conn()
    #print(get_conn)
    if get_conn[0] > 10:
        print("UNDER ATTACK")
        path = "/users/garrison/est-att-conn.txt"
        with open(path,'w+') as f:
            f.write("")
        with open("attacker.txt","a+") as f:
            f.write(str(get_conn[0]) + " " + str(get_conn[1]))
        defend_attack()
        exit(0)
    time.sleep(.1)

def defend_attack():
    mig_client.migrate() 
    
def main():
    listen()

if __name__ == '__main__':
    #app.run(debug=True)
    main()
