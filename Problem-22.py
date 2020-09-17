capacity = 50
weights = [10,20,30]
values = [60,100,120]


# Algorithm 1 : Brute Force


def knapsack(w,v,c,n):
    if c == 0 or n == 0 :
        res = 0
    elif w[n-1] > c :
        res = knapsack(w,v,c,n-1)
    else:
        skip_item = knapsack(w,v,c,n-1)
        add_item = knapsack(w,v,c-w[n-1],n-1) + v[n-1]
        res = max(skip_item,add_item)
    return res

res = knapsack(weights,values,capacity,3)

print("Brute Force : ",res)


# Algorithm 2 : Dynamic Programming


dp = [[0]*50]*3

def knapsack(w,v,c,n):
    
    if c == 0 or n == 0 :
        res = 0
    elif w[n-1] > c :
        res = knapsack(w,v,c,n-1)
    else:
        skip_item = knapsack(w,v,c,n-1)
        add_item = knapsack(w,v,c-w[n-1],n-1) + v[n-1]
        res = max(skip_item,add_item)
    dp[n-1][c-1] = res
    
    return res

res = knapsack(weights,values,capacity,3)

print("Dynamic Programming : ",res)


