"""Best Time to Buy and Sell Stock
Find maximum profit from one buy and one sell.
"""
li=[7,1,5,3,6,4] # these are the prices of each day from day1 to day6 first day has price 7
# first we need to buy stock and after sell
minBuy=li[0]
minIndex=0
for i in range(len(li)):
    if li[i] < minBuy:
        minBuy=li[i]
        minIndex=i
maxSell=li[minIndex+1]
for i in range(minIndex+1,len(li)):
    if li[i]>maxSell:
        maxSell=li[i]
profit=maxSell-minBuy
print(profit)

# method 2
MinPrice=float('inf') # means very very large number
maxProfit=0
for price in li:
    if price < MinPrice:
        MinPrice=price
    else:
        maxProfit=max(maxProfit,price-MinPrice)
print(maxProfit)
