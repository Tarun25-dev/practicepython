# Problem: 
# Given coin denominations and an amount,
# find minimum number of coins needed. (Coins: 1, 5, 10, 25)
# Example: Amount=36 → 25+10+1 = 3 coins
# denominations means we can use any no.of times of a single coin to get min coins count

amt = int(input())
coins = [25, 10, 5, 1]
count = 0
for i in coins:
    count = count + (amt//i) # why amt//i beacuse we need to find how many coins where i can fullfill in that example if 11/2 => 5 two rupees coins max
    amt = amt % i # ammount remove which one has already coin counted and that updated in amount.
print(count)