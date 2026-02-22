# | Command           | OS        | What it does         |
# | ----------------- | --------- | -------------------- |
# | `echo %USERNAME%` | Windows   | Get current username |
# | `echo $USER`      | Linux/Mac | Get current username |
# | `systeminfo`      | Windows   | Show system info     |
# | `uname -a`        | Linux/Mac | Show system info     |

import os
print(os.system("echo %USERNAME%"))
print(os.system("systeminfo"))