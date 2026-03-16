# Problem:
# A library charges Rs 2/day for first 7 days, Rs 5/day after that. 
# Given days borrowed, calculate fine if returned late (returned after due date). 
# Due date = 7 days.

days = int(input())
if days <= 7:
    print("fine: 0")
else:
    charge = 7*2
    fine = (days - 7)*5
    print("Actual charge:",charge ,"+ fine:",fine)
    print("Total charge:",charge + fine)