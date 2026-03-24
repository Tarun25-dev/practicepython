# find parking cost.  if vehicle stays for 2 hours then 100 rs / hr is the charge,
# if it stayed for less than 5 hours then 50 rs per hour (excluding the first 2 hours which had 100 rs/hr),
# and if vehicle is parked for more than 5 hours then 20 rs per hour. 


hours = int(input("Enter Hours:"))
cost = 0
if hours == 2:
    cost = 100
elif hours < 5:
    cost = hours * 50
elif hours > 5:
    cost = hours * 20
else:
    print("input invalid")
print("cost is",cost)
print("total hours",hours)
print("cost per hour is",cost // hours)
