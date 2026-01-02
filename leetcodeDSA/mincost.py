def mincost(cost,i):
    if i==0:
        return cost[0]
    if i==1:
        return cost[1]
    return cost[i]+min(mincost(cost,i-1),mincost(cost,i-2))
cost=[10,15,20]
n=len(cost)
result=min(mincost(cost,n-1),mincost(cost,n-2))
print(result)