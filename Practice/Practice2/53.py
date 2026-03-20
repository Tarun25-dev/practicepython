# a person wants to go to the gym for N months,
# gym gives different plans(offers),
# you must find minimum money to pay.
# 1m = 500
# 6m = 2000
# 12m = 3500

n = int(input("Enter No.of months:"))
cost = n*500 # first we takes as monthly cost after we compare with other plans also

six_cost = (n // 6 )*2000 + (n % 6)*500
if six_cost < cost:
    cost = six_cost

twele_cost = (n//12)*3500 + (n%12)*500
if twele_cost < cost:
    cost = twele_cost

print(cost)