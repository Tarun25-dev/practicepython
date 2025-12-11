#A recursive function repeats the same task until a base condition stops it.
def countdown(n):
    if n==0: #base condition
        print("stops!..")
    else:
        print(n)
        countdown(n-1)
countdown(5)