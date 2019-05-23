#network, RAM, cores, GHZ
import socket
import datetime
import decoy_clients

def get_resources(val):
	return val.split('-')

decoy_1 = get_resources(decoy_clients.req_decoy_1())
decoy_2 = get_resources(decoy_clients.req_decoy_2())
decoy_3 = get_resources(decoy_clients.req_decoy_3())

def get_decoy_1():
	return decoy_1

def get_decoy_2():
	return decoy_2

def det_decoy_3():
	return deocy_3


def decide_dest():	
	max_val = 0
	i = 0
	for i in range(len(decoy_1)):
		if decoy_1[i] == decoy_2[i] == decoy_3[i]:
		  print("equal: ", decoy_1[i], decoy_2[i], decoy_3[i])	
		else:	
		    max_val = max(decoy_1[i], decoy_2[i], decoy_3[i])
		    print("max", max_val, "i:", i, "dec:", decoy_1[i], decoy_2[i], decoy_3[i]) 
		    break;
		
	#for i in range(len(decoy_1)):
	if max_val == decoy_1[i]:
		print("choose 1")
		print(max_val)
		with open("migration.txt","a+") as f:
                        f.write("Choose 1, 10.10.1.1 " + str(datetime.datetime.now())+" "+ str(datetime.datetime.now()+ datetime.timedelta(seconds = 600))+ "\n")
		return '10.10.1.1'
	
	#for i in range(len(decoy_2)):
	if max_val == decoy_2[i]:
		print("choose 2")
		with open("migration.txt","a+") as f:
                        f.write("Choose 1, 10.10.2.1 " + str(datetime.datetime.now())+" "+ str(datetime.datetime.now()+ datetime.timedelta(seconds = 600))+ "\n")
		return '10.10.2.1'
		
	#for i in range(len(decoy_3)):
	if max_val == decoy_3[i]:
		print("choose 3")
		with open("migration.txt","a+") as f:
                        f.write("Choose 1, 10.10.4.1 "+ str(datetime.datetime.now())+" "+ str(datetime.datetime.now()+ datetime.timedelta(seconds = 600))+ "\n")
		return '10.10.4.1'

def main():
	decide_dest()

if __name__ == '__main__':	
	main()
