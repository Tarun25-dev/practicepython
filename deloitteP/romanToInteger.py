# roman values are the another form of numbers it is not type of numbers it just another way to represents.
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000
# Must remember one thing if the next value is bigger value then it takes bigger value minus 1
# example if next value is 5 then IV (1-5=4)
s='XIII'
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # mapping the roman numbers with their corresponding values
total=0
prev=0
for ch in reversed(s): # if we comes from reversed then we can identify easily any bigger number before value so we can easily do minus
    cur=d[ch]
    if cur < prev:
        total-=cur
    else:
        total+=cur
    prev=cur
print(total)
