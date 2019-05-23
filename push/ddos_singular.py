

import os 
import sys
print("SYS ARG", sys.argv[1])
os.system("slowhttptest -c 1000 -H -g -o ./templates/att_graph_result" + str(sys.argv[1]) +  " -i 10 -r" + "100" + " -t GET -u  http://pcvm2-16.geni.uchicago.edu:5000 -x 24 -p 3 -l 180")
