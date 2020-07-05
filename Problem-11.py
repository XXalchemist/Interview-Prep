'Problem-11 : subarray sum equals k'

'''
Solution : We use cumulative sum and if differnce of cumulative sum and k present in dictionary then we increase the count.
'''
def subarraySum(arr,k):
    sumdict = {0:1}
    n = len(arr)
    count = 0
    cs = 0

    for num in arr:
        cs = cs + num
        if cs-k in sumdict:
            count = count + sumdict[cs-k]
        if cs in sumdict:
            sumdict[cs]+=1
        else:
            sumdict[cs] = 1
    return count

print('Input : [1,1,1] , k = 2','\nOutput : ',subarraySum([1,1,1],2))
