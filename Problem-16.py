'''
Problem 16 Minimum length of sum of subarray

Example : 
Input : s=7 nums = [2,3,1,2,4,3]
Output : 2
Subarray [4,3] has minimum length of 2

'''

def miniLength(nums, s):
    result = 99999
    left = 0
    val_sum = 0

    for i in range(0,len(nums)):
        val_sum += nums[i]

        while( val_sum >= s):
            result = min(result, i+1-left)
            val_sum -= nums[left]
            left = left+1
            print(result, left)
    return result if result!=99999 else 0

print('Input : s=7 nums = [2,3,1,2,4,3]','\nOutput : ',miniLength([2,3,1,2,4,3], 7))

