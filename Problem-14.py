'''
Problem 14 : Longest continous subsequence
'''

# Solution

def longestCommonSubsequence(nums):
    result = 0
    anchor = 0
    for i in range(0,len(nums)):
        if (i > 0 and nums[i-1] >= nums[i]):
            anchor = i
        result = max(result, i-anchor+1)
    return result

print('*'*35)
print('Input : [1,3,5,4,7]','\nOutput : ',longestCommonSubsequence([1,3,5,4,7]))
print('*'*35)
print('Input : [1,3,4,5,7]','\nOutput : ',longestCommonSubsequence([1,3,4,5,7]))
print('*'*35)
print('Input : [2,2,2]','\nOutput : ',longestCommonSubsequence([2,2,2]))
print('*'*35) 
