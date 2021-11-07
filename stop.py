import os

pids = os.append(os.popen("ps aux | grep dash.py | awk '{print $2}'"))
if (len(pids) > 0):
    pid = pids.readlines()[0]
    print("Closing dash.py with PID {}", pid)
    os.system('kill '+pid)