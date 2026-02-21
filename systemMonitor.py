import psutil,time,os # psutil(python system and process utilities) module used to get information about your susyem and running processes.
while True:
    os.system("cls" if os.name=="nt" else "clear")
    print("CPU usage: ",psutil.cpu_percent(),"%")
    print("RAM usage: ",psutil.virtual_memory().percent,"%")

    time.sleep(1)
