n=int(input())
discount=0
if n<=0:
	print("Error")
	exit()
elif n<1000:
	discount=5
elif n>=1000 and n<=5000:
	discount=10
else:
	discount=15
d=discount/100*n
pay=n-d
print(int(pay))
print("discount:",int(n-pay))
