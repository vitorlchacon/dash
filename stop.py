import os

pids = os.popen("ps aux | grep dash.py | awk '{print $2}'").readlines()
if (len(pids) > 0):
    pid = pids[0]
    print("Closing dash.py with PID {}", pid)
    os.system('kill '+pid)
