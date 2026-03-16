# Problem:
# A factory produces X units in 24 days. How many units in Y days?
# Example: X=480, Y=15 → Answer: 300

X = int(input("Enter X units:"))
Y = int(input("Enter Y days:"))
# first simple logic we understood what is if x units in 24 days the what will they produce in one day if we find that we can easily find answer as well.\
dayOne = X//24
print(f"in {Y} days:", dayOne * Y)
