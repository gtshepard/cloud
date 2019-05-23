
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
from flask import request
#import queue
import signal
import subprocess
import psutil


process_list = []
current_pVal = 1
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

@app.route("/")
def start():
   return "<h1> welcome </h1>"

@app.route("/index", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            #print("Encrypted" , file=sys.stdout)
            print("Encrypted")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            #print("Decrypted" , file=sys.stdout)
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")


@app.route("/results", methods=['GET', 'POST'])
def results():
        return render_template("att_graph_result1.html")

       
@app.route("/attacker_UI", methods=['GET', 'POST'])
def attacker_UI():
    global current_pVal
    global process_list
    intensity = 0
    max_reached = False
    try:
        with open("intensity.txt", "r") as file:
            output = file.readline()
            #print(output)
            intensity = int(output)
            #print("Intensity", intensity)
    except IOError:
        print("IOERROR")
    #print(request.method)
    server_up = "Running"
    try:
        if request.method == 'POST':
            if request.form.get('Increase-Attack') == 'Increase':
                #print("here")
                
                if intensity >= 1000:
                    max_reached = True
                else:
                    intensity += 100
                    cmd = ['python3', 'ddos_singular.py'] #'python3', 'ddos_singular.py'
                    process = subprocess.Popen(['python3', 'ddos_singular.py', str(current_pVal)], shell = False, stdin=None, stdout=None, stderr=None, close_fds = True) #,preexec_fn=os.setsid)
                    process_list.append(process.pid)
                    current_pVal+=1
                if intensity == 1000:
                    max_reached = True
                #print(intensity)
                with open("intensity.txt", "w+") as file:
                    file.write(str(intensity))
            if request.form.get('Decrease-Attack') == 'Decrease':
                if intensity >= 100:
                    intensity -= 100
                    try:
                        current_process = process_list.pop()
                        kill(current_process)
                        #print(process_list)
                    except:
                        print("Failed to kill process")
                if intensity == 0:
                    server_up = "Stopped"
                #print(intensity)
                with open("intensity.txt", "w+") as file:
                    file.write(str(intensity))
            if request.form.get('Stop-Attack') == 'Stop':
                intensity = 0
                with open("intensity.txt", "w+") as file:
                    file.write(str(intensity))
                server_up = "Stopped"
                try:
                    for var in process_list:
                        print(var)
                        kill(var)
                    process_list = []
                except:
                    print("Failed to kill process")
        elif request.method == 'GET':
            print("No Post Back Call")
        #print("max_reached", max_reached)
        return render_template('AttackerUi.html', server_ip = "192.122.236.119", attack_intensity = intensity, server_status = server_up, max_limit = max_reached)
    except:
        return render_template('AttackerUi.html', server_ip = "192.122.236.119", attack_intensity = intensity, server_status = server_up)


if __name__ == '__main__':
    app.run(debug=True)
