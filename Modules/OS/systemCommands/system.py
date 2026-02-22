# os.system(command) → Runs a system/terminal command from Python.
import os
os.system("dir") # for windows
# how it works first it checks current dir if no then go back that file . again check if not found ..
# it checks upto your current path first dir 
# 02/20/2026  09:57 PM    <DIR>          .
# 02/20/2026  09:57 PM    <DIR>          ..
# 02/20/2026  08:41 PM    <DIR>          CreatedByOS
# 02/20/2026  08:15 PM               734 Define.txt
# 02/20/2026  09:54 PM    <DIR>          EnvironmentVariables
# 02/20/2026  08:27 PM               423 osLib.txt
# 02/20/2026  09:47 PM    <DIR>          PathManagement
# 02/20/2026  09:57 PM    <DIR>          systemCommands
# 02/20/2026  08:51 PM    <DIR>          workingWithDirectories.py
# 02/20/2026  09:25 PM    <DIR>          workingWithFiles
#                2 File(s)          1,157 bytes
#                8 Dir(s)  815,296,049,152 bytes free
# if linux/mac then use this syntax os.system("ls") 



# | Command            | OS        | What it does                                |
# | ------------------ | --------- | ------------------------------------------- |
# | `dir`              | Windows   | List files and folders in current directory |
# | `ls`               | Linux/Mac | List files and folders                      |
# | `mkdir foldername` | All       | Create a folder                             |
# | `rmdir foldername` | Windows   | Remove empty folder                         |
# | `rm -r foldername` | Linux/Mac | Remove folder recursively                   |
# | `del filename`     | Windows   | Delete file                                 |
# | `rm filename`      | Linux/Mac | Delete file                                 |
