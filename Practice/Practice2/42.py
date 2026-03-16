# Problem:
# ATM has notes of 2000, 500, 200, 100.
# Withdraw amount using minimum notes. Print note counts.
# Example: Amount=2800 → 2000:1, 500:1, 200:1, 100:1

amt = int(input())
notes = [2000,500,200,100]
for n in notes:
    print(f"{n}:",amt // n)
    amt = amt % n 
