import psutil,time,os
while True:
    os.system("cls" if os.name=="nt" else "clear")
    print("CPU usage: ",psutil.cpu_percent(),"%")
    print("RAM usage: ",psutil.virtual_memory().percent,"%")
    time.sleep(1)