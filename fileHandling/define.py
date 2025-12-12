# FILE HANDLING - File handling means creating, reading, writing, and updating files using Python.
#.1 at first we must open the file before accessing the file
# We use the open() function.
# syntax: file = open("filename", "mode")
file=open("fileHandling/text.txt","r")
"""
| Mode     | Meaning                                 |
| -------- | --------------------------------------- |
| "r"      | Read (file must exist)                  |
| "w"      | Write (creates new file OR overwrites)  |
| "a"      | Append (adds content at end)            |
| "r+"     | Read + Write                            |
| "w+"     | Write + Read (overwrites)               |
| "a+"     | Append + Read                           |
"""
