# sys.stdout - is used to display output to the screen(standard output)
# normal print
print("Sys")
# but internally works like 
import sys
sys.stdout.write("Sys\n")


# for write lines - writes a list (or iterable) of strings to a file or output stream.
lines = ["Hello\n", "Tarun\n", "Python\n"]
sys.stdout.writelines(lines)

# Hello
# Tarun
# Python