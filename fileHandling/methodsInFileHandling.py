#1. opening a file using open()
# Syntax: file = open("filename", "mode")
file1=open("fileHandling/text.txt",'r')

#2. reading the entire file content using read()
file2=open("fileHandling/text.txt",'r')
content1=file2.read()
print(content1)

#3. reads one line at a time using readline()
file3=open("fileHandling/text.txt",'r')
print(file3.readline()+ file3.readline()+ file3.readline()) #tharun
                                                            #kumar
                                                            #10

#4. reads all lines into a list using readlines()
file4=open("fileHandling/text.txt",'r')
print(file4.readlines()) #['tharun\n', 'kumar\n', '10']

#5. write text to a file using write()
# which is only for writing single line.
#when we use write mode the preivious data will be deleted Because "w" mode = overwrite mode Python clears the file before writing new text.
file5=open("fileHandling/text.txt",'w')
file5.write("kodiganti")

#6. Writes multiple lines (list). using writelines()
file6=open("fileHandling/text.txt",'w+')
file6.writelines(["tharun\n","kumar\n","10\n"])
print(file6.read()) #['tharun\n', 'kumar\n', '10\n']

#7. closes the file using close() after read/write the file we must close the file at last
file6.close()

#8.append the text using 'a' mode
file7=open("fileHandling/text1.txt",'a')
file7.write("tharun")
file7.write("kumar")

#"w" → write (creates new file, overwrites if exists)
# "a" → append (creates new file if not exists)
# "x" → create ONLY (error if file exists)
# If file already exists → old content is deleted

file = open("fileHandling/myfile.txt", "w")
file.write("Hello, this is a new file!")
file.close()

# Creates new file If file already exists → Error (FileExistsError)
files = open("newfile.txt", "x")
files.write("Created with x mode")
files.close()

# deleting an existing file
import os
if os.path.exists("fileHandling/text2.txt"):
    os.remove("fileHandling/text2.txt")
else:
    print("file doesn't found")









