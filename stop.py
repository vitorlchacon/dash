import os

pids = os.popen("ps aux | grep app.py | awk '{print $2}'").readlines()
if (len(pids) > 0):
    pid = pids[0]
    print("Closing app.py with PID: ", pid)
    os.system('kill '+pid)
