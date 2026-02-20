# | Command           | OS        | What it does                |
# | ----------------- | --------- | --------------------------- |
# | `ping google.com` | All       | Check internet connectivity |
# | `ipconfig`        | Windows   | Show IP addresses           |
# | `ifconfig`        | Linux/Mac | Show IP addresses           |

import os
ping = os.system('ping google.com') #  it retuens two outputs if you get 0 then internet available or 1 you dont have any internet connection
if ping == 0:
    print("internet connected")
else:
    print("No internet Available")
ip = os.system("ipconfig")
print(ip)