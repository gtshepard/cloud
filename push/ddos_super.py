

import os 

os.system("slowhttptest -c 10000 -H -g -o att_graph1 -i 10 -r" + "1000" + " -t GET -u  http://pcvm2-16.geni.uchicago.edu:5000 -x 24 -p 3 -l 180")
