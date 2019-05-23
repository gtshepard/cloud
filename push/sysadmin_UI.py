
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
# define for IIS module registration.
wsgi_app = app.wsgi_app
import sys




@app.route("/")
def hello():
        return "Hello World!"

def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/html"),
                                  ('Content-Length', str(len(self.html)))])

        return [self.html]

@app.route("/about")
def about():
	return render_template('hello.html', name=name)

@app.route("/adminUI")
def adminUI():
	name = "Francis :("
	app_status = "Running"
	Attack_IP = "" #"192.167.201.20"
	Connections = "N/A"
	Attack_Data = []
	Migration_Data = []
	Migration_IP = "192.50.20.12"
	Migration_Start = "N/A"
	Migration_End = "N/A"
	Decoy_Info = []
	Decoy_CPU = []
	CPU_Core = []
	RAM = []
	Bandwidth = []
	Dummy_IP = "192.42.12.51"
	Dummy_Traffic = "Crap"
	#print('Hello world!', file=sys.stdout)
	
	try:
		#print("Rip", file=sys.stdout)
		with open("/users/garrison/attacker.txt", 'r') as file:
			Attack_IP = file.read()
			#print("Line?" + Attack_IP, file=sys.stdout)
			#print("HELLO: " + Attack_IP, file=sys.stdout)
			tempStr = ""
			for var in Attack_IP:
				tempStr += var
			tempStr = tempStr.split()
			for obj in tempStr:
				Attack_Data.append(obj)
			Connections = Attack_Data[0]
			Attack_IP = Attack_Data[1].split(":")[0]
			#print("HUH")
	except:
		Attack_IP = "Not currently attacked"


	try:
		with open("/users/garrison/migration.txt", 'r') as file:
			file = file.read()
			#print(file.split()[0])
			Migration_Data = file.split()
			
			Migration_IP = Migration_Data[2]
			Migration_Start = Migration_Data[3] + " " +  Migration_Data[4]
			Migration_End = Migration_Data[5] + " " + Migration_Data[6]
	except:
		Migration_IP = "Not currently attacked"

	try:
		fileData = []
		with open("/users/garrison/decoyInfo.txt", 'r') as file:
			#.readline().split("-")
			file = file.read().split()	
			for line in file:
				fileData.append(line)
			for var in fileData:
				var = var.split("-")
				Decoy_CPU.append(var[0] + " Ghz")
				CPU_Core.append(var[1] + " Cores")
				RAM.append(var[2]+ " Gigs")
				Bandwidth.append(var[3]+ " mbps")
	except:
		Decoy_CPU = [] 
	
	try:
		return render_template('sysadmin.html', 
		s_status = app_status, 
		attack_target_ip = Attack_IP,	
		n_connections = Connections, 
		m_target_ip =Migration_IP, 
		m_start_time = Migration_Start, 
		m_end_time = Migration_End, 
		cpu_val_1 = Decoy_CPU[0] ,
		cpu_val_2 = Decoy_CPU[1] ,
		cpu_val_3 = Decoy_CPU[2] ,
		n_core_1 = CPU_Core[0], 
		n_core_2 = CPU_Core[1],
		n_core_3 = CPU_Core[2],
		ram_val_1 = RAM[0], 
		ram_val_2 = RAM[1],
		ram_val_3 = RAM[2],
		bw_val_1 = Bandwidth[0],
		bw_val_2 = Bandwidth[1],
		bw_val_3 = Bandwidth[2],
		dummy_ip = Dummy_IP, dummy_traffic = Dummy_Traffic
		)
	except:
		return render_template('sysadmin.html', 
		s_status = app_status, 
		attack_target_ip = Attack_IP,	
		n_connections = Connections, 
		m_target_ip =Migration_IP, 
		m_start_time = Migration_Start, 
		m_end_time = Migration_End, 
		cpu_val_1 = "N/A" ,
		cpu_val_2 = "N/A" ,
		cpu_val_3 = "N/A" ,
		n_core_1 = "N/A" ,
		n_core_2 = "N/A" ,
		n_core_3 = "N/A" ,
		ram_val_1 = "N/A" ,
		ram_val_2 = "N/A" ,
		ram_val_3 = "N/A" ,
		bw_val_1 = "N/A" ,
		bw_val_2 = "N/A" ,
		bw_val_3 = "N/A" ,
		dummy_ip = Dummy_IP, dummy_traffic = Dummy_Traffic
		)

if __name__ == '__main__':
        app.run(debug=True)
        #app.run(host= '0.0.0.0', port="33")
        #app.run(host= '192.170.230.112', port=9000, debug=False)

