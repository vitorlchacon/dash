import os
    
pid = os.popen("ps aux | grep dash.py | awk '{print $2}'").readlines()[0] #call pid
print("Closing dash.py with PID {}", pid)
os.system('kill '+pid) #kill process